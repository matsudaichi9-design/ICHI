import json, re

with open('lom_status.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lom-status-living-record",
    "scriptName": "Lord of the Mysteries — The Living Record (Status)",
    "findRegex": "/<LOM_STATUS>([\\s\\S]*?)<\\/LOM_STATUS>/gm",
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

out = 'regex_lom_status.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Standalone lorebook file for this feature ──
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

def entry(uid, comment, content, order, key=None, constant=True):
    e = {"uid": uid, "key": key or [], "keysecondary": [],
         "comment": comment, "content": content,
         "constant": constant, "order": order, "displayIndex": uid}
    e.update(BOILERPLATE)
    return e

E0 = """\
## LORD OF THE MYSTERIES — STATUS PANEL (THE LIVING RECORD)

A persistent, always-present status HUD for {{user}}'s character, collapsed to a slim bar by default so it doesn't dominate the reply, expandable by the player into a full tabbed sheet.

### PLACEMENT — READ CAREFULLY, THIS TAG WORKS LIKE <LOM_LOCATION>
1. **Always last.** This tag must always be the very last thing in every one of your replies, after all narrative text and after any other Astral Ledger tag in that same reply.
2. **Every single reply, no exceptions.** Post the FULL current `<LOM_STATUS>` block at the end of every reply for the rest of the story — even if nothing changed since the last message. This is what makes it a persistent status bar rather than an occasional notification.
3. **Always resend the complete state**, not a diff — the card has no memory between messages. Carry forward every field from the previous post and only change what actually changed in the story.

<LOM_STATUS>
{JSON}
</LOM_STATUS>

---

### JSON SCHEMA

```json
{
  "charColor": "#8B5FBF",
  "character": {
    "name": "Percy Alstreim",
    "level": "Sequence 7 — Fool Pathway",
    "appearance": "Tall, sharp-featured, dark hair kept short and neat.",
    "outfit": "A grey wool coat, dockworker's boots, a silver pocket watch on a chain.",
    "condition": "Lightly wounded — favoring the left arm.",
    "funds": "120 Pounds",
    "extra": [{"label": "Faction", "value": "Tingen Night Watch"}]
  },
  "abilities": [
    {"name": "Spirit Vision", "description": "Can perceive residual emotion left on objects and in rooms."}
  ],
  "locations": [
    {"name": "Backlund Fogbound Market", "summary": "A night market that opens only in fog.",
     "details": "Vendors here trade in more than coin — rare reagents, forbidden pamphlets. Pickpocket wraiths slip between the stalls after midnight."}
  ],
  "inventory": [
    {"name": "The Ashen Compass", "category": "Sealed Artifact", "tier": "Sequence 6",
     "description": "A brass compass whose needle points toward whatever the holder fears most."}
  ],
  "bestiary": [
    {"name": "The Weeping Tailor", "dangerLevel": 5.5, "summary": "Stitches living shadows into cloth that binds the wearer."}
  ],
  "extraTab": {
    "title": "Reputation",
    "items": [{"label": "Tingen Night Watch", "value": "Trusted"}]
  }
}
```

### TAB REFERENCE
| Tab | Fields | Notes |
|---|---|---|
| **Character** | `name`, `level`, `appearance`, `outfit`, `condition`, `funds`, `extra[]` | `level` should reflect their actual Sequence + Pathway (see the Sealed Registry system). `extra` is an open-ended array of `{label, value}` pairs for anything else worth tracking (a title, a faction rank, an affliction) — add or remove entries as the story calls for it. Any field left out entirely is simply not shown. |
| **Abilities** | array of `{name, description}` | Every genuine ability/characteristic/technique the character currently has, in plain list form. Add a new entry the moment they gain one (e.g. after a `<LOM_SKILL>` first establishes it, or a Sequence advancement grants one) — don't wait to be asked. |
| **Locations** | array of `{name, summary, details}` | Every location the character has actually discovered (this should track the same places that earned a `<LOM_LOCATION>` post). `summary` is the always-visible one-liner; `details` is the fuller text revealed when the player expands that entry. |
| **Inventory** | array of `{name, category, tier, description}` | Every item currently in the character's possession (should stay in sync with items granted via `<LOM_ITEM>`/`<LOM_TAROT_REWARD>` and removed when lost/used/sold). `category` and `tier` are both free text — describe the item's kind and its power level however fits (a Sequence number, "Common"/"Rare", etc.) |
| **Bestiary** | array of `{name, dangerLevel, summary}` | Every creature/threat the character has encountered (should track the same entities covered by `<LOM_MONSTER>`). `dangerLevel` (0-10) colors the entry's marker the same way it colors a full `<LOM_MONSTER>` card. |
| **Reputation / extraTab** | `{title, items:[{label,value}]}` | Optional sixth tab, entirely your call — use it for whatever the story actually tracks that doesn't fit the other five (faction standing, notoriety, a relationship meter, active afflictions). Omit `extraTab` entirely if there's nothing that warrants it; the sixth tab then simply doesn't appear. |

### OUTPUT RULES
• Keep this in sync with the story's actual state — an item that's been lost or sold should drop out of `inventory`; a Sequence advancement should update `character.level` and add any new ability to the `abilities` list.
• This is a summary index, not the place for extended prose — keep `summary`/`description` fields short, and use `details` (locations) or the item's own `<LOM_ITEM>` notification for anything longer.
• Don't skip a reply's `<LOM_STATUS>` post because "nothing changed" — resend it unchanged. The player relies on it always being at the bottom of the page.\
"""

path = 'lom_status_lorebook.json'
lorebook = {"name": "Lord of the Mysteries — The Astral Ledger (Living Record / Status)", "entries": {}}
lorebook["entries"]["0"] = entry(0, "LOM Status Panel — The Living Record", E0, 101)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), {len(lorebook['entries'])} entries (standalone file)")
print("Done!")
