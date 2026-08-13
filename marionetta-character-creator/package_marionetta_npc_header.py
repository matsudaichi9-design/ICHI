import json

# Tag syntax: [MARIONETTA_NPC|Name|Role|#hexcolor]
# $1 = Name   $2 = Role/descriptor   $3 = #hexcolor
html = (
    '<link href="https://fonts.googleapis.com/css2?family=UnifrakturMaguntia'
    '&family=Cormorant+Garamond:ital,wght@0,500;1,400;1,500&display=swap" rel="stylesheet"/>'

    # ── Outer strip — thinner ticket-perforation borders, muted vs. the main cast header ──
    '<div style="position:relative;max-width:380px;margin:10px auto 8px;padding:6px 14px 7px;'
    "font-family:'Cormorant Garamond',serif;background:transparent;"
    'border-top:1px dashed rgba(184,134,46,.18);border-bottom:1px dashed rgba(184,134,46,.18);opacity:.92;">'

    # Inner row
    '<div style="position:relative;display:flex;align-items:center;gap:11px;">'

    # ── Small puppet badge — permanent cross-bar & strings glyph, no portrait slot ──
    '<div style="position:relative;width:36px;height:36px;flex-shrink:0;border-radius:50%;'
    'border:1.3px solid $3;background:#0F0A06;'
    'box-shadow:0 0 8px -2px $3,inset 0 0 6px -3px $3;'
    'display:flex;align-items:center;justify-content:center;">'

    '<div style="position:absolute;inset:0;border-radius:50%;'
    'background:radial-gradient(circle at 50% 32%,rgba(184,134,46,.12),#0F0A06 72%);"></div>'

    '<svg width="18" height="18" viewBox="0 0 26 26" fill="none" style="position:relative;z-index:1;opacity:.8;">'
    '<line x1="6" y1="6" x2="20" y2="6" stroke="$3" stroke-width="1.3"/>'
    '<line x1="9" y1="6" x2="6" y2="19" stroke="$3" stroke-width="1" opacity=".8"/>'
    '<line x1="13" y1="6" x2="13" y2="19" stroke="$3" stroke-width="1" opacity=".8"/>'
    '<line x1="17" y1="6" x2="20" y2="19" stroke="$3" stroke-width="1" opacity=".8"/>'
    '<circle cx="6" cy="20" r="1.3" fill="$3"/><circle cx="13" cy="20" r="1.3" fill="$3"/>'
    '<circle cx="20" cy="20" r="1.3" fill="$3"/>'
    '</svg>'

    '</div>'  # end badge

    # ── Text block ──
    '<div style="flex:1;min-width:0;display:flex;align-items:baseline;gap:7px;flex-wrap:wrap;">'

    # Name — smaller blackletter than the main cast header
    "<span style=\"font-family:'UnifrakturMaguntia',cursive;font-size:15.5px;"
    'color:#D8C7A0;letter-spacing:.3px;line-height:1.1;'
    'white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'
    'text-shadow:0 0 9px -3px $3;">$1</span>'

    # Role/descriptor — small pill, accent-colored
    '<span style="font-size:9px;font-style:italic;letter-spacing:.3px;color:$3;'
    'background:rgba(255,255,255,.03);border:1px solid $3;border-radius:99px;'
    'padding:1px 8px;white-space:nowrap;opacity:.9;">$2</span>'

    '</div>'  # end text block

    '</div>'  # end inner row
    '</div>'  # end outer strip
)

data = {
    "id": "marionetta-npc-header",
    "scriptName": "Marionetta NPC Header",
    "findRegex": r"/\[MARIONETTA_NPC\|(.*?)\|(.*?)\|(.*?)\]/g",
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

out = 'regex_marionetta_npc_header.json'
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
## MARIONETTA NPC HEADER

A second, separate header tag for background/incidental characters — the ones who will never have a portrait: townspeople, soldiers, Aspett staff, unnamed circus attendants, one-scene strangers. Use this instead of the main [MARIONETTA|...] character header whenever the speaking/focus character is NOT one of the established named cast.

### SYNTAX
```
[MARIONETTA_NPC|Name|Role|#hexcolor]
```

- `Name` — whatever name or descriptor fits the moment. A real given name if the NPC has one ("Corporal Weiss"), or a plain descriptor in place of a name if they're truly anonymous ("The Ticket Vendor", "A Kalgratti Soldier").
- `Role` — a short 1-4 word tag for who/what they are in this scene (e.g. "Kalgratti Soldier", "Circus Attendant", "Aspett Researcher", "Townsperson", "Ah'kon Captive"). This is what visually distinguishes them from named cast in the UI.
- `#hexcolor` — accent color; reuse the same COLOR GUIDE as the main character header (gold for neutral humans, mystic violet for Ah'kon, steel blue for Kalgratti officials/military, wax red for circus folk, clinical teal for Aspett researchers).

### WHEN TO USE THIS VS. THE MAIN CHARACTER HEADER
- Main `[MARIONETTA|catbox_code|Name|#hexcolor]` header → established named cast (see the Character List entry), whether or not they currently have an image configured.
- This `[MARIONETTA_NPC|...]` header → everyone else: one-off, incidental, or background characters who were never going to get a portrait in the first place. Do not put these NPCs through the main header's `_` no-image fallback — use this dedicated tag instead, so the UI itself reads as "background character" at a glance.

### RULES
- Output it ONCE per response, on its own line, at the very top — same placement rules as the main character header.
- Never repeat it mid-response, even if the NPC speaks multiple times.
- If a background NPC becomes a recurring, named presence in the story, consider "promoting" them to the main character list and header instead of continuing to use this one.
- Omit entirely if the scene has no single focus character (a crowd, a montage, pure narration).

### EXAMPLE
```
[MARIONETTA_NPC|Corporal Weiss|Kalgratti Soldier|#3E5A82]

*He doesn't look up from the checkpoint ledger.* "Papers," he says, already bored of the answer before you give it.
```\
"""

lorebook = {
    "name": "Marionetta NPC Header",
    "entries": {
        "0": entry(0, "Marionetta NPC Header — Format Instructions", E0, 93)
    }
}

out_lb = 'marionetta_npc_header_lorebook.json'
with open(out_lb, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
size_lb = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"Done! {out_lb} — {size_lb:,} bytes ({size_lb/1024:.1f} KB)")
