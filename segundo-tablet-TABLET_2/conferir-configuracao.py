import os
import json
import re
import shlex
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

base = Path(__file__).resolve().parent
adb = base.parent / 'tools/platform-tools/adb.exe'
serial = os.environ.get('ADB_SERIAL', '').strip()
if not serial:
    raise SystemExit('Defina ADB_SERIAL com o serial do tablet de destino.')
target = json.loads((base / 'config-alvo.json').read_text(encoding='utf8'))
checks = {}

def call(*args):
    p = subprocess.run([str(adb), '-s', serial, *args], capture_output=True)
    if p.returncode:
        raise RuntimeError(p.stderr.decode('utf8', 'replace'))
    return p.stdout.decode('utf8', 'replace').strip()

def shell(command):
    return call('shell', command)

def root(command):
    return shell('su -c ' + shlex.quote(command))

def record(name, actual, expected):
    checks[name] = {'atual': actual, 'alvo': expected, 'confere': actual == expected}

record('serial', call('get-serialno'), serial)
record('lineage', shell('getprop ro.lineage.version'), target['lineage'])
record('boot_concluido', shell('getprop sys.boot_completed'), '1')
record('magisk', shell('magisk -v').split(':')[0], target['magisk'])
record('root', 'uid=0' in root('id'), True)
record('anims', [float(shell('settings get global ' + k)) for k in
       ('window_animation_scale', 'transition_animation_scale', 'animator_duration_scale')], [0, 0, 0])
record('densidade', 'Override density: 200' in shell('wm density'), True)
record('fonte', float(shell('settings get system font_scale')), 1.05)
record('modo_aviao', shell('settings get global airplane_mode_on'), '1')
record('bluetooth', shell('settings get global bluetooth_on'), '1')
wifi = shell('cmd wifi status')
record('wifi_conectado', 'Wifi is connected to' in wifi, True)
record('perfetto', shell('getprop persist.traced.enable'), '0')
disabled = set(shell('pm list packages -d').splitlines())
for package in target['disabled_packages']:
    record('desativado:' + package, 'package:' + package in disabled, True)
for module in target['modules']:
    record('modulo:' + module, root(f'test -f /data/adb/modules/{module}/module.prop && '
           f'test ! -e /data/adb/modules/{module}/disable && echo ativo'), 'ativo')
overlays = shell('cmd overlay list')
for suffix in ('corners', 'icon.ios', 'taskbar', 'settings'):
    record('overlay:' + suffix, '[x] com.sistema2d.theme.' + suffix in overlays, True)
magisk_path = root('magisk --path')
assert re.fullmatch(r'/[A-Za-z0-9_./-]+', magisk_path)
record('magisk_preinit', root(f'if [ -b {magisk_path}/.magisk/device/preinit ] || '
       f'[ -b {magisk_path}/.magisk/block/preinit ]; then echo presente; fi'), 'presente')
raw = root('cat /data/user/0/org.schabi.newpipe/shared_prefs/org.schabi.newpipe_preferences.xml')
prefs = {n.get('name'): n.get('value') if n.tag == 'boolean' else n.text for n in ET.fromstring(raw)}
for key, expected in target['newpipe_preferences'].items():
    if isinstance(expected, bool): expected = str(expected).lower()
    record('newpipe:' + key, prefs.get(key), expected)
for package, version in [('org.schabi.newpipe', target['newpipe']), ('com.topjohnwu.magisk', target['magisk'])]:
    match = re.search(r'versionName=([^\s]+)', shell('dumpsys package ' + package))
    record('versao:' + package, match[1] if match else None, version)
vm = root('cat /proc/sys/vm/swappiness /proc/sys/vm/vfs_cache_pressure /proc/sys/vm/dirty_ratio /proc/sys/vm/dirty_background_ratio')
record('vm', vm.split(), ['100', '100', '20', '5'])
(base / 'conferencia-final.json').write_text(json.dumps(checks, indent=2, ensure_ascii=False), encoding='utf8')
failed = [name for name, result in checks.items() if not result['confere']]
print('Conferencia de configuracao:', len(checks) - len(failed), '/', len(checks))
for name in failed: print('PENDENTE:', name, checks[name])
raise SystemExit(bool(failed))
