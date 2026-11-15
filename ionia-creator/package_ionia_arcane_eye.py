import json, re

with open('ionia_arcane_eye.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "ionia-arcane-eye",
    "scriptName": "Ionia — Arcane Eye Awakening",
    "findRegex": "/<IONIA_EYE>([\\s\\S]*?)<\\/IONIA_EYE>/gm",
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

out = 'regex_ionia_arcane_eye.json'
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
## IONIA — ARCANE EYE AWAKENING CARD

Ionia's magic includes exactly Twelve Arcane Eyes: unique, living ocular anomalies that are never taught or crafted — they simply manifest in a host. When a character in the roleplay genuinely manifests or is confirmed to bear one of the Twelve for the first time in the story (NOT a rumor, NOT a guess — an actual on-screen awakening or a moment the story is establishing as real), post this tag alone:

<IONIA_EYE>
{JSON}
</IONIA_EYE>

Do not post this card speculatively or to foreshadow — only when the story has actually committed to the fact that this character now bears this Eye.

---

### JSON SCHEMA

```json
{
  "characterName": "Elowen Vask",
  "eyeNumeral": "VII",
  "eyeTitle": "Eye of Fractured Compass",
  "eyeTitleLocal": "เนตรแห่งเข็มทิศแตกร้าว",
  "eyeColor": "#2E7D8C",
  "domain": "Spatial anchoring",
  "mark": "The pupil splits into seven fine lines radiating like a cracked compass needle, faintly glowing in low light.",
  "power": "Can anchor a location in memory and open a momentary tear back to it from anywhere in the same territory.",
  "cost": "Each anchor drawn permanently erases one of her own long-term memories, chosen at random by the Eye.",
  "significance": "The first confirmed bearer of this Eye since records began.",
  "quote": "I didn't ask for this. I just wanted to go home."
}
```

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `eyeNumeral` | one of the Roman numerals `I` through `XII` — this drives which of the 12 spokes around the medallion lights up, a visual nod to "one of twelve." Use the canonical numeral for the Eye actually involved (see the Twelve Arcane Eyes reference entry for the full list of domains) |
| `eyeTitle` / `eyeTitleLocal` | the Eye's canonical name; `eyeTitleLocal` is optional (e.g. a Thai name) shown as a small subtitle |
| `eyeColor` | a hex color for the iris/glow — pick something that matches the Eye's canonical `mark` description (e.g. silver-white fog → pale blue, blood/psychic control → deep red) |
| `characterName` | who now bears it — omit only if the story is deliberately leaving the bearer unconfirmed |
| `domain` / `mark` / `power` / `cost` | pull directly from the Eye's established lore where it exists; invent plausible specifics only for the two canonically-unconfirmed details if the story requires them, and stay consistent once invented |
| `significance` | optional flavor line — use it to flag world-level weight (e.g. "first confirmed holder since the Sundering"), not mechanical description |
| `quote` | optional — a short in-character line from the new bearer |

---

### CANON GUARDRAILS — IMPORTANT
- Only **two** Eyes have a confirmed current holder in established canon: Shiken (Eye of Gaia, III) and Lucis Erander (Netra of Tartarus, IV). Never casually assign one of the other ten Eyes to a background character or NPC without this actually being a deliberate, significant story beat.
- Never retroactively claim a past or rumored holder for an Eye whose holder is listed as unknown — the lore explicitly treats those as unresolved mysteries, not blanks to fill in casually.
- If this card is used for Shiken or Lucis Erander themselves, keep `domain`/`power`/`cost` consistent with their established entries rather than inventing new mechanics.
- Transfer mechanics are canonically mysterious (on a holder's death the Eye may transfer immediately, lie dormant for decades, or follow an unobservable process) — don't invent a tidy ritual or rule for how this new bearer got it unless the story has already shown it.\
"""

lorebook = {
    "name": "Ionia — Arcane Eye Awakening",
    "entries": {
        "0": entry(0, "Ionia Arcane Eye Awakening Card", E0, 87),
    }
}

out_lb = "ionia_arcane_eye_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
