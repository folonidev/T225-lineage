"""Read property strings from the local, verified ext4 image; never mount/write it."""
from pathlib import Path
import re

pattern = re.compile(rb'(?:^|[\r\n\x00])(ro\.(?:(?:system\.)?build\.(?:version\.security_patch|fingerprint)|lineage\.version)=[^\r\n\x00]{1,240})')
result = set()
tail = b''
image = Path('D:/tablet-sistema2d/imagens/lineage-21.0-arm64_bgN.img')
with image.open('rb') as f:
    while data := f.read(8 * 1024 * 1024):
        block = tail + data
        for match in pattern.finditer(block):
            result.add(match[1].decode('utf8', 'replace'))
        tail = block[-512:]
text = '\n'.join(sorted(result))
Path(__file__).with_name('gsi-propriedades-offline.txt').write_text(text, encoding='utf8')
print(text)
