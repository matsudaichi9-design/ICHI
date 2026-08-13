import json, re

with open('marisol_enrollment_form.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "marisol-enrollment-form",
    "scriptName": "Marisol Bay High — Enrollment Form",
    "findRegex": "/<MARISOL_ENROLL>([\\s\\S]*?)<\\/MARISOL_ENROLL>/gm",
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

out = 'regex_marisol_enrollment_form.json'
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
## MARISOL BAY HIGH — ENROLLMENT FORM SYSTEM

This is the character-creation flow for a new student at Marisol National Comprehensive High School. Do not front-load this as a list of questions — walk {{user}} through it the way enrollment actually happens: in person, at the Guidance Office, filling in a paper form while someone (a guidance counselor — Ms. Reyes is the school's counselor of record, if no other staff member is established for this scene) makes small talk, glances at the form, asks a follow-up question here and there. Let the ordinary bureaucratic texture of the moment carry some of the scene — the scratch of a ballpoint pen, a fan rattling in the corner, the smell of old paper — per this world's grounded-realism tone guidance.

Once you have enough to fill in the form (it does not need to be exhaustive on the first pass — fields can stay blank and be filled in over later scenes), append a block on its own line with no extra text around it:

<MARISOL_ENROLL>
{JSON}
</MARISOL_ENROLL>

The JSON must be a complete, valid object. Re-post the full block (carrying forward every field, updating only what changed) any time enrollment information is added, corrected, or filled in further — e.g. later in the same scene, or if the character transfers, retakes a subject, changes clubs, etc.

---

### JSON SCHEMA

```json
{
  "charColor": "#2E5C4E",
  "controlNo": "2026-000482",
  "schoolYear": "2026-2027",
  "photo": "abc123.jpg",
  "name": "Marisol dela Peña",
  "nickname": "Mari",
  "age": 16,
  "sex": "F",
  "birthdate": "March 3, 2010",
  "address": "Purok 4, Brgy. Malinao, Marisol Bay",
  "gradeLevel": "Grade 11",
  "section": "Sampaguita",
  "track": "STEM",
  "previousSchool": "Marisol Bay Elementary & Junior High",
  "generalAverage": "91.4",
  "guardian": {
    "name": "Teresita dela Peña",
    "relation": "Mother",
    "contact": "0917-XXX-XXXX",
    "occupation": "OFW — Domestic Worker, Hong Kong"
  },
  "interests": ["Journalism Club", "Chess Club", "Science Club"],
  "statement": "I want to make my mother proud, even from here...",
  "dateFiled": "June 3, 2026"
}
```

---

### FIELD REFERENCE
| Field | Notes |
|---|---|
| `charColor` | accent color for the form; the default institutional teal (`#2E5C4E`) is fine to leave alone unless there's a specific reason to change it |
| `photo` | catbox image code if {{user}} has provided one; omit entirely to show the blank ID-photo silhouette — most students will not have one, and that's the normal state, not an error |
| `controlNo` / `schoolYear` | bureaucratic flavor — invent a plausible control number if none is established; school year should match the current in-story year |
| `track` | Senior High only (Grade 11–12): STEM, ABM, HUMSS, GAS, TVL, or Arts. Leave blank/omit for Grade 7–10 |
| `guardian.occupation` | a small but meaningful detail — this is a natural, unforced way to reflect a family's financial situation, an absent OFW parent, a family business, etc., per this world's texture |
| `interests` | UNLIMITED — clubs the character is signing up for or curious about; see the Clubs & Organizations entries for the full roster |
| `statement` | the form's "Statement of Purpose" field. Keep it in the character's own voice, brief, and grounded — this is the one place on an otherwise cold bureaucratic form where something true and a little unguarded can surface. It does not need to be sad or dramatic; an ordinary, sincere line is just as fitting as a quietly heavy one. Never force melodrama here |

---

### OUTPUT RULES
• It's normal and expected for fields to be missing or blank on an early pass — an enrollment form filled out incompletely, in a hurry, or with a guardian who couldn't make it that day is more realistic than a perfectly completed one.
• Never invent dramatic backstory just to fill the `statement` field — follow this world's tone guidance (small, specific, ordinary detail over declared emotion).
• Once submitted, treat the form as this character's on-file record — update it in place rather than generating a second, separate one, unless the story specifically calls for a new enrollment (e.g. a transfer to a different section or track).\
"""

lorebook = {
    "name": "Marisol Bay High — Enrollment Form",
    "entries": {
        "0": entry(0, "Marisol Bay High — Enrollment Form System", E0, 90),
    }
}

out_lb = "marisol_enrollment_form_lorebook.json"
with open(out_lb, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"{out_lb} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
