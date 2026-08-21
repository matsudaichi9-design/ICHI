import json, re

with open('status_tracker.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "universal-status-tracker",
    "scriptName": "Universal Status Tracker",
    "findRegex": "/<USER_STATUS>([\\s\\S]*?)<\\/USER_STATUS>/gm",
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

out = 'regex_status_tracker.json'
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
## UNIVERSAL STATUS TRACKER SYSTEM

You are running a general-purpose status tracker for {{user}}. After EVERY response you write, append a status block on its own line with no extra text around it:

<USER_STATUS>
{JSON}
</USER_STATUS>

The JSON must be a complete, valid object. Never omit the block, even in short replies.

---

### STATUS JSON SCHEMA

```json
{
  "charColor": "#4A90D9",
  "name": "Elyse Rowan",
  "avatar": "abc123.jpg",
  "hp": {"cur": 72, "max": 100},
  "stamina": {"cur": 55, "max": 100},
  "conditions": ["Bruised knee", "Tired"],
  "skills": [
    {"name": "Swordsmanship", "level": 3, "maxLevel": 5}
  ],
  "inventory": [
    {"category": "Weapons", "name": "Steel Dagger", "qty": 1, "desc": "A well-balanced blade, recently sharpened."}
  ],
  "relationships": [
    {
      "name": "Marcus",
      "avatar": "def456.jpg",
      "status": "Ally",
      "closeness": 78,
      "opinion": "Trusts them with his life after the bridge incident.",
      "note": "A steady presence, rarely speaks unless it matters."
    }
  ],
  "wealth": {
    "currency": "Gold Crowns",
    "amount": 1250,
    "assets": [
      {"name": "Family Signet Ring", "value": "Priceless", "note": "The last thing left of home."}
    ]
  },
  "events": [
    {"title": "Meet the merchant at dusk", "date": "Day 4", "status": "upcoming", "desc": "He claims to have information about the missing shipment."}
  ]
}
```

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `charColor` | accent color set at creation; keep it stable across updates |
| `avatar` / `relationships[].avatar` | catbox.moe filenames; omit entirely if none — a monogram initial is shown automatically |
| `skills` | optional; `level`/`maxLevel` render as a dot meter (defaults to a 5-dot scale) |
| `inventory` | UNLIMITED — no cap on item count; `category` groups the Inventory tab (use whatever categories fit: Weapons, Consumables, Documents, Misc, etc.) |
| `relationships[].closeness` | 0-100 |
| `relationships[].opinion` | **how THAT character currently feels about {{user}}** — write it from their perspective, in-character, not a generic label |
| `relationships[].status` | a short role/label: Ally, Rival, Friend, Stranger, Enemy, Romantic Interest, etc. |
| `wealth.assets` | property/valuables beyond loose currency — `value` is free text (a number, "Priceless", an estimate, etc.) |
| `events[].status` | `"upcoming"` \| `"ongoing"` \| `"completed"` \| `"cancelled"` — drives the color of the event's timeline dot |

---

### OUTPUT RULES
• Copy the full JSON from the previous block and modify only what changed.
• Never drop an item, relationship, asset, or event unless it was actually resolved, used up, lost, or explicitly removed in the story.
• Update `relationships[].opinion` whenever a scene meaningfully shifts how that character feels about {{user}} — it should read like their private thought, not a status label.
• Add new items to `inventory` immediately when {{user}} acquires something, however small — do not wait to be asked.
• `events` is player/story-driven: add an entry whenever a specific future or ongoing event is established in the narrative (a meeting, a deadline, a plan), and flip its `status` to `"completed"` or `"cancelled"` once it resolves rather than deleting it, so the log stays a record of what happened.\
"""

lorebook = {
    "name": "Universal Status Tracker",
    "entries": {
        "0": entry(0, "Universal Status Tracker System", E0, 89),
    }
}

out_lb = "status_tracker_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
