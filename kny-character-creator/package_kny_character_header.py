import json

html = (
    '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700'
    '&family=Shippori+Mincho:wght@500;600&family=Noto+Serif+JP:wght@500;700'
    '&family=Noto+Serif+Thai:wght@500;600&display=swap" rel="stylesheet"/>'

    # Outer container — centered, narrow, stacked vertically (NOT a side-by-side card)
    '<div style="max-width:300px;margin:16px auto 12px;'
    "font-family:'Shippori Mincho','Noto Serif JP','Noto Serif Thai','Times New Roman',serif;"
    'background:transparent;text-align:center;">'

    # ── Top symmetric fade line ──────────────────────────────────────
    '<div style="height:1px;'
    'background:linear-gradient(90deg,rgba(0,0,0,0),$3 40%,$3 60%,rgba(0,0,0,0));'
    'opacity:.5;margin-bottom:14px;"></div>'

    # ── Avatar: centered, octagonal ──────────────────────────────────
    '<div style="position:relative;width:76px;height:76px;margin:0 auto 10px;">'

    # Outer glow pulse
    '<div style="position:absolute;inset:-6px;'
    'clip-path:polygon(29% 0%,71% 0%,100% 29%,100% 71%,71% 100%,29% 100%,0% 71%,0% 29%);'
    'background:$3;opacity:.09;"></div>'

    # Border ring (slightly larger, $3 solid)
    '<div style="position:absolute;inset:-2px;'
    'clip-path:polygon(29% 0%,71% 0%,100% 29%,100% 71%,71% 100%,29% 100%,0% 71%,0% 29%);'
    'background:$3;opacity:.6;"></div>'

    # Inner content (octagonal clip, dark bg)
    '<div style="position:absolute;inset:0;'
    'clip-path:polygon(29% 0%,71% 0%,100% 29%,100% 71%,71% 100%,29% 100%,0% 71%,0% 29%);'
    'background:#06060d;overflow:hidden;">'

    # Radial tint
    '<div style="position:absolute;inset:0;'
    'background:radial-gradient(circle at 50% 36%,rgba(28,12,50,.32),#06060d 70%);'
    'z-index:1;pointer-events:none;"></div>'

    # Fallback SVG silhouette
    '<div style="position:absolute;inset:0;display:flex;align-items:center;'
    'justify-content:center;z-index:2;">'
    '<svg viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="$3" '
    'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" style="opacity:.82;">'
    '<circle cx="12" cy="8.5" r="3.5"/>'
    '<path d="M5 20.5a7 7 0 0 1 14 0"/>'
    '</svg></div>'

    # Portrait image
    '<img src="https://files.catbox.moe/$1" alt="$2" '
    'style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;'
    'display:block;background:#06060d;z-index:3;" onerror="this.style.display=\'none\'"/>'

    '</div>'  # end inner octagon

    # Badge — bottom-right, pentagon/shield shape (NOT a diamond, NOT bottom-right rotate)
    '<div style="position:absolute;bottom:-6px;right:-6px;z-index:20;'
    'width:20px;height:20px;background:$3;'
    'clip-path:polygon(50% 0%,100% 38%,80% 100%,20% 100%,0% 38%);'
    'display:flex;align-items:center;justify-content:center;'
    'box-shadow:0 0 10px -2px $3;">'
    "<span style=\"font-family:'Shippori Mincho','Noto Serif JP',serif;"
    'font-size:9px;font-weight:700;color:#05050b;line-height:1;display:block;'
    'margin-top:2px;">刃</span>'
    '</div>'

    '</div>'  # end avatar outer

    # ── Name: centered below avatar ──────────────────────────────────
    "<span style=\"display:block;font-family:'Cinzel','Times New Roman',serif;"
    'font-size:15px;font-weight:600;color:#f0eae0;letter-spacing:2.8px;'
    'white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'
    'text-shadow:0 0 18px -3px $3;margin-bottom:9px;">$2</span>'

    # ── Subtitle: short lines + ◆ 鬼 殺 隊 ◆ ────────────────────────
    '<div style="display:flex;align-items:center;justify-content:center;'
    'gap:7px;margin-bottom:13px;">'
    '<div style="height:1px;width:22px;'
    'background:linear-gradient(90deg,rgba(0,0,0,0),$3);opacity:.6;"></div>'
    '<span style="color:$3;font-size:5px;opacity:.6;line-height:1;">◆</span>'
    "<span style=\"font-size:7.5px;letter-spacing:5px;color:#6a5f78;"
    "font-family:'Shippori Mincho','Noto Serif JP',serif;\">鬼 殺 隊</span>"
    '<span style="color:$3;font-size:5px;opacity:.6;line-height:1;">◆</span>'
    '<div style="height:1px;width:22px;'
    'background:linear-gradient(90deg,$3,rgba(0,0,0,0));opacity:.6;"></div>'
    '</div>'

    # ── Bottom symmetric fade line ───────────────────────────────────
    '<div style="height:1px;'
    'background:linear-gradient(90deg,rgba(0,0,0,0),$3 40%,$3 60%,rgba(0,0,0,0));'
    'opacity:.28;"></div>'

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
