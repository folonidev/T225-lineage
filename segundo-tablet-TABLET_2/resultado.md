# Segundo Galaxy Tab A7 Lite SM-T225 — configuração replicada

Concluído em 09/11/2026. Segundo tablet: serial ADB TABLET_2; identificador Download DOWNLOAD_ANONIMIZADO. O primeiro tablet TABLET_1 não foi alterado nesta instalação.

A configuração registrada do primeiro tablet foi reproduzida e conferida após o reinício final: 36 itens de configuração correspondentes, incluindo versões, módulos, preferências e desativações. Não foram repetidos benchmarks ou testes prolongados, conforme solicitado.

- LineageOS 21 / Android 14, build 21.0-20260614-UNOFFICIAL-arm64_bgN, mesma imagem da primeira instalação.
- TWRP 3.7.1_12-1, Magisk 30.7 oficial e quatro módulos Sistema2D: tweaks, bootanim, ui_ios, rom_provisioning. Quatro overlays ativos e Perfetto desativado conforme o projeto.
- Boot extraído deste próprio segundo tablet, original preservado em boot-original.img; SPL do cabeçalho alinhado a 2026-06 para compatibilidade com a GSI, e Magisk instalado neste aparelho. A reinstalação pelo app Magisk concluiu o armazenamento de preinit em cache. O ajuste do cabeçalho não representa novas correções de kernel.
- Densidade 200 dpi, fonte 1.05, animações em 0; mesmo script service.d e parâmetros VM 100/100/20/5 do primeiro.
- Navegador Jelly e NewPipe 0.29.1 oficial, com MPEG-4, 720p, popup 480p, ação padrão player de vídeo e tema automático. As preferências foram copiadas por lista permitida; contas, senhas e histórico do primeiro tablet não foram transferidos.
- Google Pesquisa/assistente, Bem-estar Digital, Android Auto e Eleven desativados para o usuário 0, como no primeiro.
- Modo avião ligado, Wi-Fi conectado e Bluetooth ligado, correspondentes à configuração alvo.

Os dois apps abriram após o reinício. O registro limita-se a instalação, correspondência de configuração e abertura básica; não declara um benchmark comparativo ou teste prolongado de reprodução.

Os dados do tablet foram apagados, o bootloader foi desbloqueado e a instalação inclui root e FBE desativado, como autorizado para repetir o primeiro. O firmware Samsung original correspondente T225XXSBEYE1/ZTO continua disponível em D:\tablet-sistema2d\firmware-samsung para recuperação. Retornar ao Samsung exige outro procedimento de gravação/apagamento e não restaura o fusível Knox. Não bloquear o bootloader com a GSI instalada.

Arquivos úteis:
- config-alvo.json: configuração de referência aprovada.
- conferencia-final.json: valores finais conferidos, todos correspondentes.
- registro.md e logs flash-*.log: etapas e resultados de gravação.
- estado-antes-ajustes.json e alteracoes.jsonl: estado anterior e ajustes desta etapa.
- rollback-ajustes.ps1: restaura interface e quatro pacotes ao estado anterior dentro desta GSI; não restaura a ROM Samsung e não remove módulos.
- boot-original.img, fstabs originais e boot-header-original.txt: originais deste segundo aparelho.

O problema de PS Remote Play investigado no primeiro não faz parte da configuração base replicada. Não foram aplicados módulos adicionais de ocultação ou alterações de DenyList.

## Apps adicionais solicitados

WhatsApp oficial instalado por ADB a partir do APK vinculado em whatsapp.com/android (CDN scontent.whatsapp.net), sem depender de login Google. Origem e hash registrados em apps-adicionais/whatsapp-origem.json. Instalação retornou Success. Registro/vinculação de conta ainda depende do dono no próprio app; nenhuma mensagem foi enviada e nenhum dado de conversas foi consultado.

Solicitada instalação de Word/Excel/PowerPoint para uso offline. Play Store está instalada, mas a página do Word abriu em modo sem autenticação; aguardando login pelo dono ou escolha de suíte alternativa. Nenhuma assinatura ou compra autorizada/realizada.

Atualização: localizado APK Microsoft Office Older version diretamente em microsoft.com/download/details.aspx?id=100590, arquivo16.0.16827.20278 arm64. Download efetuado de download.microsoft.com; origem/hash em apps-adicionais/office-origem.json. Tentativa de instalação recusada com INSTALL_FAILED_VERIFICATION_FAILURE (Install not allowed). Office não instalado; edição offline não testada. Nenhuma configuração de verificação/segurança foi desativada. WhatsApp2.26.44.76 oficial permanece instalado.

Atualização da instalação Office: o APK oficial pôde ser instalado pela confirmação interativa no tablet. Pacote com.microsoft.office.officehubrow presente, versão16.0.16827.20278, contendoWord/Excel/PowerPoint. A conclusão anterior de que a recusa do ADB impediria a instalação estava incorreta. APK disponível em /sdcard/Download/Microsoft-Office-oficial.apk. Nenhuma configuração global de verificação foi desligada. App abriu a configuração inicial, aguardando opção do dono por uso local ou contaMicrosoft; ediçãooffline ainda não foi validada naUI. WhatsApp2.26.44.76 oficial já instalado.
