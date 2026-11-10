import hashlib
import json
from pathlib import Path
import subprocess
import tarfile
import time
import zipfile

root = Path('D:/tablet-sistema2d')
archive = root / 'firmware-samsung/SM-T225_4_20250524034241_cnxe51mdi0_fac.zip'
deadline = time.monotonic() + 1200
while not archive.exists():
    if time.monotonic() > deadline:
        raise SystemExit('Download nao terminou; nenhum arquivo foi gravado no tablet.')
    time.sleep(10)

dest = root / 'firmware-samsung/extraido'
dest.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(archive) as z:
    members = [x for x in z.infolist() if x.filename.endswith('.tar.md5')]
    if not all(any(Path(x.filename).name.startswith(prefix) for x in members)
               for prefix in ('AP_', 'BL_', 'CP_', 'CSC_')):
        raise SystemExit('Firmware sem conjunto completo AP/BL/CP/CSC')
    for member in members:
        if Path(member.filename).name != member.filename:
            raise SystemExit('Caminho inesperado no firmware')
        z.extract(member, dest)
        print('Extraido e CRC validado:', member.filename, flush=True)

exe = Path(__file__).resolve().parent / 'samloader/samloader.exe'
files = sorted(dest.glob('*.tar.md5'))
subprocess.run([str(exe), 'verify-md5', *map(str, files)], check=True)
with tarfile.open(next(dest.glob('AP_*.tar.md5'))) as ap:
    boot_members = [m for m in ap.getmembers() if m.name in ('boot.img.lz4', 'boot.img')]
    if len(boot_members) != 1:
        raise SystemExit('Imagem boot original nao identificada univocamente')
    boot = boot_members[0]
    with ap.extractfile(boot) as src, (root / 'imagens' / boot.name).open('wb') as dst:
        import shutil
        shutil.copyfileobj(src, dst)

result = {'firmware': str(archive), 'pacotes': [str(p) for p in files],
          'boot_original': str(root / 'imagens' / boot.name),
          'validacao': 'CRC ZIP e MD5 dos pacotes validados; nao aplicado ao tablet'}
(root / 'firmware-verificado.json').write_text(json.dumps(result, indent=2), encoding='utf8')
print(json.dumps(result, indent=2), flush=True)
