param([string]$Destino='estado-anterior')
$Serial = $env:ADB_SERIAL
if ([string]::IsNullOrWhiteSpace($Serial)) { throw 'Defina ADB_SERIAL com o serial do tablet de destino.' }
$ErrorActionPreference='Stop'
$adb=(Resolve-Path "$PSScriptRoot\..\..\tools\platform-tools\adb.exe").Path
$dest=Join-Path $PSScriptRoot $Destino
New-Item -ItemType Directory -Path $dest -Force | Out-Null
foreach($p in @('com.sec.android.app.sbrowser','com.android.chrome','com.google.android.youtube')) {
    $a=(& $adb -s $Serial shell cmd package resolve-activity --brief --user 0 -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p $p | Where-Object {$_ -match '^\S+/\S+$'} | Select-Object -Last 1).Trim()
    & $adb -s $Serial shell "am start -W --user 0 -n '$a'" | Out-Null
    Start-Sleep -Seconds 3
    for($i=1;$i -le 3;$i++) {
        & $adb -s $Serial shell am force-stop --user 0 $p
        & $adb -s $Serial shell "am start -W --user 0 -n '$a'" | Set-Content "$dest\abertura-$p-$i.txt" -Encoding UTF8
        Start-Sleep -Seconds 3
    }
}
& $adb -s $Serial shell dumpsys battery | Set-Content "$dest\bateria-medicao.txt"
& $adb -s $Serial shell input keyevent KEYCODE_HOME
