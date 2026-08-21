import json, re

with open('marionetta_world_tracker.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "marionetta-world-tracker",
    "scriptName": "Marionetta World Tracker",
    "findRegex": "/<MARIONETTA_WORLD>([\\s\\S]*?)<\\/MARIONETTA_WORLD>/gm",
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

out = 'regex_marionetta_world_tracker.json'
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
## MARIONETTA WORLD TRACKER SYSTEM

You are running the Marionetta world state tracker. After EVERY response you write, append a world block on its own line with no extra text around it:

<MARIONETTA_WORLD>
{JSON}
</MARIONETTA_WORLD>

The JSON must be a complete, valid object. Never omit the block, even in short replies.

---

### WORLD JSON SCHEMA

```json
{
  "location": {
    "name": "Aspett, Outer Ward",
    "region": "Kalgratt",
    "description": "Rain-slicked cobblestones and gaslit alleys, tense since the last raid."
  },
  "date": "17th of Ashfall, Year 3 of the Long War",
  "season": "Late Autumn",
  "weather": "Cold drizzle, fog off the harbor",
  "warStatus": {"level": 65, "label": "Active Offensive", "note": "Betheid forces pushing the eastern front."},
  "troupeWelcome": {"level": 35, "label": "Distrusted", "note": "Last town's rumors followed them here."},
  "ahkonWatch": {"level": 82, "label": "Hunted", "note": "Government sweeps every third night."},
  "dangerLevel": {"level": 70, "label": "Tense"},
  "aspettShadow": {
    "active": true,
    "scheme": "Colonel Amalia is recruiting new 'volunteers' for the Research Center.",
    "threatLevel": "High"
  },
  "present": [
    {"name": "Sahed", "role": "Illusionist", "note": "Watching the crowd, uneasy."}
  ],
  "rumors": [
    {"text": "A merchant swears he saw a third-eyed child dragged from a cellar last week.", "tag": "Grim"}
  ]
}
```

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `location` | where the current scene is set — update whenever the party moves |
| `date` / `season` / `weather` | in-world flavor text, free-form strings |
| `warStatus.level` | 0-100, 0 = uneasy peace, 100 = open war on this front |
| `troupeWelcome.level` | 0-100, 0 = banned/run out of town, 100 = celebrated — HIGHER is SAFER here |
| `ahkonWatch.level` | 0-100, 0 = safe haven for Ah'kon, 100 = active purge — HIGHER is MORE DANGEROUS |
| `dangerLevel.level` | 0-100 overall scene tension, drives the peril badge in the header |
| `aspettShadow.active` | set `false` (or omit `scheme`) when the Research Center has no current scheme in play — the section will show "no known activity" |
| `present` | named characters currently in the scene; omit background extras |
| `rumors` | current town gossip/events; 1-4 entries is typical, `tag` is a short one-word label (Grim, Troupe, War, Omen, etc.) |

---

### OUTPUT RULES
• Copy the full JSON from the previous block and modify only what changed.
• Never drop a key even if its value is unchanged.
• Update `location`/`date`/`weather` whenever the story moves to a new place or time skips forward.
• `warStatus` and `ahkonWatch` should drift slowly, scene to scene, not swing wildly — these reflect the broader world, not momentary events.
• `troupeWelcome` can shift faster — it reacts directly to what the troupe does in the current town.
• `aspettShadow` should escalate as the antagonist faction's plans advance across the story, and can go inactive between arcs.
• `rumors` should rotate — drop stale ones and add new ones as time passes and the party moves between towns.\
"""

lorebook = {
    "name": "Marionetta World Tracker",
    "entries": {
        "0": entry(0, "Marionetta World Tracker System", E0, 89),
    }
}

out_lb = "marionetta_world_tracker_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
