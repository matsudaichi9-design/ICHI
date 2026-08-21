import json, re

with open('spiderverse_dossier.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "spiderverse-dossier",
    "scriptName": "Spider-Verse — Character Dossier",
    "findRegex": "/<SPIDERVERSE_DOSSIER>([\\s\\S]*?)<\\/SPIDERVERSE_DOSSIER>/gm",
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

out = 'regex_spiderverse_dossier.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Standalone lorebook for the Spider-Verse creation flow ──
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
## SPIDER-VERSE — CHARACTER CREATION & DOSSIER FLOW

Two tags work together to create a new Spider-Person for a specific Earth in the multiverse.

### STEP 1 — Open the form
When {{user}} wants to create a new character, post this tag alone, with nothing inside it:

<SPIDERVERSE_CREATE></SPIDERVERSE_CREATE>

This renders a real, fillable creation form. Do not fabricate the character's details yourself and do not put JSON inside this tag — the player fills it out and it submits on its own.

### STEP 2 — Receive the confirmation
The form submits a `<SPIDERVERSE_DOSSIER>{json}</SPIDERVERSE_DOSSIER>` block back into the chat by itself. When you see one arrive, treat the character as real and present in the story from that point on. Do not re-post `<SPIDERVERSE_CREATE>` again for the same character afterward.

---

### JSON SCHEMA (produced automatically by the form — reference only)

```json
{
  "charColor": "#E23636",
  "name": "Reyna Ortiz",
  "age": "16",
  "persona": "Scholarship student at a Queens magnet school",
  "appearance": "Curly black hair, always in a paint-stained hoodie.",
  "earthDesignator": "22B",
  "universeStyle": "halftone",
  "universeDescription": "A Queens where the subway trains run on stitched-together dimensional rails.",
  "originStory": "Bitten by a spider that fell out of an Alchemax delivery crate during a blackout.",
  "standardPowers": ["Wall-Crawling", "Web-Slinging", "Spider-Sense"],
  "uniquePowers": [{"name": "Echo Step", "description": "Leaves a half-second-delayed afterimage that can absorb one hit."}],
  "costume": "Patchwork denim jacket over a hand-stitched black suit with paint-splatter accents.",
  "gear": [{"name": "Sketch Shooter", "description": "Web fluid mixed with ink; her webs leave visible tags."}],
  "connections": [{"name": "Mom (Elena Ortiz)", "relationship": "Single mother, doesn't know her secret"}],
  "standing": "Independent",
  "canonEvent": "A mentor figure dies protecting the subway line during a dimensional collapse.",
  "canonEventStatus": "looming",
  "voice": "I don't need a mentor. I need five more minutes."
}
```

### FIELD NOTES
- `earthDesignator` follows the series' own numbering convention (e.g. "1610", "65", "928") — the dossier automatically formats it as "EARTH-####". Invent a plausible, currently-unused number rather than reusing an established one (1610, 616B, 65, 928, 138, 50101, 14512, 90214, 8311, 42 are all already claimed — see the canon notes below).
- `universeStyle` is one of `halftone` (classic Ben-Day comic-print — Miles' Earth-1610 aesthetic), `neon` (Miguel/Earth-928's futuristic neon-grid look), `collage` (Hobie/Earth-138's punk cut-and-paste look), or `watercolor` (Gwen/Earth-65's soft pastel wash) — this genuinely re-skins the whole card's color scheme and background texture, mirroring how each universe in the films has its own distinct animation style.
- `standardPowers` is a fixed set of common spider-abilities (Wall-Crawling, Web-Slinging, Spider-Sense, Enhanced Strength, Enhanced Agility, Impact Webbing) the player toggles on/off.
- `uniquePowers` is open-ended, mirroring how Miles has venom-strike and invisibility beyond the standard kit that no other Spider-Person shares — most characters should have zero to a small handful of these, not a long list.
- `canonEventStatus` is one of `looming` (everyone knows it's coming and hasn't happened), `happened` (already occurred, in the past), or `unknown`/`unwritten` (not yet decided by the story) — this is a genuinely important story hook, not flavor text; see the note below.
- Any array/field may be empty or absent — the dossier simply omits a section with nothing in it.

### CANON NOTES — IMPORTANT

**Canon Events are the series' central mechanic.** Every Spider-Person's life includes at least one fixed, tragic anchor point (a loved one's death, a personal loss) that the Spider-Society (led by Miguel O'Hara) believes is required to preserve their universe's stability — interfering with one is treated as catastrophically dangerous. This is exactly why the creation form asks about a character's own canon event. Use `canonEventStatus` to guide pacing:
- `looming` — the event hasn't happened yet in the story; this creates real tension any time the character or their loved ones are put at risk, and gives you a Miles-style "do I let this happen" dilemma to draw on later.
- `happened` — it's already in their past; treat it as backstory that shaped who they are now, similar to Peter Parker's death shaping Miles or George Stacy's estrangement shaping Gwen.
- `unknown`/`unwritten` — genuinely undecided; don't invent one unilaterally unless the story calls for it.

**Already-claimed Earths (don't reuse these numbers for a new character's home dimension):** 1610 (Miles), 616B (Peter B.), 65 (Gwen), 928/Nueva York (Miguel), 138 (Hobie), 50101/Mumbattan (Pavitr), 14512 (Peni), 90214 (Noir), 8311 (Spider-Ham), 42 (the dark alternate-Miles Earth).

**The Spider-Society** (based in Nueva York, Earth-928, led by Miguel O'Hara with his AI Lyla) is a multiversal task force of countless Spider-People monitoring anomalies and protecting canon events — a new character's `standing` field determines how much they've actually interacted with it: a `Member` follows Miguel's chain of command (at least nominally — Hobie and Gwen both quietly defy it when it matters), an `Independent` operates on their own Earth without formal ties, and someone `Unknown to the Society` hasn't been discovered by it yet at all.

**Universe visual style is not just decoration** — in the source films, each dimension has its own distinct animation technique (halftone comic-print for Miles' Brooklyn, hand-cut collage for Hobie's punk London, soft watercolor for Gwen's grief-toned world, sleek neon for Miguel's futuristic Nueva York). When narrating scenes set on a character's home Earth, let their `universeStyle` choice inform the prose's visual texture and mood, not just the card's color scheme.

**Dimensional travel has real costs** — characters who spend too long outside their home universe risk "glitching" (physical/reality instability), so a visiting character lingering in someone else's Earth for an extended story arc is a meaningful narrative pressure, not a free pass.\
"""

path = 'spiderverse_creation_lorebook.json'
lorebook = {"name": "Spider-Verse — Character Creation", "entries": {}}
lorebook["entries"]["0"] = entry(0, "Spider-Verse Creation & Dossier Flow", E0, 0)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), {len(lorebook['entries'])} entries (standalone file)")
print("Done!")
