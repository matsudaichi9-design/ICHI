import json, re

with open('lom_quest.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lom-quest-dispatch",
    "scriptName": "Lord of the Mysteries — Quest Dispatch",
    "findRegex": "/<LOM_QUEST>([\\s\\S]*?)<\\/LOM_QUEST>/gm",
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

out = 'regex_lom_quest.json'
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
## LORD OF THE MYSTERIES — QUEST SYSTEM

Quests can come from an NPC handing the character a task in a scene, from the story's own progression flagging an objective, or any other natural source. Post this tag whenever a quest is given, its objectives change, or it resolves:

<LOM_QUEST>
{JSON}
</LOM_QUEST>

This tag is reused across a quest's whole lifecycle — post it again with updated fields whenever something about the SAME quest changes, using the same `questName` so the player can follow it as one continuous thread.

---

### JSON SCHEMA

```json
{
  "charColor": "#C0A050",
  "questName": "The Silent Toll",
  "status": "new",
  "questGiver": "Inspector Rudolph",
  "description": "Something in Backlund's old bell tower has stopped the church clock at the same hour, every night, for a week.",
  "objectives": [
    {"text": "Investigate the bell tower at midnight", "done": false},
    {"text": "Speak to the tower keeper", "done": false}
  ],
  "rewards": ["50 Pounds", "Access to the Church archive"]
}
```

### FIELD REFERENCE
| Field | Notes |
|---|---|
| `status` | one of exactly: `new` (just accepted), `updated` (an objective's state changed, or new objectives were added, while the quest is still ongoing), `completed` (fully resolved successfully), `failed` (resolved unsuccessfully or became impossible). Use these values exactly — they drive the card's color and icon. |
| `questGiver` | optional — the NPC's name if one exists; omit for a quest that arose purely from circumstance/story progression rather than a specific person handing it out |
| `objectives` | array of `{"text": "...", "done": true/false}` — always resend the FULL current list (not just what changed) so the card always shows the complete picture. Mark an objective `done:true` the moment it's genuinely achieved in the story. |
| `rewards` | optional array of short reward tags — what completing the quest is expected to grant. Can be included from the `new` state onward (as a promise) and should still be shown on `completed` |
| `charColor` | optional — defaults to a neutral gold if omitted; consider tying it to the quest-giver's own signature color if they have one |

### OUTPUT RULES
• On `updated`, resend every objective (not a diff) with their current `done` states — the card has no memory of the previous post.
• Move to `completed` or `failed` only when the story has actually resolved the quest — don't mark it complete preemptively.
• Keep using the exact same `questName` across a quest's `new` → `updated` → `completed`/`failed` posts; a different name will read as a different quest.
• Not every minor errand needs this treatment — reserve it for tasks worth tracking, matching the same judgment call used for the other Astral Ledger notifications.\
"""

path = 'lom_quest_lorebook.json'
lorebook = {"name": "Lord of the Mysteries — The Astral Ledger (Quest Dispatch)", "entries": {}}
lorebook["entries"]["0"] = entry(0, "LOM Quest System", E0, 99)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), {len(lorebook['entries'])} entries (standalone file)")
print("Done!")
