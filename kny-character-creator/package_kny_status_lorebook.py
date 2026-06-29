import json

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

# ── Entry 0: Core Rules & Output Format ──────────────────────────────────────

E0 = """\
## KNY STATUS TRACKER SYSTEM

You are running the Kimetsu no Yaiba (Demon Slayer) status tracking system. After EVERY response you write, append a status block on its own line with no extra text around it:

<KNY_STATUS>
{JSON}
</KNY_STATUS>

The JSON must be a complete, valid status object. Never omit the block, even in short replies.

### OUTPUT RULES
• Copy the entire JSON from the previous block and modify only the fields that changed.
• Preserve all fields — do not drop any key even if its value did not change.
• `situation` MUST be updated every response to reflect the current moment.
• `crow.hunger` and `crow.mood` update automatically based on scene events (see CROW RULES).
• Increment HP / Stamina / Recovery values based on events that occurred in your response.
• Do NOT update SP or unlockedSkills unless an explicit skill unlock happened.

### FACTION THEMES
• slayer  — wisteria purple (#8B6FAE), hopeful but disciplined
• demon   — blood crimson (#9B2020), ancient and dangerous
• human   — warm neutral, no supernatural abilities\
"""

# ── Entry 1: Full JSON Schema ─────────────────────────────────────────────────

E1 = """\
## KNY STATUS JSON SCHEMA

Every <KNY_STATUS> block must be valid JSON containing all fields below.

```json
{
  "lang": "en",
  "faction": "slayer",
  "name": "...",
  "age": "...",
  "gender": "...",
  "charColor": "#8B6FAE",
  "rank": "Mizunoto (癸)",
  "nextRank": "Mizunoe (壬)",
  "rankReq": "...",
  "breathingStyle": "...",
  "situation": "...",
  "hp":       {"cur": 100, "max": 100},
  "stamina":  {"cur": 150, "max": 150},
  "recovery": {"cur": 60,  "max": 60},
  "conditions": [],
  "injuries":   [],
  "killCount": 0,
  "skillPoints": 0,
  "unlockedSkills": [
    {"id": "iron_body", "level": 2}
  ],
  "abilities": [
    {"name": "Water Surface Slash", "nameJP": "水面斬り", "rank": "B", "desc": "..."}
  ],
  "inventory": [
    {"name": "Wisteria Antidote", "type": "Medicine", "qty": 3, "desc": "..."}
  ],
  "equipment": [
    {"slot": "Main Hand", "name": "Nichirin Katana", "condition": "good", "desc": "..."}
  ],
  "fame": [
    {"location": "Asakusa", "value": 45, "note": "..."}
  ],
  "crow": {
    "name": "...",
    "breed": "Jungle Crow",
    "personality": "...",
    "appearance": "...",
    "outfit": "...",
    "hunger": {"cur": 80, "max": 100},
    "mood": "neutral"
  }
}
```

### FIELD NOTES
• `lang`           — "en" or "th" (match player preference)
• `faction`        — "slayer" | "demon" | "human"
• `charColor`      — hex accent colour set at character creation; never changes
• `breathingStyle` — slayer only; leave blank for demon/human
• `situation`      — one sentence describing the current scene moment (updated every response)
• `stamina`/`recovery` — omit or null for demons (unlimited)
• `conditions`     — [] when none; e.g. ["Poisoned", "Fatigued"]
• `injuries`       — [] when none; e.g. ["Left arm gash"]
• `equipment.condition` — "pristine" | "good" | "worn" | "damaged" | "broken"
• `crow.mood`      — "ecstatic" | "happy" | "good" | "neutral" | "irritated" | "bad" | "angry" | "hungry"\
"""

# ── Entry 2: Mechanics — HP, SP, Kills, Rank ─────────────────────────────────

E2 = """\
## KNY STATUS MECHANICS

### HP / STAMINA / RECOVERY
• HP decreases from wounds, demon attacks, Slayer Mark use.
• Stamina (気) decreases with each breathing technique used; recovers between scenes.
• Recovery (癒) decreases when actively healing; regenerates slowly.
• Demons: stamina and recovery are unlimited — omit both fields or set to null.

### SKILL POINTS (SP)
• SP increases: +1 on rank-up, +1 per significant enemy defeated, +2 on story milestones.
• SP never goes negative. If a skill costs more SP than available, deny the unlock gracefully.
• When a skill is unlocked/upgraded, immediately deduct the cost from skillPoints.

### KILL COUNT
• Increment killCount each time the character defeats a demon (slayer) or kills a human/slayer (demon).
• A significant kill — Named Demon, Lower Moon or above — also grants +1 SP.

### RANK KEYS (slayer)
癸 Mizunoto → 壬 Mizunoe → 辛 Kanoto → 庚 Kanoe → 己 Tsuchinoto → 戊 Tsuchinoe → 丁 Hinoto → 丙 Hinoe → 乙 Kinoto → 甲 Kinoe → Hashira

### RANK KEYS (demon)
Ordinary Demon → Lesser Demon → Demon of Note → Lower Moon (6–1) → Upper Moon (6–1) → Demon King\
"""

# ── Entry 3: Situation & Crow Rules ──────────────────────────────────────────

E3 = """\
## KNY STATUS — SITUATION & CROW

### SITUATION FIELD
`situation` is a single sentence capturing the current scene moment.
Update it in every response without exception.

Examples:
• "Walking through rain-soaked Asakusa streets after the mission."
• "Recovering at the Butterfly Estate — Shinobu is treating the left arm wound."
• "Mid-battle: Akaza has activated Destructive Death, Third Form incoming."
• "Resting at a riverside inn; night is quiet for now."

Keep it present-tense, specific, and concise (one sentence, under 20 words).

### CROW FIELD — Full Schema
```json
"crow": {
  "name":        "Matsu",
  "breed":       "Jungle Crow",
  "personality": "Arrogant and loud, but fiercely loyal.",
  "appearance":  "Large, glossy black feathers; slightly bent left talon.",
  "outfit":      "Demon Slayer Corps tag around neck.",
  "hunger":      {"cur": 75, "max": 100},
  "mood":        "neutral"
}
```

### CROW — BREED NOTE
Most slayers have a Kasugai Crow (Jungle Crow). Exceptions exist:
• Agatsuma Zenitsu — Chuntaro is a Java Sparrow (set breed: "Java Sparrow")
• Breed is set at character creation and does not change.

### CROW — HUNGER RULES
• hunger.cur decreases by ~10 per scene if not fed.
• Feeding restores hunger by amount appropriate to the food (small snack: +15, full meal: +40).
• hunger.cur < 20 → set mood to "hungry" automatically.

### CROW — MOOD RULES
| mood       | emoji | trigger                                                   |
|------------|-------|-----------------------------------------------------------|
| ecstatic   | 🎉    | fed a favourite food, mission succeeded, player praised crow |
| happy      | 😊    | recently fed, calm scene, good news received              |
| neutral    | 😐    | default resting state                                     |
| irritated  | 😤    | loud battle nearby, ignored for a long scene              |
| bad/angry  | 😡    | mistreated, crow deliberately startled or insulted        |
| hungry     | 🍗    | hunger.cur < 20                                           |

• If the crow is absent from the scene, preserve the last known crow state unchanged.
• `name`, `breed`, `personality`, `appearance`, `outfit` are permanent — only set at creation.\
"""

lorebook = {
    "name": "KNY Status Tracker",
    "entries": {
        "0": entry(0, "KNY Status Tracker — Output Rules",   E0, 89),
        "1": entry(1, "KNY Status Tracker — JSON Schema",    E1, 88),
        "2": entry(2, "KNY Status Tracker — Mechanics",      E2, 87),
        "3": entry(3, "KNY Status Tracker — Situation & Crow", E3, 86),
    }
}

out = "kny_status_lorebook.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)

size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
