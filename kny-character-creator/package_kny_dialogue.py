import json

# ── [SAY|$1|$2] ───────────────────────────────────────────────────────────────
# $1 = hex color   $2 = speech text
# Design: left accent strip + diagonal corner brackets (TL+BR) + dark atmospheric box
# Feel: attributed declaration, matches the corner-bracket language of the KNY header

SAY_HTML = (
    '<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;600'
    '&family=Noto+Serif+JP:wght@500;700'
    '&family=Noto+Serif+Thai:wght@500;600&display=swap" rel="stylesheet"/>'

    # Outer container — overflow:hidden clips the left strip to border-radius
    '<div style="position:relative;max-width:500px;margin:6px auto 16px;'
    'padding:12px 17px 13px 19px;overflow:hidden;'
    'background:linear-gradient(150deg,rgba(16,11,24,.65),rgba(8,6,14,.72));'
    'border:1px solid rgba(255,255,255,.08);border-radius:4px;'
    "color:#ede8f5;font-size:14px;line-height:1.66;"
    "font-family:'Shippori Mincho','Noto Serif JP','Noto Serif Thai','Times New Roman',serif;"
    'box-shadow:0 5px 18px rgba(0,0,0,.55),0 0 16px -7px $1;">'

    # Left accent strip — gradient fade top/bottom, clipped by overflow:hidden
    '<div style="position:absolute;left:0;top:0;bottom:0;width:2.5px;'
    'background:linear-gradient(180deg,rgba(0,0,0,0),$1 18%,$1 82%,rgba(0,0,0,0));"></div>'

    # TL corner bracket
    '<span style="position:absolute;top:0;left:0;width:11px;height:11px;'
    'border-top:1.5px solid $1;border-left:1.5px solid $1;opacity:.6;"></span>'

    # BR corner bracket (diagonal pair — asymmetric, more interesting than 4-corner)
    '<span style="position:absolute;bottom:0;right:0;width:11px;height:11px;'
    'border-bottom:1.5px solid $1;border-right:1.5px solid $1;opacity:.6;"></span>'

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
# $1 = character name   $2 = hex color   $3 = inner-thought text
# Design: ◆ Name · 心の声 ◆ label + soft inward-glow container
# Feel: ethereal "soul window" — distinct from the harder SAY box

THINK_HTML = (
    '<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;600'
    '&family=Noto+Serif+JP:wght@500;700'
    '&family=Noto+Serif+Thai:wght@500;600&display=swap" rel="stylesheet"/>'

    '<div style="max-width:494px;margin:9px auto 12px;'
    "font-family:'Shippori Mincho','Noto Serif JP','Noto Serif Thai','Times New Roman',serif;\">"

    # Name label — ◆ Name · 心の声 ◆  (matches our header's subtitle ◆ pattern)
    '<div style="display:flex;align-items:center;gap:5px;margin:0 0 5px 6px;">'
    '<span style="color:$2;font-size:5px;opacity:.65;line-height:1;">◆</span>'
    '<span style="font-size:9.5px;font-weight:600;line-height:1;'
    "font-family:'Shippori Mincho','Noto Serif JP',serif;"
    'letter-spacing:3px;color:$2;">$1 · 心の声</span>'
    '<span style="color:$2;font-size:5px;opacity:.65;line-height:1;">◆</span>'
    '</div>'

    # Thought container — soft, inward glow, no hard bracket corners (distinct from SAY)
    '<div style="background:rgba(6,4,14,.54);border-radius:12px;'
    'border:1px solid rgba(255,255,255,.06);'
    'padding:11px 16px;font-style:italic;color:#adbbd0;font-size:13.5px;line-height:1.65;'
    'box-shadow:inset 0 0 0 1px rgba(255,255,255,.06),'
    'inset 0 2px 24px -8px $2,'
    '0 3px 10px rgba(0,0,0,.4);">'
    '$3'
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

# ── Write both files ──────────────────────────────────────────────────────────

for data, fname in [
    (say_data,   "regex_kny_dialogue.json"),
    (think_data, "regex_kny_monologue.json"),
]:
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    size = len(json.dumps(data, ensure_ascii=False, indent=4).encode("utf-8"))
    print(f"{fname} — {size:,} bytes ({size/1024:.1f} KB)")

print("Done!")
