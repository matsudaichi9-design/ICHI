import json, re

with open('lol_craft.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)

data = {
    "id": "lol-runeterra-craft-request",
    "scriptName": "LoL Runeterra Crafting Request",
    "findRegex": "/<LOL_CRAFT>([\\s\\S]*?)<\\/LOL_CRAFT>/gm",
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

with open('regex_lol_craft.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"Done! regex_lol_craft.json — {size:,} bytes ({size/1024:.1f} KB)")
