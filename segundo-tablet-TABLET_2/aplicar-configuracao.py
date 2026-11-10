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

def call(*args, check=True):
    p = subprocess.run([str(adb), '-s', serial, *args], capture_output=True)
    out = p.stdout.decode('utf8', 'replace').strip()
    if check and p.returncode:
        raise RuntimeError(f'ADB falhou: {args}: {out} {p.stderr.decode("utf8", "replace")}')
    return out

def shell(command, **kwargs):
    return call('shell', command, **kwargs)

def root(command, **kwargs):
    return shell('su -c ' + shlex.quote(command), **kwargs)

assert call('get-serialno') == serial
assert shell('getprop ro.lineage.version') == target['lineage']
assert shell('am get-current-user') == '0'
assert 'uid=0' in root('id')
before = {'density': shell('wm density'), 'settings': {}, 'packages': {}}
for namespace, key in [('global', 'window_animation_scale'), ('global', 'transition_animation_scale'),
                       ('global', 'animator_duration_scale'), ('global', 'airplane_mode_on'),
                       ('global', 'bluetooth_on'), ('system', 'font_scale')]:
    before['settings'][namespace + ':' + key] = shell(f'settings get {namespace} {key}')
for package in target['disabled_packages']:
    dump = shell('dumpsys package ' + package)
    (base / ('package-anterior-' + package + '.txt')).write_text(dump, encoding='utf8')
    match = re.search(r'User 0:.*?installed=true.*?enabled=(\d+)', dump)
    if not match:
        raise RuntimeError('Pacote nao confirmado: ' + package)
    before['packages'][package] = match[1]
(base / 'estado-antes-ajustes.json').write_text(json.dumps(before, indent=2), encoding='utf8')

with (base / 'alteracoes.jsonl').open('a', encoding='utf8') as log:
    def change(kind, name, old, new, command):
        row = {'tipo': kind, 'nome': name, 'anterior': old, 'novo': new, 'comando': command,
               'resultado': 'pendente'}
        log.write(json.dumps(row) + '\n'); log.flush()
        out = shell(command)
        row['resultado'] = out or 'aplicado'
        log.write(json.dumps(row) + '\n'); log.flush()
        print(name + ': aplicado', flush=True)

    for key in ('window_animation_scale', 'transition_animation_scale', 'animator_duration_scale'):
        change('setting', 'global:' + key, before['settings']['global:' + key], '0',
               f'settings put global {key} 0')
    change('density', 'density', before['density'], '200', 'wm density 200')
    change('setting', 'system:font_scale', before['settings']['system:font_scale'], '1.05',
           'settings put system font_scale 1.05')
    for package, state in before['packages'].items():
        if state not in ('0', '1'):
            print(package + ': ja desativado; preservado', flush=True)
            continue
        change('package', package, state, 'disabled-user', f'pm disable-user --user 0 {package}')
    change('radio', 'airplane_mode_on', before['settings']['global:airplane_mode_on'], '1',
           'cmd connectivity airplane-mode enable')
    shell('svc wifi enable')
    shell('cmd bluetooth_manager enable')

call('shell', 'am', 'force-stop', 'org.schabi.newpipe')
prefs = '/data/user/0/org.schabi.newpipe/shared_prefs'
filename = 'org.schabi.newpipe_preferences.xml'
raw = root(f'if [ -f {prefs}/{filename} ]; then cat {prefs}/{filename}; fi')
if raw:
    (base / 'newpipe-preferencias-anteriores.xml').write_text(raw, encoding='utf8')
    tree = ET.fromstring(raw)
else:
    tree = ET.Element('map')
for key, value in target['newpipe_preferences'].items():
    node = next((n for n in tree if n.get('name') == key), None)
    if node is not None:
        tree.remove(node)
    if isinstance(value, bool):
        ET.SubElement(tree, 'boolean', {'name': key, 'value': str(value).lower()})
    else:
        ET.SubElement(tree, 'string', {'name': key}).text = value
out = base / 'newpipe-preferencias.xml'
ET.ElementTree(tree).write(out, encoding='utf8', xml_declaration=True)
owner = root('stat -c ' + shlex.quote('%u:%g') + ' /data/user/0/org.schabi.newpipe')
assert re.fullmatch(r'\d+:\d+', owner), owner
call('push', str(out), '/data/local/tmp/codex-newpipe-prefs.xml')
root(f'mkdir -p {prefs}; cp /data/local/tmp/codex-newpipe-prefs.xml {prefs}/{filename}; '
     f'chown {owner} {prefs} {prefs}/{filename}; chmod 0771 {prefs}; '
     f'chmod 0660 {prefs}/{filename}; restorecon -R {prefs}')
shell('pm grant org.schabi.newpipe android.permission.POST_NOTIFICATIONS')
print('NewPipe: mesmas preferencias, sem copiar historico ou contas', flush=True)
