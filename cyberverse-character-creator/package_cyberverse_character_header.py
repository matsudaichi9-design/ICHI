import json

html = (
    '<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800;900'
    '&family=Rajdhani:wght@500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet"/>'

    # ── Outer container — dark HUD panel, flat border, faint scanlines ──
    '<div style="position:relative;max-width:420px;margin:14px auto 10px;padding:11px 14px 12px;'
    "font-family:'Rajdhani',sans-serif;overflow:hidden;border-radius:5px;"
    'background:linear-gradient(165deg,#0a0c16 0%,#05060a 100%);'
    'border:1px solid rgba(0,0,0,.6);box-shadow:0 0 0 1px $3 inset,0 8px 26px -10px rgba(0,0,0,.85);">'

    # Scanline texture overlay
    '<div style="position:absolute;inset:0;pointer-events:none;opacity:.035;z-index:0;'
    'background:repeating-linear-gradient(0deg,#fff 0 1px,transparent 1px 3px);"></div>'

    # Top accent rule
    '<div style="position:absolute;top:0;left:0;right:0;height:2px;background:$3;opacity:.85;"></div>'

    # Inner row
    '<div style="position:relative;z-index:1;display:flex;align-items:center;gap:13px;">'

    # ── Avatar — octagonal HUD-clipped frame with targeting reticle ticks ──
    '<div style="position:relative;width:56px;height:56px;flex-shrink:0;">'

    # Border-fill layer (octagon)
    '<div style="position:absolute;inset:0;'
    'clip-path:polygon(20% 0,80% 0,100% 20%,100% 80%,80% 100%,20% 100%,0 80%,0 20%);'
    'background:$3;box-shadow:0 0 14px -3px $3;"></div>'

    # Content layer (octagon, inset to fake a clipped border)
    '<div style="position:absolute;inset:1.6px;overflow:hidden;'
    'clip-path:polygon(20% 0,80% 0,100% 20%,100% 80%,80% 100%,20% 100%,0 80%,0 20%);'
    'background:#05060a;">'

    # Tint overlay
    '<div style="position:absolute;inset:0;'
    'background:radial-gradient(circle at 50% 34%,rgba(0,240,255,.16),#05060a 72%);'
    'z-index:1;pointer-events:none;"></div>'

    # Fallback silhouette
    '<div style="position:absolute;inset:0;display:flex;align-items:center;'
    'justify-content:center;z-index:2;">'
    '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="$3" '
    'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" style="opacity:.8;">'
    '<circle cx="12" cy="8.5" r="3.5"/>'
    '<path d="M5 20.5a7 7 0 0 1 14 0"/>'
    '</svg></div>'

    # Portrait
    '<img src="https://files.catbox.moe/$1" alt="$2" '
    'style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;'
    'display:block;background:#05060a;z-index:3;" onerror="this.style.display=\'none\'"/>'

    '</div>'  # end content layer

    # Targeting reticle ticks — 4 corners around the avatar
    '<div style="position:absolute;top:-3px;left:-3px;width:8px;height:8px;'
    'border-top:1.5px solid $3;border-left:1.5px solid $3;opacity:.85;pointer-events:none;"></div>'
    '<div style="position:absolute;top:-3px;right:-3px;width:8px;height:8px;'
    'border-top:1.5px solid $3;border-right:1.5px solid $3;opacity:.85;pointer-events:none;"></div>'
    '<div style="position:absolute;bottom:-3px;left:-3px;width:8px;height:8px;'
    'border-bottom:1.5px solid $3;border-left:1.5px solid $3;opacity:.85;pointer-events:none;"></div>'
    '<div style="position:absolute;bottom:-3px;right:-3px;width:8px;height:8px;'
    'border-bottom:1.5px solid $3;border-right:1.5px solid $3;opacity:.85;pointer-events:none;"></div>'

    # Online status dot
    '<div style="position:absolute;bottom:1px;left:1px;width:9px;height:9px;border-radius:50%;z-index:10;'
    'background:#39ff8a;border:1.5px solid #05060a;box-shadow:0 0 6px 1px rgba(57,255,138,.7);"></div>'

    # Chip badge — top-right corner
    '<div style="position:absolute;top:-4px;right:-4px;z-index:10;width:15px;height:15px;'
    'border-radius:3px;background:$3;display:flex;align-items:center;justify-content:center;'
    'box-shadow:0 0 8px -1px $3;">'
    '<svg viewBox="0 0 16 16" width="9" height="9" fill="none">'
    '<rect x="5" y="5" width="6" height="6" rx="1" stroke="#05060a" stroke-width="1.3"/>'
    '<line x1="8" y1="1" x2="8" y2="5" stroke="#05060a" stroke-width="1.3"/>'
    '<line x1="8" y1="11" x2="8" y2="15" stroke="#05060a" stroke-width="1.3"/>'
    '<line x1="1" y1="8" x2="5" y2="8" stroke="#05060a" stroke-width="1.3"/>'
    '<line x1="11" y1="8" x2="15" y2="8" stroke="#05060a" stroke-width="1.3"/>'
    '</svg>'
    '</div>'

    '</div>'  # end avatar

    # ── Text block ────────────────────────────────────────────────────
    '<div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:5px;">'

    # Name
    "<span style=\"font-family:'Orbitron',sans-serif;font-size:14px;font-weight:700;"
    'color:#eafcff;letter-spacing:1px;text-transform:uppercase;'
    'white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'
    'text-shadow:0 0 14px -2px $3;">$2</span>'

    # Subtitle row — monospace HUD tag, no pill/kanji
    '<div style="display:flex;align-items:center;gap:7px;">'
    '<span style="height:1px;width:20px;background:linear-gradient(90deg,$3,transparent);flex-shrink:0;"></span>'
    "<span style=\"font-family:'Share Tech Mono',monospace;font-size:8px;letter-spacing:2.2px;"
    'color:$3;opacity:.85;white-space:nowrap;">VERIFIED · NET-ID</span>'
    '<span style="width:4px;height:4px;border-radius:50%;background:$3;opacity:.7;flex-shrink:0;'
    'box-shadow:0 0 4px $3;"></span>'
    '</div>'

    '</div>'  # end text block

    '</div>'  # end inner row

    # Bottom divider
    '<div style="position:relative;z-index:1;height:1px;margin-top:11px;'
    'background:linear-gradient(90deg,$3,rgba(0,240,255,.12) 65%,transparent);opacity:.6;"></div>'

    '</div>'  # end outer container
)

data = {
    "id": "cyberverse-character-header",
    "scriptName": "Cyberverse Character Header",
    "findRegex": r"/\[CYBERID\|(.*?)\|(.*?)\|(.*?)\]/g",
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

out = 'regex_cyberverse_character_header.json'
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
## CYBERVERSE CHARACTER HEADER

At the very start of your response (before any narrative or dialogue), output a character header tag when the scene focuses on a specific character.

### SYNTAX
```
[CYBERID|catbox_code|Character Name|#hexcolor]
```

- `catbox_code` — filename from files.catbox.moe (e.g. `abc123.jpg`). If no image is configured, write `_` and the silhouette placeholder will appear automatically.
- `Character Name` — full name or street handle (e.g. `Kai "Nightowl" Mercer`)
- `#hexcolor` — accent color for the character; use role default if not specified

### ROLE ACCENT COLORS
| Role | Color |
|---------|-------|
| Solo / merc | `#FF3B6E` |
| Netrunner | `#00F0FF` |
| Techie | `#FFB627` |
| Fixer | `#B070E0` |
| Corpo | `#5088D8` |
| Nomad | `#FF8C42` |
| Media / Rockerboy | `#FF2079` |
| Civilian / unaffiliated | `#7898C8` |

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
[CYBERID|abc123.jpg|Kai "Nightowl" Mercer|#00F0FF]

A flicker of optic feedback crossed Kai's vision as the alley's neon bled through the rain. "Wakako better have my eddies ready."
```\
"""

lorebook = {
    "name": "Cyberverse Character Header",
    "entries": {
        "0": entry(0, "Cyberverse Character Header — Format Instructions", E0, 92)
    }
}

out_lb = 'cyberverse_character_header_lorebook.json'
with open(out_lb, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
size_lb = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"Done! {out_lb} — {size_lb:,} bytes ({size_lb/1024:.1f} KB)")
