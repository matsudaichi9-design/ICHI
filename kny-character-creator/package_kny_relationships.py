import json, re

def pack(html_file, out_file, script_name, find_regex, tag_name):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'(html\s*,\s*body\s*\{[^}]*background\s*:\s*)[^;]+;', r'\1transparent;', html)
    data = {
        "id": out_file.replace('.json','').replace('regex_',''),
        "scriptName": script_name,
        "findRegex": find_regex,
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
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
    print(f"{out_file} — {size:,} bytes ({size/1024:.1f} KB)")

pack(
    'kny_relationship_tracker.html',
    'regex_kny_relationship_tracker.json',
    'KNY Relationship Tracker',
    r'/<KNY_RELATION>([\s\S]*?)<\/KNY_RELATION>/gm',
    'KNY_RELATION'
)
pack(
    'kny_relationship_edit_card.html',
    'regex_kny_relationship_edit_card.json',
    'KNY Relationship Edit Card',
    r'/<KNY_RELATION_EDIT>([\s\S]*?)<\/KNY_RELATION_EDIT>/gm',
    'KNY_RELATION_EDIT'
)
pack(
    'kny_relationship_delete_card.html',
    'regex_kny_relationship_delete_card.json',
    'KNY Relationship Delete Card',
    r'/<KNY_RELATION_DELETE>([\s\S]*?)<\/KNY_RELATION_DELETE>/gm',
    'KNY_RELATION_DELETE'
)
print("Done!")
