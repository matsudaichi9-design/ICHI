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
  "codename": "Iota",
  "codenameGlyph": "\\u0399",
  "specialty": "Stealth & Infiltration",
  "abilities": [
    {"name": "Presence Erasure", "description": "Can suppress her presence to the point of being unnoticed even in direct eye contact, for up to ten minutes."},
    {"name": "Silent Step", "description": "Moves without a sound on any surface."}
  ],
  "gear": [
    {"name": "Twin Fog Blades", "description": "A matched pair of short blades treated with a numbing agent."}
  ],
  "traits": ["Stoic", "Insomniac", "Secretly Kind", "Distrustful of authority"],
  "legend": "They say she was the sole survivor of a village erased by the Cult in a single night — and that she walked out of the ashes already knowing every one of their faces.",
  "motive": "To find out whether the boy who saved her that night was real, or another story she told herself to survive.",
  "extra": [{"label": "Blood Type", "value": "AB"}]
}
```

### FIELD NOTES
- `abilities` and `gear` are both open-ended arrays of `{name, description}` — the form lets the player add as many of each as the character actually has (or none at all). If the story later grants a new ability or item, feel free to describe that character as having gained it even though it won't retroactively appear on this already-submitted dossier — track ongoing changes the same way `<LOM_STATUS>`-style tracking would, in prose or your own notes.
- `traits` is a flat array of short quirk/personality tags.
- `extra` is a fully open-ended array of `{label, value}` pairs for anything the player wanted to record that didn't fit elsewhere.
- Any of these arrays may be empty or absent — the dossier simply omits a section with nothing in it.

### CANON NOTES — IMPORTANT
- **The Seven Shadows already exist and are already named.** Alpha (commander-in-chief, first seat), Beta (operations), Gamma (finance and business), Delta (ferocious close-combat instinct), Epsilon (elegant perfectionist, slime manipulation), Zeta (secret long-term missions and experiments), and Eta (mad scientist, weapons and tech) are all established named characters. A newly created character is **never** one of these seven and should never be assigned their letters (Α–Η) as a codename.
- That's why the enlistment form's codename picker starts at **Θ (Theta)** and continues through the Greek alphabet — a new operative is a rank-and-file recruit or aspirant within Shadow Garden, using the same naming convention without claiming an already-occupied seat.
- **Cid Kagenou ("Shadow")** leads the organization from the shadows and is, in-universe, extremely reluctant to reveal himself directly — a newly enlisted character would likely be recruited, tested, or observed by an existing Shadow Garden member (or by Shadow himself in disguise) rather than meeting "Shadow" plainly and immediately. Keep first contact suitably mysterious.
- `legend` is meant to capture this series' signature comedy — an overly dramatic, half-mythologized backstory a character has come to believe about themselves (often seeded by Cid's own theatrics) that may not be entirely true. Play into that tone when it comes up in the story, without necessarily confirming or denying it outright.
- `persona` is their mundane, everyday-life cover identity (student, shopkeeper, etc.) — most Shadow Garden members maintain one, mirroring how Cid himself poses as an unremarkable student.\
"""

path = 'shadow_enlistment_lorebook.json'
lorebook = {"name": "The Eminence in Shadow — Shadow Garden Enlistment", "entries": {}}
lorebook["entries"]["0"] = entry(0, "Shadow Garden Enlistment & Dossier Flow", E0, 0)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), {len(lorebook['entries'])} entries (standalone file)")
print("Done!")
