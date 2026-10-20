$targets = @(
  "minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_bottom.json",
  "minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_top_no_seeds.json",
  "minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_top_with_seeds.json",
  "minecraft/kubejs/assets/minecraft/models/block/flowerbed_1.json",
  "minecraft/kubejs/assets/minecraft/models/block/flowerbed_2.json",
  "minecraft/kubejs/assets/minecraft/models/block/flowerbed_3.json",
  "minecraft/kubejs/assets/minecraft/models/block/flowerbed_4.json",
  "minecraft/kubejs/assets/minecraft/models/block/sunflower_bottom.json",
  "minecraft/kubejs/assets/minecraft/models/block/sunflower_top.json"
)

Write-Host "=== JSON PARSING TEST ==="
$allValid = $true
foreach ($t in $targets) {
    try {
        $content = Get-Content -Path $t -Raw | ConvertFrom-Json
        Write-Host "VALID JSON: $t"
    } catch {
        Write-Host "INVALID JSON: $t - $_"
        $allValid = $false
    }
}

Write-Host "=== SEARCH FOR MADE WITH BLOCKBENCH ==="
$bbHits = Get-ChildItem -Path "minecraft/kubejs/assets" -Filter "*.json" -Recurse | Select-String -Pattern "Made with Blockbench"
Write-Host "Blockbench occurrences in kubejs/assets: $($bbHits.Count)"

Write-Host "=== VERIFY COMMUNITY CREDITS (zanderest) ==="
$zHits = Get-ChildItem -Path "minecraft/kubejs/assets/cubicleaves/models/block" -Filter "*.json" | Select-String -Pattern '"credit":\s*"zanderest"'
Write-Host "zanderest occurrences in cubicleaves: $($zHits.Count)"

Write-Host "=== VERIFY PACK CREDIT (PEAK) ==="
$peakHit = Select-String -Path "minecraft/kubejs/assets/kubejs/models/block/green_screen.json" -Pattern '"credit":\s*"PEAK"'
Write-Host "PEAK occurrences in green_screen.json: $($peakHit.Count)"
