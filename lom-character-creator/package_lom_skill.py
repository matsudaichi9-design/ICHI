import json, re

with open('lom_skill.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lom-skill-used",
    "scriptName": "Lord of the Mysteries — Skill / Ability Used",
    "findRegex": "/<LOM_SKILL>([\\s\\S]*?)<\\/LOM_SKILL>/gm",
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

out = 'regex_lom_skill.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Standalone lorebook file for this feature ──
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
## LORD OF THE MYSTERIES — SKILL / ABILITY USED NOTIFICATION

Whenever a character actually uses a named technique, Beyonder characteristic, spell, or combat move in the story — post this tag right at the point of use:

<LOM_SKILL>
{JSON}
</LOM_SKILL>

This is a compact, frequent-use HUD element — unlike the other Astral Ledger notifications, it's meant to fire often (every notable skill use in a scene, potentially several times per reply if the character uses multiple techniques). Keep it lightweight: don't hesitate to use it, but don't fire it for pure flavor description that isn't an actual named ability being invoked (e.g. just "she ran across the room" doesn't need this).

---

### JSON SCHEMA

```json
{
  "charColor": "#8B5FBF",
  "skillName": "Illusory Doppelganger",
  "abilityType": "Fool Pathway — Sequence 7 Characteristic",
  "costValue": "40",
  "costUnit": "Spiritual Power",
  "description": "Splits a fragment of the user's spirituality into a perfect illusory double, indistinguishable from the original at a glance, able to act independently for up to one minute before dissolving."
}
```

### FIELD REFERENCE
| Field | Notes |
|---|---|
| `charColor` | optional — hex color, ideally matching the caster's own signature color (from their `<LOM_CONFIRM>` dossier if they have one) so the card visually ties back to them; omit for a neutral default violet |
| `skillName` | the move/technique's actual name — required for the card to mean anything, but if genuinely unnamed just describe it briefly ("A Wild Slash") rather than omitting |
| `abilityType` | optional short line for what kind of ability this is — a Pathway + Sequence characteristic, a mundane combat technique, a passive trait, a ritual, etc. Omit if there's nothing meaningful to add |
| `costValue` | optional — the resource spent. Free text, not strictly numeric: a plain number ("40"), a phrase ("All Remaining"), or omit entirely for a free/passive ability with no cost |
| `costUnit` | optional — what `costValue` is measured in ("Spiritual Power", "Stamina", "HP", or anything the story uses); only shown alongside a `costValue` |
| `description` | optional — what the ability actually does. If provided, the card shows a small toggle to expand/collapse it, so the compact bar can be used repeatedly in a scene without permanently cluttering the screen. Omit for very minor/repeated actions where a fresh explanation isn't needed. |

### OUTPUT RULES
• This tag is for a real, specific use of a named ability — not a generic combat action.
• It's fine — expected, even — to post this tag multiple times in a single reply if the character uses several distinct techniques in sequence.
• Don't invent a cost that hasn't been established for a given ability; if the story hasn't defined one, omit `costValue`/`costUnit` rather than guessing.
• Reuse the same `skillName`/`abilityType`/cost values consistently for the same technique across multiple uses, unless the story specifically changes them (e.g. a weakened cast, an empowered version).\
"""

path = 'lom_skill_lorebook.json'
lorebook = {"name": "Lord of the Mysteries — The Astral Ledger (Techniques)", "entries": {}}
lorebook["entries"]["0"] = entry(0, "LOM Skill / Ability Used", E0, 94)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), {len(lorebook['entries'])} entries (standalone file)")
print("Done!")
