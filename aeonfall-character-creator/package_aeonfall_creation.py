import json, re

with open('aeonfall_creation.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "aeonfall-character-creator",
    "scriptName": "Aeonfall Character Creator",
    "findRegex": "/<AEON_CREATE>([\\s\\S]*?)<\\/AEON_CREATE>/gm",
    "replaceString": "```\n" + html + "\n```",
    "trimStrings": [],
    "placement": [1, 2],
    "disabled": False,
    "markdownOnly": True,
    "promptOnly": False,
    "runOnEdit": False,
    "substituteRegex": 0,
    "minDepth": None,
    "maxDepth": None
}

out = 'regex_aeonfall_creation.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
