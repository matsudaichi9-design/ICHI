import json, re

with open('lom_tarot_reward.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lom-tarot-reward",
    "scriptName": "Lord of the Mysteries — The Fifth Card's Boon (Tarot Set Reward)",
    "findRegex": "/<LOM_TAROT_REWARD>([\\s\\S]*?)<\\/LOM_TAROT_REWARD>/gm",
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

out = 'regex_lom_tarot_reward.json'
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
## LORD OF THE MYSTERIES — TAROT SET REWARD (5-card completion item)

This is the dedicated reveal for the special ITEM granted when a character's Tarot card collection reaches 5 (see the Tarot Card System entry). It is a companion to, not a replacement for, `<LOM_TAROT>` — post both, in order, in the same reply that completes the set:

1. First, the normal `<LOM_TAROT>` block for the 5th card itself, with `cardsCollected: 5` and its own `rewardName`/`rewardDescription` fields filled in as a short teaser (per the Tarot Card System entry's existing rules).
2. Immediately after, this tag for the full reveal of the actual item:

<LOM_TAROT_REWARD>
{JSON}
</LOM_TAROT_REWARD>

Only use this tag for the tarot 5-card milestone reward specifically — a regular item pickup still belongs in `<LOM_ITEM>` instead.

---

### JSON SCHEMA

```json
{
  "charColor": "#C0A050",
  "itemName": "The Sealed Hand",
  "image": "abc123.jpg",
  "description": "A cold, folded thing that was not there a moment ago — five card-shapes pressed into a single sealed relic, warm only in fog.",
  "properties": ["Grants one true premonition per year", "Cannot be sold or given away", "Warm to the touch only in fog"],
  "cardNames": ["The Fool", "The Hanged Man", "Death", "The Star", "The World"]
}
```

### FIELD REFERENCE
| Field | Notes |
|---|---|
| `itemName` | should generally match (or clearly follow from) the `rewardName` already given in the completing `<LOM_TAROT>` post |
| `image` | optional catbox filename; omit for the default astral sigil |
| `properties` | UNLIMITED short tags — concrete effects, same spirit as `<LOM_ITEM>`'s properties field |
| `cardNames` | optional but encouraged — the 5 card names that formed this particular hand (in the order drawn), shown as a small remembrance row on the card |

### OUTPUT RULES
• Only fire this alongside a 5th-card `<LOM_TAROT>` completion — never on its own.
• Make the reward proportionate to a genuine milestone (five successful draws) — this should feel notably more significant than an average `<LOM_ITEM>` pickup.
• After this reward is granted, the character's card count resets to 0 for the next set of five (per the Tarot Card System entry).\
"""

path = 'lom_tarot_reward_lorebook.json'
lorebook = {"name": "Lord of the Mysteries — The Astral Ledger (Tarot Set Reward)", "entries": {}}
lorebook["entries"]["0"] = entry(0, "LOM Tarot Set Reward — The Fifth Card's Boon", E0, 100)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), {len(lorebook['entries'])} entries (standalone file)")
print("Done!")
