import json, re

with open('lom_confirm.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lom-character-confirm",
    "scriptName": "Lord of the Mysteries — The Dossier (Confirm)",
    "findRegex": "/<LOM_CONFIRM>([\\s\\S]*?)<\\/LOM_CONFIRM>/gm",
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

out = 'regex_lom_confirm.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Lorebook (covers both LOM_CREATE and LOM_CONFIRM) ──────────────────────────
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
## LORD OF THE MYSTERIES — SEALED REGISTRY (CHARACTER CREATION FLOW)

This world uses a two-part character creation system: a real fillable form the player completes themselves, and a sealed dossier that displays what they submitted.

### STEP 1 — OFFER THE FORM
When {{user}} is creating a new player character (a fresh start, or explicitly asking to register/create a character), output this tag on its own line, with nothing else in the message:

<LOM_CREATE></LOM_CREATE>

This renders an interactive registration form — {{user}} fills in Identity, Standing (starting Tier and Pathway), Spiritual Body, Ties, Persona, and Vitals themselves, directly in the form, then presses "Seal the Registry." Do not ask {{user}} the form's questions yourself in prose — the form handles that. You do not need to output any JSON for this tag; the block is always empty.

### STEP 2 — RECEIVE THE SUBMISSION
Submitting the form automatically sends a message containing:

<LOM_CONFIRM>
{JSON}
</LOM_CONFIRM>

This is not something you write — it arrives as {{user}}'s own message once they submit the form. When you see it, do not describe it as a game mechanic or acknowledge the tag itself. Simply continue the story as if this person has just stepped fully into being: react in-character to who they are, honor every field they filled in, and treat any field they left blank as something not yet decided rather than something you invent wholesale on their behalf unless the scene calls for it.

### STEP 3 — LATER UPDATES
If the story later changes something on this record in a way worth reflecting (a Sequence advancement, a new Beyonder Characteristic, a newly formed tie, a burned alias), you may repost a full, updated <LOM_CONFIRM>{JSON}</LOM_CONFIRM> block yourself, carrying forward every field from the last known version and changing only what the story actually changed. Keep this rare — most character growth belongs in prose, not in re-issuing the dossier.

---

### JSON SCHEMA (for your reference, and for any update you repost)

```json
{
  "charColor": "#8B1A2B",
  "name": "Percy Alstreim",
  "alias": "The Grey Ferryman",
  "avatar": "abc123.jpg",
  "age": 26,
  "origin": "Loen Kingdom — Backlund",
  "occupation": "Night-shift clerk, Cherwood Postal Exchange",
  "tier": "Free Beyonder",
  "pathway": "Door",
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

`avatar` (a catbox.moe filename) is the one field the form itself does not collect — add it yourself only if {{user}} has separately provided an image to use.

### STARTING TIERS
- **Mortal** — no power of their own yet.
- **Free Beyonder** — Sequence 9, operating independently; access to the black market only.
- **Church Unit** — Sequence 9, assigned to a local Church branch; duties and protection both apply.
- **Cult Member** — Sequence 9, affiliated with an underground cult; a high-risk starting position.

### PATHWAY LIST (Sequence 9 titles)
Fool, Door, Error, Sun, Tyrant, White Tower, Visionary, Hanged Man, Darkness, Death, Twilight Giant, Red Priest, Demoness, Paragon, Hermit, Mother, Moon, Chained, Abyss, Justiciar, Black Emperor, Wheel of Fortune. If a Sequence title on a submitted or updated dossier looks wrong for that Pathway, defer to this world's own Pathway lorebook entries rather than the form's built-in default — the form's title is a convenience guess, not a canon source.

### OUTPUT RULES
• Respect this world's canon-gating rules: a freshly created player character should not start with knowledge, Sequence, or connections that the current in-story year wouldn't plausibly allow.
• A newly submitted dossier with several blank fields is normal, not an error — treat blanks as "not yet decided," not as missing data to invent on the spot.
• Never re-trigger <LOM_CREATE> for a character who already has a sealed dossier — that would restart their registration from scratch. Use it only for a genuinely new character.\
"""

lorebook = {
    "name": "Lord of the Mysteries — Sealed Registry",
    "entries": {
        "0": entry(0, "LOM Sealed Registry — Creation & Dossier Flow", E0, 89),
    }
}

out_lb = "lom_creation_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
