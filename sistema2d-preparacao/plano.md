# Preparação da instalação Sistema2D

Aparelho: Samsung SM-T225, serial TABLET_1, CSC ZTO, build/bootloader T225XXSBEYE1 (binário B), Android 14, patch 2025-05-01. Bateria inicial 96%. Bootloader locked, warranty_bit=0, sys.oem_unlock_allowed=0. Nenhum desbloqueio ou flash executado nesta preparação.

O dono confirmou que pode perder os dados. A autorização anterior no MD proibia desbloqueio, root e flash; ainda é necessária a confirmação específica da mudança de escopo e da alteração permanente do Knox antes de iniciar.

Fonte Sistema2D: commit 79069eaafcdfa5e8406e0571d11bcbd27d89252e; release v1.0.0. Arquivos da release baixados e SHA-256 conferidos contra os digests da API GitHub. Magisk-v30.7.apk também corresponde ao digest do repositório original topjohnwu/Magisk. Fontes salvas em fontes/; binários em arquivos/.

Driver Samsung baixado de developer.samsung.com, assinatura Authenticode Valid com publicador Samsung Electronics. Apenas baixado; não instalado.

Ferramenta adicional samloader 2.2.0 obtida de topjohnwu/samloader-rs, indicada na documentação oficial do Magisk. Hash validado contra o digest da release. Até aqui somente help, consulta e download foram executados; nenhum comando flash.

C: tem aproximadamente 0,54 GiB livres. A extração da GSI e o firmware de recuperação estão sendo preparados em D:\tablet-sistema2d. Não foram excluídos arquivos pessoais para liberar espaço.

Servidor Samsung consultado via samloader: firmware ZTO mais recente é T225XXSBEYE1/T225OWOBEYE1/T225XXSBEYE1/T225XXSBEYE1, igual à instalação atual. Download iniciado diretamente do serviço Samsung para D:\tablet-sistema2d\firmware-samsung. Extrair e validar pacotes antes de usar como recuperação.

## Sequência prevista

1. Concluir download/extracao/verificacao da GSI e firmware original. Confirmar conteúdo e tamanho da imagem; preservar BL/AP/CP/CSC originais no PC.
2. Autorizar explicitamente instalação de LineageOS GSI + Sistema2D, desbloqueio, apagamento, root e alteração permanente do Knox.
3. Habilitar desbloqueio OEM na tela do tablet; confirmar OEM Lock e KnoxGuard no modo Download. Não contornar bloqueio de conta/KnoxGuard. Se não permitir, parar sem gravar.
4. O dono confirma desbloqueio com botões físicos. Tablet será apagado. Reconectar à rede e conferir estado de desbloqueio; reautorizar ADB.
5. Conferir identidade no modo Download e tabela PIT antes de gravar. Instalar recovery compatível, sem reparticionar. Reinício para recovery exige botões e coordenação com o dono.
6. Capturar boot/vbmeta originais em recovery e conferir tamanhos/hashes. Preparar Magisk com a imagem correta no próprio tablet. O guia Sistema2D omite parte desta etapa; não usar boot.img de outra pessoa nem presumir que instalar o APK basta para root.
7. Instalar a GSI e os componentes necessários conforme o estado real do recovery/partições. Não gravar bootloader, modem ou up_param por estética. Sem alteração térmica/CPU/GPU.
8. Primeiro boot, configuração e verificação de Wi-Fi, áudio, vídeo, teclado, Google/YouTube e login pelo dono. Aplicar módulos revisados e ajustes adequados ao objetivo; não executar o script do autor diretamente porque contém caminho de outro PC e não fixa serial.
9. Reiniciar, medir novamente, registrar desempenho e limitações. Restaurar firmware Samsung completo se houver regressão impeditiva.

## Achados da revisão

- O guia requer root/Magisk e desativação de criptografia de arquivos. O fbe_disabler altera fstabs em vendor; não é somente um tema reversível dentro do Android atual.
- O script de interface muda densidade para 200 e animações para 0.5; isso não deve ser aplicado automaticamente no Samsung atual nem tratado como aumento de processamento. Neste tablet as animações já estão em 0.
- Parte dos módulos muda apenas aparência/idioma/boot. Não há garantia de ganho no navegador ou vídeo.
- O módulo de boot escreve framebuffer e força brilho durante o boot; é cosmético e pode ser omitido se contrariar o objetivo de simplicidade.
- O script de sysctl modifica políticas de memória. Avaliar após medir o sistema novo; não aplicar por promessa genérica de desempenho.
- Existe issue aberta sobre extração de boot.img para Magisk (issues.json).
- Voltar ao firmware original não restaura o fusível Knox após alteração.

Estado atual: preparação em andamento; nenhuma alteração de ROM no tablet. Não há garantia de compatibilidade completa até testar o sistema instalado.

## Preparação concluída no PC

Todos os 10 arquivos da release Sistema2D baixados com SHA-256 correspondente ao digest publicado. GSI extraída com validação gzip/CRC: 3.202.322.432 bytes; ext4 identificado, tamanho inferior à partição system atual (6.664.192 setores de 512 bytes = 3.412.066.304 bytes). Conferir novamente os nomes/tamanhos em recovery antes de gravar.

Firmware Samsung original baixado do servidor Samsung, cinco pacotes AP/BL/CP/CSC/HOME_CSC extraídos com CRC ZIP válido e MD5 verificado por samloader (exit 0). boot.img.lz4 original extraído de AP. Caminhos em firmware-verificado.json; arquivos grandes em D:\tablet-sistema2d. Driver oficial com assinatura válida disponível, instalação ainda pendente e dependente de permissões do Windows.

Dono confirmou opção Desbloqueio OEM visível e desligada; não foi ativada. Confirmou também que pode perder os dados. Ainda falta consentimento específico para desbloqueio/root/flash e alteração permanente de Knox, pois a autorização original do MD vedava essas ações.

Nenhum comando flash, format, unlock ou alteração de partição executado. Esta preparação deixa arquivos e procedimento prontos para a próxima etapa; compatibilidade prática e possibilidade de gravação só podem ser confirmadas no modo Download/recovery. Preparação de boot Magisk no próprio aparelho e validação do boot continuam etapas da instalação, não procedimentos já realizados.

Autorizacao atualizada: o dono declarou 'esqueça o md. eu quero.' apos ser informado sobre desbloqueio, flash, root, apagamento e Knox. Autorizada a instalacao; nao solicitar novamente o mesmo consentimento.

Continuação: autorização explícita recebida para instalação completa; OEM unlocking habilitado (sys.oem_unlock_allowed=1). Tablet reiniciado em Download somente para leitura. Windows reconheceu USB VID_04E8 PID_685D; samloader estabeleceu protocolo e salvou PIT original de 16384 bytes, sem flash e sem reboot automático. Driver Samsung instalador retornou 8; dispositivo acabou reconhecido no modo Download e leitura PIT funcionou. Identificação textual pela API samloader veio vazia, portanto não foi tratada como confirmação independente de modelo. Modelo SM-T225/serial foram confirmados por ADB imediatamente antes de entrar neste modo. Aguardando entrada manual na tela de aviso/Device Unlock Mode.

Dono confirmou tela de aviso com 'Volume up long press: Device unlock mode'. Orientada confirmacao fisica de desbloqueio; aguardando resultado. Nenhum flash enviado.

Dono confirmou desbloqueio fisico em Device Unlock Mode; aparelho apagando/reiniciando. Aguardando Android e verificacao tecnica do estado antes de flash.

Pre-flash: ADB confirmou SM-T225, ro.boot.flash.locked=0, vbmeta.device_state=unlocked, OEM=1. Recovery TWRP e vbmeta da release verificados e encaixam nas particoes PIT. Originais recovery/vbmeta extraidos do firmware correspondente para recuperacao.

Download confirmou modelName=SM-T225 e serialNumber=DOWNLOAD_ANONIMIZADO (identificador do protocolo Download, diferente do ADB). Flash planejado: recovery TWRP + vbmeta desabilitado, --no-reboot; nenhuma reparticao.

Flash concluido sem erro (samloader exit 0): IDs 39 recovery e 14 vbmeta da release Sistema2D, --no-reboot. Identidade Download confirmada modelName SM-T225, serial DOWNLOAD_ANONIMIZADO imediatamente antes. Log flash-recovery-ids-tentativa2.log. Verificacao funcional pendente de entrada no TWRP; dono orientado a reiniciar diretamente para recovery.

TWRP funcional confirmado via ADB recovery, root, versao3.7.1_12-1. Hash recovery no dispositivo confere com imagem. Boot dispositivo confere com firmware original. Format Data concluido (twrp RC=0), recovery reiniciado. Fstabs originais de vendor salvos e fbe_disabler aplicado (updater RC=0). GSI offline: Lineage21 20260614, SPL2026-06-01. Boot SPL-alinhado preparado pelo magiskboot oficial no proprio tablet: os_patch_level2025-05->2026-06; os_version e kernel mantidos, recompressao feita pela ferramenta. Isso e ajuste de compatibilidade, nao atualizacao de seguranca do kernel. Boot SPL ainda nao gravado.

Fastbootd confirmado is-userspace=yes, product=gta7lite, serial TABLET_1, unlocked=yes. Driver oficial Google VID18d1PID4ee0 assinado instalado via pnputil elevado exit0. GSI system gravada em12partes, fastboot exit0; boot SPL gravado exit0. Reinicio para recovery para formatacao final e preparacao Magisk. Logs flash-lineage-system.log e flash-boot-spl.log. Mensagem 'Invalid sparse file format at header magic' foi reconhecimento de imagem raw, seguido de conversao/envio sparse bem-sucedido; nao foi falha de gravacao.

Format Data final apos GSI concluido. Magisk30.7 instalado pelo modo recovery suportado/depreciado da documentacao oficial (boot possui ramdisk), updaterRC=0; boot gravado com Magisk preservando SPL2026-06. Arquivos auxiliares foram armazenados em /data/magisk por /data/adb ainda nao existir; migracao prevista no primeiro boot. Tentativa de modulo tweaks pelo recovery falhou antes de aplicar (util_functions.sh esperado em /data/adb/magisk). Demais modulos ainda nao instalados. Vendor fstab hash confirmado apos instalacao. Primeiro boot Lineage iniciado.

Primeiro boot Lineage confirmado sys.boot_completed=1, build21.0-20260614-UNOFFICIAL-arm64_bgN, warranty_bit=1. Magisk30.7 responde e su -c id retorna root. Magisk APK oficial instalado via ADB com Success. Configuracao inicial ainda incompleta; Wi-Fi conectado. Modulos copiados para /data/local/tmp mas CLI reportou 'Incomplete Magisk install' porque arquivos auxiliares ainda em /data/magisk; falta concluir setup/reparacao pelo app Magisk antes de instalar modulos.

Setup Lineage concluido (user_setup_complete=1). App Magisk mostrou Configuracao adicional exigida; aceito OK por UI dentro da autorizacao de instalacao. Auxiliares /data/adb/magisk/util_functions.sh apareceram e reinicio automatico ocorreu. Aguardando reconexao; nao considerar modulos instalados ate verificar sucesso.

NewPipe0.29.1 oficial TeamNewPipe baixado, SHA25618447bfb1e06d113edc88df93f471827280de06f6f3d4dc42f56f28b9c1bab79 confere com digestGitHub, instalado com Success. Dono optou sem contaGoogle e pediu cliente mais leve sem anuncios; YouTube original nao instalado. Particao product Samsung montada somente-leitura para inspecao e desmontada sem alteracao. Quatro modulos Sistema2D instalados com CLI Magisk apos reparacao do app, outputs Done e diretorios modules_update confirmados. Density200, font1.05, animacoes0 aplicados com snapshot anterior. Script sysctlverificado copiado para service.d conforme projeto, valoresVM anteriores salvos com root. Modoaviao1/WiFi religado; Bluetooth1preservado. Reinicio para ativar modulos a seguir.

Concluido: quatro modulos ativos apos reboot e quatro overlays habilitados; Perfetto0; sw640dp/200dpi; WiFi reconectado, aviao1 e Bluetooth1. NewPipe0.29.1 oficial instalado sem contaGoogle por preferencia do dono, MP4/720p ajustados, reproducao final PLAYING confirmada. Dono confirmou imagem e som normais. Jellypaginaexterna e teclado testados, nenhumANR, bateria37C. Relatorio final resultado.md. Nenhum procedimento pendente de instalacao; testes de longo prazo e PIN/atualizacao nao realizados.
