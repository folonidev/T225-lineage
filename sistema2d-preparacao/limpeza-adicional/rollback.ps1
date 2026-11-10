$Serial = $env:ADB_SERIAL
if ([string]::IsNullOrWhiteSpace($Serial)) { throw 'Defina ADB_SERIAL com o serial do tablet de destino.' }
$ErrorActionPreference='Stop'
$adb=(Resolve-Path "$PSScriptRoot\..\..\..\tools\platform-tools\adb.exe").Path
if((& $adb -s $Serial get-serialno).Trim() -ne $Serial){throw 'Serial divergente'}
if((& $adb -s $Serial shell getprop ro.lineage.version) -notmatch '^21\.0-20260614-UNOFFICIAL-arm64_bgN'){throw 'ROM divergente'}
if((& $adb -s $Serial shell am get-current-user).Trim() -ne '0'){throw 'Usuario divergente'}
foreach($r in (Import-Csv "$PSScriptRoot\alteracoes.csv")) {
    if($r.resultado -notmatch 'aplicado|pendente'){continue}
    & $adb -s $Serial shell pm default-state --user 0 $r.pacote
    if($LASTEXITCODE -ne 0){throw "Falha ao restaurar $($r.pacote)"}
}
