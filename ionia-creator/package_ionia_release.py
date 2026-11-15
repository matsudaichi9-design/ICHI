import json, re

with open('ionia_release.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "ionia-release",
    "scriptName": "Ionia — Release / Ultimate Technique",
    "findRegex": "/<IONIA_RELEASE>([\\s\\S]*?)<\\/IONIA_RELEASE>/gm",
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

out = 'regex_ionia_release.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Standalone lorebook ──────────────────────────────────────────────────────
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
## IONIA — RELEASE / ULTIMATE TECHNIQUE CARD

When a character (most often a Kakujo member, but any sufficiently powerful Ionia character qualifies) unleashes a named signature technique, domain, or "Release" at a genuinely dramatic moment in the scene — not routine combat — post this tag alone:

<IONIA_RELEASE>
{JSON}
</IONIA_RELEASE>

Reserve this for real turning points: a technique being used for the first time in the story, a desperate last resort, or a moment meant to land hard. Don't fire it for every attack a character throws.

---

### JSON SCHEMA

```json
{
  "characterName": "Yuta Ichisaki",
  "techniqueName": "Four Fangs of Lament",
  "releaseType": "Boundless Release",
  "techColor": "#5B3FA0",
  "scale": "Domain-Scale",
  "description": "A vast domain manifests around him, containing every weapon and spell he has ever copied or stolen. Destroyed weapons reform instantly, and his techniques cost no magic while the domain holds.",
  "limit": "Critical injury breaks the domain immediately. On collapse, his right-brain magical generator resets, refilling his reserves near maximum — but he is left exposed for several seconds.",
  "quote": "Then let's see how much you've got."
}
```

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `techniqueName` | the signature name exactly as established in the character's lore (e.g. "Four Fangs of Lament", "Lunar Fragment Chaos", "Dragon's Wrath") — do not invent a new one for an established character |
| `releaseType` | optional category/epithet shown under the name (e.g. "Boundless Release") — omit if the technique has no such subtitle |
| `techColor` | hex color for the burst/glow — pick something matching the character's established power (e.g. Buzz's earth magic → brown/gold, Renma's lunar blades → silver-blue, Zohaku's blood circuit → crimson) |
| `scale` | optional short tag for how big the effect is (e.g. "Personal", "City-Scale", "Continent-Scale Theoretical Potential") — only include it if the character's lore actually supports that scale; don't inflate it for drama |
| `description` | what actually manifests/happens — pull from the character's established power description where one exists |
| `limit` | the real cost, weakness, or breaking condition — every major technique in this world has one; don't give a technique free of any limit unless its lore explicitly says so |
| `quote` | optional short in-character line delivered as the technique activates |

---

### GUARDRAILS
- Keep `description` and `limit` consistent with what's already established for that character — this card dramatizes an existing power, it doesn't invent a new one on the fly.
- If a character's technique has no established name yet (a new OC, or genuinely first use), it's fine to name it in the moment — but stay consistent with that name afterward.
- Don't use this card for ordinary attacks, parries, or minor spellcasting — it's reserved for a character's defining signature move.\
"""

lorebook = {
    "name": "Ionia — Release Card",
    "entries": {
        "0": entry(0, "Ionia Release / Ultimate Technique Card", E0, 86),
    }
}

out_lb = "ionia_release_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
