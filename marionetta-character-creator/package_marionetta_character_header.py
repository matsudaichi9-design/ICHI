import json

html = (
    '<link href="https://fonts.googleapis.com/css2?family=UnifrakturMaguntia'
    '&family=Cormorant+Garamond:ital,wght@0,500;1,400;1,500&display=swap" rel="stylesheet"/>'

    # ── Outer strip — ticket-perforation borders, no solid card ──
    '<div style="position:relative;max-width:420px;margin:14px auto 10px;padding:9px 16px 11px;'
    "font-family:'Cormorant Garamond',serif;background:transparent;"
    'border-top:1px dashed rgba(184,134,46,.28);border-bottom:1px dashed rgba(184,134,46,.28);">'

    # Corner flourishes
    '<div style="position:absolute;top:-8px;left:0;color:$3;font-size:12px;opacity:.6;">❦</div>'
    '<div style="position:absolute;top:-8px;right:0;color:$3;font-size:12px;opacity:.6;'
    'transform:scaleX(-1);">❦</div>'

    # Inner row
    '<div style="position:relative;display:flex;align-items:center;gap:14px;padding-top:4px;">'

    # ── Wax-seal medallion avatar ────────────────────────────────
    '<div style="position:relative;width:54px;height:54px;flex-shrink:0;">'

    # Wax drip — small irregular blob peeking from the bottom edge
    '<div style="position:absolute;bottom:-4px;left:50%;transform:translateX(-50%);width:20px;height:12px;'
    'background:$3;opacity:.85;border-radius:45% 55% 40% 60%/60% 60% 40% 40%;z-index:0;"></div>'

    # Main medallion
    '<div style="position:absolute;inset:0;border-radius:50%;overflow:hidden;z-index:1;'
    'border:2px solid $3;background:#0F0A06;'
    'box-shadow:0 0 14px -2px $3,inset 0 0 10px -4px $3;">'

    # Tint overlay
    '<div style="position:absolute;inset:0;'
    'background:radial-gradient(circle at 50% 32%,rgba(184,134,46,.16),#0F0A06 72%);'
    'z-index:1;pointer-events:none;"></div>'

    # Fallback: marionette cross-bar & strings glyph
    '<div style="position:absolute;inset:0;display:flex;align-items:center;'
    'justify-content:center;z-index:2;">'
    '<svg width="26" height="26" viewBox="0 0 26 26" fill="none">'
    '<line x1="6" y1="6" x2="20" y2="6" stroke="$3" stroke-width="1.4"/>'
    '<line x1="9" y1="6" x2="6" y2="19" stroke="$3" stroke-width="1.1" opacity=".85"/>'
    '<line x1="13" y1="6" x2="13" y2="19" stroke="$3" stroke-width="1.1" opacity=".85"/>'
    '<line x1="17" y1="6" x2="20" y2="19" stroke="$3" stroke-width="1.1" opacity=".85"/>'
    '<circle cx="6" cy="20" r="1.5" fill="$3"/><circle cx="13" cy="20" r="1.5" fill="$3"/>'
    '<circle cx="20" cy="20" r="1.5" fill="$3"/>'
    '</svg></div>'

    # Portrait
    '<img src="https://files.catbox.moe/$1" alt="$2" '
    'style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;'
    'display:block;background:#0F0A06;z-index:3;" onerror="this.style.display=\'none\'"/>'

    '</div>'  # end medallion
    '</div>'  # end avatar wrap

    # ── Text block ────────────────────────────────────────────────────
    '<div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:4px;">'

    # Name — blackletter
    "<span style=\"font-family:'UnifrakturMaguntia',cursive;font-size:19px;"
    'color:#E8D9B8;letter-spacing:.5px;line-height:1.15;'
    'white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'
    'text-shadow:0 0 14px -2px $3;">$2</span>'

    # Subtitle — flanked flourish, italic
    "<span style=\"font-size:11px;font-style:italic;color:#B8A585;letter-spacing:.3px;\">"
    '<span style="color:$3;opacity:.75;">❦</span> Bound to the Stage '
    '<span style="color:$3;opacity:.75;">❦</span></span>'

    '</div>'  # end text block

    '</div>'  # end inner row

    '</div>'  # end outer strip
)

data = {
    "id": "marionetta-character-header",
    "scriptName": "Marionetta Character Header",
    "findRegex": r"/\[MARIONETTA\|(.*?)\|(.*?)\|(.*?)\]/g",
    "replaceString": html,
    "trimStrings": [],
    "placement": [1, 2],
    "disabled": False,
    "markdownOnly": True,
    "promptOnly": False,
    "runOnEdit": True,
    "substituteRegex": 0,
    "minDepth": None,
    "maxDepth": 2
}

out = 'regex_marionetta_character_header.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Lorebook ──────────────────────────────────────────────────────────────────
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
## MARIONETTA CHARACTER HEADER

At the very start of your response (before any narrative or dialogue), output a character header tag when the scene focuses on a specific character.

### SYNTAX
```
[MARIONETTA|catbox_code|Character Name|#hexcolor]
```

- `catbox_code` — filename from files.catbox.moe (e.g. `abc123.jpg`). If no image is configured, write `_` and the marionette-strings placeholder will appear automatically.
- `Character Name` — full name, alias in quotes optional (e.g. `Odile Marchetti "The Vanishing Girl"`)
- `#hexcolor` — accent color for the character; use the guide below if not otherwise specified

### COLOR GUIDE
| Character type | Color |
|---|---|
| Human protagonist / neutral | `#B8862E` (antique gold) |
| Ah'kon | `#5A3E8A` (mystic violet) |
| Kalgratti official / military | `#3E5A82` (steel blue) |
| Circus troupe / performer | `#7A1220` (wax red) |
| Steinheimer / antagonist | `#7A1220` with a colder edge — pair with narration, not hue, to convey menace |
| Researcher / Aspett staff | `#3E7A82` (clinical teal) |

### WHEN TO OUTPUT
- At the start of a response where YOU (the AI) are speaking or acting as a specific named character
- When a scene begins and a particular character is the clear focus
- When introducing a new character for the first time

### RULES
- Output it ONCE per response, on its own line, at the very top
- Never repeat it mid-response
- Do NOT output it for background/unnamed characters
- Use the PLAYER CHARACTER's configured color if narrating from their POV
- If the scene has no single focus character, omit the tag entirely

### EXAMPLE
```
[MARIONETTA|abc123.jpg|Odile Marchetti|#5A3E8A]

The scarf shifted as she tilted her head, just enough to make you wonder what it hid. "You're staring," she said, not unkindly.
```\
"""

lorebook = {
    "name": "Marionetta Character Header",
    "entries": {
        "0": entry(0, "Marionetta Character Header — Format Instructions", E0, 92)
    }
}

out_lb = 'marionetta_character_header_lorebook.json'
with open(out_lb, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
size_lb = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"Done! {out_lb} — {size_lb:,} bytes ({size_lb/1024:.1f} KB)")
