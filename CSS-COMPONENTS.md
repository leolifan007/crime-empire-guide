# CSS Component Library

All components defined in `main.css` under `/* ===== COMPONENT: ... ===== */` section markers.

## Available Components

| Component | CSS Classes | Shortcodes Using It | Usage |
|-----------|-------------|--------------------|-------|
| **Callout Cards** | `.callout`, `.pro-tip` | `{{< callout "type" >}}` | Info/warning boxes with gold left border |
| **Content Box** | `.content-box` | `{{< box >}}` | Dark card with rounded border |
| **Section Head** | `.section-head h2` | `{{< section "Title" >}}` | Section title with gold left accent |
| **Schema Diagram** | `.schema-diagram` | `{{< diagram "path" "alt" "width" >}}` | Full-width SVG with shadow |
| **Recipe Result** | `.recipe-result` | Raw HTML div | Green-bordered result highlight |
| **Step Cards** | `.step-card`, `.step-num` | Raw HTML div | Numbered step cards with left circle |
| **Game Recipe Icons** | `.game-row`, `.game-slot`, `.game-img`, `.game-qty`, `.game-name`, `.game-plus` | `{{< recipe >}}`, `{{< material >}}` | Recipe display with item icons |
| **Inline Icons** | `p .game-slot`, `li .game-slot`, `.callout .game-slot` | `{{< material >}}` in text | Icons inline with text (28x28) |
| **Material Card** | `.mat-card`, `.mat-card-img` | `{{< mat >}}` | Icon card with quantity badge |
| **Check-row** | `.check-row`, `.check-item`, `.check-icon`, `.check-count` | `{{< check >}}` | Checkbox-style item list |
| **Table Icons** | `td .game-slot`, `td .game-img` | `{{< material >}}` in tables | 60x60 icons in table cells |

## Writing SVG Charts (Standard)

1. Use viewBox matching actual dimensions
2. Background rect must match viewBox size
3. All bars: start from bottom baseline, go UP (negative height in SVG)
4. Font sizes: 12-14px minimum (SOP), title 20-22px
5. No UTF-8 BOM
6. Run `validate_svg.py` before deployment
7. For interactive testing: set up Chrome CDP screenshot via `--remote-debugging-port`

## Adding New Components

1. Add section marker: `/* ========== COMPONENT: Name ========== */`
2. Add component row above
