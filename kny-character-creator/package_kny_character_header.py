import json

html = (
    '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700'
    '&family=Shippori+Mincho:wght@500;600&family=Noto+Serif+JP:wght@500;700'
    '&family=Noto+Serif+Thai:wght@500;600&display=swap" rel="stylesheet"/>'

    # Outer container — padded, relative, corner brackets frame the card
    '<div style="position:relative;max-width:420px;margin:14px auto 10px;padding:11px 14px;'
    "font-family:'Shippori Mincho','Noto Serif JP','Noto Serif Thai','Times New Roman',serif;"
    'background:transparent;">'

    # Corner bracket — top-left
    '<div style="position:absolute;top:0;left:0;width:13px;height:13px;'
    'border-top:1.5px solid $3;border-left:1.5px solid $3;opacity:.55;'
    'pointer-events:none;"></div>'

    # Corner bracket — bottom-right
    '<div style="position:absolute;bottom:0;right:0;width:13px;height:13px;'
    'border-bottom:1.5px solid $3;border-right:1.5px solid $3;opacity:.55;'
    'pointer-events:none;"></div>'

    # Background watermark kanji 鬼
    '<div style="position:absolute;right:14px;top:50%;transform:translateY(-50%);'
    "font-family:'Noto Serif JP','Shippori Mincho',serif;"
    'font-size:62px;font-weight:700;color:$3;opacity:.07;line-height:1;'
    'pointer-events:none;user-select:none;z-index:0;letter-spacing:0;">鬼</div>'

    # Inner row — above watermark
    '<div style="position:relative;z-index:1;display:flex;align-items:center;gap:13px;">'

    # ── Avatar ────────────────────────────────────────────────────────
    '<div style="position:relative;width:56px;height:56px;flex-shrink:0;">'

    # Main frame: rectangular, no circular elements
    '<div style="position:absolute;inset:0;border-radius:3px;overflow:hidden;'
    'background:#06060d;border:1.5px solid $3;'
    'box-shadow:0 0 22px -5px $3,inset 0 0 12px -6px $3;">'

    # Tint overlay
    '<div style="position:absolute;inset:0;'
    'background:radial-gradient(circle at 50% 36%,rgba(28,12,50,.3),#06060d 66%);'
    'z-index:1;pointer-events:none;"></div>'

    # Fallback SVG silhouette
    '<div style="position:absolute;inset:0;display:flex;align-items:center;'
    'justify-content:center;z-index:2;">'
    '<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="$3" '
    'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" style="opacity:.82;">'
    '<circle cx="12" cy="8.5" r="3.5"/>'
    '<path d="M5 20.5a7 7 0 0 1 14 0"/>'
    '</svg></div>'

    # Portrait image
    '<img src="https://files.catbox.moe/$1" alt="$2" '
    'style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;'
    'display:block;background:#06060d;z-index:3;" onerror="this.style.display=\'none\'"/>'

    '</div>'  # end main frame

    # Badge tab — top-LEFT corner (flat tab, not a rotated diamond or circle)
    '<div style="position:absolute;top:-1px;left:-1px;z-index:10;'
    'padding:2px 5px;background:$3;border-radius:0 0 4px 0;">'
    "<span style=\"font-family:'Shippori Mincho','Noto Serif JP',serif;"
    'font-size:8px;font-weight:700;color:#05050b;line-height:1;display:block;">隊</span>'
    '</div>'

    '</div>'  # end avatar

    # ── Text block ────────────────────────────────────────────────────
    '<div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:5px;">'

    # Name — no uppercase (different from JJK), tighter letter-spacing
    "<span style=\"font-family:'Cinzel','Times New Roman',serif;"
    'font-size:14.5px;font-weight:600;color:#f0eae0;letter-spacing:1.5px;'
    'white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'
    'text-shadow:0 0 18px -4px $3;">$2</span>'

    # Thin divider line below name (no gradient line before the subtitle — different structure)
    '<div style="height:1px;background:linear-gradient(90deg,$3,rgba(0,0,0,0) 70%);'
    'opacity:.38;"></div>'

    # Subtitle: outlined pill — completely different from JJK's bare text + left gradient
    '<div>'
    '<span style="display:inline-flex;align-items:center;gap:5px;'
    'border:1px solid $3;border-radius:20px;padding:2px 9px;opacity:.72;">'
    '<span style="color:$3;font-size:5px;line-height:1;">◆</span>'
    "<span style=\"font-size:7.5px;letter-spacing:5px;color:#7a6f88;"
    "font-family:'Shippori Mincho','Noto Serif JP',serif;\">鬼 殺 隊</span>"
    '<span style="color:$3;font-size:5px;line-height:1;">◆</span>'
    '</span>'
    '</div>'

    '</div>'  # end text block

    '</div>'  # end inner row

    '</div>'  # end outer container
)

data = {
    "id": "kny-character-header",
    "scriptName": "KNY Character Header",
    "findRegex": r"/\[KNY\|(.*?)\|(.*?)\|(.*?)\]/g",
    "replaceString": html,
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

out = 'regex_kny_character_header.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
