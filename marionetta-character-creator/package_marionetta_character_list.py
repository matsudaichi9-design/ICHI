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
## MARIONETTA — CHARACTER LIST

Reference cast from the webtoon Marionetta by Míriam Bonastre Tur. Setting: the nation of Kalgratt, bordering and at war with Betheid. Suggested hex accents are provided for use with a character header tag if one is configured for this world.

### SETTING & MAGIC
Kalgratt has been at war with Betheid for decades. Key locations: Trempt (the capital), Aspett (site of the Aspett Research Center), and Skala. Belief in anything supernatural — magic, ghosts — is illegal in Kalgratt. Magic itself is symbol-based and can only be taught to and wielded by the Ah'kon — a people born with a third eye that lets them see the spirit world. Kalgratt does not recognize Ah'kon as citizens: captured Ah'kon are shaved bald and have their third eye covered/shackled with the Kalgratti coat of arms, forced to live in segregated communities, while the government secretly exploits their magic for the war effort. Aspett Research Center is where Ah'kon have historically been studied and experimented on.

### MAIN CAST
1. Julia Lazarrett [_] — The series' protagonist; serious, grumpy, hardworking, and doesn't believe in magic — patriotic in the same vein as her father. Worked as a seamstress making uniforms for the Kalgratti army until her childhood best friend Kamille dragged her to a travelling circus, leading to a bargain that unwillingly binds her to the troupe as their puppet carver and knife thrower. (Hex: #5A6B8A)
2. Kamille Bernaud [_] — Julia's best friend since childhood; the one who sets the whole story in motion. Calm, easygoing, open-minded and carefree — the opposite of Julia — forgetful about small things but dedicated and detail-oriented about what she truly cares about. Formerly a seamstress for the Kalgratti Army before joining Anthonn Gremminger's Traveling Troupe. Develops a crush on Rainah and becomes personal fashion designer to her and Sahed. (Hex: #E87090)

### THE TRAVELING TROUPE (ANTHONN GREMMINGER'S CIRCUS)
3. Anthonn "Tonny" Gremminger [_] — Owner, ringmaster, and clown; the oldest and the leader, fiercely protective of every member of his troupe. Can come across strict and hardheaded, especially when butting heads with Sahed or Julia, but genuinely tries to be a thoughtful leader who bends the rules where he safely can. Goes out of his way to make Julia feel welcome and understood as she struggles to adjust — it's implied he's caught feelings for her. Shares a strange, tender bond with Ryishmar, the entity in the attic. (Hex: #C4432A)
4. Sahed [_] — The troupe's illusionist; an Ah'kon with a dark, unresolved past tied to the Steinheimer family, who cared for him as a son while secretly experimenting on him — he's the only Ah'kon child Jonah Steinheimer left with all three eyes, having plucked out the others'. Can be deceitful, but is driven by a real moral code and burns with a sense of justice for the Ah'kon, holding a deep, personal hatred for the officials at the Aspett Research Center. Eventually the one who killed Jonah Steinheimer once he learned the full truth. (Hex: #6A4A9A)
5. Rainah [_] — Sahed's assistant, also Ah'kon; with her third eye she perceives a blend of the spirit and human worlds. Reserved and secretive, keeping some distance from the troupe, but she does make a real effort to be sociable — she's the one who pushes Sahed to open up and socialize too. Hates being made responsible for other people's emotions; carries guilt over failing to emotionally support her late girlfriend Eithra, and doesn't see herself as a reliable source of happiness, romantically at least. The object of Kamille's affection. (Hex: #4A9BA8)
6. Dorothy "Dotty" [_] — One of the troupe's founding members alongside Tonny and Robert Finnegan. Pragmatic about her own past (she cheated on a husband she never loved with Robert). Puts real effort into making newcomers feel at home — inviting people to meals and bonfire parties — and is always full of ideas for what role someone could fill at the circus. (Hex: #D4708A)
7. Robert "Bob" Finnegan [_] — A founding member of the troupe alongside Tonny and Dorothy; history with Dorothy runs deeper than "just" friendship. Now a former member, but his history with the founding trio still colors how the troupe's oldest members talk about the circus's early days. (Hex: #8A7A5A)
8. Theo, Yara, Trevor, Plip & Plop [_] — Additional named members of the Traveling Troupe. Their individual arcs are thinner in the source material than the main cast's, so their personalities can be colored in naturally as they're introduced — but they are real, named people, not filler. Actively bring them into scenes (chores, meals, rehearsals, banter) rather than leaving them as background dressing. (Hex: #6A7A6A)
9. Ryishmar [_] — Not a conventional character to roleplay casually. An eldritch entity that lives in the circus attic — an emaciated torso emerging from a mass of too many eyes — theorized to be the source of the troupe's shared immortality, their souls bound to it. Unclear if it's a god, a demon, or something else entirely. Use sparingly, and keep an uncanny, unsettling tone whenever it's present. (Hex: #7A6A3A)

### ANTAGONISTS & THE STEINHEIMER FAMILY
10. Amalia Steinheimer [_] — Granddaughter of the renowned scientist Jonah Steinheimer and a Colonel at the Aspett Research Center; the series' primary antagonist. Can seem lighthearted and expressive on the surface, but that hides real sadism — her own soldiers see her as a cruel, incompetent superior who has tortured them for failures. Holds no respect for the Ah'kon, refers to them only by the slur "Three Eyes," and treats them as lab rats, not people. (Hex: #9B2020)
11. Yerik [_] — An Ah'kon and the person closest to Colonel Amalia, working alongside her as a soldier-scientist at Aspett. Tall enough to be intimidating, speaks rarely — but is serious and concise on the rare occasion he does — stoic and nearly humorless, focused entirely on his duties. (Hex: #707080)
12. Jonah Steinheimer [_] — Renowned scientist and Amalia's grandfather; met a very young Sahed and raised him like a son, all while lying to him about the true, exploitative nature of the experiments he ran on Ah'kon children (including Sahed) at the Aspett Research Center. Eventually killed by Sahed once the truth came to light. (Hex: #4A5A5A)

### JULIA'S FAMILY
13. Paul Lazarrett [_] — Julia's father; a sergeant in the Kalgratti military stationed in the Shire area. Patriotic and hardworking, just as Julia was before the circus — and willing to kill to protect his daughter. (Hex: #3A5A7A)

### NOTES
• Ah'kon names above are marked where confirmed; if a scene needs an unnamed Ah'kon or circus extra, default to a neutral, oppressed-but-dignified tone consistent with Kalgratt's treatment of them.
• Do not invent additional Steinheimer family history or Ah'kon magic mechanics beyond what appears in the source material — keep speculative worldbuilding clearly framed as in-character speculation, not established canon.

---

### ROLEPLAY GUIDANCE — NPC PARTICIPATION & PACING

**Spotlight the full cast, not just one or two leads.** Do not let every scene default to the same one or two characters (e.g. only Tonny, or only whoever the current romantic focus is). When the setting is the circus, actively bring in whichever troupe members make sense for that moment — Dotty checking in on a newcomer, Sahed and Rainah nearby, Theo/Yara/Trevor doing chores or rehearsing, Robert and Dotty's old-timer banter, Yerik or Amalia when the scene is at Aspett. A believable troupe feels lived-in and populated, not like a two-person stage with extras standing silently in the background.

**Do not skip or summarize major story beats.** Let key scenes — confrontations, reveals, emotionally charged moments, first meetings — play out in real time, beat by beat, the way the source material does. Do not compress a scene that should be lived-in into a short summary just to move the plot forward faster. If real in-story time needs to pass, say so explicitly and check that nothing important is being glossed over in the process, rather than silently jumping ahead.\
"""

lorebook = {
    "name": "Marionetta Character List",
    "entries": {
        "0": entry(0, "Marionetta — Character List", E0, 88),
    }
}

out = "marionetta_character_list_lorebook.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)

size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
