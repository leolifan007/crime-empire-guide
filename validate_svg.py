#!/usr/bin/env python3
"""SVG chart validator: verifies layout correctness before deployment"""
import re, sys, json

def validate_svg(path):
    with open(path, 'rb') as f:
        raw = f.read()

    issues = []
    
    # 1. BOM check
    if raw[:3] == b'\xef\xbb\xbf':
        issues.append(("ERROR", "SVG has UTF-8 BOM - will break on GitHub Pages"))
    
    # 2. Size check (SOP: max 2MB)
    if len(raw) > 2 * 1024 * 1024:
        issues.append(("ERROR", f"SVG too large: {len(raw)} bytes (limit 2MB)"))
    
    # 3. Parse viewBox
    text = raw.decode('utf-8')
    vb = re.search(r'viewBox="([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)"', text)
    if not vb:
        issues.append(("ERROR", "Missing viewBox"))
        return issues
    
    vb_w, vb_h = float(vb.group(3)), float(vb.group(4))
    
    # 4. Check background rect matches viewBox
    bg = re.search(r'<rect[^>]*width="([\d.]+)"[^>]*height="([\d.]+)"', text)
    if bg:
        bg_w, bg_h = float(bg.group(1)), float(bg.group(2))
        if abs(bg_w - vb_w) > 1 or abs(bg_h - vb_h) > 1:
            issues.append(("ERROR", f"Background rect ({bg_w}x{bg_h}) doesn't match viewBox ({vb_w}x{vb_h})"))
    
    # 5. Find chart area boundaries
    # Extract all text elements with their positions
    texts = []
    for m in re.finditer(r'<text[^>]*y="(-?\d+)"[^>]*>(.*?)</text>', text):
        y = int(m.group(1))
        content = re.sub(r'<[^>]+>', '', m.group(2)).strip()[:40]
        texts.append((y, content))
    
    # 6. Check font sizes (SOP: 12-14px for labels)
    font_sizes = [int(s) for s in re.findall(r'font-size="(\d+)"', text)]
    min_font = min(font_sizes) if font_sizes else 0
    if min_font > 0 and min_font < 12:
        issues.append(("WARN", f"Font size {min_font}px below SOP minimum 12px"))
    
    # 7. Check bars don't overflow or overlap
    # Extract bar positions
    profit_bars = re.findall(r'<rect\s+x="(\d+)"\s+y="(-?\d+)"\s+width="(\d+)"\s+height="(-?\d+)"', text)
    for x, y, w, h in profit_bars:
        bar_top = int(y) + int(h)  # negative h means going up
        if bar_top < -20:  # bar goes above chart area
            issues.append(("INFO", f"Bar at x={x} extends above chart (y_top={bar_top}) - may be truncated"))
    
    # 8. Find any elements outside viewBox
    all_y = [int(m.group(1)) for m in re.finditer(r'\sy="(-?\d+)"', text)]
    for y in all_y:
        if y < -50 or y > vb_h + 50:
            issues.append(("WARN", f"Element at y={y} outside viewBox (0-{vb_h})"))
    
    # Summary
    result = {
        "path": path,
        "size_bytes": len(raw),
        "viewBox": f"{vb_w}x{vb_h}",
        "font_sizes": sorted(set(font_sizes)),
        "text_elements": len(texts),
        "issues": issues
    }
    
    return result

if __name__ == "__main__":
    import os
    target = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\ROG\.qclaw\workspace-ua58rsb93veqtxl7\_hugo_preview\static\images\diagrams"
    
    for root, dirs, files in os.walk(target):
        for f in files:
            if f.endswith('.svg'):
                path = os.path.join(root, f)
                result = validate_svg(path)
                print(f"\n{'='*50}")
                print(f"Validating: {f}")
                print(f"Size: {result['size_bytes']} bytes | ViewBox: {result['viewBox']}")
                print(f"Font sizes: {result['font_sizes']}px")
                if result['issues']:
                    for level, msg in result['issues']:
                        icon = {"ERROR": "!!", "WARN": "??", "INFO": "ii"}[level]
                        print(f"  {icon} [{level}] {msg}")
                else:
                    print("  [OK] No issues found")
