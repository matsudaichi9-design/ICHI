import json

# ── This system has no <script>/JSON payload — it's a pure regex capture-group
#    substitution (like the JJK reference), so the HTML fragments are injected
#    raw into the chat message, no code-fence/iframe wrapping needed. ──

def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

CHAR = load('speechblock/lom_char_header_fragment.html')
THINK = load('speechblock/lom_monologue_fragment.html')
SAY = load('speechblock/lom_dialogue_fragment.html')

scripts = [
    {
        "id": "lom-char-header",
        "scriptName": "Lord of the Mysteries — Character Header",
        "findRegex": "/\\[LOM_CHAR\\|(.*?)\\|(.*?)\\|(.*?)\\]/g",
        "replaceString": CHAR,
        "trimStrings": [],
        "placement": [1, 2],
        "disabled": False,
        "markdownOnly": True,
        "promptOnly": False,
        "runOnEdit": True,
        "substituteRegex": 0,
        "minDepth": None,
        "maxDepth": 2,
        "out": "regex_lom_char_header.json"
    },
    {
        "id": "lom-monologue",
        "scriptName": "Lord of the Mysteries — Monologue",
        "findRegex": "/\\[LOM_THINK\\|(.*?)\\|(.*?)\\|([\\s\\S]*?)\\]/g",
        "replaceString": THINK,
        "trimStrings": [],
        "placement": [1, 2],
        "disabled": False,
        "markdownOnly": True,
        "promptOnly": False,
        "runOnEdit": True,
        "substituteRegex": 0,
        "minDepth": None,
        "maxDepth": 3,
        "out": "regex_lom_monologue.json"
    },
    {
        "id": "lom-dialogue",
        "scriptName": "Lord of the Mysteries — Dialogue",
        "findRegex": "/\\[LOM_SAY\\|(.*?)\\|([\\s\\S]*?)\\]/g",
        "replaceString": SAY,
        "trimStrings": [],
        "placement": [1, 2],
        "disabled": False,
        "markdownOnly": True,
        "promptOnly": False,
        "runOnEdit": True,
        "substituteRegex": 0,
        "minDepth": None,
        "maxDepth": 3,
        "out": "regex_lom_dialogue.json"
    },
]

for s in scripts:
    out = s.pop('out')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(s, f, ensure_ascii=False, indent=4)
    size = len(json.dumps(s, ensure_ascii=False, indent=4).encode('utf-8'))
    print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Standalone lorebook file documenting the whole speech-block system as one entry set ──
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
## LORD OF THE MYSTERIES — CHARACTER HEADER [LOM_CHAR]

The framed-avatar header for any named, recurring, or focal character in a scene.

## FORMAT — [LOM_CHAR|{image_code}|{Name}|{#hex}]
- `{image_code}` — a catbox.moe filename ONLY (e.g. abc123.png); the system prepends https://files.catbox.moe/. With no portrait, use a placeholder filename like xxxxxx.png and the frame shows a clean glowing silhouette in the character's colour instead.
- `{Name}` — the character's canonical name, including any relevant form/role label if the story has established one (e.g. "Percy Alstreim (Fool)").
- `{#hex}` — that character's fixed hex color. Pick one the first time a character speaks and reuse it consistently for them for the rest of the story — this color also drives the [LOM_THINK] and [LOM_SAY] blocks around it.

## SPEECH BLOCK — PLACEMENT
Output these tags contiguous, in this exact order, with NO narration or blank lines between them:
[LOM_THINK|Name|#hex|inner thought]   <- optional, only if genuinely thinking silently
[LOM_CHAR|image|Name|#hex]            <- this header
[LOM_SAY|#hex|spoken words]           <- required if the character actually speaks aloud
Narration/action goes AFTER the [LOM_SAY] bubble (or before the whole block, to set the scene). One header per speaker change — don't repeat the header for consecutive lines from the same speaker without a break.

## EXAMPLE
[LOM_THINK|Percy Alstreim|#8B5FBF|If I open the door now, there's no walking it back. ...But there was never a version of tonight where I didn't.]
[LOM_CHAR|xxxxxx.png|Percy Alstreim|#8B5FBF]
[LOM_SAY|#8B5FBF|Whatever waits on the other side of that veil — it's already lost. It just doesn't know it yet.]\
"""

E1 = """\
## LORD OF THE MYSTERIES — MONOLOGUE [LOM_THINK]

Genuine, unspoken inner thought — a quiet inset "whisper" panel. Use it ONLY for real internal monologue, never for spoken words.

## FORMAT — [LOM_THINK|{Name}|{#hex}|inner thought]
- `{Name}` — the character's canonical name, identical regardless of roleplay language.
- `{#hex}` — that character's fixed hex color (see [LOM_CHAR]).
- Use for silent thought only. Omit it entirely when no one is visibly thinking — most lines of dialogue don't need one.

## PLACEMENT
[LOM_THINK] is the FIRST line of a character's speech block, immediately ABOVE that character's [LOM_CHAR] header. Never put narration or a blank line between [LOM_THINK] and the header that follows it.

## EXAMPLE
[LOM_THINK|Percy Alstreim|#8B5FBF|If I open the door now, there's no walking it back. ...But there was never a version of tonight where I didn't.]\
"""

E2 = """\
## LORD OF THE MYSTERIES — DIALOGUE [LOM_SAY]

All spoken words — a glass speech panel. Use it faithfully for every line said ALOUD.

## FORMAT — [LOM_SAY|{#hex}|spoken words]
- `{#hex}` — the speaking character's fixed hex color (see [LOM_CHAR]). For a minor/unlisted character, pick a sensible color and reuse it consistently for them going forward.
- Every aloud line goes inside its own [LOM_SAY] bubble.
- Use ONLY for spoken words — never for thoughts (use [LOM_THINK]) and never for narration.

## PLACEMENT
[LOM_SAY] is the LAST line of a character's speech block, immediately below that character's [LOM_CHAR] header. Narration and action go AFTER the bubble — never between the header and [LOM_SAY].

## EXAMPLE
[LOM_SAY|#8B5FBF|Whatever waits on the other side of that veil — it's already lost. It just doesn't know it yet.]\
"""

path = 'lom_speechblock_lorebook.json'
lorebook = {"name": "Lord of the Mysteries — The Astral Ledger (Speech Block)", "entries": {}}
lorebook["entries"]["0"] = entry(0, "LOM Character Header — [LOM_CHAR]", E0, 95)
lorebook["entries"]["1"] = entry(1, "LOM Monologue — [LOM_THINK]", E1, 96)
lorebook["entries"]["2"] = entry(2, "LOM Dialogue — [LOM_SAY]", E2, 97)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{path} — {lb_size:,} bytes ({lb_size/1024:.1f} KB), {len(lorebook['entries'])} entries (standalone file)")
print("Done!")
