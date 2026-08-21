import json, re

with open('lom_advancement.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lom-sequence-advancement",
    "scriptName": "Lord of the Mysteries — The Stars Realign (Advancement)",
    "findRegex": "/<LOM_ADVANCE>([\\s\\S]*?)<\\/LOM_ADVANCE>/gm",
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

out = 'regex_lom_advancement.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Add an entry to the shared LOM lorebook (alongside the Creation/Dossier flow entry) ──
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

E1 = """\
## LORD OF THE MYSTERIES — SEQUENCE ADVANCEMENT NOTIFICATION

Whenever a player character's Sequence actually advances in the story — they finish digesting a potion via the Acting Method and their Sequence number goes down — announce it with this tag, on its own line, once, right at the moment the advancement completes:

<LOM_ADVANCE>
{JSON}
</LOM_ADVANCE>

This is a one-time celebratory notification, not a persistent tracker — post it once per actual advancement, not on every message. Do not post it for a Sequence someone already holds, and do not post it preemptively before digestion is actually complete.

---

### JSON SCHEMA

```json
{
  "charColor": "#8B5FBF",
  "name": "Percy Alstreim",
  "pathway": "Moon",
  "oldSequence": 9,
  "newSequence": 8,
  "newSequenceTitle": "Alchemist",
  "newCharacteristic": "Can identify any potion's ingredients by scent alone.",
  "flavorLine": "The Acting Method is not a performance. It is who you are now."
}
```

### FIELD REFERENCE
| Field | Notes |
|---|---|
| `pathway` | must match the character's actual Pathway exactly (see the Pathway List in the Sealed Registry system entry) |
| `oldSequence` / `newSequence` | the Sequence they held before and now hold — remember Sequence counts DOWN as power increases (9 is weakest, 0 is True God) |
| `newSequenceTitle` | the correct in-canon title for that Pathway at `newSequence` — pull this from that Pathway's own lorebook entry (each Pathway entry documents its full Seq.9→Seq.0 title progression), never invent one |
| `newCharacteristic` | optional — only include if this specific advancement actually manifested a new Beyonder Characteristic; omit otherwise, most advancements don't grant one |
| `flavorLine` | optional — a single short, grounded line about what the moment felt like or cost. Keep it earned, not generic; it's fine to omit this field entirely for a quieter advancement |

### OUTPUT RULES
• Only fire this for genuine Sequence advancement — never for joining an organization, gaining an item, or other non-Sequence progress (those don't belong in this notification).
• If the character's Sequence ever regresses (a rare, story-significant event), do not use this tag — narrate it in prose instead; this notification is specifically for the moment of ascension.
• After posting, also update the character's living record — the next <LOM_CONFIRM> block you post (if the story calls for one) should reflect the new `sequence` and `sequenceTitle`.\
"""

path = 'lom_creation_lorebook.json'
try:
    with open(path, 'r', encoding='utf-8') as f:
        lorebook = json.load(f)
except FileNotFoundError:
    lorebook = {"name": "Lord of the Mysteries — Sealed Registry", "entries": {}}

lorebook["entries"]["1"] = entry(1, "LOM Sequence Advancement — The Stars Realign", E1, 90)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), now {len(lorebook['entries'])} entries")
print("Done!")
