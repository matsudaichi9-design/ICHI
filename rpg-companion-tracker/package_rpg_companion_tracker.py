import json, re

with open('rpg_companion_tracker.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "rpg-companion-tracker",
    "scriptName": "RPG Companion Tracker",
    "findRegex": "/<RPG_STATUS>([\\s\\S]*?)<\\/RPG_STATUS>/gm",
    "replaceString": "```\n" + html + "\n```",
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

out = 'regex_rpg_companion_tracker.json'
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
## RPG COMPANION TRACKER SYSTEM

You are running a full RPG companion tracker for {{user}}. After EVERY response you write, append a status block on its own line with no extra text around it:

<RPG_STATUS>
{JSON}
</RPG_STATUS>

The JSON must be a complete, valid object. Never omit the block, even in short replies.

---

### STATUS JSON SCHEMA

```json
{
  "charColor": "#C9922A",
  "name": "The Chosen One",
  "avatar": "abc123.jpg",
  "class": "Wizard",
  "race": "Human",
  "raceDetail": "Raceless",
  "level": 1,
  "location": "Gate of Descent",
  "xp": {"cur": 0, "max": 100, "zone": "Traveling"},

  "overview": {
    "nickname": "Not yet chosen",
    "language": "None known",
    "origin": "Chosen",
    "mpRegen": "5/hr",
    "affiliation": "Chosen",
    "firstRace": "Outsider",
    "status": "Unknown",
    "mission": {"name": "Uncover the Gate's Secret", "progress": 15, "risk": "Low", "followers": "—"}
  },

  "stats": {"str": 10, "dex": 10, "con": 10, "int": 10, "wis": 10, "cha": 10, "per": 10, "for": 10, "com": 10, "will": 10, "points": 0},
  "equipment": {"weapon": "None", "accessory": "None", "oath": "No bond has been sworn yet."},

  "world": {
    "location": "Gate of Descent",
    "area": "great_hall",
    "day": 1,
    "time": "08:00",
    "season": "Autumn",
    "weather": "Cool",
    "year": "732 A.S.",
    "note": "A faint hum radiates from the stones underfoot."
  },

  "elements": [
    {"name": "Fire", "icon": "🔥", "color": "#e0733a", "value": 0, "max": 100},
    {"name": "Water", "icon": "💧", "color": "#4a90d9", "value": 0, "max": 100}
  ],
  "elementsNote": "Season of Ash",

  "npcs": [
    {"name": "Seed", "avatar": "def456.jpg", "relation": "Guide", "closeness": 70, "note": "A mysterious voice that renders the world into being."}
  ],

  "inventory": {
    "items": [
      {"name": "Traveler's Cloak", "icon": "🧥", "qty": 1}
    ],
    "resources": [
      {"name": "Gold", "icon": "🪙", "amount": 0},
      {"name": "Gem", "icon": "💎", "amount": 0}
    ],
    "note": "Nothing noteworthy yet."
  },

  "records": [
    {"title": "A New Beginning", "tag": "Economy", "desc": "You walked through the city gate and encountered a mysterious old man passing by.", "time": "Day 1"},
    {"title": "Red Dragon", "tag": "NPC", "desc": "An adventurer mentioned seeing a red dragon fly across the sky last night.", "time": "5h ago"},
    {"title": "Scent Beneath", "tag": "Mystery", "desc": "A faint Void scent lingers hidden beneath the ground in this area.", "time": "5h ago"}
  ],

  "map": {
    "nodes": [
      {"id": "gate", "name": "Gate of Descent", "x": 50, "y": 30, "current": true, "discovered": true},
      {"id": "insula", "name": "Insula Castle", "x": 50, "y": 50, "discovered": true, "note": "A castle to the north."},
      {"id": "n1", "x": 20, "y": 60, "discovered": false}
    ],
    "edges": [["gate", "insula", "0 km"], ["insula", "n1"]]
  }
}
```

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `charColor` | accent color set at creation; keep it stable |
| `overview.mission` | the character's current driving objective — omit or set `name` empty when there is none active |
| `stats` | the 10-attribute sheet (STR/DEX/CON/INT/WIS/CHA/PER/FOR/COM/WILL); `points` is unspent attribute points |
| `equipment` | currently equipped weapon/accessory plus `oath` — a sworn bond or vow text, if any |
| `world` | current scene's place and time — update whenever the party moves or time passes |
| `elements` | UNLIMITED list of elemental/attribute affinities, each with its own `icon` (emoji), `color` (hex) and `value`/`max`. `elementsNote` is a free-text line shown at the bottom of that tab (e.g. current season) |
| `npcs` | UNLIMITED — every named character {{user}} has met; `closeness` 0-100 drives the bar and the relation-tag color |
| `inventory.items` | UNLIMITED — carried items, each with `icon` (emoji) and `qty`. Rendered as a slot grid (minimum 8 slots shown) |
| `inventory.resources` | UNLIMITED — currencies/materials (gold, gems, tokens, etc.), each with `icon` and `amount` |
| `records` | UNLIMITED — the "Aetheric Records" journal, rendered as its own collapsible section below the tracker. Each entry is a discrete piece of lore, rumor, or event the player has learned. `tag` is a short category label (Economy, NPC, Mystery, War, Lore, Quest, or invent your own) — it powers the in-UI search/filter. `time` is an optional free-text timestamp (e.g. "Day 1", "5h ago") |
| `map.nodes` | UNLIMITED list of locations. `x`/`y` are percentage coordinates (0-100) on the map canvas — lay them out to roughly match their relative geography. `current: true` on exactly one node marks {{user}}'s present location. `discovered: false` renders the node as "???" (not yet explored/named). `note` is an optional one-line description shown in the location list under the map |
| `map.edges` | `[fromId, toId]` pairs of connected node `id`s; add an optional third string for a distance label (e.g. `["gate","insula","12 km"]`), shown only between two discovered nodes |

---

### OUTPUT RULES
• Copy the full JSON from the previous block and modify only what changed.
• Never drop an NPC, record, item, or map node unless the story explicitly removes it (e.g. an NPC dies and should be memorialized, not deleted — consider updating their `relation` instead).
• Add a new `records` entry whenever {{user}} learns something noteworthy — a rumor, a piece of history, a discovered secret — not for routine dialogue.
• Add a new `map.nodes` entry (with `discovered: false` and approximate `x`/`y`) as soon as a new location is mentioned, even before {{user}} has been there — flip `discovered: true` once they actually arrive or learn its name. Move `current` to the new node when {{user}} travels there.
• `overview.mission.progress` should move deliberately in response to story beats, not tick up automatically each turn.
• `stats` should stay fixed unless the story explicitly grants a level-up or attribute training moment.\
"""

lorebook = {
    "name": "RPG Companion Tracker",
    "entries": {
        "0": entry(0, "RPG Companion Tracker System", E0, 89),
    }
}

out_lb = "rpg_companion_tracker_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
