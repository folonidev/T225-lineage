# Otimização do Galaxy Tab A7 Lite SM-T225

01/11/2026. Serial TABLET_1; usuário ativo 0; Android 14 Samsung, build UP1A.231005.007.T225XXSBEYE1.

33 pacotes de fábrica desativados em seis lotes, preservando dados. A lista individual com motivo, estado original, comando e reversão está em alteracoes.csv. Inclui recomendações promocionais, Samsung Free/Bixby/rotinas/Edge, launcher de jogos, instaladores Kids/Wearable, Smart Switch, integrações com PC, clima, papéis dinâmicos e editores opcionais da galeria.

Pacotes habilitados: 345 → 312. Isso não é contagem de processos rodando. Modo avião ativado por cmd connectivity, com Wi-Fi religado e reconectado. Bluetooth estava desligado e permaneceu desligado; telefonia/IMS/RIL preservados.

As três animações já estavam em 0.0 e não foram alteradas. Sem ganho novo de animações nesta sessão. Eliminar animações reduz esperas visuais, sem aumentar potência de processamento.

## Medições antes/depois (antes de reiniciar)

Atividades reais descobertas por Package Manager. Aquecimento antes da série, três aberturas com force-stop e am start -W. Mesmos apps/versões, rede e animações. Arquivos exploratórios de abertura foram substituídos pelas séries válidas.

| App | TotalTime antes (ms) | TotalTime depois (ms) | Medianas (ms) | Variação observada |
|---|---|---|---|---|
| Samsung Internet, padrão | 2090,1584,1831 | 1758,1388,1326 | 1831 → 1388 | 24,2% menor |
| Chrome | 1562,1517,1461 | 1562,1600,1318 | 1517 → 1562 | 3,0% maior |
| YouTube | 2714,2867,2861 | 3183,2816,2664 | 2861 → 2816 | 1,6% menor |

Fórmula: (antes - depois) / antes * 100. São variações de abertura desta amostra, não ganho causal comprovado ou benchmark geral. Temperatura da bateria ao final das séries: 35 °C antes e 37 °C depois. Sem controle do conteúdo remoto/página/vídeo e sem condições térmicas idênticas: os percentuais não podem ser atribuídos apenas à limpeza. TotalTime não mede carregamento completo da página/vídeo.

MemAvailable: 936904 → 861112 kB em instantes e cargas diferentes; não aumentou nesta coleta e isoladamente não mede velocidade. MemTotal: 2823436 kB (aprox. 2,69 GiB). Armazenamento: cerca de 22 GB totais, 7,5 GB usados e 15 GB livres; desativar preserva APKs e dados e não libera grande espaço.

## Preservados e escolhas

Samsung Internet, Chrome, YouTube oficial, Google Play Services, Play Store, GSF, WebView ativo (com.google.android.webview 155.0.8059.43), Galaxy Store, contas e sincronização. Olauncher padrão e sua acessibilidade, demais launchers, teclado Samsung, Pinterest e apps pessoais preservados. Gmail/Maps mantidos para preservar acesso a possíveis dados pessoais.

SystemUI, Configurações, segurança, Knox, instalador/verificador/permissões, arquivos/documentos/downloads, rede, áudio/vídeo, codecs, telefonia e gestão térmica/bateria mantidos. Game Optimizing Service e Smart FPS Adjuster mantidos porque gerenciam desempenho e não há evidência de benefício para este uso. Serviços compartilhados de papel incerto e nuvem preservados.

Suporte a compilação consultado em cmd package help; mantida política padrão por falta de justificativa medida para forçar speed. Sem limpeza de caches, root, flash, reset, exclusão de dados, alteração de CPU/GPU, zRAM, resolução ou atualizações.

## Validação

Em cada lote, Configurações, Olauncher, Samsung Internet e YouTube retornaram Status: ok na abertura. Teclado listado e Wi-Fi conectado. Não comprova renderização completa, digitação ou reprodução. Captura exploratória do YouTube mostrou tela escura durante inicialização; nenhum ANR registrado antes do reboot.

Reinicialização comandada após os lotes. Validação final pós-reboot será registrada abaixo. Pendentes até teste visual: desbloqueio, digitação, página pela internet, reprodução com imagem/áudio por alguns minutos, codec efetivo, instalação/atualização, download e seletor de arquivos. Não houve instalação de apps ou download pessoal para testar.

## Recuperação

rollback.ps1 valida serial, modelo e usuário antes de restaurar somente as alterações registradas nesta sessão. Restaura default-state nos pacotes originalmente default, não habilita pacotes previamente desativados e retorna modo avião desligado/Wi-Fi ligado. Em PowerShell com política restrita, usar powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\rollback.ps1 a partir desta pasta, no mesmo perfil Windows autorizado no tablet. Bypass vale apenas para esse processo. O script não foi executado, para preservar a otimização.

Referência: https://github.com/cavaleiro-ai/Tirando-defeito-programado-dos-tablets no commit 1b7e6f46d8aac5f969a6ed5db9010a0022dddf58. README e guia lidos e salvos em referencia/. Projeto para outro hardware (SM-X200/Unisoc); sua lista e comandos de limpeza/compilação global não foram aplicados.

Conclusão: Samsung Internet abriu mais rápido nesta amostra. Chrome não melhorou; YouTube ficou próximo do anterior. Sem evidência para afirmar melhora global ou na reprodução. Limite de cerca de 3 GB de RAM permanece. LineageOS fica para tarefa separada.

## Validação final pós-reinício

sys.boot_completed=1. Usuário desbloqueou a tela; verificação mostrou mDreamingLockscreen=false. As 33 desativações persistiram. Modo avião=1 e Wi-Fi reconectado. Configurações, launcher, navegador e YouTube abriram após o reboot. Samsung Internet carregou https://example.com, com conteúdo renderizado em browser2.png.

YouTube reproduziu Big Buck Bunny (Blender) com capturas mostrando quadros diferentes e sessão PLAYING. Saída de áudio reportada no alto-falante, mídia sem mute e volume 1/15; confirmação auditiva depende do dono. Nenhum ajuste de volume foi feito.

Gargalo observado no teste: media.resource_manager relacionou o processo do YouTube (PID 7553) a decoder AV1 c2.android.av1-dav1d.decoder em execução, 854x480/30 fps, explicitamente sw codec: yes e allocated hw codec count 0. Portanto este teste usou decodificação de vídeo por software, não há evidência de aceleração por hardware neste fluxo. Nenhum codec ou configuração de renderização foi desativado. Outros vídeos/formatos podem usar caminhos diferentes.

A temperatura da bateria estava em 37 °C durante a reprodução. Logs técnicos e capturas ficam somente nesta pasta local. Ainda pendentes: teste de instalação/atualização, download/seletor de arquivos e confirmação auditiva/fluidez pelo dono. Esses testes não foram declarados aprovados.

Atualização final: o dono confirmou “Sim, imagem e som normais” no vídeo de teste. Teclado Samsung abriu visualmente na barra de endereços (mInputShown=true); entrada de texto de teste enviada sem confirmar navegação e depois cancelada. Capturas em teclado.png/digitacao.png. No encerramento, às 17:06, o navegador estava em primeiro plano, portanto não foi possível certificar reprodução ininterrupta por vários minutos; teste prolongado permanece pendente. Temperatura: 37 °C; nenhum ANR desde o boot. Tablet deixado no launcher. Confirmação auditiva deixou de ser pendência.
