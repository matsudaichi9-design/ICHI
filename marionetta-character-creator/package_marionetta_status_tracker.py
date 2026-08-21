import json, re

with open('marionetta_status_tracker.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "marionetta-status-tracker",
    "scriptName": "Marionetta User Status Tracker",
    "findRegex": "/<MARIONETTA_STATUS>([\\s\\S]*?)<\\/MARIONETTA_STATUS>/gm",
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

out = 'regex_marionetta_status_tracker.json'
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
## MARIONETTA USER STATUS TRACKER SYSTEM

You are running the Marionetta status tracker for {{user}}. After EVERY response you write, append a status block on its own line with no extra text around it:

<MARIONETTA_STATUS>
{JSON}
</MARIONETTA_STATUS>

The JSON must be a complete, valid object. Never omit the block, even in short replies. This tracker is inventory-heavy — track every item {{user}} is carrying in detail, not just a summary.

---

### STATUS JSON SCHEMA

```json
{
  "hp": {"cur": 72, "max": 100},
  "stamina": {"cur": 45, "max": 100},
  "conditions": ["Bruised ribs", "Cold", "Slightly damp"],
  "purse": {"amount": 340, "currency": "coin"},
  "details": [
    "Hem of the coat is torn from last night's escape.",
    "Smells faintly of greasepaint and rain.",
    "A fresh ink stain marks the left hand."
  ],
  "onPerson": [
    {"name": "Illusionist's Coat", "condition": "worn", "desc": "Deep pockets sewn with hidden compartments."}
  ],
  "trunk": [
    {"category": "Tools of the Trade", "name": "Marked Cards", "qty": 1, "desc": "Weighted just enough to cheat an honest game."},
    {"category": "Provisions", "name": "Wisteria-laced tea", "qty": 3, "desc": "A gift from a sympathetic apothecary."},
    {"category": "Keepsakes", "name": "Mother's locket", "qty": 1, "desc": "Empty. The photo inside was lost years ago."},
    {"category": "Documents", "name": "Forged travel papers", "qty": 1, "desc": "Good enough to pass a cursory checkpoint glance."}
  ]
}
```

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `hp` / `stamina` | plain `{cur, max}` vitals |
| `conditions` | current ailments/afflictions — [] when fine |
| `purse` | current coin on hand; `currency` is free text (default "coin") |
| `details` | UNLIMITED array of small present-state facts — appearance quirks, stains, smells, minor injuries not worth a full "condition", anything that makes the moment feel lived-in. Rewrite this list often; drop stale details and add new ones as the scene changes |
| `onPerson` | items actively worn or equipped — clothing, a weapon in hand, a prop mid-use. `condition`: "pristine" \| "worn" \| "damaged" \| "broken" |
| `trunk` | UNLIMITED array — everything packed away and not currently worn/held. No cap on item count — track everything {{user}} plausibly owns and carries |
| `trunk[].category` | groups the Trunk section — use whatever categories fit the story (e.g. "Tools of the Trade", "Provisions", "Keepsakes", "Documents", "Miscellany"); consistent naming keeps items grouped together |
| `trunk[].qty` | defaults to 1 if omitted |

---

### OUTPUT RULES
• Copy the full JSON from the previous block and modify only what changed.
• Never drop an item from `trunk` or `onPerson` unless it was actually used up, given away, lost, or stolen in the story.
• When {{user}} acquires something new — however small — add it to `trunk` (or `onPerson` if worn/wielded immediately). Do not wait to be asked.
• `details` should feel like marginalia, not a status readout — short, specific, sensory. 2-4 entries is typical; refresh them as time passes.
• Move an item between `onPerson` and `trunk` when {{user}} puts it on/away or draws/holsters it.\
"""

lorebook = {
    "name": "Marionetta User Status Tracker",
    "entries": {
        "0": entry(0, "Marionetta User Status Tracker System", E0, 89),
    }
}

out_lb = "marionetta_status_tracker_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
