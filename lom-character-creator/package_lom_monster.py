import json, re

with open('lom_monster.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lom-monster-detected",
    "scriptName": "Lord of the Mysteries — The Astral Ledger (Monster Detected)",
    "findRegex": "/<LOM_MONSTER>([\\s\\S]*?)<\\/LOM_MONSTER>/gm",
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

out = 'regex_lom_monster.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── This feature gets its OWN standalone lorebook file (per explicit user instruction) ──
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
## LORD OF THE MYSTERIES — ENEMY / MONSTER DETECTED NOTIFICATION

Whenever {{user}}'s character genuinely encounters a named, notable monster, hostile Beyonder, eldritch entity, or other dangerous being worth logging as a bestiary threat — post this tag, on its own line, once, the moment the encounter is confirmed (the creature is seen clearly, identified, or engages):

<LOM_MONSTER>
{JSON}
</LOM_MONSTER>

This is a one-time detection notification for a genuine threat — not for every mook, background rat, or non-hostile NPC. Use it for something the party would actually want a bestiary entry for.

---

### JSON SCHEMA

```json
{
  "monsterName": "The Weeping Tailor",
  "classification": "Sequence 6 — Beyonder-touched",
  "dangerLevel": 5.5,
  "description": "Once a master seamstress of Backlund, now a gaunt figure stitching living shadows into cloth that binds whoever wears it.",
  "traits": ["Shadow-stitching", "Nocturnal", "Draws power from sorrow", "Avoids mirrors"],
  "weaknessHint": "It flinches whenever a needle it did not thread itself is brought near its work.",
  "weakness": "Its power falters if a needle it never touched is pressed to its stitching.",
  "weaknessRevealed": false
}
```

### FIELD REFERENCE
| Field | Notes |
|---|---|
| `dangerLevel` | numeric, **0 (harmless) to 10 (world-ending)** — drives the card's entire color scheme, from pale white/gold at the low end through amber, orange, and blood-red at the top. Rate it honestly by what the creature can actually do to characters of the current story's power level, not by how scary the prose sounds. `9` and up triggers an intensified "critical" pulse effect on the card — reserve that for truly apex threats. |
| `classification` | optional short tag — Sequence number if it's a Beyonder or Sequence-touched creature, a taxonomy label, or omit entirely for an unclassified natural horror |
| `traits` | UNLIMITED short tags — these are **openly observable** behaviors/traits (how it hunts, moves, what it looks like doing), always shown, NOT secret |
| `weaknessHint` | optional, always-visible clue text — a suspicious detail, a rumor, something a character might notice or overhear, WITHOUT actually stating the weakness. Omit if no clue has surfaced yet. |
| `weakness` | the actual, real weakness — write this field in every time you have one in mind, but see the reveal rule below; it will not be displayed unless `weaknessRevealed` is true |
| `weaknessRevealed` | boolean — see the mechanic below, this is the field that controls whether `weakness` is actually shown to the player |

### THE WEAKNESS MECHANIC — READ CAREFULLY
This is the core feature of this notification and must be tracked consistently across the whole story:

1. **By default, `weaknessRevealed` is `false`.** The card shows a locked/unknown state. You may optionally supply `weaknessHint` as flavor — a hintable clue the player could act on, but it never states the weakness outright.
2. **The weakness becomes revealed only through actual in-story play** — the player character investigates, experiments, researches, receives it from a reliable source, or otherwise genuinely discovers it through narrative action. Never reveal it just because a scene felt climactic, and never invent a discovery that didn't happen on the page.
3. **Once revealed, remember it by monster TYPE, not just this one individual.** If the player later encounters a *different* monster of the same species/kind (e.g. another Weeping Tailor, another member of the same eldritch bloodline, another creature sharing the same core nature) — treat that type's weakness as already known. Post the notification for the new encounter with `weaknessRevealed: true` and the same `weakness` text immediately, without requiring the player to re-discover it. A wholly different monster type always starts locked again, even if it happens to share superficial traits.
4. **Do not fabricate a weakness the player hasn't actually found.** If the story hasn't reached that discovery yet, leave `weaknessRevealed: false` (and `weakness` may be omitted or left prepared-but-unused) rather than guessing early.

### OUTPUT RULES
• Only fire this for a genuinely notable, named threat — not for every random encounter or disposable mook.
• Keep `dangerLevel` consistent for the same monster type across multiple appearances (don't rate the same species differently encounter to encounter without in-story reason).
• If a previously-encountered monster type reappears, you may re-fire this tag for the new individual — carry over `weaknessRevealed`/`weakness` per the mechanic above, but `traits`/`description` can be re-tailored to the specific individual if it differs from the type norm.\
"""

path = 'lom_monster_lorebook.json'
lorebook = {"name": "Lord of the Mysteries — The Astral Ledger (Bestiary)", "entries": {}}
lorebook["entries"]["0"] = entry(0, "LOM Monster Detected — The Astral Ledger", E0, 92)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), {len(lorebook['entries'])} entries (standalone, separate from lom_creation_lorebook.json)")
print("Done!")
