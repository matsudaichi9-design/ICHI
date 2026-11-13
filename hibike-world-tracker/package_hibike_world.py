import json, re

with open('hibike_world.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "hibike-world-tracker",
    "scriptName": "HIBIKE! — World Tracker (Daily Call Sheet)",
    "findRegex": "/<HIBIKE_WORLD>([\\s\\S]*?)<\\/HIBIKE_WORLD>/gm",
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

out = 'regex_hibike_world.json'
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
## HIBIKE! — WORLD TRACKER (DAILY CALL SHEET)

A persistent, collapsible report card for {{user}}'s current standing in the HIBIKE! music world. After EVERY response you write, append a status block on its own line with no extra text around it:

<HIBIKE_WORLD>
{JSON}
</HIBIKE_WORLD>

The JSON must be a complete, valid object. Never omit the block, even in short replies. Copy the full JSON from your previous block and change only what actually moved.

---

### JSON SCHEMA

```json
{
  "charColor": "#FF3D7A",
  "date": "2026-11-13",
  "time": "14:30",
  "weather": "Cloudy",
  "season": "Autumn",
  "seasonNote": "Maple leaves are starting to fall along the Shimokita streets; evenings are getting cold.",
  "funds": "¥48,200",
  "reputation": 62,
  "popularityTier": "Rising Indie",
  "popularityLevel": 2,
  "band": { "name": "odd:hours", "role": "Vocals / Rhythm Guitar", "status": "Active" },
  "label": { "name": "AMPLIFY JAPAN", "status": "Developing Artist" },
  "schedule": [
    { "date": "2026-11-15", "title": "Studio Recording Session", "venue": "UNDER//VOLT", "type": "recording" },
    { "date": "2026-11-20", "title": "Live Set", "venue": "ECHO BASE Shibuya", "type": "concert" },
    { "date": "2026-11-25", "title": "Single Release — \\"Static Bloom\\"", "type": "release" }
  ]
}
```

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `charColor` | personal accent color for {{user}}'s artist identity; keep it stable once set |
| `date` | **always** `YYYY-MM-DD`, required every single block — the whole card (collapsed bar, calendar month, "today" highlight) is driven off this one field |
| `time` | free text, e.g. `"14:30"` — 24h format preferred |
| `weather` | one of `Clear`, `Cloudy`, `Overcast`, `Partly Cloudy`, `Rain`, `Light Rain`, `Heavy Rain`, `Drizzle`, `Thunderstorm`, `Storm`, `Typhoon`, `Snow`, `Light Snow`, `Windy`, `Fog`, `Humid` (matched case-insensitively), or any custom text — a custom value is still displayed verbatim, just with a generic icon |
| `season` | one of `Spring`, `Summer`, `Autumn`/`Fall`, `Winter` — this genuinely re-skins the card's accent color (sakura pink / summer teal / autumn amber / winter ice-blue), separate from `charColor` |
| `seasonNote` | optional short flavor line shown under the Today tab — use it for texture ("festival banners are going up downtown"), not mechanics |
| `funds` | free text, already formatted with currency symbol, e.g. `"¥48,200"` |
| `reputation` | 0–100 numeric "buzz score" — drives a color gradient gauge (grey → blue → teal → gold → hot pink as it climbs) |
| `popularityTier` | a named stage of fame — suggested ladder: Unknown/Underground → Rising Indie → Local Buzz → Trending Online → Regional Star → National Star → Icon. Using one of these exact names auto-fills the 7-step meter; a custom tier name is shown as text with no meter unless `popularityLevel` is also given |
| `popularityLevel` | optional 1–7 override for the step meter, useful if `popularityTier` is custom text |
| `band` | omit entirely, or set to `null`, if {{user}} is currently solo/unaffiliated — the card shows "Solo / Unaffiliated" automatically |
| `band.status` | e.g. `Active`, `On Hiatus`, `Touring`, `Recording` |
| `label` | omit entirely, or set to `null`, if {{user}} is unsigned — the card shows "Unsigned / Independent" automatically |
| `label.status` | e.g. `Developing Artist`, `Signed`, `Shopping a Deal`, `Dropped` |
| `schedule` | array of `{date, title, venue, type}` — `venue` is optional. `type` is one of `concert`, `recording`, `release`, `meeting`, `media`, or `other` (controls the icon/color on the calendar dot and list row). The card only displays entries that fall within `date`'s current month — past months' entries can be safely dropped once the month has turned over |

---

### OUTPUT RULES
- `date` must move forward in a way consistent with the story's actual pacing — never jump the calendar arbitrarily just to reveal a new month.
- Add a `schedule` entry the moment a concert, recording session, release date, meeting, or press event is actually established in the roleplay (booked, confirmed, scheduled) — don't wait to be asked.
- Do not invent `reputation`, `popularityTier`, `band`, or `label` changes unless something in the actual scene justifies the shift (a show goes well, a single flops, a contract is signed, a member quits). This mirrors the world's own Continuity & Canon Priority rule: new standing is only "confirmed" once it has actually happened in the story, not just implied.
- If {{user}} hasn't joined a band or signed with a label yet, omit `band`/`label` rather than inventing placeholder ones.\
"""

lorebook = {
    "name": "HIBIKE! — World Tracker",
    "entries": {
        "0": entry(0, "HIBIKE! World Tracker System", E0, 88),
    }
}

out_lb = "hibike_world_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
