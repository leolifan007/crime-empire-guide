import sys

path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero card NEW badge - red for all
content = content.replace(
    '.card-badge.new-badge{background:rgba(146,198,109,.15);color:#92C66D;border:1px solid rgba(146,198,109,.3)}.card-badge.new-badge.pulse{animation:badgePulse 2s ease-in-out infinite}.theme-dds2 .card-badge.new-badge{background:rgba(212,168,67,.15);color:#d4a843;border-color:rgba(212,168,67,.3)}.theme-crime-sim .card-badge.new-badge{background:rgba(52,152,219,.15);color:#3498db;border-color:rgba(52,152,219,.3)}',
    '.card-badge.new-badge{background:rgba(231,76,60,.15);color:#e74c3c;border:1px solid rgba(231,76,60,.3)}.card-badge.new-badge.pulse{animation:badgePulse 2s ease-in-out infinite}'
)

# 2. Guide card NEW badge - red for all
content = content.replace(
    '.guide-card-new{position:absolute;top:8px;left:8px;padding:3px 10px;border-radius:6px;font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;z-index:3;pointer-events:none;animation:newGlow 2s ease-in-out infinite}.guide-card.theme-schedule-i .guide-card-new{background:rgba(146,198,109,.9);color:#050508}.guide-card.theme-dds2 .guide-card-new{background:rgba(212,168,67,.9);color:#050508}.guide-card.theme-crime-sim .guide-card-new{background:rgba(52,152,219,.9);color:#fff}',
    '.guide-card-new{position:absolute;top:8px;left:8px;padding:3px 10px;border-radius:6px;font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;z-index:3;pointer-events:none;background:rgba(231,76,60,.92);color:#fff;animation:newGlowRed 2s ease-in-out infinite}@keyframes newGlowRed{0%,100%{box-shadow:0 0 8px rgba(231,76,60,.3)}50%{box-shadow:0 0 16px rgba(231,76,60,.5)}}'
)

# 3. Sidebar items - more button-like
old_side = (
    '.sidebar-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:8px;font-size:13px;'
    'color:var(--text2);transition:all .2s;text-decoration:none}'
    '.sidebar-item:hover{background:var(--surface-hover);color:var(--text)}'
    '.sidebar-item.active{background:var(--gold-dim);color:var(--gold);border:1px solid rgba(212,168,67,.12)}'
    '.guide-sidebar.game-schedule-i .sidebar-item.active{background:rgba(146,198,109,.12);color:#92C66D;'
    'border-color:rgba(146,198,109,.2)}'
    '.sidebar-back{display:block;margin-top:20px;padding:10px 14px;font-size:13px;color:var(--text3);'
    'text-align:center;border:1px dashed var(--border);border-radius:8px;text-decoration:none;transition:all .2s}'
    '.sidebar-back:hover{color:var(--gold);border-color:rgba(212,168,67,.2)}'
)
new_side = (
    '.sidebar-item{display:flex;align-items:center;gap:10px;padding:12px 16px;border-radius:8px;font-size:13px;'
    'color:var(--text2);transition:all .2s;text-decoration:none;border:1px solid transparent;position:relative}'
    '.sidebar-item:hover{background:var(--surface-hover);color:var(--text);border-color:var(--border-light);padding-left:20px}'
    '.sidebar-item.active{background:var(--gold-dim);color:var(--gold);border:1px solid rgba(212,168,67,.15);'
    'border-left:3px solid var(--gold)}'
    '.guide-sidebar.game-schedule-i .sidebar-item.active{background:rgba(146,198,109,.12);color:#92C66D;'
    'border-color:rgba(146,198,109,.2);border-left:3px solid #92C66D}'
    '.sidebar-item.active::after{content:\"\\2192\";position:absolute;right:14px;font-size:12px;opacity:0;transition:opacity .2s}'
    '.sidebar-item.active::after{opacity:.6}'
    '.sidebar-back{display:block;margin-top:20px;padding:10px 14px;font-size:13px;color:var(--text3);'
    'text-align:center;border:1px dashed var(--border);border-radius:8px;text-decoration:none;transition:all .2s}'
    '.sidebar-back:hover{color:var(--gold);border-color:rgba(212,168,67,.2)}'
)
content = content.replace(old_side, new_side)

# 4. Back to top button CSS
content += (
    '\n\n/* Back to top button */'
    '\n.back-to-top{position:fixed;bottom:32px;right:32px;z-index:999;width:48px;height:48px;border-radius:50%;'
    'background:rgba(231,76,60,.12);border:1.5px solid rgba(231,76,60,.25);color:#e74c3c;font-size:22px;cursor:pointer;'
    'display:flex;align-items:center;justify-content:center;transition:all .25s;opacity:0;pointer-events:none;'
    'backdrop-filter:blur(8px);box-shadow:0 4px 20px rgba(0,0,0,.3);font-family:var(--font-body)}'
    '\n.back-to-top.visible{opacity:1;pointer-events:auto}'
    '\n.back-to-top:hover{background:rgba(231,76,60,.2);transform:translateY(-3px);box-shadow:0 6px 25px rgba(231,76,60,.15)}'
    '\n'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('CSS OK')
