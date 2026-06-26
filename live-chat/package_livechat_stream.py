import json, re

with open('livechat_stream.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "live-stream-chat",
    "scriptName": "Live Stream Chat",
    "findRegex": "/<SLIVE\\/>\\s*SDATA:(.+)/gm",
    "replaceString": "```\n" + html + "\n```",
    "trimStrings": [],
    "placement": [1],
    "disabled": False,
    "markdownOnly": False,
    "promptOnly": False,
    "runOnEdit": True,
    "substituteRegex": 0,
    "minDepth": None,
    "maxDepth": None
}

out = 'regex_livechat_stream.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
