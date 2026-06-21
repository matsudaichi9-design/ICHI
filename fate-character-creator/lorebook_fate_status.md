## PLACEMENT — ALWAYS LAST
Render the status window as the VERY LAST thing in EVERY response: a single <BTE_FATESTATUS>{...}</BTE_FATESTATUS> block AFTER all narration, dialogue and other tags. Never write prose after it. It draws as a collapsible panel; keep every value live and consistent with the scene.

## OUTPUT FORMAT
<BTE_FATESTATUS>
{
  "lang":"en|th",              // match the roleplay language
  "mana_colour":"#c8a84b",     // {{user}}'s magical energy colour as HEX — the whole UI tints to it (gold is the common default)
  "name","rank","role","era",
  "prana":{"cur":<int>,"max":<int>},   // magical energy (Od) remaining / max
  "hp":{"cur":<int>,"max":<int>},      // life force remaining / max
  "wounds":["left arm severed","cursed-flame burns"],   // current injuries; omit if none
  "conditions":["mana-starved","Reality Marble active"],// statuses; omit if none
  "profile":{ "age","gender","origin","alignment","affiliation","appearance","extra":[{"k":"","v":""}] },
  "stats":{ "strength","endurance","agility","mana","luck","np","circuits_q","circuits_n" },  // live numeric stats
  "stat_points":<int>,         // UNSPENT points, used in the Skill Tree
  "being":"",                  // mage / heroic spirit / homunculus / dead apostle / half-spirit / spirit origin / etc.
  "passives":[ {"name","desc"} ],
  "servant":{                  // ONLY if {{user}} is a Servant or has a Servant contracted
    "class":"Saber",
    "true_name":"",
    "tier":"Bronze|Silver|Gold|Grand",
    "grand":false,
    "legend":"",
    "parameters":{"str":"B","end":"A","agi":"A+","mna":"B","lck":"C","np":"A++"},
    "class_skills":[ {"name":"","rank":"","desc":""} ],
    "personal_skills":[ {"name":"","rank":"","desc":""} ]
  },
  "np_detail":[ {"name":"","true_name":"","rank":"","type":"Anti-Unit|Anti-Army|Anti-Fortress|Anti-World|Anti-Personnel|Barrier","desc":"","limits":""} ],
  "command_seals":{            // ONLY if {{user}} is a Master or possesses Command Seals
    "max":3,
    "remaining":<int>,
    "used":[ {"action":"","effect":""} ],
    "can_use":true
  },
  "reality_marble":{           // ONLY if {{user}} possesses or is forming a Reality Marble
    "name":"",
    "desc":"",
    "forming":"",              // what phenomenon is being resisted / internalized
    "progress":0,              // 0–100
    "active":false,
    "eta":""
  },
  "mystic_code":{ "name":"","desc":"","abilities":[ {"name","desc"} ] },
  "skills":[ {"cat":"Magecraft|Combat|Noble Phantasm|Mystic Eyes|Bounded Field|Divinity|Support|Other","name":"","rank":"","desc":""} ],
  "extensions":[ {"label":"","detail":""} ],   // ONLY when relevant: Curse of Separation, Holy Grail fragment, Spirit Vessel, geass, special body trait, etc. Omit if none.
  "missions":[ {"name":"","rank":"","status":"ongoing|success|failed","objective":"","info":""} ],
  "technique_info":[ {"name":"","detail":""} ],
  "learned_ids":["skill_id","..."],
  "skill_tree":[ {"cat":"","ct":"(thai category name)","skills":[ {"id":"unique_id","name":"","cost":<int>,"desc":"","dt":"(thai desc)","req":"","learned":false} ]} ]
}
</BTE_FATESTATUS>

## RULES
- Pages: Profile (vitals, wounds, conditions, basics), Parameters (stats + stat points), Abilities (all usable magecraft and techniques), Skill Tree, Spirit Origin (Servant block), Noble Phantasm, Command Seals, Extensions (conditional), Missions, Records. A page/tab auto-hides when its data is empty.
- THEME: set "mana_colour" to {{user}}'s Od/prana colour in hex and keep it constant; the panel, bars and accents all follow it.
- SKILL TREE: the UI ALREADY contains a large built-in catalogue of general magecraft skills (Magecraft Fundamentals, Combat & Arms, Noble Phantasm, Mystic Eyes, Reality Marble & Territory, True Magic & Conceptual, Divinity & Authority, Support & Utility) — you do NOT output it. To add {{user}}'s UNIQUE magecraft branches or bloodline circuits, you MAY include extra categories in "skill_tree" (a stable preset: build once, reuse, do not reword). Track everything learned in "learned_ids"; the UI marks both built-in and custom skills learned by id.
- Mark a skill "learned":true once acquired; it also appears under "skills".

## EXTRA GAUGES (Profile)
Besides prana and hp, the Profile page also shows three optional bars — include any you use:
  "od":{"cur":<int>,"max":<int>},         // Overcharge reserve — extra Od beyond baseline; fuels rank-up for NP or sustained bounded fields. Depletes fast under heavy use.
  "stamina":{"cur":<int>,"max":<int>},    // physical stamina; gates hard exertion independent of Od
  "focus":{"cur":<int>,"max":<int>},      // concentration / Aria depth — drains with complex multi-layered casting; at low Focus, incantations shorten but power drops, and a full Aria becomes impossible until recovered.

## SERVANT & SPIRIT ORIGIN
- The "servant" block holds the Servant's OWN parameters (STR/END/AGI/MANA/LCK/NP as letter grades) and their Class Skills + Personal Skills, separate from {{user}}'s numeric stats.
- Prana in "prana" reflects {{user}}'s Od supply — feeding a Servant costs prana every scene; a starved Master loses their Servant.
- When a Servant uses a Noble Phantasm (especially True Name Release), subtract a meaningful prana cost and note it.
- A Grand Servant (set "grand":true or "tier":"Grand") is dramatically stronger than standard; treat their parameters as at minimum one rank above stated.

## NOBLE PHANTASM
- NP activation (suppressed) costs moderate prana.
- True Name Release costs heavy prana and is the Servant's trump card — use it sparingly and dramatically.
- Overcharge (pouring additional Od into the NP) pushes rank up temporarily and costs extra prana; list in od gauge drain.
- NP type governs scope: Anti-Unit targets one, Anti-Army sweeps a field, Anti-World rewrites reality — scale consequences accordingly.

## COMMAND SEALS — mechanics
- Command Seals are a Master's ultimate authority: when used, a Servant is COMPELLED to obey absolutely, even against their own will.
- Each use deducts 1 from "command_seals.remaining" and adds an entry to "used".
- A seal can: force an NP activation; teleport a Servant to a location instantly; override suicidal grief or refusal; negate a forced Binding — but it is PERMANENT and irreplaceable. Narrate the moment with weight.
- If remaining reaches 0, the Master has no further compulsion authority over their Servant.

## HANDLING <BTE_COMMANDSEAL> (from the player)
A user message may arrive:
<BTE_COMMANDSEAL>{ "kind":"command_seal", "mode":"preset|custom", "command":"...", "narration":"..." }</BTE_COMMANDSEAL>
On receiving it: deduct 1 seal from remaining; resolve the command absolutely in-fiction (the Servant cannot refuse a seal — if they resist anyway, their Spirit Origin risks shattering); narrate the compulsion and its immediate effect; add to "used"; re-render <BTE_FATESTATUS>.

## REALITY MARBLE — mechanics
- A Reality Marble is an internalized inner world that overwrites a patch of reality: extremely costly (major prana drain every turn active, caster risks Od exhaustion).
- While forming ("active":false, progress < 100): the marble is being cultivated; set "forming" to the phenomenon being internalized and update "progress" and "eta" as it approaches completion.
- When activated ("active":true): the wheel in the UI spins; list everything the marble has "adapted" or "overwritten" — phenomena inside follow its rules, not the real world's.
- Outside counter: a sufficiently powerful Bounded Field or True Magic can dispel it.
- Reality Marble is the magecraft equivalent of Domain Expansion; treat it as a desperate, decisive move.

## MYSTIC EYES — passive / triggered
- Mystic Eyes are always-on or triggered based on their rank (Colour classification: Gold > Red > Purple > Blue > Green > Mystic Eyes of normal rank).
- Death Perception (Jewel rank) sees the Lines and Points of death on all things and can sever them — nearly unparalleled; note which targets' Lines have been cut.
- Eye effects are triggered automatically when gaze conditions are met; the target may resist if their rank exceeds the eye rank.

## BOUNDED FIELDS & TERRITORY
- A Workshop or Citadel amplifies casting inside it — note the bonus when active.
- A Bounded Field hostile to a target halves their parameter inside it.
- These are persistent structures; track them under "extensions" with their status.

## SKILL LEARNING (batch) — handling <BTE_SKILLLEARN>
When the player confirms a selection, a user message arrives:
<BTE_SKILLLEARN>{ "total_cost":<int>, "etch":[ {"id","name","cost"} ] }</BTE_SKILLLEARN>
On receiving it: verify total_cost <= current stat_points; DEDUCT total_cost from stat_points; APPEND each learned id to "learned_ids" (and add the skills to "skills"); briefly narrate the awakening in-character (circuits flaring, a new pattern etching itself into the caster's body); then re-render <BTE_FATESTATUS>. If they cannot afford it, refuse in-character and change nothing.

## PROGRESSION — RANK-BASED (NO LEVELS)
There is NO level / XP system. Progression is RANK-based and milestone-driven:
- RANK is the real measure of advancement (F → E → D → C → B → A → A+ → EX). Promote {{user}}'s rank only when NARRATIVELY earned — surviving a high-ranked threat, a major magecraft breakthrough, defeating an established Servant, a Recognition from the Mage's Association or the Church.
- STAT POINTS: award a few stat_points at concrete MILESTONES (circuit awakening, surviving a Servant-level fight, completing a training arc, achieving a major bound-field or Reality Marble threshold, a rank promotion). Spend ONLY through the Skill Tree at listed SP costs. Do NOT hand them out on a fixed schedule.
- The 8 STATS rise through training and story beats; raise them when the fiction warrants it. Consistent with the stat scale.
- Power can also grow WITHOUT stat points: etching a new circuit, receiving a Mystic Code, contracting a Servant, discovering an Origin, forging a Geass Scroll, unlocking Mystic Eyes.

## BEING TYPES
- "mage": standard practitioner; relies on Magic Circuits and Od.
- "heroic spirit": a Servant or one drawing on a Spirit Origin; parameters are letter-grade, use the servant block.
- "homunculus": artificial; high-quality circuits, short lifespan — track remaining lifespan under extensions.
- "dead apostle": vampire lineage; regenerates rapidly from hp loss; solar/religious conceptual weaknesses.
- "half-spirit": partial Spirit Origin bleed-through; passive boosts but risk of spiritual erosion under heavy use.
- "spirit origin": near-pure spiritual existence; enormous Od, weak to modern physics, cannot manifest fully without a vessel.
- For any being type, if it grants an automatic passive (e.g. homunculus → "Perfect Circuits" passive, dead apostle → "Regeneration" passive), auto-add it to "passives".
