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
## 86 -EIGHTY-SIX- — CHARACTER LIST & SETTING

Reference material from the light novel series 86 -EIGHTY-SIX- by Asato Asato (illustrated by Shirabii), adapted into an anime by A-1 Pictures. Suggested hex accents are provided for use with a character header tag (e.g. `[EIGHTYSIX|catbox_code|Name|#hexcolor]`, `[_]` marking where an image code would go) if one is configured for this world.

### SETTING
The Republic of San Magnolia has spent nine years fighting the neighboring Empire of Giad, which fields the Legion — an army of fully autonomous, self-replicating war machines that has been steadily grinding the Republic down. The Republic is made up of two peoples: the silver-haired, light-eyed Alba, the ruling majority, and the darker, varied-featured Colorata, an underclass the Alba have scapegoated for generations. The Republic is administratively split into 86 sectors — the Alba live safely behind walls in the first 85, while the Colorata have been stripped of citizenship and interned in a hidden 86th sector.

The Republic publicly claims to fight the entire war with unmanned drones. This is a lie: those "unmanned" units, called Juggernauts, are piloted by conscripted 86 — officially still termed "Processors," never soldiers or citizens — and remotely overseen from safety by Alba "Handlers" who are trained not to think of their charges as people. The Republic eventually falls to the Legion; survivors relocate to the Federacy of Giad (the Empire's post-revolution successor state), which is fighting the same war from the other side.

The Legion can convert a captured or dying human processor into a "Shepherd" unit — a Legion machine built around a harvested human mind that retains fragments of the original person's memory and, sometimes, intent.

### MAIN CAST
1. Shinei "Shin" Nouzen [_] — Callsign Undertaker; known across the front as "the Reaper" for surviving the death of every squad he's commanded. Black hair, red eyes. Field commander of Spearhead Squadron. Can hear the residual "Voices of the Dead" trapped inside Legion Shepherd units, an ability that awakened after a traumatic encounter with his own older brother. Stoic and withdrawn, having quietly made peace with his own death as inevitable; carries a shard of aluminum alloy engraved with the name of every teammate he's lost, a private ritual of "burying" them himself since the Republic won't. (Hex: #B5352E)
2. Vladilena "Lena" Milizé [_] — Callsign Handler One; Alba, silver hair, blue-violet eyes. A Republic officer who commands Spearhead Squadron remotely through the long-range Para-RAID communicator. Unlike nearly every other Alba, she insists on treating the 86 under her command as human beings rather than disposable drones — a position that makes her a social pariah among her own people. Idealistic, stubborn, and willing to risk her career and safety fighting the Republic's institutional racism from the inside. (Hex: #7A6FBF)

### SPEARHEAD SQUADRON
3. Raiden Shuga [_] — Callsign Wehrwolf; Shin's second-in-command and closest friend. Blunt, reliable, and the squad's emotional grounding — the "mother hen" who keeps the younger pilots in line and supplies the compassion Shin often can't spare. Was more volatile and confrontational when he first arrived among the 86, before his squadmates settled him. (Hex: #4A5A3A)
4. Theoto "Theo" Rikka [_] — One of Spearhead's core five; regarded by the others as something like a younger adoptive brother to the squad. (Hex: #6A5A4A)
5. Anju Emma [_] — Of mixed heritage, rejected at first by both the Alba-run Republic and some of her fellow 86 — settled into the squad's older-sister role as a result, holding tightly to the found family she has left. Endured serious abuse in the internment camps before joining Spearhead, including scars cut into her back by fellow prisoners, which she keeps hidden under her long hair and clothing. Skilled and steady in combat despite it. (Hex: #8A6A9A)
6. Kurena Kukumila [_] — Spearhead's youngest member; entered the war young and grew into a lethal sharpshooter — fierce, quick-tempered, and fiercely protective of Shin in particular. (Hex: #B54A6A)

### THE FEDERACY OF GIAD & NORDLICHT SQUADRON
7. Frederica Rosenfort [_] — Last living descendant of the Giadian imperial line; child-sized but centuries removed from an ordinary life, dry and imperious despite her stature. Carries a rare ability to see into the past and present of people she shares a bond with. Effectively the mascot and ward of Nordlicht Squadron once Spearhead's survivors relocate to Giad. (Hex: #C9A227)
8. Grethe Wenzel [_] — A Giadian officer (Leftenant-Colonel) who reassembles Shin's surviving squadmates into the new Nordlicht Squadron within Giad's military once the Republic falls. (Hex: #3A5A6A)
9. Ernst Zimmerman [_] — Guardian figure to Frederica, and later to Shin and his squadmates once they relocate to Giad — a steady adult presence for characters who have had very few. (Hex: #5A4A3A)

### THE LEGION & ANTAGONIST THREADS
10. Shourei "Rei" Nouzen [_] — Shin's older brother, roughly ten years his senior; a former Republic Processor on the Eastern Front who was captured and converted into a Legion Shepherd unit (personal name Dullahan), retaining enough of his original mind to recognize — and target — Shin specifically. The source of Shin's ability to hear the Legion's trapped voices, and the emotional core of his arc. (Hex: #2A2A2A)
11. The Legion [_] — The Empire/Federacy of Giad's autonomous war machine army; "unmanned" in the same hollow sense the Republic claims for its own military. Some high-value Legion units (Shepherds) are built around the harvested mind of a captured human processor, blurring the line between machine and captive soldier. (Hex: #5A5A5A)

### NOTES
• `[_]` marks characters with no image configured for a header UI tag, if one is set up for this world.
• Alba characters typically have silver hair and light blue/violet eyes; Colorata/86 characters have a wide range of hair and eye colors — silver hair and light eyes read as a visual marker of Alba privilege inside the Republic, and NPCs should react to them accordingly.
• The Republic never officially refers to the 86 as soldiers or citizens — its language calls them "Processors" piloting "self-propelled unmanned weapons," even though every "unmanned" unit has a human inside it. Republic-sector NPCs should speak and think in these terms by default, unless a character has specifically had that illusion broken.
• Do not resolve the story's central irony for the player — let the gap between the Republic's official language and its actual practice surface through what characters say and do, not narrator commentary.
• Do not invent additional Legion mechanics, Shepherd-conversion details, or major plot resolutions beyond what appears in the source material — keep speculative worldbuilding clearly framed as in-character speculation, not established canon.\
"""

lorebook = {
    "name": "86 -Eighty-Six- Character List",
    "entries": {
        "0": entry(0, "86 -Eighty-Six- — Character List & Setting", E0, 88),
    }
}

out = "eightysix_character_list_lorebook.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)

size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
