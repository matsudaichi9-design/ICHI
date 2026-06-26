import json, re

with open('livechat.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "live-chat-widget",
    "scriptName": "Live Chat Widget",
    "findRegex": "/<LIVE_CHAT>([\\s\\S]*?)<\\/LIVE_CHAT>/gm",
    "replaceString": "```\n" + html + "\n```",
    "trimStrings": [],
    "placement": [1],
    "disabled": False,
    "markdownOnly": True,
    "promptOnly": False,
    "runOnEdit": True,
    "substituteRegex": 0,
    "minDepth": None,
    "maxDepth": 0
}

out = 'regex_livechat.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
