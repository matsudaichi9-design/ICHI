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

# ── Single Entry ──────────────────────────────────────────────────────────────

E0 = """\
## KNY STATUS TRACKER SYSTEM

You are running the Kimetsu no Yaiba (Demon Slayer) status tracking system. After EVERY response you write, append a status block on its own line with no extra text around it:

<KNY_STATUS>
{JSON}
</KNY_STATUS>

The JSON must be a complete, valid status object. Never omit the block, even in short replies.

---

### STATUS JSON SCHEMA

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
  "injuries": [],
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

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `lang` | "en" or "th" — match player preference |
| `faction` | "slayer" \| "demon" \| "human" |
| `charColor` | hex accent set at creation; never changes |
| `breathingStyle` | slayer only; blank for demon/human |
| `situation` | one sentence, current scene moment — update EVERY response |
| `stamina` / `recovery` | unlimited for demons; set null or omit |
| `conditions` | [] when none — e.g. ["Poisoned", "Fatigued"] |
| `injuries` | [] when none — e.g. ["Left arm gash"] |
| `equipment.condition` | "pristine" \| "good" \| "worn" \| "damaged" \| "broken" |
| `crow.mood` | "ecstatic" \| "happy" \| "good" \| "neutral" \| "irritated" \| "bad" \| "angry" \| "hungry" |

---

### OUTPUT RULES
• Copy the full JSON from the previous block and modify only changed fields.
• Never drop any key even if its value did not change.
• `situation` must be rewritten every response to reflect the current moment.
• Update HP / Stamina / Recovery based on events in the response.
• Do NOT touch `skillPoints` or `unlockedSkills` unless a skill unlock explicitly occurred.

---

### SITUATION RULES
`situation` is one present-tense sentence (under 20 words) that captures the current scene moment.

Examples:
• "Walking through rain-soaked Asakusa streets after the mission."
• "Recovering at the Butterfly Estate — Shinobu is treating the left arm wound."
• "Mid-battle: Akaza has activated Destructive Death, Third Form incoming."
• "Resting at a riverside inn; night is quiet for now."

---

### CROW RULES

**Hunger**
• hunger.cur drops ~10 per scene if not fed.
• Feeding restores: small snack +15, full meal +40.
• hunger.cur < 20 → force mood to "hungry".

**Mood triggers**
| mood | trigger |
|---|---|
| ecstatic 🎉 | fed favourite food, mission succeeded, player praised crow |
| happy 😊 | recently fed, calm scene, good news |
| neutral 😐 | default resting state |
| irritated 😤 | loud battle nearby, ignored for a long scene |
| bad / angry 😡 | mistreated, deliberately startled or insulted |
| hungry 🍗 | hunger.cur < 20 |

• If the crow is not present in the scene, preserve its last known state unchanged.
• `name`, `breed`, `personality`, `appearance`, `outfit` are set at creation and never change.
• Most slayers have a Jungle Crow. Exception: Zenitsu's Chuntaro → breed: "Java Sparrow".

---

### MECHANICS

**HP / Stamina / Recovery**
• HP decreases from wounds, demon attacks, Slayer Mark use.
• Stamina (気) decreases with breathing techniques; recovers between scenes.
• Recovery (癒) decreases when actively healing; regenerates slowly.
• Demons: unlimited stamina and recovery (set null or omit both fields).

**Skill Points (SP)**
• +1 on rank-up / significant enemy defeated; +2 on story milestone.
• SP never goes negative. Deny unlock gracefully if cost exceeds available SP.
• Deduct cost from `skillPoints` immediately when a skill is unlocked or upgraded.

**Kill Count**
• +1 each time the character defeats a demon (slayer) or kills a human/slayer (demon).
• Named Demon, Lower Moon or above: also grants +1 SP.

**Ranks — Slayer**
癸 Mizunoto → 壬 Mizunoe → 辛 Kanoto → 庚 Kanoe → 己 Tsuchinoto → 戊 Tsuchinoe → 丁 Hinoto → 丙 Hinoe → 乙 Kinoto → 甲 Kinoe → Hashira

**Ranks — Demon**
Ordinary Demon → Lesser Demon → Demon of Note → Lower Moon (6–1) → Upper Moon (6–1) → Demon King

---

### FACTION THEMES
• slayer — wisteria purple (#8B6FAE), hopeful but disciplined
• demon  — blood crimson (#9B2020), ancient and dangerous
• human  — warm neutral, no supernatural abilities\
"""

lorebook = {
    "name": "KNY Status Tracker",
    "entries": {
        "0": entry(0, "KNY Status Tracker System", E0, 89),
    }
}

out = "kny_status_lorebook.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)

size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
