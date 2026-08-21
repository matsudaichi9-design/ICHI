import json

html = (
    '<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800;900'
    '&family=Rajdhani:wght@500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet"/>'

    # ── Outer wrapper — icon-led, no card chrome (matches main header) ──
    '<div style="position:relative;max-width:420px;margin:14px auto 10px;'
    "font-family:'Rajdhani',sans-serif;background:transparent;\">"

    # Inner row
    '<div style="position:relative;z-index:1;display:flex;align-items:center;gap:13px;">'

    # Left accent bar — replaces the avatar for unidentified NPCs
    '<div style="width:3px;height:38px;flex-shrink:0;background:$2;'
    'border-radius:1.5px;opacity:.75;box-shadow:0 0 8px -1px $2;"></div>'

    # ── Text block ────────────────────────────────────────────────────
    '<div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:5px;">'

    # Name
    "<span style=\"font-family:'Orbitron',sans-serif;font-size:14px;font-weight:700;"
    'color:#eafcff;letter-spacing:1px;text-transform:uppercase;'
    'white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'
    'text-shadow:0 0 14px -2px $2;">$1</span>'

    # Subtitle row — "no record" HUD tag, mirrors the header signature
    '<div style="display:flex;align-items:center;gap:7px;">'
    '<span style="height:1px;width:20px;background:linear-gradient(90deg,$2,transparent);flex-shrink:0;"></span>'
    "<span style=\"font-family:'Share Tech Mono',monospace;font-size:8px;letter-spacing:2.2px;"
    'color:$2;opacity:.7;white-space:nowrap;">UNVERIFIED · NO DATA</span>'
    '<span style="width:4px;height:4px;border-radius:50%;background:$2;opacity:.55;flex-shrink:0;"></span>'
    '</div>'

    '</div>'  # end text block

    '</div>'  # end inner row

    '</div>'  # end outer wrapper
)

data = {
    "id": "cyberverse-npc-header",
    "scriptName": "Cyberverse NPC Header",
    "findRegex": r"/\[CYBERNPC\|(.*?)\|(.*?)\]/g",
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

out = 'regex_cyberverse_npc_header.json'
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
## CYBERVERSE NPC HEADER SYSTEM

### FORMAT
[CYBERNPC|Name (Role)|#hexcolor]

Place at the very start of your response — before narrative or dialogue — when an NPC who is NOT a named/established character first appears or speaks in the current response.

### WHEN TO USE
• Street vendors, fixers-of-the-moment, bar patrons, gang grunts
• Unnamed corpo security, drones' operators, ripperdocs without a recurring role
• Any character introduced organically during the scene who has no portrait/ID on file
• Do NOT use for characters in the established Character List — those use [CYBERID|catbox_code|Name|#hexcolor]
• Do NOT use for {{user}}

### COLOR GUIDE
Pick a color that fits the character's affiliation and vibe:
• Unnamed corpo security / suits:      #5088D8 (steel corporate blue)
• Gang muscle (generic/unaffiliated):  #C4432A (rust-red aggression)
• Street vendor / fixer contact:       #8A7A5A (worn utilitarian brown)
• Ripperdoc / med tech:                #4A9BA8 (clinical teal)
• Netrunner-for-hire:                  #B070E0 (data-purple)
• Nomad / drifter:                     #FF8C42 (dusty road orange)
• Civilian / bystander:                #7898C8 (muted neutral blue-grey)

### NAMING CONVENTION
Include a role descriptor after the name when no real name is known:
  "Corpo Security (Arasaka Plaza)"
  "Ripperdoc (Back-Alley Clinic)"
  "Maelstrom Grunt (Unnamed)"
  "Fixer Contact (Watson District)"
If given a real name/handle, use it directly: "Ozob \"Ratchet\" Nkemdi (Fixer)"

### RESPONSE FORMAT
Structure your response exactly like this:

[CYBERNPC|Ripperdoc (Back-Alley Clinic)|#4A9BA8]

The old ripperdoc didn't look up from her tray of tools. "Sit down, and don't bleed on my chair."

### RULE
Use [CYBERNPC] ONCE per NPC per response, placed immediately before their first appearance or spoken line. Never repeat the tag for the same character later in the same response.\
"""

lorebook = {
    "name": "Cyberverse NPC Header",
    "entries": {
        "0": entry(0, "Cyberverse NPC Header — Format Instructions", E0, 91)
    }
}

out_lb = 'cyberverse_npc_header_lorebook.json'
with open(out_lb, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
size_lb = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"Done! {out_lb} — {size_lb:,} bytes ({size_lb/1024:.1f} KB)")
