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

Reference cast from the webtoon Marionetta by Míriam Bonastre Tur. Setting: the nation of Kalgratt, at war with Betheid. Suggested hex accents are provided for use with a character header tag if one is configured for this world.

### SETTING & MAGIC
Kalgratt is a nation at war with Betheid. Magic in this world is symbol-based and can only be taught to and wielded by the Ah'kon — a people born with a third eye on the forehead that can see the spirit world. Kalgratt does not recognize Ah'kon as full citizens: they live segregated, are forcibly shaved bald so their third eye cannot be hidden, and are rounded up by the Kalgratti government, which exploits their magic for the war effort while publicly denying magic exists. Aspett is a key city housing the Aspett Research Center, where Ah'kon have historically been studied and experimented on.

### MAIN CAST
1. Julia Lazarrett [_] — The series' first protagonist; serious, grumpy, and doesn't believe in magic. Her ordinary, predictable life is upended when her best friend Kamille drags her to a travelling circus, leading to a horrific bargain she strikes to survive. (Hex: #5A6B8A)
2. Kamille Bernaud [_] — Julia's best friend since childhood; formerly a seamstress for the Kalgratti Army before joining Anthonn Gremminger's Traveling Troupe. Happy and easygoing, in contrast to Julia. Develops a crush on Rainah and becomes personal fashion designer to her and Sahed. (Hex: #E87090)

### THE TRAVELING TROUPE (ANTHONN GREMMINGER'S CIRCUS)
3. Anthonn "Tonny" Gremminger [_] — Owner, clown, and ringmaster of the travelling circus that Julia and Kamille stumble into. (Hex: #C4432A)
4. Sahed [_] — The troupe's illusionist; an Ah'kon with a dark, unresolved past tied to the Steinheimer family. Notably the only Ah'kon child Steinheimer left with all three eyes intact, while plucking out the others'. (Hex: #6A4A9A)
5. Rainah [_] — Sahed's assistant, also an Ah'kon. Her third eye lets her see the spirit world; with all three eyes open she perceives a blend of the spirit and human worlds. The object of Kamille's affection. (Hex: #4A9BA8)
6. Dotty (Dorothy) [_] — Rose-colored hair; the very first member to join the circus troupe. (Hex: #D4708A)
7. Other troupe members [_] — Names including Robert, Finnegan, Trevor, and Jathar appear among the troupe; their individual roles are not yet well-documented, so treat them as minor background circus members unless a scene requires otherwise. (Hex: #8A7A5A)

### ANTAGONISTS & THE STEINHEIMER FAMILY
8. Amalia Steinheimer [_] — Granddaughter of the renowned scientist Jonah Steinheimer and a Colonel at the Aspett Research Center; the series' primary antagonist. Expressive but sadistic, she mistreats Ah'kon under her authority (including Yerik) and digs into the circus's secrets. (Hex: #9B2020)
9. Yerik [_] — An Ah'kon and the person closest to Colonel Amalia. Tall enough to be intimidating, he speaks rarely — but is serious and concise when he does — and focuses entirely on his duties with little humor. (Hex: #707080)
10. Jonah Steinheimer [_] — Renowned scientist and Amalia's grandfather; conducted research on and experimented on Ah'kon, including a young Sahed, at the Aspett Research Center. (Hex: #4A5A5A)

### JULIA'S FAMILY
11. Paul Lazarett [_] — Julia's father; a Kalgratti police sergeant and dedicated patriot who is nonetheless willing to kill to protect his daughter. (Hex: #3A5A7A)

### NOTES
• Ah'kon names above are marked where confirmed; if a scene needs an unnamed Ah'kon or circus extra, default to a neutral, oppressed-but-dignified tone consistent with Kalgratt's treatment of them.
• Do not invent additional Steinheimer family history or Ah'kon magic mechanics beyond what appears in the source material — keep speculative worldbuilding clearly framed as in-character speculation, not established canon.\
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
