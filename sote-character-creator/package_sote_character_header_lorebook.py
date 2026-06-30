import json

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
## SOTE CHARACTER HEADER

At the very start of your response (before any narrative or dialogue), output a character header tag when the scene focuses on a specific character.

### SYNTAX
```
[SOTE|catbox_code|Character Name|#hexcolor]
```

- `catbox_code` — filename from files.catbox.moe (e.g. `abc123.jpg`). If no image is configured, write `_` and the silhouette placeholder will appear automatically.
- `Character Name` — full name, rank/unit optional (e.g. `Yuichiro Hyakuya`, `Lieutenant Colonel · Guren Ichinose`)
- `#hexcolor` — accent color for the character; use faction default if not specified

### FACTION ACCENT COLORS
| Faction | Color |
|---------|-------|
| JIDA soldier / Moon Demon Company | `#8B1A1A` |
| vampire nobility / progenitor | `#5A1040` |
| vampire (lower rank, no progenitor) | `#7A2050` |
| seraph / horseman of the apocalypse | `#C4A830` |
| Hyakuya orphan / civilian | `#5A7A9B` |
| Hyakuya Sect / cultist | `#2A2A3A` |

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
[SOTE|abc123.jpg|Yuichiro Hyakuya|#8B1A1A]

"I'll kill every last one of them." Yuichiro's grip tightened on Asuramaru's hilt as the vampire's silhouette emerged from the dark.
```\
"""

lorebook = {
    "name": "SOTE Character Header",
    "entries": {
        "0": entry(0, "SOTE Character Header — Core Instructions", E0, 92),
    }
}

out = "sote_character_header_lorebook.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)

size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
