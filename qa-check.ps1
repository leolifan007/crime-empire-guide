# qa-check.ps1 — Article Quality Gate
# Run after writing each article.
# Usage: .\qa-check.ps1 -FilePath "content/schedule-i/automation/workshop.md"

param(
    [Parameter(Mandatory=$true)]
    [string]$FilePath,
    [switch]$FixBom
)

$ErrorCount = 0
$WarningCount = 0
$report = @()

Write-Host "=== QA Check: $FilePath ===" -ForegroundColor Cyan

# --- 1. File existence ---
if (-not (Test-Path $FilePath)) {
    Write-Host "ERROR: File not found" -ForegroundColor Red
    exit 1
}

$content = Get-Content $FilePath -Raw -Encoding UTF8
$lines = $content -split "`n"

# --- 2. BOM check ---
$bytes = [System.IO.File]::ReadAllBytes($FilePath)
if ($bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
    if ($FixBom) {
        $contentNoBom = [System.Text.Encoding]::UTF8.GetString($bytes, 3, $bytes.Length - 3)
        [System.IO.File]::WriteAllText($FilePath, $contentNoBom, [System.Text.UTF8Encoding]::new($false))
        Write-Host "  [FIXED] BOM removed" -ForegroundColor Yellow
        $FixBom = $false
    } else {
        Write-Host "  [FAIL] File has BOM. Run again with -FixBom" -ForegroundColor Red
        $ErrorCount++
    }
} else {
    Write-Host "  [PASS] No BOM" -ForegroundColor Green
}

$body = $content
# Remove front matter
if ($body -match '^---\r?\n(.*?)\r?\n---\r?\n(.*)') {
    $body = $matches[2]
}

# --- 3. Unicode special chars check ---
$badChars = @{
    '\u2014' = 'em-dash (—)'
    '\u2013' = 'en-dash (–)'
    '\u2018' = 'left single quote (')'
    '\u2019' = 'right single quote (')'
    '\u201c' = 'left double quote (")'
    '\u201d' = 'right double quote (")'
    '\u00a0' = 'non-breaking space'
}

$foundBad = @{}
foreach ($char in $badChars.Keys) {
    $pattern = [char]::ConvertFromUtf32([int]$char)
    if ($content.Contains($pattern)) {
        $foundBad[$char] = $badChars[$char]
    }
}

if ($foundBad.Count -gt 0) {
    Write-Host "  [FAIL] Unicode special chars found:" -ForegroundColor Red
    foreach ($item in $foundBad.GetEnumerator()) {
        Write-Host "    $($item.Value)" -ForegroundColor Red
        $ErrorCount++
    }
} else {
    Write-Host "  [PASS] No unicode special chars" -ForegroundColor Green
}

# --- 4. Emoji check (SOP 07) ---
$emojiPattern = '[\x{1F600}-\x{1F64F}\x{1F300}-\x{1F5FF}\x{1F680}-\x{1F6FF}\x{1F1E0}-\x{1F1FF}\x{2600}-\x{26FF}\x{2700}-\x{27BF}\x{FE00}-\x{FE0F}\x{1F900}-\x{1F9FF}\x{1FA00}-\x{1FA6F}\x{1FA70}-\x{1FAFF}\x{200D}\x{2934}\x{2935}\x{25AA}\x{25AB}\x{25B6}\x{25C0}\x{25FB}-\x{25FE}]'
if ($body -match $emojiPattern) {
    Write-Host "  [FAIL] Emoji found (SOP 07 forbids emoji in articles)" -ForegroundColor Red
    $ErrorCount++
} else {
    Write-Host "  [PASS] No emoji" -ForegroundColor Green
}

# --- 5. Shortcode balance check ---
$openCount = ([regex]::Matches($body, '{{<')).Count
$closeCount = ([regex]::Matches($body, '>}}')).Count
# Account for inline shortcodes that use />}}
$closeInline = ([regex]::Matches($body, '/>}}')).Count
$totalClose = $closeCount - $closeInline

if ($openCount -ne $totalClose) {
    Write-Host "  [FAIL] Shortcode mismatch: $openCount open vs $totalClose close" -ForegroundColor Red
    $ErrorCount++
} else {
    Write-Host "  [PASS] Shortcodes balanced ($openCount pairs)" -ForegroundColor Green
}

# --- 6. Material icon existence check ---
$iconDir = "C:\Users\ROG\.qclaw\workspace-ua58rsb93veqtxl7\_hugo_preview\static\images\game-icons"
$iconRefs = ([regex]::Matches($body, '{{<\s*material\s+"(.+?)"')).Captures.Name | Select-Object -Unique
$missingIcons = @()
foreach ($icon in $iconRefs) {
    $iconFile = Join-Path $iconDir "$icon.png"
    if (-not (Test-Path $iconFile)) {
        $missingIcons += $icon
    }
}
if ($missingIcons.Count -gt 0) {
    Write-Host "  [FAIL] Missing material icons: $($missingIcons -join ', ')" -ForegroundColor Red
    $ErrorCount++
} else {
    Write-Host "  [PASS] All material icons exist ($($iconRefs.Count) references)" -ForegroundColor Green
}

# --- 7. Word count check ---
$plainText = $body -replace '\{\{<.*?>\}\}', '' -replace '<[^>]+>', '' -replace '\s+', ' '
$wordCount = ($plainText -split '\s+' | Where-Object { $_ -ne '' }).Count
if ($wordCount -lt 600) {
    Write-Host "  [WARN] Low word count: $wordCount (min 600)" -ForegroundColor Yellow
    $WarningCount++
} else {
    Write-Host "  [PASS] Word count: $wordCount" -ForegroundColor Green
}

# --- 8. Data presentation check (at least 2 tables, 1 table with 3+ rows, or diagram) ---
$tableCount = ([regex]::Matches($body, '^\|').Count -gt 2)
$diagramCount = ([regex]::Matches($body, '{{<\s*diagram').Count)
$stepGroupCount = ([regex]::Matches($body, '{{<\s*stepgroup').Count)

$dataScore = 0
if ($diagramCount -gt 0) { $dataScore++ }
if ($stepGroupCount -gt 0) { $dataScore++ }
if ($tableCount) { $dataScore++ }

if ($dataScore -lt 2) {
    Write-Host "  [WARN] Less than 2 data presentations (tables/diagrams/stepgroups)" -ForegroundColor Yellow
    $WarningCount++
} else {
    Write-Host "  [PASS] Data presentations: $dataScore" -ForegroundColor Green
}

# --- 9. Internal links check ---
$internalLinks = ([regex]::Matches($body, '/schedule-i/')).Count
if ($internalLinks -eq 0 -and $dataScore -gt 0) {
    Write-Host "  [WARN] No internal links found" -ForegroundColor Yellow
    $WarningCount++
} else {
    Write-Host "  [PASS] Internal links: $internalLinks" -ForegroundColor Green
}

# --- 10. Resource grid check ---
$resourceGridCount = ([regex]::Matches($body, '{{<\s*resourcegrid').Count
if ($resourceGridCount -eq 0) {
    Write-Host "  [WARN] No resourcegrid shortcode (bottom community resources)" -ForegroundColor Yellow
    $WarningCount++
} else {
    Write-Host "  [PASS] Resource grid present" -ForegroundColor Green
}

# --- Summary ---
Write-Host ""
if ($ErrorCount -eq 0 -and $WarningCount -eq 0) {
    Write-Host "=== QA PASSED (clean) ===" -ForegroundColor Green
} elseif ($ErrorCount -eq 0) {
    Write-Host "=== QA PASSED with $WarningCount warnings ===" -ForegroundColor Yellow
} else {
    Write-Host "=== QA FAILED: $ErrorCount errors, $WarningCount warnings ===" -ForegroundColor Red
    exit 1
}
