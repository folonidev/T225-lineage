$Serial = $env:ADB_SERIAL
if ([string]::IsNullOrWhiteSpace($Serial)) { throw 'Defina ADB_SERIAL com o serial do tablet de destino.' }
$ErrorActionPreference='Stop'
$adb=(Resolve-Path "$PSScriptRoot\..\..\tools\platform-tools\adb.exe").Path
function Invoke-Device([string[]]$Command) {
    $out=& $adb -s $Serial @Command 2>&1
    if($LASTEXITCODE -ne 0){throw "ADB falhou: $out"}
    return $out
}
if((Invoke-Device @('get-serialno')).Trim() -ne $Serial){throw 'Serial divergente'}
if((Invoke-Device @('shell','getprop','ro.product.model')).Trim() -ne 'SM-T225'){throw 'Modelo divergente'}
if((Invoke-Device @('shell','am','get-current-user')).Trim() -ne '0'){throw 'Usuario ativo divergente'}
$rows=@(Import-Csv "$PSScriptRoot\alteracoes.csv")
[array]::Reverse($rows)
foreach($r in $rows) {
    if($r.resultado -notmatch 'aplicado|pendente'){continue}
    if($r.tipo -eq 'pacote') {
        $verb=if($r.estado_anterior -eq '0'){'default-state'}elseif($r.estado_anterior -eq '1'){'enable'}else{throw 'Estado inesperado'}
        $result=Invoke-Device @('shell','pm',$verb,'--user','0',$r.pacote_ajuste)
        $result
        $dump=(Invoke-Device @('shell','dumpsys','package',$r.pacote_ajuste)) -join "`n"
        $state=[regex]::Match($dump,'User 0:.*?installed=true.*?enabled=(\d+)')
        if(!$state.Success -or $state.Groups[1].Value -ne $r.estado_anterior){throw "Restauracao nao confirmada: $($r.pacote_ajuste)"}
    } elseif($r.tipo -eq 'radio') {
        Invoke-Device @('shell','cmd','connectivity','airplane-mode','disable')
        Invoke-Device @('shell','svc','wifi','enable')
        if((Invoke-Device @('shell','settings','get','global','airplane_mode_on')).Trim() -ne '0'){throw 'Modo aviao nao restaurado'}
    }
}
Write-Output 'Reversao concluida. Nenhum pacote previamente desativado foi habilitado.'
