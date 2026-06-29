import json

FONTS = (
    '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700'
    '&family=Shippori+Mincho:wght@500;600&family=Noto+Serif+JP:wght@500;700'
    '&family=Noto+Serif+Thai:wght@500;600&display=swap" rel="stylesheet"/>'
)

html = (
    FONTS +

    '<div style="position:relative;max-width:420px;margin:14px auto 10px;padding:11px 14px;'
    "font-family:'Shippori Mincho','Noto Serif JP','Noto Serif Thai','Times New Roman',serif;"
    'background:transparent;">'

    # TL bracket — same spec as main header
    '<div style="position:absolute;top:0;left:0;width:13px;height:13px;'
    'border-top:1.5px solid $2;border-left:1.5px solid $2;opacity:.55;'
    'pointer-events:none;"></div>'

    # BR bracket
    '<div style="position:absolute;bottom:0;right:0;width:13px;height:13px;'
    'border-bottom:1.5px solid $2;border-right:1.5px solid $2;opacity:.55;'
    'pointer-events:none;"></div>'

    # Watermark 鬼
    '<div style="position:absolute;right:14px;top:50%;transform:translateY(-50%);'
    "font-family:'Noto Serif JP','Shippori Mincho',serif;"
    'font-size:62px;font-weight:700;color:$2;opacity:.07;line-height:1;'
    'pointer-events:none;user-select:none;z-index:0;letter-spacing:0;">鬼</div>'

    # Inner row
    '<div style="position:relative;z-index:1;display:flex;align-items:center;gap:13px;">'

    # Left accent bar — replaces the avatar for unnamed NPCs
    '<div style="width:3px;height:42px;flex-shrink:0;background:$2;'
    'border-radius:1.5px;opacity:.75;"></div>'

    # Text block
    '<div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:5px;">'

    # Name
    "<span style=\"font-family:'Cinzel','Times New Roman',serif;"
    'font-size:14.5px;font-weight:600;color:#f0eae0;letter-spacing:1.5px;'
    'white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'
    'text-shadow:0 0 18px -4px $2;\">$1</span>'

    # Divider
    '<div style="height:1px;background:linear-gradient(90deg,$2,rgba(0,0,0,0) 70%);'
    'opacity:.38;"></div>'

    # Pill — "― ― ―" signals unnamed/anonymous NPC
    '<div>'
    '<span style="display:inline-flex;align-items:center;gap:5px;'
    'border:1px solid $2;border-radius:20px;padding:2px 9px;opacity:.72;">'
    '<span style="color:$2;font-size:5px;line-height:1;">◆</span>'
    "<span style=\"font-size:7.5px;letter-spacing:5px;color:#7a6f88;"
    "font-family:'Shippori Mincho','Noto Serif JP',serif;\">― ― ―</span>"
    '<span style="color:$2;font-size:5px;line-height:1;">◆</span>'
    '</span>'
    '</div>'

    '</div>'  # end text block
    '</div>'  # end inner row
    '</div>'  # end outer container
)

regex_data = {
    "id": "kny-npc-header",
    "scriptName": "KNY NPC Header",
    "findRegex": r"/\[KNYNPC\|(.*?)\|(.*?)\]/g",
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
## KNY NPC HEADER SYSTEM

### FORMAT
[KNYNPC|Name (Role)|#hexcolor]

Place at the very start of your response — before narrative or dialogue — when an NPC who is NOT in the main character list first appears or speaks in the current response.

### WHEN TO USE
• Townspeople, bystanders, merchants, villagers
• Unnamed or minor demons not listed in the character list
• Wisteria House staff, medical personnel, Corps clerks
• Any character introduced organically during the scene
• Do NOT use for characters in the KNY Character List — those use [KNY|code|name|hex]
• Do NOT use for {{user}}

### COLOR GUIDE
Pick a color that fits the character's role and atmosphere:
• Unnamed Demon Slayer Corps member:  #5A7090 (muted slate-blue)
• Civilians / neutral townspeople:    #8A7060 (warm earthy brown)
• Minor / unnamed demons:             #7A3040 (dark crimson)
• Wisteria House / healers:           #5A7050 (muted sage)
• Authority / elders:                 #7A6A50 (aged gold-brown)
• Children / innocents:               #A08060 (soft warm)
• Merchants / travelers:              #7A6840 (dusty gold)

### NAMING CONVENTION
Include a role descriptor after the name when no real name is known:
  "Villager Elder (Asakusa)"
  "Inn Keeper Masa"
  "Cultist Guard"
  "Lower Demon (Natagumo Forest)"
  "Corps Recruit (Unnamed)"
If given a real name, use Japanese name order: "Sato Kenji (Merchant)"

### RESPONSE FORMAT
Structure your response exactly like this:

[KNYNPC|Inn Keeper Masa|#8A7060]

The old man wiped the counter without looking up. "We don't get many slayers through here anymore."

### RULE
Use [KNYNPC] ONCE per NPC per response, placed immediately before their first appearance or spoken line. Never repeat the tag for the same character later in the same response.\
"""

lorebook = {
    "name": "KNY NPC Header",
    "entries": {
        "0": entry(0, "KNY NPC Header — Format Instructions", E0, 91)
    }
}

# ── Write ─────────────────────────────────────────────────────────────────────

for obj, fname, indent in [
    (regex_data, "regex_kny_npc_header.json",    4),
    (lorebook,   "kny_npc_header_lorebook.json", 2),
]:
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
    size = len(json.dumps(obj, ensure_ascii=False, indent=indent).encode("utf-8"))
    print(f"{fname} — {size:,} bytes ({size/1024:.1f} KB)")

print("Done!")
