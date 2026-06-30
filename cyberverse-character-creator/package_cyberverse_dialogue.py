import json

FONTS = (
    '<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800'
    '&family=Rajdhani:wght@500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet"/>'
)

# ── [VOX|$1|$2] ─────────────────────────────────────────────────────────────
# Spoken dialogue — "voice-message" data panel: asymmetric notched corners
# (top-left + bottom-right cut), a static waveform column + sideways-rotated
# "VOICE LINK" tag on the left edge, faint scanline texture, outer glow.
# Distinct silhouette from the symmetric bracket frames used elsewhere.

NOTCH = 'polygon(15px 0,100% 0,100% calc(100% - 15px),calc(100% - 15px) 100%,0 100%,0 15px)'

# Static waveform bars — fixed heights in px for a "snapshot" look
BAR_HEIGHTS = [9, 16, 24, 13, 20, 8, 15]

def waveform():
    bars = ''.join(
        f'<div style="width:3px;height:{h}px;border-radius:2px;background:$1;'
        f'opacity:{".9" if h > 18 else ".55"};box-shadow:0 0 4px -1px $1;"></div>'
        for h in BAR_HEIGHTS
    )
    return (
        '<div style="display:flex;align-items:flex-end;gap:2.5px;height:24px;flex-shrink:0;">'
        + bars + '</div>'
    )

VOX_HTML = (
    FONTS +

    '<div style="position:relative;max-width:500px;margin:8px auto 16px;">'

    # Border-fill layer (notched, colored, glow)
    f'<div style="position:absolute;inset:0;clip-path:{NOTCH};background:$1;'
    'box-shadow:0 0 22px -8px $1;"></div>'

    # Content layer (notched, inset to fake a clipped border)
    f'<div style="position:relative;clip-path:{NOTCH};margin:1.6px;overflow:hidden;'
    'background:linear-gradient(150deg,rgba(10,12,22,.92),rgba(5,6,10,.96));'
    "font-family:'Rajdhani',sans-serif;font-size:14.5px;line-height:1.62;color:#dff6ff;"
    'box-shadow:0 5px 20px rgba(0,0,0,.6);">' +

    # Faint scanline texture
    '<div style="position:absolute;inset:0;pointer-events:none;opacity:.03;z-index:0;'
    'background:repeating-linear-gradient(0deg,#fff 0 1px,transparent 1px 3px);"></div>' +

    # Inner row: rotated tag + waveform | divider | text
    '<div style="position:relative;z-index:1;display:flex;align-items:center;'
    'gap:13px;padding:14px 18px 14px 15px;">' +

    # Left column — sideways label above a static waveform snapshot
    '<div style="display:flex;flex-direction:column;align-items:center;gap:7px;flex-shrink:0;">'
    "<span style=\"writing-mode:vertical-rl;font-family:'Share Tech Mono',monospace;"
    'font-size:7px;letter-spacing:2px;color:$1;opacity:.6;">VOICE LINK</span>' +
    waveform() +
    '</div>' +

    # Divider
    '<div style="width:1px;align-self:stretch;background:$1;opacity:.22;flex-shrink:0;"></div>' +

    # Speech text
    '<div style="flex:1;min-width:0;">$2</div>' +

    '</div>'  # end inner row

    '</div>'  # end content layer
    '</div>'  # end outer wrap
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
