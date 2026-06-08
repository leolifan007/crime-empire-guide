#!/usr/bin/env python3
import sys, re, os

IDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images', 'game-icons')

def check(fp):
    e = w = 0
    with open(fp, 'rb') as f: raw = f.read()
    print('--- QA: ' + os.path.basename(fp) + ' ---')

    if raw[:3] == b'\xef\xbb\xbf': print('  FAIL BOM'); e += 1
    else: print('  PASS BOM')

    t = raw.decode('utf-8')
    body = t
    m = re.match(r'^---\n.*?\n---\n(.*)', t, re.DOTALL)
    if m: body = m.group(1)

    bad = {'emdash':chr(0x2014),'endash':chr(0x2013),
           'lsquo':chr(0x2018),'rsquo':chr(0x2019),
           'ldquo':chr(0x201C),'rdquo':chr(0x201D),'nbsp':chr(0xA0)}
    fb = [k for k,v in bad.items() if v in t]
    if fb: print('  FAIL Unicode:', fb); e += 1
    else: print('  PASS Unicode')

    for ch in body:
        if ord(ch) > 0xFFFF: print('  FAIL emoji'); e += 1; break
    else: print('  PASS emoji')

    oc = t.count('{{<'); cc = t.count('>}}'); ic = t.count('/>}}'); tc = cc - ic
    if oc != tc: print('  FAIL shortcodes', oc, 'vs', tc); e += 1
    else: print('  PASS shortcodes', oc)

    irefs = set(re.findall(r'\{\{<\s*material\s+"(.+?)"', body))
    mi = [i for i in irefs if not os.path.exists(os.path.join(IDIR, i + '.png'))]
    if mi: print('  FAIL icons:', mi); e += 1
    else: print('  PASS icons', len(irefs))

    pt = re.sub(r'\{\{<.*?\}\}', '', body)
    pt = re.sub(r'<[^>]+>', '', pt)
    wc = len(pt.split())
    if wc < 600: print('  WARN wc', wc); w += 1
    else: print('  PASS wc', wc)

    dg = len(re.findall(r'\{\{<\s*diagram', body))
    sg = len(re.findall(r'\{\{<\s*stepgroup', body))
    tl = len(re.findall(r'^\|', body, re.MULTILINE))
    ds = (1 if dg > 0 else 0) + (1 if sg > 0 else 0) + (1 if tl >= 3 else 0)
    if ds < 2: print('  WARN data', ds); w += 1
    else: print('  PASS data', ds)

    il = len(re.findall(r'/schedule-i/', body))
    if il == 0: print('  WARN no internal links'); w += 1
    else: print('  PASS internal links', il)

    rg = len(re.findall(r'\{\{<\s*resourcegrid', body))
    if rg == 0: print('  WARN no resourcegrid'); w += 1
    else: print('  PASS resourcegrid')

    if e == 0 and w == 0: print('=== PASSED clean ==='); return 0
    if e == 0: print('=== PASSED', w, 'warnings ==='); return 0
    print('=== FAILED', e, 'errors', w, 'warnings ===')
    return 1

if __name__ == '__main__':
    sys.exit(check(sys.argv[1]))
