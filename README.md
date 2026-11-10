# Repetir a configuração do Galaxy Tab A7 Lite SM-T225

> **Versão pública:** seriais ADB, identificadores Download e dados de rede dos diagnósticos foram anonimizados.
> `TABLET_1`, `TABLET_2` e `DOWNLOAD_ANONIMIZADO` são identificadores fictícios.
> Os scripts recebem o serial real por `ADB_SERIAL`; não use identificadores fictícios em comandos.
> Downloads, firmware, APKs, executáveis e capturas ficam fora do Git.
> Guarde novos backups e resultados em `tablet-local/`, ignorada pelo Git.


Documento de transferência para outra IA com acesso ao computador e às ferramentas USB, como Claude. Baseado nas duas instalações concluídas neste workspace em novembro de 2026. O objetivo é reproduzir a configuração aprovada pelo dono para **navegar e assistir vídeos pelo NewPipe**.

**Escopo de aplicativos: navegador Jelly + NewPipe.** Preservar os componentes necessários do Android. Não instalar outros aplicativos de uso pessoal. Não aplicar a limpeza antiga da ROM Samsung sobre o LineageOS.

## 1. Instrução para a IA que receber este arquivo

Execute o procedimento por etapas, verificando o resultado de cada gravação antes da próxima. Faça as operações pelo computador sempre que possível; peça ao dono apenas as ações físicas, autorizações USB e configurações que dependem da tela. Não basta entregar outro plano ao usuário.

O dono quer repetir a configuração que já aprovou, sem novos benchmarks, testes prolongados ou experimentos para ganhar desempenho. Faça as verificações essenciais de identidade, compatibilidade, integridade, boot, root, rede e aplicativos. Não prometa que este é o desempenho máximo possível nem atribua percentuais de ganho aos ajustes.

Este README é um procedimento, não um instalador automático. Os comandos de gravação abaixo dependem das verificações anteriores. Confirme o aparelho conectado e o consentimento do dono para apagar esse aparelho, desbloquear o bootloader e instalar root, caso isso ainda não esteja autorizado na nova conversa. A autorização dada para os dois tablets anteriores não vale automaticamente para um aparelho de outra pessoa.

Não apague nem reinstale os tablets anteriores apenas para consultar a referência. Não copie contas, senhas, histórico, chaves ADB privadas, EFS, NVRAM, modem ou identificadores entre aparelhos. Prepare o boot a partir do próprio tablet de destino.

### Como a IA deve orientar o usuário

Leia este README inteiro antes de executar comandos. Ele define o procedimento atual; os arquivos em `tablet-optimization/`, `referencia/`, logs e relatórios são históricos. Não execute a limpeza antiga da ROM Samsung para reproduzir o alvo LineageOS.

1. Identifique o modelo físico, firmware, estado do bootloader e sistema do aparelho atual. Se ele já estiver na configuração alvo, confira o estado antes de propor uma reinstalação.
2. Explique o apagamento dos dados, a alteração permanente do Knox, root e FBE desativado. Peça ao dono que salve seus arquivos pessoais antes de começar. Confirme o consentimento para esse aparelho se ainda não tiver sido dado.
3. Prepare downloads, hashes, drivers e firmware de recuperação no PC antes de gravar. Pare se faltar um arquivo ou houver incompatibilidade não resolvida.
4. Execute uma etapa por vez. Para cada ação física, explique a tela esperada, os botões e quando soltar. Espere o usuário concluir e confira o resultado pelo PC antes de avançar.
5. Deixe senhas de Wi-Fi, autenticação Google/FRP e autorizações para o dono digitar ou confirmar diretamente na tela. Não peça credenciais no chat nem as salve em logs.
6. Ao terminar, informe o que foi instalado e conferido, pendências e localização dos backups privados. Mostre como abrir Jelly para navegar e NewPipe para vídeos e confirme som/imagem com o dono.

O usuário precisa de um PC Windows, cabo de dados, bateria com pelo menos 60%, acesso físico aos botões e tela e backup pessoal concluído. A IA faz a preparação e os comandos no PC; o usuário confirma UAC/USB/root, opera botões e faz autenticações na tela quando necessário.

## 2. Hardware e configuração aprovados

O procedimento foi realizado em **Samsung Galaxy Tab A7 Lite LTE SM-T225 / gta7lite**, com cerca de 3 GB de RAM. **Não aplicar automaticamente ao SM-T220 ou a outros modelos.** Nos dois aparelhos, o firmware inicial era:

| Item | Referência |
|---|---|
| Firmware / bootloader | `T225XXSBEYE1`, binário B |
| Android Samsung | Android 14 |
| Patch Samsung | `2025-05-01` |
| CSC | `ZTO` |
| ROM instalada | LineageOS 21 / Android 14, GSI `arm64_bgN` |
| Build Lineage | `21.0-20260614-UNOFFICIAL-arm64_bgN` |
| Recovery | TWRP `3.7.1_12-1`, pacote gta7lite v2.2 |
| Root | Magisk oficial `30.7` |
| Zygisk | Integrado ao Magisk, ativado e confirmado após reiniciar |
| Camada de ajustes | Sistema2D `v1.0.0` |
| Navegador | Jelly, pacote `org.lineageos.jelly` |
| WebView observado | `com.android.webview`, `149.0.7827.114` |
| Vídeo | NewPipe oficial `0.29.1`, pacote `org.schabi.newpipe` |
| Interface | 200 dpi, fonte 1.05, três escalas de animação em 0 |
| Idioma | pt-BR, com en-US como idioma secundário |
| Rádios | Modo avião ligado, Wi-Fi ligado/conectado, Bluetooth ligado |

Se firmware, partições, boot ou estado de bloqueio diferirem, investigue a compatibilidade antes de gravar. Não faça downgrade de bootloader. Após a GSI, o modelo lógico pode aparecer como `TrebleDroid with GApps`; use a identidade registrada antes da instalação para comprovar o hardware.

Consequências da instalação aprovada: apagamento dos dados, bootloader desbloqueado, root, alteração permanente do Knox e FBE desativado. Voltar ao firmware Samsung não restaura o fusível Knox. Não bloquear o bootloader enquanto esta GSI estiver instalada. Os dados desta configuração não devem ser considerados protegidos por criptografia de arquivos.

## 3. Arquivos locais e o que entregar à outra IA

Estrutura de trabalho esperada no Windows. Os binários abaixo **não vêm no Git**; obtenha-os pelas fontes da seção 4 antes de executar os comandos:

```text
C:\Users\USUARIO\OneDrive\Desktop\tablet
├── README.md
├── tools\platform-tools\                 adb.exe e fastboot.exe
├── sistema2d-preparacao\
│   ├── arquivos\                         GSI comprimida, APK, ZIPs e drivers
│   ├── imagens-pequenas\                 recovery.img, vbmeta.img, magiskboot
│   ├── samloader\samloader.exe           versão 2.2.0
│   ├── google-usb-driver\usb_driver\     driver Google para fastbootd
│   ├── fontes\                           fontes Sistema2D consultadas
│   ├── release.json                       URLs e digests da release
│   ├── firmware-verificado.json           localização da recuperação Samsung
│   └── resultado.md                       resultado do primeiro tablet
└── segundo-tablet-TABLET_2\
    ├── config-alvo.json                    configuração alvo
    ├── aplicar-configuracao.py             ajustes finais; usa ADB_SERIAL
    ├── conferir-configuracao.py            comparação; usa ADB_SERIAL
    ├── conferencia-final.json              resultado histórico 36/36
    ├── rollback-ajustes.ps1                reversão parcial; usa ADB_SERIAL
    ├── boot-original.img                   backup privado; ausente no clone
    ├── registro.md                         registro da segunda instalação
    └── resultado.md                        relatório histórico
```

Na sessão original, os arquivos grandes ficaram fora do workspace. Estes caminhos são exemplos históricos; em outro PC, escolha o armazenamento local e ajuste os comandos:

```text
D:\tablet-sistema2d\imagens\lineage-21.0-arm64_bgN.img
D:\tablet-sistema2d\firmware-samsung\
D:\tablet-sistema2d\firmware-samsung\extraido\   AP, BL, CP, CSC e HOME_CSC
```

Se a outra IA trabalhar neste PC, ela pode consultar essas pastas. Em outro PC, envie este README e os arquivos necessários, ou baixe-os das fontes abaixo. O README sozinho não transporta as imagens. Não é necessário enviar capturas de tela, dumps de interface, dados de apps ou a pasta de aplicativos adicionais da segunda instalação.

**Referências anonimizadas:** primeiro tablet `TABLET_1`; segundo `TABLET_2`. O identificador Download é diferente do serial ADB; obtenha ambos do aparelho atual e mantenha-os nos registros privados.

Crie `tablet-local/` na raiz do clone para o aparelho atual, conforme a seção 5. Essa pasta é privada e ignorada pelo Git. A posição preserva os caminhos relativos de `tools/`. Preserve os registros históricos. Os scripts existentes não fazem a instalação de ROM: servem apenas para ajustar/conferir o sistema já instalado. O rollback depende do estado anterior salvo nesse mesmo aparelho.

## 4. Fontes e integridade

Versões fixadas para reprodução, sem trocar silenciosamente por “latest”:

- Sistema2D: <https://github.com/Sistema2D/SM-T225>, commit `79069eaafcdfa5e8406e0571d11bcbd27d89252e`.
- Release e todos os componentes da instalação: <https://github.com/Sistema2D/SM-T225/releases/tag/v1.0.0>.
- API de metadados: <https://api.github.com/repos/Sistema2D/SM-T225/releases/tags/v1.0.0>.
- Magisk upstream: <https://github.com/topjohnwu/Magisk/releases/tag/v30.7>; instalação: <https://topjohnwu.github.io/Magisk/install.html>.
- NewPipe: <https://github.com/TeamNewPipe/NewPipe/releases/tag/v0.29.1>.
- Platform-tools: <https://developer.android.com/tools/releases/platform-tools>.
- Driver Samsung: <https://developer.samsung.com/android-usb-driver>.
- Driver Google: <https://developer.android.com/studio/run/win-usb>.
- Samloader usado: <https://github.com/topjohnwu/samloader-rs/releases/tag/v2.2.0>.

Para os dez arquivos Sistema2D, a URL segue `https://github.com/Sistema2D/SM-T225/releases/download/v1.0.0/NOME_DO_ARQUIVO`. Os hashes registrados são:

| Arquivo | SHA-256 |
|---|---|
| `lineage-21.0-arm64_bgN.img.gz` | `2b0141d22271d38dcc9a1f5116deb50f8b8abc9af7480216f24edba0fc0fed5d` |
| `TWRP_v2.2_gta7lite.tar` | `c0df26e4c19aa3f8901c2ce17c78bc05ff0c33d324e84e04eedb70b51f244908` |
| `vbmeta_disabled.tar` | `5d1a74d12c22018452fde93b15c69712cfd1e49fa051d7e69771f2567557f185` |
| `fbe_disabler_gta7lite.zip` | `7ea68fa8ede2d9f5dc51b0d5c8cdf9e9f32b83b7a84676173affda1b3195188d` |
| `Magisk-v30.7.apk` | `e0d32d2123532860f97123d927b1bb86c4e08e6fd8a48bfc6b5bee0afae9ebd5` |
| `sistema2d_tweaks.zip` | `6d38579aa537782d71556f0c234a45ee078f76b563d74c00eee242b79743251e` |
| `sistema2d_bootanim.zip` | `bce06edbf7923ed7d04ccf6b5c005bd34e71e2c3eed835abf5a73ef37d201848` |
| `sistema2d_ui_ios.zip` | `4854632af51657ff87007bf715a02216b2f7380c4e07f0cca09f9bae5f51ff46` |
| `sistema2d_rom_provisioning.zip` | `5f81aadc3e6fe0ca2af474574d18935f90d2a0df1032c7a78f27e6c5eecc2bfe` |
| `99-aosp-tweaks.sh` | `8b4c9880c4b703752706a4e85f7be52b2acd209efe1658f5a536b6241a73ab65` |
| `NewPipe_v0.29.1.apk` | `18447bfb1e06d113edc88df93f471827280de06f6f3d4dc42f56f28b9c1bab79` |

Confira com `Get-FileHash -Algorithm SHA256`. Valide os arquivos antes de qualquer gravação. A imagem GSI descomprimida usada tinha **3.202.322.432 bytes**, formato ext4. Extraia os TARs de recovery/vbmeta; os comandos samloader abaixo usam as imagens internas, não o TAR inteiro como conteúdo bruto da partição.

Tenha firmware Samsung de recuperação compatível com o aparelho antes de começar. Neste PC, `firmware-verificado.json` aponta para o firmware `T225XXSBEYE1/ZTO`, obtido do servidor Samsung; ZIP/CRC e MD5 dos cinco pacotes foram conferidos. Em outro firmware, obtenha a recuperação correspondente. Reserve espaço para a GSI extraída e o firmware completo, além dos downloads.

### Preparar um clone novo

Instale Python 3 e Git no Windows. Abra o PowerShell na raiz do repositório e prepare os arquivos antes de executar as seções de gravação:

1. Baixe Platform-tools do Google e extraia a pasta `platform-tools` para `tools/`, resultando em `tools/platform-tools/adb.exe` e `fastboot.exe`.
2. Baixe os dez componentes Sistema2D da tabela acima em `sistema2d-preparacao/arquivos/`, além do APK NewPipe da fonte oficial. Confira todos os SHA-256; se houver divergência, pare e investigue. O script histórico `fontes/ferramentas/baixar-ferramentas.ps1` só baixa Platform-tools e não prepara a instalação inteira.
3. Obtenha Samloader Windows 2.2.0 pela release indicada e extraia o executável em `sistema2d-preparacao/samloader/samloader.exe`.
4. Obtenha os drivers Samsung e Google pelas páginas oficiais. Extraia o driver Google em `sistema2d-preparacao/google-usb-driver/`. Instale o driver correspondente a cada modo quando necessário, com o usuário confirmando o UAC.
5. Extraia dos TARs os arquivos `recovery.img` e `vbmeta.img` para `sistema2d-preparacao/imagens-pequenas/`. Extraia do APK Magisk, tratado como ZIP, `lib/arm64-v8a/libmagiskboot.so` e salve nessa pasta como `magiskboot`. Não use imagens boot de referência de outro aparelho.
6. Descomprima a GSI `.img.gz` para um `.img` em armazenamento local com espaço suficiente; não basta renomear a extensão. Anote o caminho e substitua o exemplo `D:\tablet-sistema2d\imagens\lineage-21.0-arm64_bgN.img` na seção 9 pelo caminho real.
7. Obtenha e valide firmware Samsung de recuperação compatível com o destino. `firmware-verificado.json` é um registro histórico, não comprova que os arquivos existem neste PC. Os scripts `preparar-firmware.py` e `inspecionar-gsi.py` também contêm caminhos da sessão original: leia e adapte antes de usar.

Confira a existência de cada arquivo usado pelo próximo comando. Se qualquer fonte estiver indisponível, comunique o arquivo faltante; não substitua automaticamente a versão ou use um download de procedência desconhecida.

## 5. Preparação e seleção do aparelho

Use cabo de dados e bateria de pelo menos 60%. Conecte somente o tablet de destino quando usar Download/samloader, pois os exemplos dessa ferramenta não selecionam serial. Feche outras ferramentas que disputem a conexão USB.

No PowerShell, a partir do workspace:

```powershell
$adb = Join-Path $PWD 'tools\platform-tools\adb.exe'
$fastboot = Join-Path $PWD 'tools\platform-tools\fastboot.exe'
$samloader = Join-Path $PWD 'sistema2d-preparacao\samloader\samloader.exe'
& $adb devices -l
$serialTablet = 'SUBSTITUIR_PELO_SERIAL_DO_TABLET_ATUAL'
$env:ADB_SERIAL = $serialTablet
& $adb -s $serialTablet shell getprop ro.product.model
& $adb -s $serialTablet shell getprop ro.bootloader
& $adb -s $serialTablet shell getprop ro.build.version.security_patch
& $adb -s $serialTablet shell getprop ro.boot.sales_code
& $adb -s $serialTablet shell getprop ro.boot.flash.locked
& $adb -s $serialTablet shell getprop ro.boot.vbmeta.device_state
& $adb -s $serialTablet shell getprop sys.oem_unlock_allowed
& $adb -s $serialTablet shell dumpsys battery
```

Esses exemplos pressupõem que o dono ativou Depuração USB e aceitou a chave deste PC. Salve a identificação em uma pasta por aparelho. Sempre use `-s` com ADB e fastboot. Após cada troca de modo, confira novamente a conexão e a identidade disponível.

Após confirmar o destino, prepare cópias dos ajustes na pasta privada, uma vez por aparelho:

```powershell
$pastaTablet = Join-Path $PWD 'tablet-local'
if (Test-Path $pastaTablet) { throw 'Pasta privada já existe; confira os backups antes de reutilizar' }
New-Item -ItemType Directory -Path $pastaTablet | Out-Null
Copy-Item '.\segundo-tablet-TABLET_2\aplicar-configuracao.py', `
          '.\segundo-tablet-TABLET_2\conferir-configuracao.py', `
          '.\segundo-tablet-TABLET_2\config-alvo.json', `
          '.\segundo-tablet-TABLET_2\rollback-ajustes.ps1' -Destination $pastaTablet
```

Nos comandos seguintes, substitua `PASTA_DO_NOVO_TABLET` por `tablet-local`. `ADB_SERIAL` vale para a sessão atual do PowerShell; defina novamente se abrir outro terminal. Os scripts interrompem se a variável estiver vazia. O campo `serial` do JSON é uma referência anonimizada; a seleção e conferência do aparelho usam `ADB_SERIAL`.

## 6. Desbloquear o bootloader — parte física

1. No Samsung, habilite Opções do desenvolvedor com sete toques em Número de compilação. Ative Depuração USB e Desbloqueio de OEM.
2. Desligue completamente. Pode usar `adb -s SERIAL shell reboot -p`.
3. Retire o cabo, espere a tela apagar completamente e aguarde cerca de cinco segundos.
4. Segure **Volume alto + Volume baixo antes de conectar o cabo ao PC**; continue segurando até aparecer o aviso. Não aperte Ligar nesse momento.
5. Na tela de aviso, deve existir **“Volume up long press: Device unlock mode”**. Mantenha Volume alto pressionado e confirme o desbloqueio na tela seguinte, conforme indicado. **Toque curto em Volume alto entra no Download normal e não desbloqueia.**
6. O tablet apaga os dados e reinicia. O primeiro boot após isso pode demorar alguns minutos.
7. Conclua o básico, conecte ao Wi-Fi, pule restauração e PIN/senha inicialmente. Se exigir a conta anterior, o dono deve autenticar no tablet; não contornar FRP.
8. Reative Depuração USB, autorize o PC e confira OEM ligado/cinza. Confirme também por ADB `ro.boot.flash.locked=0` e `ro.boot.vbmeta.device_state=unlocked` antes de gravar.

Se o long press virar toque curto, retire a capinha e confira o botão; aconteceu no segundo tablet. Não tente substituir a confirmação física com comandos inventados. Se OEM/FRP/KnoxGuard impedir a operação, resolva legitimamente antes de continuar.

## 7. Download: gravar TWRP e vbmeta

Download Samsung e fastbootd são modos diferentes. Samsung não disponibilizou fastboot de bootloader neste procedimento. Use samloader/Odin para recovery/vbmeta e fastbootd posteriormente para system/boot.

1. Entre novamente na tela de aviso com os dois volumes e cabo, mas agora dê **toque curto em Volume alto** para Download. Alternativamente, com Android autorizado: `adb -s SERIAL reboot download`.
2. Confira o modelo e o estado de desbloqueio. A tela “Downloading… Do not turn off target” nem sempre mostra todos os campos esperados.
3. Confira a ferramenta e obtenha o PIT do próprio destino, sem reparticionar:

```powershell
& $samloader detect --json
& $samloader dump-pit --output '.\PASTA_DO_NOVO_TABLET\tablet-original.pit' --no-reboot
& $samloader print-pit --file '.\PASTA_DO_NOVO_TABLET\tablet-original.pit'
```

Consulte `print-pit --help` se a sintaxe da versão disponível diferir. Nas instalações anteriores, RECOVERY tinha ID 39 e VBMETA ID 14. **Leia o PIT atual; não suponha que os IDs sejam universais.** Nomes internos de arquivo também podem servir ao auto-matching do samloader, mas precisam corresponder ao PIT.

Após confirmar nomes, modelo, imagens, tamanhos e hashes, o formato do comando é:

```powershell
# Substituir os nomes pelos que foram confirmados no PIT atual.
& $samloader flash --no-reboot `
  -p RECOVERY '.\sistema2d-preparacao\imagens-pequenas\recovery.img' `
  -p VBMETA '.\sistema2d-preparacao\imagens-pequenas\vbmeta.img'
if ($LASTEXITCODE -ne 0) { throw 'Falha ao gravar recovery/vbmeta; não prosseguir' }
```

Não usar `--pit`, reparticionamento, erase de baixo nível ou opções para ignorar checagem de tamanho. Preserve o log e confira a gravação. Se houver falha de sessão USB, reinicie fisicamente o modo Download e diagnostique antes de repetir; não presuma que a imagem foi gravada.

O procedimento efetivo usou samloader 2.2.0. Odin com Auto Reboot desmarcado é uma alternativa com operação pela interface, mas não foi a ferramenta usada nas gravações registradas. Não deixe iniciar o Android Samsung entre a gravação e a primeira entrada no TWRP, pois pode restaurar o recovery original.

Para entrar no TWRP a partir de Download: com cabo conectado, segure **Ligar + Volume baixo** até apagar. Imediatamente troque Volume baixo por **Volume alto**, mantendo Ligar, até abrir Team Win. Se ficar em Download, repita a transição. Se houver aviso pedindo Power para continuar, siga o aviso e retome a combinação.

## 8. TWRP: dados, vendor e boot próprio

Confirme TWRP `3.7.1_12-1`, ADB em recovery e acesso root. Antes de alterar boot/vendor, salve os originais no PC. Descubra os caminhos reais com `ls -l /dev/block/by-name`; não presuma nomes sem verificar.

1. **Wipe → Format Data**, digite `yes`, ou use a CLI TWRP `twrp format data`. Confira sucesso no log.
2. Reinicie **para Recovery**, não para System, e espere o ADB voltar.
3. Monte `/data` e `/vendor`. Salve `/vendor/etc/fstab.mt6765` e `/vendor/etc/fstab.mt8768` quando presentes.
4. Leia a partição boot do próprio aparelho para `/tmp/boot-original.img` com `dd`, usando o caminho confirmado, e faça `adb pull` para a pasta deste tablet. Exemplo após verificar `/dev/block/by-name/boot`:

```powershell
& $adb -s $serialTablet shell 'dd if=/dev/block/by-name/boot of=/tmp/boot-original.img bs=1048576'
& $adb -s $serialTablet pull /tmp/boot-original.img '.\PASTA_DO_NOVO_TABLET\boot-original.img'
& $adb -s $serialTablet push '.\sistema2d-preparacao\arquivos\fbe_disabler_gta7lite.zip' /tmp/
& $adb -s $serialTablet shell twrp install /tmp/fbe_disabler_gta7lite.zip
```

Confira o retorno do instalador, o log `/tmp/recovery.log` e os fstabs resultantes. O disabler altera vendor; não é só uma preferência do Android. Faça a formatação final descrita adiante.

### Ajuste de compatibilidade SPL do boot

Nos dois tablets, o cabeçalho do boot original declarava `os_version=12.0.0` e `os_patch_level=2025-05`, embora o Samsung instalado fosse Android 14. A GSI declara patch `2026-06-01`. A cópia de boot usada para a instalação teve **somente o patch do cabeçalho alinhado a `2026-06`**, mantendo os outros campos, para compatibilidade de Keymaster desta combinação. Isso **não atualiza o kernel nem instala correções de segurança**.

Use `magiskboot` ARM64 extraído do APK oficial 30.7 (`lib/arm64-v8a/libmagiskboot.so`). Execute no tablet pelo recovery, com permissão 0755 e em diretório temporário próprio. A sequência da ferramenta é:

```sh
# Executar no shell do TWRP, num diretório temporário novo e exclusivo.
# O binário magiskboot e boot-original.img já devem estar neste diretório.
chmod 0755 ./magiskboot
./magiskboot unpack -h boot-original.img
cat header
# Apenas se o cabeçalho e a combinação de firmware forem os descritos acima:
sed -i 's/^os_patch_level=2025-05$/os_patch_level=2026-06/' header
cat header
./magiskboot repack boot-original.img boot-spl.img
```

Guarde os cabeçalhos antes/depois e traga `boot-spl.img` ao PC. Confira que a mudança pretendida foi aplicada e que a imagem cabe na partição. Nos aparelhos anteriores, as imagens boot tinham 33.554.432 bytes. Se os campos diferirem, investigue em vez de forçar essa substituição. **Nunca grave o boot com Magisk de outro tablet.**

## 9. Fastbootd: instalar a GSI e o boot preparado

Reinicie do TWRP para **fastbootd**; use a opção correspondente do recovery ou `adb -s SERIAL reboot fastboot`. Confira:

```powershell
& $fastboot devices
& $fastboot -s $serialTablet getvar is-userspace
& $fastboot -s $serialTablet getvar product
& $fastboot -s $serialTablet getvar unlocked
```

Os resultados anteriores foram `is-userspace: yes`, produto `gta7lite` e desbloqueado. Se não houver dispositivo, confira driver do fastbootd antes de culpar o cabo ou voltar a gravar recovery. Neste PC foi usado o driver Google assinado para VID `18D1`, PID `4EE0`.

Confira o tamanho real da partição system e da GSI extraída. Na referência, system tinha 3.412.066.304 bytes, maior que a imagem de 3.202.322.432 bytes. Com identidade, desbloqueio e espaço confirmados:

```powershell
& $fastboot -s $serialTablet flash system 'D:\tablet-sistema2d\imagens\lineage-21.0-arm64_bgN.img'
if ($LASTEXITCODE -ne 0) { throw 'Falha ao gravar system' }
& $fastboot -s $serialTablet flash boot '.\PASTA_DO_NOVO_TABLET\boot-spl.img'
if ($LASTEXITCODE -ne 0) { throw 'Falha ao gravar boot' }
& $fastboot -s $serialTablet reboot recovery
```

Preserve stdout/stderr dos flashes. Nas instalações anteriores apareceu `Invalid sparse file format at header magic`, seguido de conversão/envio sparse em 12 partes, todos `OKAY`, e exit 0. A mensagem isolada não foi uma falha; o que importa é a conclusão de toda a gravação. Não trate um retorno não zero como sucesso.

No TWRP, faça **Format Data final** após instalar a GSI, conforme o procedimento anterior. Confira `/data` montável antes de instalar Magisk.

## 10. Instalar e concluir o Magisk

Esta reprodução usou instalação Magisk pelo recovery, um método legado/depreciado, mas que funcionou com o boot com ramdisk destes aparelhos. Não confundir instalar o APK gerenciador com instalar root no boot.

1. Monte `/data` e crie `/data/adb` com permissão 0700 **antes** do instalador. Isso evita auxiliares acabarem apenas em `/data/magisk`.
2. Envie o APK oficial como ZIP e instale pelo TWRP:

```powershell
& $adb -s $serialTablet shell 'mkdir -p /data/adb && chmod 0700 /data/adb'
& $adb -s $serialTablet push '.\sistema2d-preparacao\arquivos\Magisk-v30.7.apk' /tmp/Magisk-v30.7.zip
& $adb -s $serialTablet shell twrp install /tmp/Magisk-v30.7.zip
```

3. Confira o log, RC=0 e conclusão da gravação do boot. Inicie o sistema. O dono conclui a configuração inicial, conecta ao Wi-Fi e pode pular conta Google, restauração e PIN inicialmente.
4. Reautorize ADB se necessário e instale o mesmo APK como aplicativo Android com `adb -s SERIAL install -r CAMINHO_DO_APK`.
5. Abra Magisk e conclua a configuração adicional/reinstalação solicitada. Nos dois tablets foi necessário finalizar pelo app e reiniciar. No segundo, a reinstalação informou `pre-init storage partition: cache` e `All done`.
6. Autorize o pedido de superusuário do **Shell** quando necessário para os ajustes. Confira `adb -s SERIAL shell su -c id`, esperado `uid=0`, e versão 30.7.

Se aparecer `Incomplete Magisk install` ou faltar `/data/adb/magisk/util_functions.sh`, conclua/repare a instalação pelo app antes de instalar módulos. Verifique o preinit após o reinício: no caminho retornado por `magisk --path`, deve existir o dispositivo de bloco `.magisk/device/preinit` ou `.magisk/block/preinit`. Os scripts locais de conferência fazem essa verificação.

### Ativar Zygisk — obrigatório nesta reprodução

O Zygisk já vem integrado ao Magisk 30.7; não precisa baixar um APK ou ZIP separado. Depois de concluir a instalação do Magisk:

1. Abra **Magisk → Configurações (engrenagem)**.
2. Ative **Zygisk**.
3. Reinicie o tablet. Se houver aviso pedindo Power/Ligar para continuar, siga o aviso.
4. Após o boot, abra Magisk e confirme **Instalado: 30.7 (30700)** e **Zygisk: Sim**. Confira também que `su -c id` continua retornando `uid=0`.

Essa ativação foi confirmada no primeiro tablet após reiniciar em 10/11/2026 e passa a fazer parte da configuração solicitada para os próximos. O botão **Instalar** continua disponível mesmo com o Magisk instalado; ele sozinho não indica falha. O script histórico de conferência de 36 itens não verifica Zygisk: registre essa confirmação adicional no relatório do novo aparelho.

Não preencher a lista de negação com apps arbitrários. Quando o dono indicar um app que precisa dessa configuração, use **Aplicar lista de negação → Configurar lista de negação**, selecione o app e seus processos, force sua parada e abra novamente. Zygisk e lista de negação não garantem ocultar todos os sinais de root. Não instalar módulos adicionais de ocultação automaticamente.

## 11. Instalar a camada Sistema2D

Com Magisk funcional, instale os quatro ZIPs pelo app **Módulos → Instalar do armazenamento**, nesta ordem, ou pela CLI `magisk --install-module` com root. Aguarde sucesso de cada instalação:

1. `sistema2d_tweaks.zip`
2. `sistema2d_bootanim.zip`
3. `sistema2d_ui_ios.zip`
4. `sistema2d_rom_provisioning.zip`

O segundo tablet recebeu os módulos pelo recovery após Magisk; o primeiro, pela CLI após concluir o app. A instalação normal pelo app/CLI com Magisk completo evita a falha de auxiliares encontrada inicialmente. Não basta copiar ZIPs ou diretórios para declarar os módulos instalados.

Instale também o script de inicialização:

```powershell
& $adb -s $serialTablet push '.\sistema2d-preparacao\arquivos\99-aosp-tweaks.sh' /data/local/tmp/
& $adb -s $serialTablet shell "su -c 'mkdir -p /data/adb/service.d && cp /data/local/tmp/99-aosp-tweaks.sh /data/adb/service.d/99-aosp-tweaks.sh && chmod 0755 /data/adb/service.d/99-aosp-tweaks.sh'"
& $adb -s $serialTablet reboot
```

Conteúdo relevante do script, mantido igual à referência:

```sh
sysctl -w vm.swappiness=100
sysctl -w vm.vfs_cache_pressure=100
sysctl -w vm.dirty_ratio=20
sysctl -w vm.dirty_background_ratio=5
setprop wifi.supplicant_scan_interval 180
setprop persist.sys.use_dithering 0
```

Esses valores reproduzem o projeto; ganho individual não foi medido. O módulo tweaks define `persist.traced.enable=0`. Os outros módulos cuidam de boot visual, overlays e idioma. Não alterar `up_param`, proteção térmica, frequências CPU/GPU, SELinux ou política de segurança para buscar desempenho adicional.

Após reiniciar, os quatro diretórios devem existir em `/data/adb/modules/`, sem arquivo `disable`, e os overlays abaixo devem aparecer `[x]` em `cmd overlay list`:

```text
com.sistema2d.theme.corners
com.sistema2d.theme.icon.ios
com.sistema2d.theme.taskbar
com.sistema2d.theme.settings
```

## 12. Interface, rádios e desativações finais

Os scripts originais do Sistema2D propõem animação 0.5; a configuração aprovada aqui usa **0**. Aplique explicitamente:

```powershell
& $adb -s $serialTablet shell wm density 200
& $adb -s $serialTablet shell settings put system font_scale 1.05
& $adb -s $serialTablet shell settings put global window_animation_scale 0
& $adb -s $serialTablet shell settings put global transition_animation_scale 0
& $adb -s $serialTablet shell settings put global animator_duration_scale 0
& $adb -s $serialTablet shell cmd connectivity airplane-mode enable
& $adb -s $serialTablet shell svc wifi enable
& $adb -s $serialTablet shell cmd bluetooth_manager enable
```

Modo avião desliga a rede móvel. Wi-Fi precisa ser religado e conectado. Bluetooth ligado faz parte da referência aprovada; não inventar outra otimização ao reproduzir.

Desative somente estes quatro pacotes extras, para usuário 0, preservando a possibilidade de reativar:

```powershell
& $adb -s $serialTablet shell pm disable-user --user 0 com.google.android.googlequicksearchbox
& $adb -s $serialTablet shell pm disable-user --user 0 com.google.android.apps.wellbeing
& $adb -s $serialTablet shell pm disable-user --user 0 com.google.android.projection.gearhead
& $adb -s $serialTablet shell pm disable-user --user 0 org.lineageos.eleven
```

Confira antes se o pacote existe. Se estiver ausente numa variante diferente, registre a diferença, sem tentar remover outro componente “equivalente”. Salve estado anterior e retorno de cada alteração.

**Preservar:** Play Services, Play Store, framework, SystemUI, launcher, teclado, Downloads, instalador de pacotes, rede, codecs, serviços de acessibilidade e WebView. A GSI escolhida já inclui GApps; o dono pode usá-la sem entrar em conta Google. O objetivo de usar apenas dois aplicativos não autoriza remover dependências do sistema.

## 13. Jelly e NewPipe

Jelly vem com o LineageOS: mantenha `org.lineageos.jelly` como navegador padrão. Não substituir por outro navegador sem pedido do dono. Mantenha o WebView funcional; a versão observada está registrada na tabela de referência, não foi instalada uma versão separada para “acelerar”.

Instale o APK oficial do NewPipe, sem conta Google:

```powershell
& $adb -s $serialTablet install -r '.\sistema2d-preparacao\arquivos\NewPipe_v0.29.1.apk'
```

Abra o app uma vez e configure estas preferências, pela interface ou por alteração controlada do XML com o app parado:

| Chave | Tipo | Valor |
|---|---|---|
| `default_resolution` | string | `720p` |
| `default_video_format` | string | `video_mp4` |
| `default_popup_resolution` | string | `480p` |
| `show_higher_resolutions` | boolean | `false` |
| `preferred_open_action_key` | string | `video_player` |
| `preferred_open_action_last_selected` | string | `video_player` |
| `theme` | string | `auto_device_theme` |
| `night_theme` | string | `dark_theme` |

Arquivo: `/data/user/0/org.schabi.newpipe/shared_prefs/org.schabi.newpipe_preferences.xml`. O script `aplicar-configuracao.py` já altera somente essas chaves, mantém as demais, identifica o UID/GID real e restaura contexto SELinux. Ele exige Lineage correto, root, usuário 0 e `ADB_SERIAL` definido para o destino. Use a cópia privada preparada na seção 5. Não copie toda a pasta de dados do NewPipe do tablet anterior.

MP4/720p foi escolhido para o hardware deste tablet. Na reprodução de referência foi observado decoder AVC MediaTek e o dono confirmou som e imagem normais. Não instalar o YouTube original junto para cumprir este escopo. Se, no futuro, o NewPipe antigo parar de funcionar por mudança do serviço, verifique uma atualização oficial e explique ao dono que isso altera a versão fixada; não usar APK modificado de procedência desconhecida.

## 14. Conferência mínima e entrega

Espere `sys.boot_completed=1` depois do reinício final e confira:

- Lineage build correto, Magisk 30.7 e `su -c id` com root.
- **Zygisk: Sim** na tela do Magisk após reiniciar; confirmação adicional aos 36 itens do script histórico.
- Quatro módulos ativos, quatro overlays `[x]`, Perfetto `0` e preinit Magisk presente.
- Densidade 200, fonte 1.05 e animações 0; configuração apresenta largura `sw640dp` na referência.
- VM em `100 / 100 / 20 / 5`, correspondendo às quatro chaves do script.
- Os quatro pacotes extras desativados para usuário 0.
- Modo avião ligado, Wi-Fi conectado e Bluetooth ligado.
- Jelly abre uma página simples; NewPipe abre e mantém as preferências acima.
- Se necessário para confirmar funcionamento inicial, reproduza um vídeo curto e peça ao dono confirmar imagem/som. Evite bateria de testes ou benchmarks.

O script `conferir-configuracao.py` compara 36 itens e grava `conferencia-final.json`. Use as cópias privadas e `ADB_SERIAL` da seção 5; confira o alvo no JSON antes de aplicar. Depois de instalar ROM, Magisk, módulos e NewPipe, execute na mesma sessão:

```powershell
python .\tablet-local\aplicar-configuracao.py
if ($LASTEXITCODE -ne 0) { throw 'Falha ao aplicar ajustes; investigar antes de continuar' }
python .\tablet-local\conferir-configuracao.py
if ($LASTEXITCODE -ne 0) { throw 'Falha na conferência; investigar o relatório' }
```

Leia o relatório e confirme os campos `confere`; confira Zygisk separadamente na interface. Um resultado histórico 36/36 não prova que o aparelho novo passou. A conferência de configuração também não substitui a abertura básica dos dois apps.

Registre versões, hashes, identidade, backups próprios, comandos/retornos, diferenças e limitações em `tablet-local/resultado.md`. Não publique essa pasta nem use `git add -f` para contornar o `.gitignore`. Não declare PIN, câmera, telefonia, atualização OTA ou duração de bateria testados se não foram. Nos dois tablets anteriores, o dono aprovou o resultado; não existe percentual de velocidade confiável medido para essa migração.

## 15. Problemas já encontrados

| Sintoma | Conduta que resolveu ou ponto a verificar |
|---|---|
| ADB não mostra o tablet | Cabo de dados, Depuração USB e aceitar autorização na tela. |
| Tablet liga normal ao tentar entrar no aviso | Desligar de verdade; segurar os dois volumes antes de conectar, sem Ligar. |
| Long press entra em Continue | Conferir linha Device unlock mode, tirar capinha e verificar contato do botão. |
| Download não lista os campos esperados | A tela simplificada pode omitir campos; cruzar ADB anterior, detect e PIT. |
| Sessão Download USB falha | Reiniciar fisicamente o modo e conferir resultado anterior antes de reenviar. |
| Saiu de Download, mas não entrou em TWRP | Fazer a troca imediata Ligar+Volume baixo → Ligar+Volume alto. |
| Fastbootd não aparece no Windows | Conferir driver Google para esse modo; driver Samsung de Download é outra conexão. |
| `/data` ilegível ou 0 MB | Conferir Format Data e reboot para recovery; não só wipe cache. |
| Magisk incompleto | Concluir reinstalação pelo app, reiniciar e verificar auxiliares/preinit. |
| Módulos instalados, overlays ausentes | Conferir logs, root, instalação completa e reinício; não copiar APKs sem contexto. |
| Python não inicia ADB no sandbox | Nesta sessão apareceu `Cannot mkdir '\\.android'`; ADB direto no PowerShell funcionava. Corrigir ambiente/permissão do processo, sem enfraquecer o tablet. |

Drivers no Windows podem exigir elevação real de administrador/UAC. Nesta sessão, pedir execução fora do sandbox não elevou automaticamente o processo. Quando necessário, foi usado processo com `Start-Process -Verb RunAs`; o dono confirma o UAC. Não exibir nem coletar credenciais.

## 16. Recuperação e limites de reversão

Interface, animações e os quatro pacotes podem ser restaurados pelos valores anteriores registrados. Módulos podem ser desativados no Magisk e o tablet reiniciado. O `rollback-ajustes.ps1` local faz só uma reversão parcial dentro da GSI e usa `ADB_SERIAL`: confira o destino e o estado anterior salvo nesse aparelho antes de usar. Não restaura a ROM Samsung, FBE ou Knox.

Retorno completo requer firmware Samsung compatível AP/BL/CP/CSC, conferência do estado atual e procedimento separado de gravação/apagamento. O firmware exato dos dois primeiros aparelhos está preservado em `D:\tablet-sistema2d\firmware-samsung`. Não reutilize cegamente em uma revisão de bootloader diferente. Não copiar boot de outro dispositivo nem seus identificadores. Não bloquear o bootloader com imagens modificadas instaladas.

Este documento substitui, para a reprodução futura, pedidos anteriores de instalar aplicativos adicionais. A entrega pretendida é a configuração Sistema2D/Lineage descrita, com **Jelly + NewPipe** para uso diário.
