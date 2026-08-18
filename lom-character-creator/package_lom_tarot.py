import json, re

with open('lom_tarot.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lom-tarot-drawn",
    "scriptName": "Lord of the Mysteries — Tarot Card Drawn",
    "findRegex": "/<LOM_TAROT>([\\s\\S]*?)<\\/LOM_TAROT>/gm",
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

out = 'regex_lom_tarot.json'
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
## LORD OF THE MYSTERIES — TAROT CARD SYSTEM (custom meta-progression, not in-world canon)

This is a game-layer collection system layered on top of the story — it is NOT a Beyonder Pathway or in-fiction magic. Treat card draws as a rewarding "the fates take notice" flourish, not something characters in-world are consciously aware of unless the story specifically decides to make it diegetic.

### WHEN TO DRAW A CARD
Whenever {{user}}'s character defeats a significant boss/enemy, completes an important quest, or receives a genuine key item, they have a chance to randomly draw ONE Tarot card. When this happens, post:

<LOM_TAROT>
{JSON}
</LOM_TAROT>

Don't fire this for routine fights or minor pickups — reserve it for the same tier of moment that would warrant a `<LOM_MONSTER>` boss or a `<LOM_ITEM>` key item in the first place. Not every qualifying moment needs to draw a card either — use judgment/pacing, roughly an occasional reward rather than guaranteed every time, unless the story establishes otherwise.

### JSON SCHEMA

```json
{
  "charColor": "#8B5FBF",
  "cardName": "The Hanged Man",
  "cardNumber": "XII",
  "reversed": false,
  "image": "abc123.jpg",
  "meaning": "Suspended between choices, you finally see what dangling costs you.",
  "cardsCollected": 3,
  "rewardName": "The Sealed Hand",
  "rewardDescription": "A full set of five, bound together. Something in the fog takes notice."
}
```

### FIELD REFERENCE
| Field | Notes |
|---|---|
| `cardName` | pick from an actual tarot deck (the 22 Major Arcana are the natural pool — The Fool, The Magician, The High Priestess, The Empress, The Emperor, The Hierophant, The Lovers, The Chariot, Strength, The Hermit, Wheel of Fortune, Justice, The Hanged Man, Death, Temperance, The Devil, The Tower, The Star, The Moon, The Sun, Judgement, The World) — draw randomly, don't cherry-pick for convenience |
| `cardNumber` | that card's traditional number (0 for The Fool through XXI for The World) |
| `reversed` | roughly a coin flip each draw — a reversed card should color the `meaning` text with a twisted/shadow reading of the card's usual sense, not just the same meaning restated |
| `image` | optional catbox filename for real card artwork; omit for the default astral sigil |
| `meaning` | a short, evocative line — what this card portends for the character right now, grounded in what just happened in the story, not a generic tarot-guidebook definition |
| `cardsCollected` | **the running total of cards this character has collected, from 1 to 5** — track this yourself across the story. After a 5th card is drawn and its reward is granted, the count resets to 0 and starts building toward the next set of five. |
| `rewardName` / `rewardDescription` | **only include these two fields when `cardsCollected` is exactly 5** — invent a fitting reward (an item, a boon, a story development) proportionate to a genuine milestone; omit both fields entirely on every other draw |

### OUTPUT RULES
• Keep a private running tally of how many cards this character currently holds toward the next set of five — the player only sees it through this card's own display, so get it right.
• On the 5th card of a set, you must supply `rewardName`/`rewardDescription` — this is the payoff the user specifically asked for.
• Don't repeat the exact same card twice in a row for the same character if avoidable; over a full set of 5, prefer variety.\
"""

path = 'lom_tarot_lorebook.json'
lorebook = {"name": "Lord of the Mysteries — The Astral Ledger (Tarot)", "entries": {}}
lorebook["entries"]["0"] = entry(0, "LOM Tarot Card System", E0, 98)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), {len(lorebook['entries'])} entries (standalone file)")
print("Done!")
