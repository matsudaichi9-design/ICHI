import json

FONTS = (
    '<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800'
    '&family=Rajdhani:wght@500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet"/>'
)

# ── [VOX|$1|$2] ─────────────────────────────────────────────────────────────
# Spoken dialogue — "voice transmission" HUD frame: 4-corner brackets, fade-in
# lines from each corner toward a center hex mark, faint scanline texture,
# small "// VOICE LINK" tag in the top-left, outer accent-color glow.

def corner(pos_v, pos_h, bord_v, bord_h):
    return (
        f'<div style="position:absolute;{pos_v}:0;{pos_h}:0;width:15px;height:15px;'
        f'border-{bord_v}:2px solid $1;border-{bord_h}:2px solid $1;'
        'opacity:.7;pointer-events:none;"></div>'
    )

def hline(side_v, direction):
    grad = 'linear-gradient(90deg,$1,rgba(0,0,0,0))' if direction == 'ltr' else 'linear-gradient(90deg,rgba(0,0,0,0),$1)'
    anchor = 'left:15px;right:calc(50% + 8px)' if direction == 'ltr' else 'right:15px;left:calc(50% + 8px)'
    op = '.4' if side_v == 'top' else '.26'
    return (
        f'<div style="position:absolute;{side_v}:0;{anchor};height:1px;'
        f'background:{grad};opacity:{op};pointer-events:none;"></div>'
    )

def hexmark(side_v, op):
    shift = 'translate(-50%,-50%)' if side_v == 'top' else 'translate(-50%,50%)'
    return (
        f'<div style="position:absolute;{side_v}:0;left:50%;transform:{shift};'
        f'color:$1;font-size:8px;line-height:1;opacity:{op};pointer-events:none;">⬡</div>'
    )

VOX_HTML = (
    FONTS +

    '<div style="position:relative;max-width:500px;margin:8px auto 16px;'
    'padding:15px 19px 14px;overflow:hidden;border-radius:4px;'
    'background:linear-gradient(150deg,rgba(10,12,22,.74),rgba(5,6,10,.82));'
    "font-family:'Rajdhani',sans-serif;"
    'font-size:14.5px;line-height:1.62;color:#dff6ff;'
    'box-shadow:0 0 22px -8px $1,0 5px 20px rgba(0,0,0,.6);">' +

    # Faint scanline texture
    '<div style="position:absolute;inset:0;pointer-events:none;opacity:.03;z-index:0;'
    'background:repeating-linear-gradient(0deg,#fff 0 1px,transparent 1px 3px);"></div>' +

    # Voice-link tag, top-left
    "<div style=\"position:relative;z-index:1;font-family:'Share Tech Mono',monospace;"
    'font-size:7.5px;letter-spacing:2px;color:$1;opacity:.55;margin-bottom:8px;">// VOICE LINK</div>' +

    # 4 corner brackets
    corner('top',    'left',  'top',    'left')  +
    corner('top',    'right', 'top',    'right') +
    corner('bottom', 'left',  'bottom', 'left')  +
    corner('bottom', 'right', 'bottom', 'right') +

    # Top: left fade-line · ⬡ · right fade-line
    hline('top', 'ltr') +
    hexmark('top', '.7') +
    hline('top', 'rtl') +

    # Bottom: left fade-line · ⬡ · right fade-line
    hline('bottom', 'ltr') +
    hexmark('bottom', '.45') +
    hline('bottom', 'rtl') +

    # Speech text
    '<div style="position:relative;z-index:1;">$2</div>'

    '</div>'
)

vox_data = {
    "id": "cyberverse-dialogue",
    "scriptName": "Cyberverse Dialogue",
    "findRegex": r"/\[VOX\|(.*?)\|([\s\S]*?)\]/g",
    "replaceString": VOX_HTML,
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

# ── [NEURO|$1|$2|$3] ─────────────────────────────────────────────────────────
# Inner monologue — "neural log" readout: HUD label tag (matches the character
# header subtitle signature: line + monospace text + dot) above a left-accent
# log entry box, italic muted text. No 4-corner frame — keeps SAY vs THINK
# visually distinct at a glance.

NEURO_HTML = (
    FONTS +
    '<div style="max-width:500px;margin:9px auto 14px;'
    "font-family:'Rajdhani',sans-serif;\">"

    # Label row — same signature motif as the Cyberverse character header subtitle
    '<div style="display:flex;align-items:center;gap:7px;margin-bottom:7px;">'
    '<span style="height:1px;width:20px;background:linear-gradient(90deg,$2,transparent);flex-shrink:0;"></span>'
    "<span style=\"font-family:'Share Tech Mono',monospace;font-size:8px;letter-spacing:2.2px;"
    'color:$2;opacity:.8;white-space:nowrap;">$1 · NEURAL LOG</span>'
    '<span style="width:4px;height:4px;border-radius:50%;background:$2;opacity:.7;flex-shrink:0;'
    'box-shadow:0 0 4px $2;"></span>'
    '</div>'

    # Log entry box — left accent border, faint dark panel
    '<div style="position:relative;padding:10px 13px;background:rgba(8,10,18,.55);'
    'border-left:3px solid $2;border-radius:0 4px 4px 0;">'
    '<div style="font-style:italic;color:#aab8cc;font-size:13.5px;line-height:1.62;'
    "font-family:'Rajdhani',sans-serif;\">$3</div>"
    '</div>'

    '</div>'
)

neuro_data = {
    "id": "cyberverse-monologue",
    "scriptName": "Cyberverse Monologue",
    "findRegex": r"/\[NEURO\|(.*?)\|(.*?)\|([\s\S]*?)\]/g",
    "replaceString": NEURO_HTML,
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

# ── Write regex JSON ──────────────────────────────────────────────────────────
for data, fname in [
    (vox_data,   "regex_cyberverse_dialogue.json"),
    (neuro_data, "regex_cyberverse_monologue.json"),
]:
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    size = len(json.dumps(data, ensure_ascii=False, indent=4).encode("utf-8"))
    print(f"{fname} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Lorebook — single entry covering both formats ─────────────────────────────
BOILERPLATE = {
    "vectorized": False, "selective": False, "selectiveLogic": 0,
    "addMemo": False, "position": 0, "disable": False,
    "excludeRecursion": False, "preventRecursion": False,
    "delayUntilRecursion": False, "probability": 100, "useProbability": False,
    "depth": 4, "group": "", "groupOverride": False, "groupWeight": 100,
    "scanDepth": None, "caseSensitive": None, "matchWholeWords": None,
    "useGroupScoring": False, "automationId": "", "role": 0,
    "sticky": 0, "cooldown": 0, "delay": 0,
}

def entry(uid, comment, content, order, key=None):
    e = {"uid": uid, "key": key or [], "keysecondary": [],
         "comment": comment, "content": content,
         "constant": True, "order": order, "displayIndex": uid}
    e.update(BOILERPLATE)
    return e

E0 = """\
## CYBERVERSE DIALOGUE & MONOLOGUE SYSTEM

Use these two tags to format spoken dialogue and inner thought for emphasis. Both are optional flourishes — use them for a character's key spoken lines or introspective beats, not for every sentence.

### SPOKEN DIALOGUE — [VOX]
```
[VOX|#hexcolor|Spoken line of dialogue here.]
```
- `#hexcolor` — the speaking character's accent color (match their `[CYBERID]` color if known)
- Use for a notable spoken line — not every line of dialogue needs to be wrapped, reserve it for moments that deserve emphasis (a threat, a confession, a key piece of intel).

Example:
```
[VOX|#00F0FF|"Wakako better have my eddies ready, or this whole job was for nothing."]
```

### INNER MONOLOGUE — [NEURO]
```
[NEURO|Character Name|#hexcolor|Inner thought goes here.]
```
- `Character Name` — whoever is thinking (usually {{user}} or the focus character)
- `#hexcolor` — that character's accent color
- Use for a private, unspoken thought — paranoia, doubt, a calculation, a memory surfacing.

Example:
```
[NEURO|Kai Mercer|#00F0FF|This deal feels wrong. Wakako never pays this much up front.]
```

### RULES
- Both tags render as standalone HTML blocks — place each on its own line, not inline within a paragraph.
- Do not nest one inside the other.
- Use sparingly: 0-2 of each per response is typical. Overuse dilutes the impact.
- Regular dialogue and narration outside these tags should still be written normally — these are accents, not a replacement for prose.\
"""

lorebook = {
    "name": "Cyberverse Dialogue & Monologue",
    "entries": {
        "0": entry(0, "Cyberverse Dialogue & Monologue — Format Instructions", E0, 91),
    }
}

out_lb = "cyberverse_dialogue_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
