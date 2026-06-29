import json

SRC = '/root/.claude/uploads/25ecaba8-1165-598a-a63b-429da1068baa/1be5ddc0-regexkny_status_tracker.json'
OUT = 'regex_kny_status_tracker.json'
OUT_LB = 'kny_status_tracker_addon_lorebook.json'

with open(SRC) as f:
    data = json.load(f)

rs = data['replaceString']

# ── 1. Smaller widget ─────────────────────────────────────────────────────────
rs = rs.replace(
    'max-width:520px;margin:0 auto',
    'max-width:480px;margin:0 auto'
)
rs = rs.replace(
    '.kny-panel{display:none;padding:14px 15px}',
    '.kny-panel{display:none;padding:11px 13px}'
)

# ── 2. Add CSS for situation card + crow panel + compact skill grid ───────────
NEW_CSS = (
    '\n/* SITUATION */\n'
    '.sit-card{background:var(--bg3);border:1px solid var(--abd);border-left:3px solid var(--acc);border-radius:var(--r2);padding:9px 12px;margin-bottom:14px}\n'
    '.sit-txt{font-size:11px;color:var(--tx2);line-height:1.65;font-style:italic}\n'
    '/* CROW */\n'
    '.crow-portrait{display:flex;align-items:center;justify-content:center;padding:14px;background:var(--bg3);border:1px solid var(--bg4);border-radius:var(--r2);margin-bottom:12px;flex-direction:column;gap:7px}\n'
    '.crow-face{font-size:44px;line-height:1;filter:drop-shadow(0 0 8px rgba(var(--acc-rgb),.45));animation:crwP 3s ease-in-out infinite}\n'
    '@keyframes crwP{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}\n'
    '.crow-mood-nm{font-family:var(--fh);font-size:9px;letter-spacing:2px;text-transform:uppercase;color:var(--acc)}\n'
    '.crow-hbar-row{display:flex;align-items:center;gap:9px;margin-bottom:7px}\n'
    '.crow-hbar-lbl{font-family:var(--fh);font-size:8px;color:var(--tx3);width:50px;text-align:right;flex-shrink:0}\n'
    '.crow-hbar-track{flex:1;height:7px;background:rgba(255,255,255,.05);border-radius:5px;overflow:hidden}\n'
    '.crow-hbar-fill{height:100%;border-radius:5px}\n'
    '.crow-hng-fill{background:linear-gradient(90deg,#c07840,#e8a060);box-shadow:0 0 6px rgba(200,130,60,.4)}\n'
    '.crow-moo-fill{background:linear-gradient(90deg,#4a9080,#60c8a8);box-shadow:0 0 6px rgba(80,180,150,.4)}\n'
    '.crow-hbar-val{font-size:9px;color:var(--tx3);min-width:38px;text-align:right}\n'
    '/* COMPACT SKILL TREE */\n'
    '.skill-grid{display:grid;grid-template-columns:1fr 1fr;gap:5px}\n'
    '.skill-mini{background:var(--bg3);border:1px solid var(--bg4);border-radius:var(--r2);padding:8px 9px;transition:border-color .2s}\n'
    '.skill-mini.unlocked{border-color:rgba(var(--acc-rgb),.35);background:rgba(var(--acc-rgb),.04)}\n'
    '.skill-mini.maxed{border-color:rgba(255,215,0,.35);background:rgba(255,215,0,.03)}\n'
    '.skill-mini.locked{opacity:.68}\n'
    '.skill-mini-top{display:flex;align-items:center;gap:6px;margin-bottom:5px}\n'
    '.skill-mini-ico{font-size:14px;width:22px;text-align:center;flex-shrink:0}\n'
    '.skill-mini-nm{font-size:10px;font-weight:700;color:var(--tx);flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}\n'
    '.skill-mini-foot{display:flex;align-items:center;justify-content:space-between;gap:4px}\n'
    '.skill-mini-lvl{font-size:8px;color:var(--tx3);font-family:var(--fh)}\n'
    '.skill-mini-lvl .cur{color:var(--acc);font-weight:700}\n'
    '.skill-mini-btn{font-size:8px;padding:2px 7px;border-radius:3px;cursor:pointer;border:none;font-family:var(--fh);font-weight:700;letter-spacing:.5px}\n'
)
rs = rs.replace('/* ── UNLOCK OVERLAY ──', NEW_CSS + '/* ── UNLOCK OVERLAY ──')

# ── 3. Add language keys for scene and crow ───────────────────────────────────
OLD_FOOT_L = "foot:['鬼滅の刃 STATUS SYSTEM','ระบบสถานะ 鬼滅の刃'],"
NEW_FOOT_L = (
    "scene:['SCENE','สถานการณ์'],"
    "crow:['KASUGAI CROW','อีกาคาซุงาอิ'],"
    "crowNm:['Name','ชื่อ'],crowBr:['Breed','สายพันธุ์'],"
    "crowPs:['Personality','นิสัย'],crowAp:['Appearance','รูปร่าง'],"
    "crowOt:['Outfit','เครื่องแต่งกาย'],crowHg:['Hunger','ความหิว'],crowMd:['Mood','อารมณ์'],"
    "moodGr:['Ecstatic','ดีมาก'],moodGo:['Happy','ดี'],"
    "moodNe:['Neutral','กลาง'],moodIr:['Irritated','หงุดหงิด'],moodBa:['Angry','โกรธ'],"
    + OLD_FOOT_L
)
rs = rs.replace(OLD_FOOT_L, NEW_FOOT_L)

# ── 4. Situation banner at top of pStatus ─────────────────────────────────────
OLD_PSTATUS_RET = "  return '<div class=\"kny-sec\">'+T('char')+'</div>'+\n    '<div class=\"igrid\">'+gh+'</div>'+\n    '<div class=\"kny-sec mt\">'+T('vital')+'</div>'+\n    '<div class=\"bars\">'+barsH+'</div>'+\n    breathH+\n    rankH+\n    '<div class=\"kny-sec mt\">'+T('cond')+'</div><div class=\"badges\">'+cb+'</div>'+\n    '<div class=\"kny-sec mt\">'+T('inj')+'</div><div class=\"badges\">'+ib+'</div>';"
NEW_PSTATUS_RET = (
    "  var sitH=d.situation?'<div class=\"kny-sec\">'+T('scene')+'</div><div class=\"sit-card\"><div class=\"sit-txt\">'+esc(d.situation)+'</div></div>':'';\n"
    "  return sitH+'<div class=\"kny-sec\">'+T('char')+'</div>'+\n    '<div class=\"igrid\">'+gh+'</div>'+\n    '<div class=\"kny-sec mt\">'+T('vital')+'</div>'+\n    '<div class=\"bars\">'+barsH+'</div>'+\n    breathH+\n    rankH+\n    '<div class=\"kny-sec mt\">'+T('cond')+'</div><div class=\"badges\">'+cb+'</div>'+\n    '<div class=\"kny-sec mt\">'+T('inj')+'</div><div class=\"badges\">'+ib+'</div>';"
)
rs = rs.replace(OLD_PSTATUS_RET, NEW_PSTATUS_RET)

# ── 5. Compact skill tree (2-col grid, no descriptions) ───────────────────────
# The section to replace: from "  var cardsH=visible.map(..." to end of pTree closing "}\n\n"
OLD_TREE_SECTION = (
    '  var cardsH=visible.map(function(sk){\n'
    '    var ul=getUnlockedSkill(sk.id);\n'
    '    var level=ul?ul.level:0;\n'
    '    var isUnlocked=level>0;\n'
    '    var isMaxed=level>=sk.m;\n'
    '    var factionOk=canUseFaction(sk.cat);\n'
    '    var reqOk=!sk.req||getUnlockedSkill(sk.req);\n'
    '    var canUnlock=!isUnlocked&&factionOk&&reqOk&&sp>=sk.c;\n'
    '    var canUpgrade=isUnlocked&&!isMaxed&&factionOk&&sp>=sk.c;\n'
)
NEW_TREE_SECTION = (
    '  var miniH=visible.map(function(sk){\n'
    '    var ul=getUnlockedSkill(sk.id);\n'
    '    var level=ul?ul.level:0;\n'
    '    var isUnlocked=level>0;\n'
    '    var isMaxed=level>=sk.m;\n'
    '    var factionOk=canUseFaction(sk.cat);\n'
    '    var reqOk=!sk.req||getUnlockedSkill(sk.req);\n'
    '    var canUnlock=!isUnlocked&&factionOk&&reqOk&&sp>=sk.c;\n'
    '    var canUpgrade=isUnlocked&&!isMaxed&&factionOk&&sp>=sk.c;\n'
)
rs = rs.replace(OLD_TREE_SECTION, NEW_TREE_SECTION, 1)

# Replace the card body: from "var cardCls='skill-card'" to ".join('');"
OLD_CARD_BODY = (
    "    var cardCls='skill-card'+(isMaxed?' maxed':isUnlocked?' unlocked':' locked');\n"
    "    var tagCls='tag-'+sk.cat.replace('_moon','');\n"
    "    var tagLabels={all:'ALL',slayer:'SLAYER',demon:'DEMON',hashira:'HASHIRA',upper_moon:'UPPER'};\n"
    "    var tagLabel=tagLabels[sk.cat]||sk.cat.toUpperCase();\n"
    "    var desc=TH?sk.tD:sk.eD;\n"
    "    var nm=TH?sk.th:sk.en;\n"
    "\n"
    "    var levDisplay='';\n"
    "    if(sk.m>1){\n"
    "      levDisplay='<span class=\"cur\">'+(isUnlocked?level:0)+'</span>/'+sk.m;\n"
    "    }else if(isUnlocked){\n"
    "      levDisplay='<span class=\"cur\">✓</span>';\n"
    "    }\n"
    "\n"
    "    var btnH='';\n"
    "    if(isMaxed){\n"
    "      btnH='<button class=\"skill-btn btn-maxed\" disabled>'+T('maxed')+'</button>';\n"
    "    }else if(!factionOk){\n"
    "      btnH='<button class=\"skill-btn btn-locked\" disabled>'+T('factionLock')+'</button>';\n"
    "    }else if(!reqOk){\n"
    "      btnH='<button class=\"skill-btn btn-locked\" disabled>'+T('locked')+'</button>';\n"
    "    }else if(isUnlocked){\n"
    "      var cls=canUpgrade?'btn-upgrade':'btn-locked';\n"
    "      var dis=canUpgrade?'':'disabled';\n"
    "      btnH='<button class=\"skill-btn '+cls+'\" '+dis+' data-sk=\"'+sk.id+'\">'+T('upg')+' ('+sk.c+'SP)</button>';\n"
    "    }else{\n"
    "      var cls2=canUnlock?'btn-unlock':'btn-locked';\n"
    "      var dis2=canUnlock?'':'disabled';\n"
    "      btnH='<button class=\"skill-btn '+cls2+'\" '+dis2+' data-sk=\"'+sk.id+'\">'+T('unlk')+' ('+sk.c+'SP)</button>';\n"
    "    }\n"
    "\n"
    "    return'<div class=\"'+cardCls+'\">'+"
    "'<div class=\"skill-card-top\">'+"
    "'<div class=\"skill-icon\">'+esc(sk.ico||'◆')+'</div>'+"
    "'<div class=\"skill-meta\">'+"
    "'<div class=\"skill-name\">'+esc(nm)+'</div>'+"
    "'<div class=\"skill-tags\">'+"
    "'<span class=\"skill-tag '+tagCls+'\">'+esc(tagLabel)+'</span>'+"
    "(sk.req?'<span class=\"skill-tag\" style=\"color:var(--tx3);border:1px solid var(--bg5);background:transparent\">REQ: '+esc(sk.req.replace('_',' ').toUpperCase())+'</span>':'')+"
    "'</div>'+"
    "'</div>'+"
    "'<div style=\"text-align:right;flex-shrink:0\">'+"
    "'<div class=\"skill-cost\">'+esc(sk.c)+' SP</div>'+"
    "'</div>'+"
    "'</div>'+"
    "'<div class=\"skill-desc\">'+esc(desc)+'</div>'+"
    "'<div class=\"skill-footer\">'+"
    "'<div class=\"skill-level\">'+"
    "(TH?'ระดับ':'Lv')+': '+levDisplay+"
    "'</div>'+"
    "btnH+"
    "'</div>'+"
    "'</div>';\n"
    "  }).join('');\n"
    "\n"
    "  return spH+\n"
    "    '<div class=\"tct-row\">'+filtersH+'</div>'+\n"
    "    (cardsH||'<div class=\"empty-state\">'+T('noskill')+'</div>');\n"
    "}\n\n"
)
NEW_CARD_BODY = (
    "    var cardCls='skill-mini'+(isMaxed?' maxed':isUnlocked?' unlocked':' locked');\n"
    "    var nm=TH?sk.th:sk.en;\n"
    "    var lvlH='';\n"
    "    if(sk.m>1)lvlH='Lv <span class=\"cur\">'+(isUnlocked?level:0)+'</span>/'+sk.m;\n"
    "    else lvlH=isUnlocked?'<span class=\"cur\">✓</span>':'—';\n"
    "    var btnH='';\n"
    "    if(isMaxed){\n"
    "      btnH='<button class=\"skill-mini-btn btn-maxed\" style=\"opacity:.5;cursor:default\" disabled>MAX</button>';\n"
    "    }else if(!factionOk||!reqOk){\n"
    "      btnH='<button class=\"skill-mini-btn\" style=\"background:var(--bg4);color:var(--tx3);cursor:default\" disabled>🔒</button>';\n"
    "    }else if(isUnlocked){\n"
    "      var cls=canUpgrade?'btn-upgrade':'btn-locked';\n"
    "      var dis=canUpgrade?'':'disabled style=\"opacity:.5;cursor:default\"';\n"
    "      btnH='<button class=\"skill-mini-btn '+cls+'\" '+dis+' data-sk=\"'+sk.id+'\">▲'+(canUpgrade?sk.c+'SP':'')+'</button>';\n"
    "    }else{\n"
    "      var cls2=canUnlock?'btn-unlock':'btn-locked';\n"
    "      var dis2=canUnlock?'':'disabled style=\"opacity:.5;cursor:default\"';\n"
    "      btnH='<button class=\"skill-mini-btn '+cls2+'\" '+dis2+' data-sk=\"'+sk.id+'\">'+(canUnlock?sk.c+'SP':'🔒')+'</button>';\n"
    "    }\n"
    "    return'<div class=\"'+cardCls+'\">'+"
    "'<div class=\"skill-mini-top\">'+"
    "'<div class=\"skill-mini-ico\">'+esc(sk.ico||'◆')+'</div>'+"
    "'<div class=\"skill-mini-nm\" title=\"'+esc(nm)+'\">'+esc(nm)+'</div>'+"
    "'</div>'+"
    "'<div class=\"skill-mini-foot\">'+"
    "'<div class=\"skill-mini-lvl\">'+lvlH+'</div>'+"
    "btnH+"
    "'</div>'+"
    "'</div>';\n"
    "  }).join('');\n"
    "\n"
    "  return spH+\n"
    "    '<div class=\"tct-row\">'+filtersH+'</div>'+\n"
    "    (miniH?'<div class=\"skill-grid\">'+miniH+'</div>':'<div class=\"empty-state\">'+T('noskill')+'</div>');\n"
    "}\n\n"
)
rs = rs.replace(OLD_CARD_BODY, NEW_CARD_BODY, 1)

# ── 6. Add pCrow() before build ───────────────────────────────────────────────
CROW_FN = (
    '// ── PANEL: CROW ──────────────────────────────────────────────────────────\n'
    'function pCrow(){\n'
    '  var cr=d.crow||{};\n'
    '  var nm=cr.name||\'—\';\n'
    '  var breed=cr.breed||\'Jungle Crow\';\n'
    '  var ps=cr.personality||\'—\';\n'
    '  var ap=cr.appearance||\'—\';\n'
    '  var ot=cr.outfit||\'—\';\n'
    '  var hg=cr.hunger||{cur:80,max:100};\n'
    '  var md=(cr.mood||\'neutral\').toLowerCase();\n'
    '  var moodMap={\n'
    '    ecstatic:{ico:\'🎉\',fill:100,col:\'#60d890\'},\n'
    '    great:{ico:\'🎉\',fill:100,col:\'#60d890\'},\n'
    '    happy:{ico:\'😊\',fill:78,col:\'#60c8a8\'},\n'
    '    good:{ico:\'😊\',fill:78,col:\'#60c8a8\'},\n'
    '    neutral:{ico:\'😐\',fill:55,col:\'#9090a0\'},\n'
    '    irritated:{ico:\'😤\',fill:30,col:\'#d4a040\'},\n'
    '    bad:{ico:\'😡\',fill:12,col:\'#d86050\'},\n'
    '    angry:{ico:\'😡\',fill:12,col:\'#d86050\'},\n'
    '    hungry:{ico:\'🍗\',fill:8,col:\'#d87840\'}\n'
    '  };\n'
    '  var mo=moodMap[md]||moodMap.neutral;\n'
    '  var moodLbl={ecstatic:T(\'moodGr\'),great:T(\'moodGr\'),happy:T(\'moodGo\'),good:T(\'moodGo\'),neutral:T(\'moodNe\'),irritated:T(\'moodIr\'),bad:T(\'moodBa\'),angry:T(\'moodBa\'),hungry:T(\'moodBa\')}[md]||T(\'moodNe\');\n'
    '  var hgP=Math.max(0,Math.min(100,Math.round((parseFloat(hg.cur)||80)/(parseFloat(hg.max)||100)*100)));\n'
    '  var moodPct=mo.fill;\n'
    '\n'
    '  var infoRows=[[T(\'crowNm\'),nm],[T(\'crowBr\'),breed],[T(\'crowPs\'),ps],[T(\'crowAp\'),ap],[T(\'crowOt\'),ot]];\n'
    '  var infoH=\'<div class="igrid">\';\n'
    '  infoRows.forEach(function(r,i){\n'
    '    infoH+=\'<div class="icard\'+(i>=2?\' full\':\'\')+\'"><div class="icard-l">\'+esc(r[0])+\'</div><div class="icard-v">\'+esc(r[1])+\'</div></div>\';\n'
    '  });\n'
    '  infoH+=\'</div>\';\n'
    '\n'
    '  return \'<div class="crow-portrait"><div class="crow-face">\'+mo.ico+\'</div><div class="crow-mood-nm">\'+esc(moodLbl)+\'</div></div>\'+\n'
    '    \'<div class="kny-sec">\'+T(\'crow\')+\'</div>\'+\n'
    '    infoH+\n'
    '    \'<div class="kny-sec mt">\'+T(\'crowHg\')+\' · \'+T(\'crowMd\')+\'</div>\'+\n'
    '    \'<div class="bars">\'+\n'
    '      \'<div class="crow-hbar-row"><div class="crow-hbar-lbl">\'+T(\'crowHg\')+\'</div><div class="crow-hbar-track"><div class="crow-hbar-fill crow-hng-fill" style="width:\'+hgP+\'%"></div></div><div class="crow-hbar-val">\'+esc(hg.cur)+\'/\'+esc(hg.max)+\'</div></div>\'+\n'
    '      \'<div class="crow-hbar-row"><div class="crow-hbar-lbl">\'+T(\'crowMd\')+\'</div><div class="crow-hbar-track"><div class="crow-hbar-fill crow-moo-fill" style="width:\'+moodPct+\'%"></div></div><div class="crow-hbar-val" style="color:\'+mo.col+\'">\'+esc(moodLbl)+\'</div></div>\'+\n'
    '    \'</div>\';\n'
    '}\n\n'
)
rs = rs.replace('// ── BUILD', CROW_FN + '// ── BUILD', 1)

# ── 7. Add crow tab in build() defs ───────────────────────────────────────────
OLD_DEFS_END = "    ['fame',TH?'ชื่อเสียง':'FAME',pFame]\n  ];\n  var tabsH=''"
NEW_DEFS_END = "    ['fame',TH?'ชื่อเสียง':'FAME',pFame],\n    ['crow',TH?'อีกา':'CROW',pCrow]\n  ];\n  var tabsH=''"
rs = rs.replace(OLD_DEFS_END, NEW_DEFS_END, 1)

# ── 8. Fix pTree return: cardsH was renamed to miniH but return wasn't patched ─
rs = rs.replace(
    "  return spH+\n    '<div class=\"tct-row\">'+filtersH+'</div>'+\n    (cardsH||'<div class=\"empty-state\">'+T('noskill')+'</div>');\n}\n\n",
    "  return spH+\n    '<div class=\"tct-row\">'+filtersH+'</div>'+\n    (miniH?'<div class=\"skill-grid\">'+miniH+'</div>':'<div class=\"empty-state\">'+T('noskill')+'</div>');\n}\n\n",
    1
)

# ── 9. Fix event handler selector for compact skill buttons ───────────────────
rs = rs.replace(
    "closest('.skill-btn[data-sk]');",
    "closest('.skill-btn[data-sk],.skill-mini-btn[data-sk]');"
)

# ── Write regex JSON ──────────────────────────────────────────────────────────
data['replaceString'] = rs
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"{OUT} — {size:,} bytes ({size/1024:.1f} KB)")

# ── Lorebook: addon trigger ───────────────────────────────────────────────────
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

def entry(uid, comment, content, order, key=None):
    e = {"uid": uid, "key": key or [], "keysecondary": [],
         "comment": comment, "content": content,
         "constant": True, "order": order, "displayIndex": uid}
    e.update(BOILERPLATE)
    return e

E0 = """\
## KNY STATUS TRACKER — ADDON FIELDS

These fields extend the base <KNY_STATUS> JSON. Include them in EVERY status block.

### SITUATION (situation)
A short sentence describing what is currently happening in the scene.
Update this every response to reflect the current moment.
Examples:
  "Walking through the rain-soaked streets of Asakusa after the mission."
  "Recovering at the Butterfly Estate. Shinobu is treating the left arm wound."
  "Mid-battle — Akaza has activated Destructive Death. Third form incoming."

```json
"situation": "Walking through the rain-soaked streets of Asakusa after the mission."
```

### KASUGAI CROW (crow)
Track your crow companion's status. Update mood and hunger when relevant events occur.

Fields:
- name       : crow's given name (e.g. "Matsu")
- breed      : species (default: "Jungle Crow"; Chuntaro = "Java Sparrow")
- personality: brief temperament ("Bossy and loud", "Shy, easily startled")
- appearance : markings, size, eye color, distinguishing features
- outfit     : any accessory or Corps-issued tag worn
- hunger     : {cur, max} — decreases when not fed; 100 = full
- mood       : "ecstatic" | "happy" | "good" | "neutral" | "irritated" | "bad" | "angry" | "hungry"

Mood change triggers:
  hungry → when hunger.cur < 20
  irritated → when injured mid-battle and crow is present
  ecstatic → when fed a favorite food or mission succeeds
  bad/angry → when crow is mistreated or ignored for too long

```json
"crow": {
  "name": "Matsu",
  "breed": "Jungle Crow",
  "personality": "Arrogant and loud, but fiercely loyal.",
  "appearance": "Large, glossy black feathers; slightly bent left talon.",
  "outfit": "Demon Slayer Corps tag around neck.",
  "hunger": {"cur": 75, "max": 100},
  "mood": "neutral"
}
```

### RULE
Both `situation` and `crow` are required in every <KNY_STATUS> block. If the crow is absent from the scene, still include the crow object with its last known state.\
"""

lorebook = {
    "name": "KNY Status Tracker — Addon Fields",
    "entries": {
        "0": entry(0, "KNY Status Tracker — Addon Fields (Situation + Crow)", E0, 90)
    }
}

with open(OUT_LB, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{OUT_LB} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
