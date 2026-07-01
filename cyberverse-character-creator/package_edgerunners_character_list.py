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

E0 = """\
## CYBERPUNK: EDGERUNNERS — CHARACTER LIST

Reference cast from the Cyberpunk: Edgerunners anime (Night City, same continuity as Cyberpunk 2077). Use the assigned hex color when introducing these characters with the [CYBERID|catbox_code|Name|#hexcolor] header tag — `[_]` marks where the catbox image code goes.

### MAIN CAST
1. David Martinez [_] — Protagonist; former Arasaka Academy honor student turned edgerunner after his mother's death; wears his late mother's Sandevistan before upgrading to military-grade chrome; idealistic and increasingly reckless chasing power to keep pace with his crew; ultimately overloads on cyberware and dies stopping Adam Smasher. (Hex: #FF3B3B)
2. Lucy / Lucyna Kushinada [_] — Elite netrunner; dreams of earning enough eddies to leave Night City for the orbital Crystal Palace (the moon); guarded past as a former Arasaka black-ops netrunner (Cynosure program) still hunted by the corp; David's love interest. (Hex: #00D4FF)

### MAINE'S CREW (EDGERUNNERS)
3. Maine Pierce [_] — Grizzled leader of the mercenary crew that recruits David; gruff but fiercely protective of his "family"; unstable relic cyberware from a past job slowly drives him toward cyberpsychosis over the series. (Hex: #8A7A5A)
4. Dorio [_] — The crew's muscle and driver; heavily armored, no-nonsense, and loyal; takes over as leader after Maine's fall and becomes a mentor to the survivors. (Hex: #4A6B4A)
5. Kiwi [_] — Elegant, composed netrunner and information broker within the crew; secretly plays multiple sides with hidden Arasaka connections; killed during the Embers restaurant confrontation. (Hex: #B070E0)
6. Rebecca [_] — Small, foul-mouthed, ferociously aggressive gunslinger; Pilar's younger sister; develops feelings for David; dies protecting him in the finale. (Hex: #FF2079)
7. Pilar [_] — Rebecca's older brother; gunner and muscle of the crew; killed early when a heist on an automated cargo convoy goes wrong. (Hex: #FF8C42)

### ANTAGONISTS & CORPORATE
8. Adam Smasher [_] — Legendary full-conversion cyborg mercenary in Arasaka's employ; nearly unkillable and a walking symbol of total cyberization; responsible, directly and indirectly, for the death of David's mother, and the primary antagonist of the finale. (Hex: #707080)
9. Faraday [_] — Calm, calculating fixer who brokers jobs for David, Lucy, and Maine's crew; morally ambiguous, with deeper and more sinister ties to Arasaka and to Lucy's past than he lets on. (Hex: #5088D8)
10. Anders Hellman [_] — Arasaka researcher central to Sandevistan and relic cybernetics R&D; forms an unlikely, complicated mentorship with David tied to his work; ultimately betrays him for the sake of his research and his own self-preservation. (Hex: #4A9BA8)

### SUPPORTING CAST
11. Gloria Martinez [_] — David's hardworking, protective mother; her death in a car chase caused indirectly by Adam Smasher is what sets David's entire arc into motion. (Hex: #C9A0A0)
12. Misty / Katie Wellington [_] — Runs an esoteric tarot shop; was a close friend of Gloria's and becomes a grounding, maternal figure for David after her death; develops a tentative relationship with Maine. (Hex: #9B70C4)

### WORLD NOTE
Setting: Night City, in the same continuity as Cyberpunk 2077. Arasaka and Militech are the dominant rival megacorporations. "Edgerunner" is Night City slang for a mercenary/outlaw who lives on the edge of society, taking any job for eddies (the local currency). Excessive cyberware use risks cyberpsychosis — a complete, often violent break from empathy and humanity.\
"""

lorebook = {
    "name": "Cyberpunk Edgerunners Character List",
    "entries": {
        "0": entry(0, "Cyberpunk Edgerunners — Character List", E0, 88),
    }
}

out = "edgerunners_character_list_lorebook.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)

size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
