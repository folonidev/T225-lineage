param([string]$Etapa='lote')
$Serial = $env:ADB_SERIAL
if ([string]::IsNullOrWhiteSpace($Serial)) { throw 'Defina ADB_SERIAL com o serial do tablet de destino.' }
$ErrorActionPreference='Stop'
$adb=(Resolve-Path "$PSScriptRoot\..\..\tools\platform-tools\adb.exe").Path
$dest="$PSScriptRoot\validacao-$Etapa"
New-Item -ItemType Directory -Path $dest -Force | Out-Null
foreach($p in @('com.android.settings','app.olauncher','com.sec.android.app.sbrowser','com.google.android.youtube')) {
    $a=(& $adb -s $Serial shell cmd package resolve-activity --brief --user 0 -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p $p | Where-Object {$_ -match '^\S+/\S+$'} | Select-Object -Last 1).Trim()
    if(!$a){throw "Sem atividade: $p"}
    $out=& $adb -s $Serial shell "am start -W --user 0 -n '$a'"
    $out | Set-Content "$dest\$p.txt"
    if(($out -join '') -notmatch 'Status: ok'){throw "Falha ao abrir $p : $out"}
}
& $adb -s $Serial shell ime list -s | Set-Content "$dest\teclados.txt"
& $adb -s $Serial shell cmd wifi status | Set-Content "$dest\wifi.txt"
& $adb -s $Serial shell dumpsys activity activities | Select-String 'mResumedActivity|topResumedActivity' | Set-Content "$dest\atividade.txt"
& $adb -s $Serial shell input keyevent KEYCODE_HOME
Write-Output "Validacao de abertura concluida: $Etapa; reproducao e digitacao ainda exigem teste visual."
