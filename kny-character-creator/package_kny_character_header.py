import json

html = (
    '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700'
    '&family=Shippori+Mincho:wght@500;600&family=Noto+Serif+JP:wght@500;700'
    '&family=Noto+Serif+Thai:wght@500;600&display=swap" rel="stylesheet"/>'

    '<div style="max-width:520px;margin:13px auto 10px;'
    "font-family:'Shippori Mincho','Noto Serif JP','Noto Serif Thai','Times New Roman',serif;"
    'background:transparent;">'

    # --- Main row ---
    '<div style="display:flex;align-items:center;gap:0;">'

    # Left accent strip
    '<div style="width:3px;align-self:stretch;flex-shrink:0;'
    'background:linear-gradient(180deg,$3 40%,rgba(0,0,0,0));'
    'border-radius:2px;margin-right:13px;min-height:54px;"></div>'

    # Avatar container
    '<div style="position:relative;width:54px;height:54px;flex-shrink:0;margin-right:12px;">'

    # Outer ring (outside clip area)
    '<div style="position:absolute;inset:-3px;border:1px solid $3;'
    'border-radius:3px;opacity:.38;pointer-events:none;"></div>'

    # Inner frame
    '<div style="position:absolute;inset:0;border-radius:2px;overflow:hidden;'
    'background:#06060d;border:1.5px solid $3;'
    'box-shadow:0 0 18px -4px $3,inset 0 0 12px -6px $3;">'

    # Radial tint overlay
    '<div style="position:absolute;inset:0;'
    'background:radial-gradient(circle at 50% 36%,rgba(30,15,55,.28),#06060d 66%);'
    'z-index:1;pointer-events:none;"></div>'

    # Fallback SVG silhouette
    '<div style="position:absolute;inset:0;display:flex;align-items:center;'
    'justify-content:center;z-index:2;">'
    '<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="$3" '
    'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" style="opacity:.8;">'
    '<circle cx="12" cy="8.5" r="3.5"/>'
    '<path d="M5 20.5a7 7 0 0 1 14 0"/>'
    '</svg></div>'

    # Portrait image
    '<img src="https://files.catbox.moe/$1" alt="$2" '
    'style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;'
    'display:block;background:#06060d;z-index:3;" onerror="this.style.display=\'none\'"/>'

    '</div>'  # end inner frame

    # Diamond badge (rotate outer 45deg, counter-rotate text)
    '<div style="position:absolute;bottom:-5px;right:-5px;width:18px;height:18px;'
    'background:$3;transform:rotate(45deg);box-shadow:0 0 8px -1px $3;">'
    '<div style="width:100%;height:100%;display:flex;align-items:center;'
    'justify-content:center;transform:rotate(-45deg);">'
    "<span style=\"font-family:'Shippori Mincho','Noto Serif JP',serif;"
    'font-size:9.5px;font-weight:600;color:#05050b;line-height:1;display:block;">刃</span>'
    '</div></div>'

    '</div>'  # end avatar container

    # Text block
    '<div style="flex:1;min-width:0;display:flex;flex-direction:column;'
    'justify-content:center;gap:5px;">'

    # Name
    "<span style=\"font-family:'Cinzel','Times New Roman',serif;"
    'font-size:14.5px;font-weight:600;color:#f0eae0;letter-spacing:2.5px;'
    'text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'
    'text-shadow:0 0 18px -4px $3;">$2</span>'

    # Subtitle row: gradient line + text
    '<div style="display:flex;align-items:center;gap:6px;">'
    '<div style="height:1.5px;width:36px;'
    'background:linear-gradient(90deg,$3,rgba(0,0,0,0));border-radius:1px;"></div>'
    "<span style=\"font-size:8px;letter-spacing:4px;color:#6a5f78;"
    "font-family:'Shippori Mincho','Noto Serif JP',serif;\">鬼 滅 の 刃</span>"
    '</div>'

    '</div>'  # end text block

    '</div>'  # end main row

    # Bottom decoration: centered gradient + diamond
    '<div style="display:flex;align-items:center;margin-top:10px;">'
    '<div style="flex:1;height:1px;'
    'background:linear-gradient(90deg,rgba(0,0,0,0),$3);opacity:.45;"></div>'
    '<span style="color:$3;font-size:5px;opacity:.5;padding:0 5px;line-height:1;">◆</span>'
    '<div style="flex:1;height:1px;'
    'background:linear-gradient(90deg,$3,rgba(0,0,0,0));opacity:.2;"></div>'
    '</div>'

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
