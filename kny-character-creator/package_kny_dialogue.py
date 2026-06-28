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
# Same outer frame as KNY header: TL+BR brackets, padding:11px 14px, transparent bg
# Minimal rgba background so text stays legible against any chat theme

SAY_HTML = (
    FONTS +
    '<div style="position:relative;max-width:500px;margin:6px auto 14px;'
    'padding:11px 14px;background:rgba(10,6,18,.32);'
    "font-family:'Shippori Mincho','Noto Serif JP','Noto Serif Thai','Times New Roman',serif;"
    'font-size:14px;line-height:1.66;color:#ede8f5;">' +
    tl('$1') + br('$1') +
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
