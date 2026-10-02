[System.Reflection.Assembly]::LoadWithPartialName('System.Drawing') | Out-Null
$dir = 'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\kubejs\assets\kubejs\textures\block'
if (!(Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }

function C($hex) {
    return [System.Drawing.ColorTranslator]::FromHtml($hex)
}

# --- TOP TEXTURE ---
$top = New-Object System.Drawing.Bitmap(16, 16)
for ($y = 0; $y -lt 16; $y++) {
    for ($x = 0; $x -lt 16; $x++) {
        $col = (C '#0F0A1F')
        if ($y -eq 0) { $col = (C '#483A6D') }
        elseif ($y -eq 15) { $col = (C '#1A1428') }
        elseif ($x -eq 0) { $col = (C '#3A2E59') }
        elseif ($x -eq 15) { $col = (C '#241C38') }
        elseif ($x -eq 1 -or $x -eq 14 -or $y -eq 1 -or $y -eq 14) { $col = (C '#251B3D') }
        
        $top.SetPixel($x, $y, $col)
    }
}

# Gold corner rivets (symmetric)
$corners = @( @(1,1), @(1,14), @(14,1), @(14,14) )
foreach ($pt in $corners) {
    $top.SetPixel($pt[0], $pt[1], (C '#F2D06B'))
}
$top.SetPixel(2,1, (C '#C99424')); $top.SetPixel(1,2, (C '#C99424'))
$top.SetPixel(13,1, (C '#C99424')); $top.SetPixel(14,2, (C '#C99424'))
$top.SetPixel(2,14, (C '#8C6212')); $top.SetPixel(1,13, (C '#8C6212'))
$top.SetPixel(13,14, (C '#8C6212')); $top.SetPixel(14,13, (C '#8C6212'))

# Void floor texture with subtle star dust
$voidDots = @( @(3,3), @(12,3), @(3,12), @(12,12), @(2,7), @(2,8), @(13,7), @(13,8), @(7,2), @(8,2), @(7,13), @(8,13) )
foreach ($pt in $voidDots) {
    $top.SetPixel($pt[0], $pt[1], (C '#241542'))
}

# Diagonal astral purple glow
$diags = @( @(4,4), @(11,4), @(4,11), @(11,11) )
foreach ($pt in $diags) {
    $top.SetPixel($pt[0], $pt[1], (C '#E08CF8'))
}
$diagInner = @( @(5,5), @(10,5), @(5,10), @(10,10) )
foreach ($pt in $diagInner) {
    $top.SetPixel($pt[0], $pt[1], (C '#B154EB'))
}

# Cardinal cyan runic arms
$armsOuter = @( @(7,3), @(8,3), @(7,12), @(8,12), @(3,7), @(3,8), @(12,7), @(12,8) )
foreach ($pt in $armsOuter) {
    $top.SetPixel($pt[0], $pt[1], (C '#8DF7FC'))
}
$armsInner = @( @(7,4), @(8,4), @(7,11), @(8,11), @(4,7), @(4,8), @(11,7), @(11,8) )
foreach ($pt in $armsInner) {
    $top.SetPixel($pt[0], $pt[1], (C '#38D9D4'))
}
$armsCore = @( @(7,5), @(8,5), @(7,10), @(8,10), @(5,7), @(5,8), @(10,7), @(10,8) )
foreach ($pt in $armsCore) {
    $top.SetPixel($pt[0], $pt[1], (C '#2CC8D4'))
}

# Central astral nexus ring
$nexusRing = @( @(6,6), @(9,6), @(6,9), @(9,9), @(7,6), @(8,6), @(7,9), @(8,9), @(6,7), @(6,8), @(9,7), @(9,8) )
foreach ($pt in $nexusRing) {
    $top.SetPixel($pt[0], $pt[1], (C '#62F0F7'))
}

# Core white-hot star
$core = @( @(7,7), @(8,7), @(7,8), @(8,8) )
foreach ($pt in $core) {
    $top.SetPixel($pt[0], $pt[1], (C '#FFFFFF'))
}

$top.Save("$dir\sanctuary_pad_top.png", [System.Drawing.Imaging.ImageFormat]::Png)
$top.Dispose()

# --- SIDE TEXTURE ---
$side = New-Object System.Drawing.Bitmap(16, 16)
for ($y = 0; $y -lt 16; $y++) {
    for ($x = 0; $x -lt 16; $x++) {
        $side.SetPixel($x, $y, (C '#251B3D'))
    }
}
for ($x = 0; $x -lt 16; $x++) {
    $side.SetPixel($x, 13, (C '#52437C')) # Top rim
    $side.SetPixel($x, 14, (C '#2C2245')) # Mid plate
    $side.SetPixel($x, 15, (C '#140F22')) # Bottom lip
}
# Runic glowing inlays along the rim
$sideRunes = @(2, 5, 7, 8, 10, 13)
foreach ($x in $sideRunes) {
    $side.SetPixel($x, 14, (C '#38D9D4'))
}
$side.SetPixel(0, 13, (C '#C99424')); $side.SetPixel(0, 14, (C '#F2D06B'))
$side.SetPixel(15, 13, (C '#C99424')); $side.SetPixel(15, 14, (C '#F2D06B'))

$side.Save("$dir\sanctuary_pad_side.png", [System.Drawing.Imaging.ImageFormat]::Png)
$side.Dispose()

# --- BOTTOM TEXTURE ---
$bot = New-Object System.Drawing.Bitmap(16, 16)
for ($y = 0; $y -lt 16; $y++) {
    for ($x = 0; $x -lt 16; $x++) {
        $c = (C '#161124')
        if ($x -eq 0 -or $x -eq 15 -or $y -eq 0 -or $y -eq 15) { $c = (C '#2C2245') }
        elseif ($x -eq $y -or $x -eq (15 - $y)) { $c = (C '#201933') }
        $bot.SetPixel($x, $y, $c)
    }
}
$bot.Save("$dir\sanctuary_pad_bottom.png", [System.Drawing.Imaging.ImageFormat]::Png)
$bot.Dispose()

Write-Host 'Textures successfully generated!'
