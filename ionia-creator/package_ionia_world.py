import json, re

with open('ionia_world.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "ionia-world-tracker",
    "scriptName": "Ionia — World Tracker (Field Dispatch)",
    "findRegex": "/<IONIA_WORLD>([\\s\\S]*?)<\\/IONIA_WORLD>/gm",
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

out = 'regex_ionia_world.json'
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
## IONIA — WORLD TRACKER (FIELD DISPATCH)

A persistent, collapsible report card tracking {{user}}'s current standing in Ionia. After EVERY response you write, append a status block on its own line with no extra text around it:

<IONIA_WORLD>
{JSON}
</IONIA_WORLD>

The JSON must be a complete, valid object. Never omit the block, even in short replies. Copy the full JSON from your previous block and change only what actually moved.

---

### JSON SCHEMA

```json
{
  "accentColor": "#B8732E",
  "location": "The Free City of Perryn",
  "territory": "Talos",
  "dangerLevel": 6,
  "weather": "Fog",
  "date": "Lucis Reign Year 12, 3rd Moon, 9th Day",
  "calendarSystem": "Britannian Court Reckoning",
  "note": "The city gates close early this week — rumors of Royal Order inspectors in the merchant quarter.",
  "royalCoin": "340",
  "hollowChits": "12",
  "factions": [
    { "name": "Britannia Crown", "standing": "Wary", "level": 2, "note": "Noted for asking too many questions near the Ashfall Quarter." },
    { "name": "The Hollow Market", "standing": "Friendly", "level": 4, "note": "Kestrel Vane still owes a favor." }
  ],
  "journey": [
    { "name": "Elarien", "territory": "Virelle", "summary": "Virelle's last standing city.", "details": "A fog-wrapped river city watched by the Thornveil Wardens." }
  ]
}
```

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `location` / `territory` | `territory` is one of `Talos`, `Ashkar`, `Virelle`, or a named sub-place (a city, the Southern District, Infinity Castle, the Spirit Realm, the Underworld, etc.) — whichever is actually true to the scene |
| `dangerLevel` | 0–10, how dangerous the current location is right now — drives a white→gold→crimson gauge. This is situational (a safe city under curfew can spike; a wild border region can calm), not a fixed property of the place |
| `date` / `calendarSystem` | Ionia has **no unified calendar** — write `date` in whatever reckoning fits where {{user}} currently is (Britannian reign-years, Corvane voyage-seasons, Ashkar oath-cycles/generations, Virelle bloom/spirit-tide markers), and name that system in `calendarSystem`. Don't invent a universal date |
| `royalCoin` | standard currency recognized across Britannia/Talos |
| `hollowChits` | the Hollow Market's own currency (Southern District) — distinct from royal coin on purpose; omit or leave at "0" if {{user}} has no dealings there |
| `factions[].standing` | suggested ladder: `Hostile` → `Unfriendly` → `Neutral` → `Friendly` → `Allied`. Using one of these exact words auto-fills the 5-pip meter; a custom/unknown standing (e.g. "Unknown") just shows as text with no pips |
| `factions[].level` | optional 1–5 override if `standing` is custom text |
| `factions` | track whichever factions are actually relevant to the current story — suggested list: Britannia Crown, The Council of the Gilded Chair / Royal Order, Ashkar Clans, Virelle Wardens, The Hollow Market / Nine Fingers, Kakujo — don't force all of them if most haven't come up yet |
| `journey` | array of `{name, territory, summary, details}` — add an entry the first time {{user}} actually arrives somewhere new, not when it's merely mentioned |

---

### OUTPUT RULES
- `dangerLevel`, faction `standing`, and wealth totals should only change when something in the actual scene justifies it (a fight, a bribe, a broken promise, a bounty paid) — never drift them for pacing alone.
- Add a `journey` entry the moment {{user}} actually sets foot somewhere new worth remembering.
- Keep `date` moving forward consistent with the story's own pacing, in whatever calendar system fits the current location — don't silently switch systems without a reason (e.g. crossing from Talos into Ashkar).
- If {{user}} hasn't interacted with a faction yet, leave it out of `factions` rather than inventing a default standing.\
"""

lorebook = {
    "name": "Ionia — World Tracker",
    "entries": {
        "0": entry(0, "Ionia World Tracker System", E0, 88),
    }
}

out_lb = "ionia_world_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
