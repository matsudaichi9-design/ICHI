import json, re

with open('shadow_dossier.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "shadow-garden-dossier",
    "scriptName": "Eminence in Shadow — Personnel File (Dossier)",
    "findRegex": "/<SHADOW_DOSSIER>([\\s\\S]*?)<\\/SHADOW_DOSSIER>/gm",
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

out = 'regex_shadow_dossier.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Standalone lorebook for the whole Shadow Garden Enlistment flow ──
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
## THE EMINENCE IN SHADOW — SHADOW GARDEN ENLISTMENT & DOSSIER FLOW

Two tags work together for creating a new character in this setting — a prospective Shadow Garden operative (or an ordinary bystander who gets pulled in, if the story goes that way).

### STEP 1 — Open the form
When {{user}} wants to create a new character, post this tag alone, with nothing inside it:

<SHADOW_ENLIST></SHADOW_ENLIST>

This renders a real, fillable enlistment form. Do not fabricate the character's details yourself and do not put JSON inside this tag — the player fills it out and it submits on its own.

### STEP 2 — Receive the confirmation
The form submits a `<SHADOW_DOSSIER>{json}</SHADOW_DOSSIER>` block back into the chat by itself. When you see one arrive, treat it as the character now being real in the story — narrate their arrival at Shadow Garden's hideout (or wherever fits the scene) accordingly. Do not re-post `<SHADOW_ENLIST>` again for the same character afterward — Step 1 only happens once, at creation.

---

### JSON SCHEMA (produced automatically by the form — reference only)

```json
{
  "charColor": "#A32638",
  "name": "Elena Voss",
  "age": "17",
  "persona": "Ordinary Millennium Academy transfer student",
  "appearance": "Silver-grey hair kept in a braid, sharp violet eyes, a small burn scar on her left hand she never explains.",
  "race": "Elf",
  "clan": "",
  "designationType": "greek",
  "codename": "Iota",
  "codenameGlyph": "\\u0399",
  "specialty": "Precision Magic & Infiltration",
  "abilities": [
    {"name": "Presence Erasure", "description": "Can suppress her presence to the point of being unnoticed even in direct eye contact, for up to ten minutes."},
    {"name": "Silent Step", "description": "Moves without a sound on any surface."}
  ],
  "gear": [
    {"name": "Twin Fog Blades", "description": "A matched pair of short blades treated with a numbing agent."}
  ],
  "traits": ["Stoic", "Insomniac", "Secretly Kind", "Distrustful of authority"],
  "recruitment": "Found half-dead outside a possessed elven settlement; Shadow healed her before she ever saw his face.",
  "legend": "They say she was the sole survivor of a village erased by the Cult in a single night — and that she walked out of the ashes already knowing every one of their faces.",
  "motive": "To find out whether the boy who saved her that night was real, or another story she told herself to survive.",
  "extra": [{"label": "Blood Type", "value": "AB"}]
}
```

### FIELD NOTES
- `abilities` and `gear` are both open-ended arrays of `{name, description}` — the form lets the player add as many of each as the character actually has (or none at all). If the story later grants a new ability or item, feel free to describe that character as having gained it even though it won't retroactively appear on this already-submitted dossier — track ongoing changes the same way `<LOM_STATUS>`-style tracking would, in prose or your own notes.
- `traits` is a flat array of short quirk/personality tags.
- `race` is one of Human, Elf, Beastkin, Vampire, or a free-text Other; `clan` is only populated when `race` is Beastkin (e.g. "Wolf Clan", "Golden Leopard Clan").
- `designationType` is `"greek"` or `"numeric"` — see the Designation Naming Convention note below for what each means and when a story should favor one over the other.
- `recruitment` captures how Shadow (or another Shadow Garden member acting on his behalf) actually found and brought in this character — see the Found-Family Theme note below for why this field matters.
- `extra` is a fully open-ended array of `{label, value}` pairs for anything the player wanted to record that didn't fit elsewhere.
- Any of these arrays/fields may be empty or absent — the dossier simply omits a section with nothing in it.

### CANON NOTES — IMPORTANT

**The Seven Shadows already exist and are already named.** Alpha, Beta, Gamma, Delta, Epsilon, Zeta, and Eta are all established characters with specific roles — never assign one of their letters (Α–Η) to a newly created character:
| Letter | Role | Notes |
|---|---|---|
| Alpha | Commander-in-chief, de facto second-in-command | An elf, descended from the legendary hero Olivier; the first person Cid ever rescued and healed, which is the origin point of Shadow Garden itself |
| Beta | Intelligence, historical research, documentation | The organization's institutional memory |
| Gamma | COO/Finance, lead strategist, head of R&D, president of the Mitsugoshi Company | Elegant Ojou-type but physically the clumsiest of the seven — one of the two weakest in direct combat |
| Delta | The organization's ultimate combat weapon | A Wolf Clan beastkin; blood-knight instincts, sees Shadow as her pack's Alpha |
| Epsilon | Precision magic and infiltration, "The Precise" | Sculpts her slime suit with extreme finesse; formerly led a church militant order called the Templars |
| Zeta | Exploration, reconnaissance, espionage | A Golden Leopard Clan beastkin (formerly named Lilim); secretly runs her own faction within Shadow Garden with a hidden agenda |
| Eta | Head of Research & Development | Elf, brilliant but eccentric "mad scientist," edges out Gamma as the stronger fighter of the two weakest members |

**Designation Naming Convention — read carefully.** The Greek letters Α–Η are reserved exclusively for the Seven Shadows. Every operative recruited afterward is a "Number" — but the source material's own roster shows Numbers using BOTH further Greek letters (Θ, Ι, Κ, Λ, Μ, Ν, Ξ, Ο, Π, Ρ, Σ, Ω, etc.) AND plain numeric codes (Rose Oriana = 666, Akane Nishino = 712, other examples include 559, 664, 665), with the shift toward pure numbers reflecting the organization's growth well beyond what the Greek alphabet can neatly cover. Both are equally valid and canon-accurate — this is exactly why the enlistment form lets the player choose either a Greek letter or a numeric code. As a loose narrative guide, earlier/smaller-scale stories can lean toward Greek letters, while a later, larger, more established Shadow Garden fits numeric codes just as well.

**Found-Family Through Rescue — a defining theme.** Every one of the Seven Shadows, and many Numbers besides, joined Shadow Garden after being personally saved by Cid/Shadow from something genuinely dire — most often demonic possession, but also grievous injury or captivity. This is the emotional engine behind the whole organization's fierce loyalty. When narrating a new character's `recruitment` field or their arrival into the story, lean into this pattern by default (a rescue, an act of healing, a debt of the kind that reshapes a life) rather than a simple job interview — though it's fine for a given character to break the mold if the story calls for it.

**Cid Kagenou ("Shadow")** is, in-universe, extremely reluctant to reveal himself directly, maintains a deliberately unremarkable public persona as an academy student, and functions as a genuinely unreliable narrator — he believes his elaborate Cult of Diablos mythology and his own dramatic pronouncements are harmless role-play, while in fact the threats are entirely real and his instincts keep being right anyway. A newly enlisted character would most naturally be recruited, tested, or observed by an existing Shadow Garden member (or by Shadow in one of his many aliases — Mundane Mann, Ski Mask Berserker, and others) rather than meeting him plainly as "Shadow" right away. `legend` exists to capture this same signature comedic device on a smaller scale: an overly dramatic, half-mythologized backstory a character has come to believe about themselves, that may not be entirely true — play into that tone without necessarily confirming or denying it outright.

**Standard equipment**: every Shadow Garden member wears a magically-conductive slime bodysuit (~99% conductivity) as their combat uniform, customizable in shape by sufficiently skilled users — worth keeping in mind as a baseline even if a character's own `gear` list focuses on more distinctive personal equipment instead. Their combat and magical training also traces back to "Shadow Wisdom" — the body of technique and philosophy Cid personally imparts, giving Shadow Garden's core members capabilities well beyond conventional military or magical schooling.

`persona` is the character's mundane, everyday-life cover identity (student, shopkeeper, etc.) — most Shadow Garden members maintain one, mirroring how Cid himself poses as an unremarkable student.\
"""

path = 'shadow_enlistment_lorebook.json'
lorebook = {"name": "The Eminence in Shadow — Shadow Garden Enlistment", "entries": {}}
lorebook["entries"]["0"] = entry(0, "Shadow Garden Enlistment & Dossier Flow", E0, 0)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), {len(lorebook['entries'])} entries (standalone file)")
print("Done!")
