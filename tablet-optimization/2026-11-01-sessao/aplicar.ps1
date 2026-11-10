param([int]$Inicio=0,[int]$Quantidade=6)
$Serial = $env:ADB_SERIAL
if ([string]::IsNullOrWhiteSpace($Serial)) { throw 'Defina ADB_SERIAL com o serial do tablet de destino.' }
$ErrorActionPreference='Stop'
$adb=(Resolve-Path "$PSScriptRoot\..\..\tools\platform-tools\adb.exe").Path
if((& $adb -s $Serial shell getprop ro.product.model).Trim() -ne 'SM-T225'){throw 'Modelo divergente'}
if((& $adb -s $Serial shell am get-current-user).Trim() -ne '0'){throw 'Usuario divergente'}
$list=@(Import-Csv "$PSScriptRoot\candidatos.csv")
for($i=$Inicio;$i -lt [Math]::Min($Inicio+$Quantidade,$list.Count);$i++) {
    $c=$list[$i]
    $dump=Get-Content "$PSScriptRoot\estado-anterior\package-$($c.pacote).txt" -Raw
    $state=[regex]::Match($dump,'User 0:.*?installed=true.*?enabled=(\d+)')
    if(!$state.Success){throw "Nao instalado: $($c.pacote)"}
    $old=$state.Groups[1].Value
    if($old -notin @('0','1')){throw "Ja desativado: $($c.pacote)"}
    $row=[pscustomobject]@{tipo='pacote';pacote_ajuste=$c.pacote;motivo=$c.motivo;estado_anterior=$old;mudanca="adb -s $Serial shell pm disable-user --user 0 $($c.pacote)";resultado='pendente';reversao="adb -s $Serial shell pm $(if($old -eq '0'){'default-state'}else{'enable'}) --user 0 $($c.pacote)"}
    $rows=@(Import-Csv "$PSScriptRoot\alteracoes.csv")
    if($rows.pacote_ajuste -contains $c.pacote){throw 'Alteracao ja registrada'}
    $rows+= $row
    $rows | Export-Csv "$PSScriptRoot\alteracoes.csv" -NoTypeInformation -Encoding UTF8
    $out=& $adb -s $Serial shell pm disable-user --user 0 $c.pacote 2>&1
    $ok=$LASTEXITCODE -eq 0 -and ($out -join '') -match 'disabled-user'
    $row.resultado=if($ok){'aplicado'}else{"falhou: $out"}
    $rows | Export-Csv "$PSScriptRoot\alteracoes.csv" -NoTypeInformation -Encoding UTF8
    "$($c.pacote): $out"
    if(!$ok){throw 'Falha ao desativar; lote interrompido'}
}
