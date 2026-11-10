# Resultado: LineageOS + Sistema2D no SM-T225

Instalação concluída em 01/11/2026, com autorização explícita do dono para apagar dados, desbloquear bootloader, instalar GSI/root e alterar permanentemente Knox. Serial ADB TABLET_1. Modelo SM-T225 confirmado antes da troca; no modo Download, modelo SM-T225 e identificador DOWNLOAD_ANONIMIZADO confirmados. Após a GSI, o modelo lógico aparece como TrebleDroid with GApps, o que é esperado da imagem genérica.

## Instalado e aplicado

- LineageOS 21 Android 14, build 21.0-20260614-UNOFFICIAL-arm64_bgN, fornecida na release Sistema2D v1.0.0. SHA-256 da imagem comprimida conferido com digest da release.
- TWRP 3.7.1_12-1 (release gta7lite v2.2). Hash do recovery efetivamente gravado conferiu com o arquivo baixado.
- Magisk 30.7 oficial, acesso root verificado com su -c id. Configuração adicional do app concluída e reinício realizado.
- Quatro módulos Sistema2D instalados e presentes após reboot: tweaks, bootanim, ui_ios e rom_provisioning. Os quatro overlays com.sistema2d.theme.* aparecem habilitados [x]. Perfetto persist.traced.enable=0.
- Densidade de 200 dpi e sw640dp para interface de tablet, fonte 1.05, três escalas de animação em 0. Animações eliminadas reduzem esperas visuais; não aumentam potência de processamento.
- Script 99-aosp-tweaks.sh da release instalado em service.d; swappiness=100, vfs_cache_pressure=100, dirty_ratio=20 e dirty_background_ratio=5 conforme projeto. Valores anteriores salvos em vm-anterior-*.txt. Ganho individual desses ajustes não foi medido.
- Modo avião ligado, Wi-Fi conectado, Bluetooth preservado ligado conforme estado anterior desta instalação.
- Navegador Jelly do LineageOS preservado como navegador padrão. WebView ativo com.android.webview 149.0.7827.114.
- A pedido do dono, NewPipe oficial 0.29.1 instalado no lugar do YouTube original. Sem login Google. APK baixado de TeamNewPipe/NewPipe; SHA-256 18447bfb1e06d113edc88df93f471827280de06f6f3d4dc42f56f28b9c1bab79 conferido com digest da release. Preferências: MPEG-4 e resolução padrão 720p. Preferências anteriores guardadas em newpipe-preferencias-anteriores.xml.

## Compatibilidade e consequências

Boot original preservado no PC; sua identidade foi comparada ao boot real do tablet antes de alterar. A imagem original indicava patch level 2025-05; o cabeçalho da cópia para instalação foi alinhado a 2026-06 para corresponder à GSI e evitar incompatibilidade de Keymaster/PIN documentada nesta família. O ajuste não instala correções novas no kernel. Magisk depois preparou o ramdisk no próprio tablet. Não foi usado boot.img modificado de outro aparelho.

Dados foram formatados. FBE foi desativado conforme procedimento da GSI, mediante alteração dos fstabs de vendor. Arquivos originais estão salvos localmente. A área de dados desta instalação não deve ser considerada protegida por criptografia de arquivos. Knox warranty_bit passou de 0 para 1; reinstalar Samsung não desfaz esse fusível. Bootloader continua desbloqueado; não tentar bloqueá-lo com esta GSI instalada.

Nenhuma troca de bootloader/modem, reparticionamento, alteração de up_param, proteção térmica, frequência de CPU/GPU ou SELinux foi feita por comandos de ajuste. As mudanças de boot/AVB necessárias ao root e à GSI fazem parte da instalação autorizada.

## Verificado

Primeiro boot e reinícios posteriores concluídos, sys.boot_completed=1. Configuração inicial concluída pelo dono. Wi-Fi reconectou após o reboot com módulos, modo avião mantido, Bluetooth ligado. Jelly carregou https://example.com com conteúdo renderizado. Teclado LatinIME apareceu (mInputShown=true); entrada de teste na barra de endereços cancelada sem navegação.

NewPipe reproduziu Big Buck Bunny sem anúncio observado. Sessão de mídia PLAYING, saída de áudio em alto-falante sem mute e capturas de quadros do vídeo registradas. Dono confirmou “Sim, imagem e som normais”. Componentes de decodificação c2.mtk.avc.decoder e c2.android.aac.decoder relacionados ao PID do NewPipe foram registrados. Isso comprova seleção do decoder AVC MediaTek neste fluxo; o nome sozinho não é uma medição de aceleração ou consumo. A preferência por MP4 evita priorizar o AV1 usado por software no teste anterior do YouTube oficial.

Temperatura da bateria em torno de 37 °C durante os testes. Nenhum ANR registrado desde o último boot. Não há validação prolongada de bateria, todos os tipos de vídeos, câmera, telefonia, PIN pós-reboot ou atualização do sistema. Esses itens não foram declarados aprovados.

## Medidas e limites da comparação

Pacotes habilitados: Samsung original 345; Lineage final 257. São pacotes, não processos. Na coleta final, MemAvailable=991428 kB e armazenamento de dados com cerca de 20 GB livres, 1,9 GB usados. A diferença de armazenamento também decorre do apagamento autorizado, não apenas da ROM.

Não há percentual confiável de ganho de velocidade: ROM, versões e aplicativos mudaram; NewPipe/Jelly não equivalem aos antigos YouTube/Samsung Internet. O teste funcional foi aprovado pelo dono, mas não constitui benchmark comparável. A limitação física de aproximadamente 3 GB de RAM permanece.

## Recuperação

Firmware Samsung original exato T225XXSBEYE1/ZTO obtido do servidor Samsung e preservado em D:\tablet-sistema2d\firmware-samsung. Pacotes AP/BL/CP/CSC/HOME_CSC extraídos com CRC ZIP e MD5 validados. Caminhos em firmware-verificado.json. PIT original em tablet-original.pit. Originais boot/recovery/vbmeta e cabeçalhos em imagens-pequenas/.

Os ajustes de interface podem ser revertidos com os valores de ajustes-estado-anterior.json. Módulos podem ser desativados pelo app Magisk e reiniciando. Isso não restaura o Android Samsung: retorno completo exige gravação do firmware original adequado e novo apagamento, com verificação do estado do aparelho antes. Não executar rollback da limpeza Samsung antiga como se fosse rollback desta ROM.

Fontes: https://github.com/Sistema2D/SM-T225 (commit 79069eaafcdfa5e8406e0571d11bcbd27d89252e); https://github.com/TeamNewPipe/NewPipe/releases/tag/v0.29.1; https://topjohnwu.github.io/Magisk/install.html. Logs de gravação, hashes, capturas e estado permanecem locais nesta pasta.

## Limpeza adicional solicitada após a entrega

Desativados de forma reversível Google Pesquisa/assistente (com.google.android.googlequicksearchbox), Bem-estar Digital (com.google.android.apps.wellbeing), Android Auto (com.google.android.projection.gearhead) e player Eleven (org.lineageos.eleven). Todos eram apps extras presentes e tinham processos residentes no diagnóstico. Nenhuma acessibilidade estava configurada nesse momento; serviços de acessibilidade foram preservados. Play Services, Play Store, framework, launcher, teclado, rede, codecs e WebView mantidos.

Estado anterior default registrado antes de cada alteração. Lista e comandos em limpeza-adicional/alteracoes.csv; reversão específica e com validação de serial/ROM/usuário em limpeza-adicional/rollback.ps1. Navegador e NewPipe abriram com Status: ok após a limpeza. Não houve benchmark comparável para atribuir um percentual de ganho. O relatório anterior de 257 pacotes habilitados passa a 253 após esta etapa. O número de pacotes não é número de processos.
