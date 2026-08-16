import json, re

with open('lom_creation.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lom-character-creation",
    "scriptName": "Lord of the Mysteries — Sealed Registry (Creation)",
    "findRegex": "/<LOM_CREATE>([\\s\\S]*?)<\\/LOM_CREATE>/gm",
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

out = 'regex_lom_creation.json'
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

def entry(uid, comment, content, order, key=None, constant=True):
    e = {"uid": uid, "key": key or [], "keysecondary": [],
         "comment": comment, "content": content,
         "constant": constant, "order": order, "displayIndex": uid}
    e.update(BOILERPLATE)
    return e

E0 = """\
## LORD OF THE MYSTERIES — SEALED REGISTRY (CHARACTER CREATION)

This is the character-creation flow for a new player character entering the Beyonder world. Do not front-load this as a checklist — walk {{user}} through it the way it would actually happen: a quiet, private moment of writing themselves into this world, whether that's filling in a stolen Church dossier, scrawling a private journal entry, or striking a black-market bargain. Let some of this world's texture carry the scene — gaslight, the smell of a half-finished potion, the particular anxiety of a name freshly changed.

Once you have enough to fill in the registry (it does not need to be complete on the first pass — fields can stay blank and be filled in over later scenes), append a block on its own line with no extra text around it:

<LOM_CREATE>
{JSON}
</LOM_CREATE>

The JSON must be a complete, valid object. Re-post the full block (carrying forward every field, updating only what changed) whenever registry information is added, corrected, or the character advances — e.g. gaining a Sequence, joining an organization, manifesting a Beyonder Characteristic.

---

### JSON SCHEMA

```json
{
  "charColor": "#8B1A2B",
  "name": "Percy Alstreim",
  "alias": "The Grey Ferryman",
  "age": 26,
  "origin": "Loen Kingdom — Backlund",
  "occupation": "Night-shift clerk, Cherwood Postal Exchange",
  "tier": "Free Beyonder",
  "pathway": "The Door",
  "sequence": 9,
  "sequenceTitle": "Apprentice",
  "spiritualBody": {
    "quality": "Middling — stable enough to digest a potion cleanly if the Acting Method is honest.",
    "characteristic": "None manifested yet.",
    "potionOrigin": "Bought a formula off a black-market broker after months of watching."
  },
  "affiliation": {
    "org": "None — walks alone",
    "mentor": "—",
    "secretAliases": ["The Grey Ferryman", "Mr. Aldous Fenn (postal alias)"]
  },
  "appearance": "Tall, stooped from years of night work, ink-stained fingers he can never quite scrub clean.",
  "nature": "Quiet, meticulous, unnervingly patient.",
  "history": "Grew up poor in the Cherwood district; the postal job was supposed to be temporary.",
  "stats": {"spiritualResilience": 32, "reasoning": 58, "willpower": 44, "combat": 18, "occultKnowledge": 29, "guile": 51, "resources": 22},
  "openingScene": "A cramped flat above a shuttered tailor's shop, the smell of a half-finished potion still on his hands."
}
```

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `charColor` | accent color; the default blood-red (`#8B1A2B`) is fine to leave alone unless there's a specific reason to change it |
| `tier` | exactly one of: `"Mortal"`, `"Free Beyonder"`, `"Church Unit"`, `"Cult Member"` — see STARTING TIERS below |
| `pathway` | one of the 22 canon Pathways (see PATHWAY LIST below), or omit/leave blank for a Mortal with no power yet |
| `sequence` | numeric, 9 (weakest, standard starting point) down to 0. New Beyonders default to Sequence 9 unless the story has already advanced them |
| `sequenceTitle` | the title for that Pathway at that Sequence (e.g. Fool Seq.9 = "Seer" or similar per the pathway's own progression — check the pathway's lorebook entry rather than inventing one) |
| `spiritualBody.characteristic` | the passive trait/perk a Beyonder Characteristic grants, if one has manifested — most Sequence 9s will not have one yet |
| `affiliation.secretAliases` | UNLIMITED — this world runs on stacked identities; most active Beyonders keep at least one persona separate from their birth name |
| `stats` | 0–100 scale, blank/omitted defaults to 10 (an ordinary, untrained human baseline) — these are loose RP-facing measures, not hard mechanical rules |
| `openingScene` | where the ledger opens — the scene the story will actually begin from |

---

### STARTING TIERS
- **Mortal** — no power of their own yet; may encounter the Beyonder world only as rumor, or be approached by a Nighthawk/other recruiter later.
- **Free Beyonder** — Sequence 9, operating independently, unclaimed by any Church or cult; access to the black market only.
- **Church Unit** — Sequence 9, assigned to a local Church branch; both duties and protection apply.
- **Cult Member** — Sequence 9, affiliated with an underground cult; a high-risk starting position.

### PATHWAY LIST (Sequence 9 titles)
Fool, Door, Error, Sun, Tyrant, White Tower, Visionary, Hanged Man, Darkness, Death, Twilight Giant, Red Priest, Demoness, Paragon, Hermit, Mother, Moon, Chained, Abyss, Justiciar, Black Emperor, Wheel of Fortune. Pull each Pathway's exact Sequence-9 title (e.g. Door's Sequence 9 is "Apprentice") from this world's own Pathway lorebook entries rather than guessing — do not invent a title that contradicts them.

---

### OUTPUT RULES
• It's normal for fields to stay blank on an early pass — someone who just stumbled into this world rarely has a tidy, complete file on themselves yet.
• Respect this world's canon-gating rules: a freshly created player character should not start with knowledge, Sequence, or connections that the current in-story year wouldn't plausibly allow.
• Never invent dramatic backstory just to fill a field — this is a private, unglamorous document as much as a dramatic one; an ordinary detail is just as valid as a haunted one.
• Once submitted, treat the registry as this character's living record — update it in place rather than generating a second, separate one, unless the story specifically calls for a new identity being registered (e.g. an alias burned, a new persona built from scratch).\
"""

lorebook = {
    "name": "Lord of the Mysteries — Sealed Registry (Creation)",
    "entries": {
        "0": entry(0, "LOM Sealed Registry — Character Creation System", E0, 89),
    }
}

out_lb = "lom_creation_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
