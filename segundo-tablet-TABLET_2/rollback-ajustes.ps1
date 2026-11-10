$Serial = $env:ADB_SERIAL
if ([string]::IsNullOrWhiteSpace($Serial)) { throw 'Defina ADB_SERIAL com o serial do tablet de destino.' }
$ErrorActionPreference='Stop'
$adb=(Resolve-Path "$PSScriptRoot\..\tools\platform-tools\adb.exe").Path
if((& $adb -s $Serial get-serialno).Trim() -ne $Serial){throw 'Serial divergente'}
if((& $adb -s $Serial shell getprop ro.lineage.version).Trim() -ne '21.0-20260614-UNOFFICIAL-arm64_bgN'){throw 'ROM divergente'}
if((& $adb -s $Serial shell am get-current-user).Trim() -ne '0'){throw 'Usuario divergente'}
$before=Get-Content "$PSScriptRoot\estado-antes-ajustes.json" -Raw | ConvertFrom-Json
foreach($p in $before.packages.PSObject.Properties){
    if($p.Value -notin @('0','1')){continue}
    $verb=if($p.Value -eq '0'){'default-state'}else{'enable'}
    & $adb -s $Serial shell pm $verb --user 0 $p.Name
    if($LASTEXITCODE -ne 0){throw "Falha ao restaurar $($p.Name)"}
}
if($before.density -match 'Override density: (\d+)'){
    & $adb -s $Serial shell wm density $Matches[1]
}else{& $adb -s $Serial shell wm density reset}
foreach($p in $before.settings.PSObject.Properties){
    $namespace,$key=$p.Name -split ':',2
    if($key -in @('airplane_mode_on','bluetooth_on')){continue}
    if($p.Value -eq 'null'){& $adb -s $Serial shell settings delete $namespace $key}
    else{& $adb -s $Serial shell settings put $namespace $key $p.Value}
}
$air=if($before.settings.'global:airplane_mode_on' -eq '1'){'enable'}else{'disable'}
& $adb -s $Serial shell cmd connectivity airplane-mode $air
& $adb -s $Serial shell svc wifi enable
$bt=if($before.settings.'global:bluetooth_on' -eq '1'){'enable'}else{'disable'}
& $adb -s $Serial shell cmd bluetooth_manager $bt
Write-Output 'Ajustes de interface e quatro pacotes restaurados. Este script nao restaura a ROM Samsung nem remove modulos.'
