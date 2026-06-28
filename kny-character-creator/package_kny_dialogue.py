import json

FONTS = (
    '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700'
    '&family=Shippori+Mincho:wght@500;600&family=Noto+Serif+JP:wght@500;700'
    '&family=Noto+Serif+Thai:wght@500;600&display=swap" rel="stylesheet"/>'
)

# Bracket helpers — IDENTICAL spec to the KNY character header
# header: width:13px;height:13px;border-X:1.5px solid $COLOR;opacity:.55
def tl(c):
    return (
        '<div style="position:absolute;top:0;left:0;width:13px;height:13px;'
        f'border-top:1.5px solid {c};border-left:1.5px solid {c};'
        'opacity:.55;pointer-events:none;"></div>'
    )
def br(c):
    return (
        '<div style="position:absolute;bottom:0;right:0;width:13px;height:13px;'
        f'border-bottom:1.5px solid {c};border-right:1.5px solid {c};'
        'opacity:.55;pointer-events:none;"></div>'
    )

# ── [SAY|$1|$2] ───────────────────────────────────────────────────────────────
# Design: 4-corner brackets (all corners) + fade-in lines from each corner toward
# center ◆ at top and bottom + colored outer glow
# Feel: "Breathing Form Declaration" — vivid, framed, distinctly KNY

def corner(pos_v, pos_h, bord_v, bord_h):
    return (
        f'<div style="position:absolute;{pos_v}:0;{pos_h}:0;width:16px;height:16px;'
        f'border-{bord_v}:2px solid $1;border-{bord_h}:2px solid $1;'
        'opacity:.7;pointer-events:none;"></div>'
    )

def hline(side_v, side_h, direction):
    # Horizontal fade-line from corner toward center on one side of top or bottom
    grad = f'linear-gradient(90deg,$1,rgba(0,0,0,0))' if direction == 'ltr' else f'linear-gradient(90deg,rgba(0,0,0,0),$1)'
    anchor = 'left:16px;right:calc(50% + 9px)' if direction == 'ltr' else 'right:16px;left:calc(50% + 9px)'
    op = '.42' if side_v == 'top' else '.28'
    return (
        f'<div style="position:absolute;{side_v}:0;{anchor};height:1px;'
        f'background:{grad};opacity:{op};pointer-events:none;"></div>'
    )

def diamond(side_v, op):
    # ◆ centered on top or bottom edge
    shift = 'translate(-50%,-50%)' if side_v == 'top' else 'translate(-50%,50%)'
    return (
        f'<div style="position:absolute;{side_v}:0;left:50%;transform:{shift};'
        f'color:$1;font-size:7px;line-height:1;opacity:{op};pointer-events:none;">◆</div>'
    )

SAY_HTML = (
    FONTS +

    # Outer container — dark atmospheric bg + outer color glow
    '<div style="position:relative;max-width:500px;margin:8px auto 16px;'
    'padding:14px 18px;'
    'background:linear-gradient(150deg,rgba(14,9,22,.6),rgba(7,5,13,.68));'
    "font-family:'Shippori Mincho','Noto Serif JP','Noto Serif Thai','Times New Roman',serif;"
    'font-size:14px;line-height:1.68;color:#ede8f5;'
    'box-shadow:0 0 24px -8px $1,0 5px 20px rgba(0,0,0,.55);">' +

    # 4 corner brackets
    corner('top',    'left',  'top',    'left')  +
    corner('top',    'right', 'top',    'right') +
    corner('bottom', 'left',  'bottom', 'left')  +
    corner('bottom', 'right', 'bottom', 'right') +

    # Top: left fade-line · ◆ · right fade-line
    hline('top', 'left',  'ltr') +
    diamond('top', '.65')        +
    hline('top', 'right', 'rtl') +

    # Bottom: left fade-line · ◆ · right fade-line
    hline('bottom', 'left',  'ltr') +
    diamond('bottom', '.45')        +
    hline('bottom', 'right', 'rtl') +

    # Speech text
    '$2'

    '</div>'
)

say_data = {
    "id": "cbe44225-0ea5-4b88-88c1-58529986e51f",
    "scriptName": "KNY Dialogue",
    "findRegex": r"/\[SAY\|(.*?)\|([\s\S]*?)\]/g",
    "replaceString": SAY_HTML,
    "trimStrings": [],
    "placement": [1, 2],
    "disabled": False,
    "markdownOnly": True,
    "promptOnly": False,
    "runOnEdit": True,
    "substituteRegex": 0,
    "minDepth": None,
    "maxDepth": 3
}

# ── [THINK|$1|$2|$3] ─────────────────────────────────────────────────────────
# Name label = pill style IDENTICAL to the KNY header subtitle pill
#   header pill: border:1px solid $3;border-radius:20px;padding:2px 9px;opacity:.72
# Thought area = same TL+BR bracket frame as the header outer container

THINK_HTML = (
    FONTS +
    '<div style="max-width:500px;margin:9px auto 14px;'
    "font-family:'Shippori Mincho','Noto Serif JP','Noto Serif Thai','Times New Roman',serif;\">"

    # Name pill — same spec as header subtitle pill
    '<div style="margin:0 0 7px 0;">'
    '<span style="display:inline-flex;align-items:center;gap:5px;'
    'border:1px solid $2;border-radius:20px;padding:2px 9px;opacity:.72;">'
    '<span style="color:$2;font-size:5px;line-height:1;">◆</span>'
    '<span style="font-size:7.5px;letter-spacing:3px;color:#7a6f88;'
    "font-family:'Shippori Mincho','Noto Serif JP',serif;\">$1 · 心の声</span>"
    '<span style="color:$2;font-size:5px;line-height:1;">◆</span>'
    '</span>'
    '</div>'

    # Thought container — same TL+BR bracket frame
    '<div style="position:relative;padding:11px 14px;background:rgba(6,4,14,.36);">' +
    tl('$2') + br('$2') +
    '<div style="font-style:italic;color:#adbbd0;font-size:13.5px;line-height:1.65;">$3</div>'
    '</div>'

    '</div>'
)

think_data = {
    "id": "1cd0005a-2c80-49e0-aaba-704f2aeba671",
    "scriptName": "KNY Monologue",
    "findRegex": r"/\[THINK\|(.*?)\|(.*?)\|([\s\S]*?)\]/g",
    "replaceString": THINK_HTML,
    "trimStrings": [],
    "placement": [1, 2],
    "disabled": False,
    "markdownOnly": True,
    "promptOnly": False,
    "runOnEdit": True,
    "substituteRegex": 0,
    "minDepth": None,
    "maxDepth": 3
}

# ── Write ─────────────────────────────────────────────────────────────────────

for data, fname in [
    (say_data,   "regex_kny_dialogue.json"),
    (think_data, "regex_kny_monologue.json"),
]:
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    size = len(json.dumps(data, ensure_ascii=False, indent=4).encode("utf-8"))
    print(f"{fname} — {size:,} bytes ({size/1024:.1f} KB)")

print("Done!")
