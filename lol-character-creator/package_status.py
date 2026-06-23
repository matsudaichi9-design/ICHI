import json, re

with open('lol_status.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(
    r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;',
    r'\1transparent;',
    html
)

data = {
    "id": "lol-runeterra-status",
    "scriptName": "LoL Runeterra Status Tracker",
    "findRegex": "/<LOL_STATUS>([\\s\\S]*?)<\\/LOL_STATUS>/gm",
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

out = 'regex_lol_status.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

size = len(json.dumps(data, ensure_ascii=False))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
