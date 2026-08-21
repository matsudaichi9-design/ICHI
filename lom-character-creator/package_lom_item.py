import json, re

with open('lom_item.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lom-item-acquired",
    "scriptName": "Lord of the Mysteries — Treasure Unsealed (Item)",
    "findRegex": "/<LOM_ITEM>([\\s\\S]*?)<\\/LOM_ITEM>/gm",
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

out = 'regex_lom_item.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Add a third entry to the shared LOM lorebook ──
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

E2 = """\
## LORD OF THE MYSTERIES — ITEM ACQUIRED NOTIFICATION

Whenever {{user}}'s character genuinely acquires a named magical item — finds, is given, buys, or steals a Sealed Artifact / wondrous treasure worth tracking — announce it with this tag, on its own line, once, right when the item actually changes hands:

<LOM_ITEM>
{JSON}
</LOM_ITEM>

This is a one-time notification for a specific, named item — not for mundane possessions (money, ordinary clothes, a normal umbrella) and not for every object mentioned in passing.

---

### JSON SCHEMA

```json
{
  "charColor": "#8B5FBF",
  "itemName": "The Ashen Compass",
  "itemCategory": "สมบัติปิดผนึก",
  "sequence": 6,
  "image": "abc123.jpg",
  "description": "A brass compass whose needle doesn't point north — it points toward whatever the holder fears most.",
  "properties": ["Reveals hidden fears", "Cannot be sold", "Whispers at midnight"],
  "origin": "Pulled from the coat pocket of a drowned man found on the Cherwood docks."
}
```

### FIELD REFERENCE
| Field | Notes |
|---|---|
| `itemCategory` | this world uses two interchangeable in-story names for magical items — "สมบัติวิเศษ" (wondrous treasure) and "สมบัติปิดผนึก" (sealed treasure/artifact) — use whichever fits the moment, in Thai or English ("Sealed Artifact" / "Wondrous Treasure"), or omit entirely for a plainer item |
| `sequence` | the item's own power rating, on the same 9 (weakest) to 0 (strongest/mythic) scale as a Beyonder's Sequence — rate it by what it can actually do, not by how dramatic the moment felt |
| `image` | optional catbox filename; omit for a tasteful gem-icon placeholder, which is the normal state for most items |
| `properties` | UNLIMITED short tags — concrete effects or notable quirks, not vague flavor |
| `origin` | optional one-line note on how it was actually obtained |

### OUTPUT RULES
• Only fire this for a genuinely significant, named item — not for every coin, tool, or piece of clothing the character picks up.
• Rate `sequence` honestly and consistently — a Sequence 0 item should be exceptionally rare and story-significant, not handed out casually.
• If this item is later lost, destroyed, or given away, do not re-fire this tag — narrate that in prose instead; this notification is specifically for the moment of acquisition.\
"""

path = 'lom_creation_lorebook.json'
try:
    with open(path, 'r', encoding='utf-8') as f:
        lorebook = json.load(f)
except FileNotFoundError:
    lorebook = {"name": "Lord of the Mysteries — Sealed Registry", "entries": {}}

lorebook["entries"]["2"] = entry(2, "LOM Item Acquired — Treasure Unsealed", E2, 91)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), now {len(lorebook['entries'])} entries")
print("Done!")
