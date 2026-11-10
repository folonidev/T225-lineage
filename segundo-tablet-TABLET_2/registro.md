# Segundo SM-T225 — reprodução da configuração aprovada

Serial ADB alvo: TABLET_2. Primeiro tablet: TABLET_1 (não alterar).
Autorização: repetir instalação completa de LineageOS/Sistema2D, apagamento, desbloqueio, Magisk/root e consequências permanentes do Knox conforme conversa. Sem repetir benchmarks; apenas verificações essenciais de identidade, compatibilidade, gravação e funcionamento.

Baseline alvo: LineageOS21 20260614 arm64_bgN; Magisk30.7; TWRP gta7lite v2.2; Sistema2D v1.0.0 (quatro módulos e service.d); densidade200, fonte1.05, animações0; Jelly + NewPipe0.29.1 oficial MP4/720p; modo avião com WiFi ligado e Bluetooth ligado; desativar GooglePesquisa, BemEstarDigital, AndroidAuto e Eleven. Não copiar contas, credenciais, dados pessoais, imagens de boot com Magisk de outro aparelho, modem/EFS/NVRAM ou identificadores do primeiro.

Pré-checagem: SM-T225/ZTO confirmado, firmware T225XXSBEYE1 Android14 patch2025-05 igual ao primeiro; usuário0, bateria71%; OEM unlocking autorizado=1; bootloader ainda locked; Knox warranty0. Firmware Samsung correspondente já disponível para recuperação. Aguardando desbloqueio físico e verificação posterior antes de qualquer flash.

knox.kg.state=Checking, ro.boot.kg.bit=00, WiFi conectado. Estado de KG difere do primeiro antes do unlock, mas Checking e aceito pelo procedimento oficial; verificar novamente apos unlock/online. Tablet desligado via reboot -p, instrucoes fisicas de unlock enviadas. Hashes dos nove artefatos menores da release comparados e iguais; sem novo download ou atualizacao de versao. Nenhum flash enviado ao segundo tablet.

Dono confirmou em09/11 que conseguiu o desbloqueio fisico e tablet reiniciando. Aguardando verificacao por ADB antes de gravar qualquer imagem.

ADB confirmou desbloqueado=0 e vbmeta=unlocked, OEM1, firmwareT225XXSBEYE1. Download confirmado SM-T225, identificadorH154758300CCFD002E99 (exclusivo do segundo). Gravar recovery e vbmeta pelos nomes de arquivo correspondentes ao PIT lido pela ferramenta, sem reboot e sem reparticionar.

Gravacao de recoveryTWRP e vbmeta concluida com exit0, arquivos associados aos nomes de particao do PIT lido no proprio segundo tablet. --no-reboot mantido. Log flash-recovery.log. Aguardando entrada fisica em TWRP; ainda nao alterados system/boot/dados pelo instalador.

TWRP3.7.1 e hashes de recovery/boot confirmados; formatacaoinicial concluida e recoveryreiniciado. Fstabsoriginais salvos, FBEdisableraplicado. Bootproprio lido do dispositivo e preparado comSPL2026-06 para mesmaGSI; originalpreservado, semcopiarbootmodificadodoprimeiro.

Lineage system e boot-SPL gravados com fastboot exit0; formatacao final realizada. Magisk30.7 instalado (RC0), auxiliares em/data/adb/magisk. Quatro modulos instalados pelo recovery e scriptservice.d copiado. Primeiro boot iniciado a seguir.

Ajustes finais aplicados pelo scriptcomvalidacaoSerial/ROM/usuario: density200,font1.05,anims0,aviao1,wifi eBluetoothligados,4desativacoes epreferenciasNewPipewhitelist semhistorico. WiFi reconectado. AppMagisk env_checkpediu fullfixporfaltaPREINIT; reinstalacaooficialpeloapp concluida, logUIindica pre-init storage partition=cache eAllDone. CapturaXMLmagisk-next.xml. ReinicioparaativarnovoBootMagisk.

Concluido: conferencia aposreboot com36de36itenscorrespondentes, incluindoPREINITMagiskpresente. JellyeNewPipeabrem. Relatorioresultado.md salvo. Sembenchmarkstestsprolongados conforme pedido.
