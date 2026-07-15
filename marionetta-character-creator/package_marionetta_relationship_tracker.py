import json, re

with open('marionetta_relationship_tracker.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "marionetta-relationship-tracker",
    "scriptName": "Marionetta Relationship Tracker",
    "findRegex": "/<MARIONETTA_RELATIONSHIPS>([\\s\\S]*?)<\\/MARIONETTA_RELATIONSHIPS>/gm",
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

out = 'regex_marionetta_relationship_tracker.json'
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
## MARIONETTA RELATIONSHIP TRACKER SYSTEM

You are running the Marionetta relationship tracker. After EVERY response you write, append a relationships block on its own line with no extra text around it:

<MARIONETTA_RELATIONSHIPS>
{JSON}
</MARIONETTA_RELATIONSHIPS>

The JSON must be a complete, valid object. Never omit the block, even in short replies. Include every named character the player has a relationship with so far — not just the ones present in the current scene.

---

### RELATIONSHIP JSON SCHEMA

```json
{
  "relationships": [
    {
      "name": "Sahed",
      "img": "abc123.jpg",
      "status": "Confidant",
      "closeness": 82,
      "warmth": "warm",
      "note": "He's the only one who understands what she carries. She trusts him with things she's told no one else.",
      "moments": [
        "First met backstage, hiding from a Kalgratti patrol",
        "He never asked about her third eye"
      ]
    }
  ]
}
```

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `name` | required |
| `img` | catbox.moe filename for a small portrait; omit entirely if none — a monogram initial is shown automatically |
| `status` | a short role/label for the bond: Confidant, Friend, Rival, Ally, Hunter, Romantic Interest, Stranger, Family, Enemy, etc. — free text |
| `closeness` | 0-100. Drives both the tier label and how taut the "string" between them is drawn (100 = taut/unbreakable, 0 = slack/severed) |
| `warmth` | `"warm"` \| `"neutral"` \| `"hostile"` — sets the string's color; `"hostile"` also renders the string frayed/dashed |
| `note` | one to two sentences describing the current state of the bond, present tense |
| `moments` | optional array of short past-tense highlights — key turning points in the relationship. 0-3 is typical |

### CLOSENESS TIERS (for reference — computed automatically from `closeness`)
| Range | Tier |
|---|---|
| 0-19 | Severed |
| 20-39 | Frayed |
| 40-59 | Loose Thread |
| 60-79 | Bound |
| 80-100 | Unbreakable |

---

### OUTPUT RULES
• Copy the full array from the previous block and modify only what changed; add new entries as new named characters form a bond with the player.
• `closeness` should move gradually — a few points per meaningful scene, not huge jumps, unless something dramatic just happened (a betrayal, a rescue, a confession).
• `warmth` can flip (e.g. warm to hostile) when a relationship is fundamentally broken — a betrayal, a death, a revealed lie — not from ordinary friction.
• Add to `moments` only for scenes that would matter to the character looking back — not every conversation.
• Do not invent relationships the player hasn't actually had a scene with yet.\
"""

lorebook = {
    "name": "Marionetta Relationship Tracker",
    "entries": {
        "0": entry(0, "Marionetta Relationship Tracker System", E0, 89),
    }
}

out_lb = "marionetta_relationship_tracker_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
