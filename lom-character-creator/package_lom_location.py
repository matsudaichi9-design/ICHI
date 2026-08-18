import json, re

with open('lom_location.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lom-location-discovered",
    "scriptName": "Lord of the Mysteries — The Map Unfolds (Location)",
    "findRegex": "/<LOM_LOCATION>([\\s\\S]*?)<\\/LOM_LOCATION>/gm",
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

out = 'regex_lom_location.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Standalone lorebook file for this feature (per the user's standing instruction to keep
#    each new LOM notification's lorebook entry in its own separate file) ──
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
## LORD OF THE MYSTERIES — NEW LOCATION DISCOVERED NOTIFICATION

Whenever {{user}}'s character(s) arrive at or discover a new, named location worth tracking — a district, building, ruin, camp, landmark, or other notable place, not just any room or street corner — post this tag:

<LOM_LOCATION>
{JSON}
</LOM_LOCATION>

---

### THIS TAG WORKS DIFFERENTLY FROM THE OTHER NOTIFICATIONS — READ CAREFULLY

Every other Astral Ledger notification (advancement, item, monster) fires **once**, at the moment it happens. This one is **persistent for as long as the scene stays in that location**:

1. **Placement — always last.** This tag must always be the very last thing in your reply, after all narrative text, with nothing following it.
2. **Repeat it every message.** For as long as the characters remain in this same location, re-post the exact same `<LOM_LOCATION>` tag (same JSON, unless updated per rule 3) at the bottom of every single reply — not just the first time they arrive. This keeps the location's mini-map visibly "pinned" on screen the whole time the scene is there.
3. **Update in place, don't re-discover.** If the party explores further and turns up a new marked zone within the *same* location (a hidden room, a new stall, a new danger), just add it to the `zones` array and keep re-posting the updated JSON — don't treat it as a brand new location.
4. **Stop only on departure.** The moment the characters actually leave this location for somewhere else, stop posting this tag. If they arrive somewhere new and notable, start a fresh `<LOM_LOCATION>` block for that new place instead.
5. Don't post this for every trivial room or transient stop — reserve it for places worth the party actually remembering (a district, a dungeon, a camp, a notable building), the same judgment call you'd use for a real bestiary or item entry.

---

### JSON SCHEMA

```json
{
  "locationName": "Backlund Fogbound Market",
  "locationType": "District — Trade Hub",
  "description": "A sprawling night market that only opens under fog, its stalls lit by pale gas lamps and stranger things. Vendors here trade in more than coin.",
  "mapImage": "abc123.jpg",
  "resourceType": "Trade Hub",
  "resources": ["Rare potion reagents", "Forbidden pamphlets", "Sealed letters"],
  "monstersPresent": true,
  "monsterNote": "Pickpocket wraiths are known to slip between the stalls after midnight.",
  "monsterTypes": ["Fog Wraith"],
  "zones": [
    {"x": 15, "y": 78, "type": "entrance", "label": "Fog Gate"},
    {"x": 40, "y": 35, "type": "resource", "label": "Reagent Row"},
    {"x": 62, "y": 60, "type": "market",   "label": "Coin Alley"},
    {"x": 82, "y": 25, "type": "danger",   "label": "The Hollow Stalls"},
    {"x": 50, "y": 15, "type": "landmark", "label": "The Fogless Fountain"}
  ]
}
```

### FIELD REFERENCE
| Field | Notes |
|---|---|
| `locationType` | optional short tag — district/ruins/sanctuary/dungeon/etc, or omit |
| `mapImage` | optional catbox filename for an actual map image as the map background; omit for the default stylized star-chart backdrop, which is the normal state for most locations |
| `resourceType` | free text — this world doesn't use a fixed category, describe it naturally: "Farming Ground", "Trade Hub", "Both", or omit if the place has nothing notable to gather or trade |
| `resources` | UNLIMITED short tags — concrete things obtainable here (materials, rare goods, ingredients); omit/leave empty if nothing notable |
| `monstersPresent` | boolean — whether hostile creatures are known to linger in or near this location |
| `monsterNote` | optional flavor line about the threat, shown only if `monstersPresent` is true |
| `monsterTypes` | optional tags naming the creature type(s), ideally matching names used in a `<LOM_MONSTER>` bestiary entry if one exists for them |
| `zones` | array of marked points on the mini-map. `x`/`y` are percentages (0-100) of position within the map (keep roughly 8-92 to avoid crowding the edges). `type` is one of: `entrance`, `resource`, `market`, `danger`, `landmark`, `other` — each renders with its own icon and color. `label` is the short name shown under the pin. Leave the array empty if no specific zones are worth marking yet. |

### OUTPUT RULES
• Rate/describe honestly — don't invent resources, monsters, or zones that haven't actually been established or discovered in the story.
• If a zone's nature turns out to be different than first assumed (e.g. a suspected `danger` zone turns out empty), it's fine to adjust its `type` or remove it in a later update while still in the same location.
• This notification is about **place**, not people or things — a notable NPC or item found here still gets its own separate notification if warranted.\
"""

path = 'lom_location_lorebook.json'
lorebook = {"name": "Lord of the Mysteries — The Astral Ledger (Cartography)", "entries": {}}
lorebook["entries"]["0"] = entry(0, "LOM Location Discovered — The Map Unfolds", E0, 93)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), {len(lorebook['entries'])} entries (standalone file)")
print("Done!")
