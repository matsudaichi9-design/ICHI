import json

FONTS = (
    '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700'
    '&family=Shippori+Mincho:wght@500;600&family=Noto+Serif+JP:wght@500;700'
    '&family=Noto+Serif+Thai:wght@500;600&display=swap" rel="stylesheet"/>'
)

CSS = """\
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:transparent;font-family:'Shippori Mincho','Noto Serif JP','Noto Serif Thai','Times New Roman',serif;font-size:13px}
@keyframes kmIn{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}
#kmwin{
  background:linear-gradient(160deg,#0d0a05,#090703,#0d0b06);
  border:1px solid rgba(196,168,48,.22);border-radius:8px;
  max-width:500px;margin:0 auto;overflow:hidden;position:relative;
  box-shadow:0 8px 40px rgba(0,0,0,.85),0 0 0 1px rgba(0,0,0,.4),inset 0 1px 0 rgba(196,168,48,.06);
  color:#e4d8c0;animation:kmIn .4s ease both;
}
/* HEAD */
#kmhead{
  display:flex;align-items:center;gap:12px;padding:11px 14px;
  background:linear-gradient(160deg,#130f04,#0d0b02,#120e04);
  border-bottom:1px solid rgba(196,168,48,.18);position:relative;overflow:hidden;
}
#kmhead::after{content:'';position:absolute;bottom:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(196,168,48,.45),transparent)}
#kmcrow{
  flex-shrink:0;font-family:'Noto Serif JP',serif;font-size:26px;font-weight:900;
  color:#C4A830;text-shadow:0 0 14px rgba(196,168,48,.6);line-height:1;
  filter:drop-shadow(0 0 6px rgba(196,168,48,.35));
}
#kmwm{
  position:absolute;right:54px;top:50%;transform:translateY(-50%);
  font-family:'Noto Serif JP',serif;font-size:54px;font-weight:900;
  color:rgba(196,168,48,.05);line-height:1;pointer-events:none;user-select:none;
}
#kmhdtxt{flex:1;min-width:0}
#kmsub{font-family:'Shippori Mincho','Noto Serif JP',serif;font-size:7.5px;letter-spacing:3px;color:rgba(196,168,48,.6);text-transform:uppercase;margin-bottom:3px}
#kmttl{font-family:'Cinzel','Times New Roman',serif;font-size:14.5px;font-weight:700;color:#f0e8d4;letter-spacing:.4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#kmdiff{
  flex-shrink:0;width:36px;height:36px;border-radius:5px;
  display:flex;align-items:center;justify-content:center;
  font-family:'Cinzel',serif;font-size:17px;font-weight:700;
}
/* STATUS BAR */
#kmstatbar{
  display:flex;border-bottom:1px solid rgba(255,255,255,.04);
  background:#080604;font-size:8px;font-family:'Shippori Mincho','Noto Serif JP',serif;
  letter-spacing:1.2px;text-transform:uppercase;
}
.km-chip{flex:1;padding:6px 8px;display:flex;align-items:center;justify-content:center;gap:5px;border-right:1px solid rgba(255,255,255,.04)}
.km-chip:last-child{border-right:none}
/* BODY */
#kmbody{padding:12px 14px}
/* SECTION HEADER */
.km-sec{margin-bottom:12px}
.km-sec:last-child{margin-bottom:0}
.km-lbl{
  font-family:'Shippori Mincho','Noto Serif JP',serif;font-size:7.5px;letter-spacing:3px;
  text-transform:uppercase;color:rgba(196,168,48,.65);
  display:flex;align-items:center;gap:7px;margin-bottom:7px;
}
.km-lbl::before,.km-lbl::after{content:'';height:1px;flex:1}
.km-lbl::before{background:linear-gradient(90deg,transparent,rgba(196,168,48,.22))}
.km-lbl::after{background:linear-gradient(90deg,rgba(196,168,48,.22),transparent)}
.km-lbl.warn{color:rgba(220,130,40,.8)}
.km-lbl.warn::before{background:linear-gradient(90deg,transparent,rgba(220,130,40,.22))}
.km-lbl.warn::after{background:linear-gradient(90deg,rgba(220,130,40,.22),transparent)}
/* LOCATION & TARGET */
.km-box{font-size:12px;color:#c8bc98;line-height:1.6;padding:7px 10px;
  background:rgba(255,255,255,.03);border-radius:4px;border-left:2px solid rgba(196,168,48,.35)}
/* OBJECTIVES */
.km-objs{display:flex;flex-direction:column;gap:5px}
.km-obj{display:flex;align-items:flex-start;gap:8px;padding:6px 9px;
  background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.04);
  border-radius:4px;transition:background .15s}
.km-obj.req{border-color:rgba(196,168,48,.12)}
.km-obj.done{opacity:.5}
.km-obj-ico{font-size:11px;flex-shrink:0;margin-top:2px}
.km-obj.req .km-obj-ico{color:rgba(196,168,48,.8)}
.km-obj.opt .km-obj-ico{color:rgba(160,148,100,.45)}
.km-obj.done .km-obj-ico{color:#58c878}
.km-obj-txt{flex:1;font-size:11.5px;color:#c4b890;line-height:1.5}
.km-obj.done .km-obj-txt{text-decoration:line-through;color:#6a6050}
.km-tag{font-size:7px;letter-spacing:.8px;padding:1px 6px;border-radius:99px;flex-shrink:0;margin-top:3px;font-family:'Shippori Mincho',serif}
.km-tag.req{color:rgba(196,168,48,.85);border:1px solid rgba(196,168,48,.28);background:rgba(196,168,48,.07)}
.km-tag.opt{color:rgba(150,138,100,.6);border:1px solid rgba(150,138,100,.18)}
/* REWARDS */
.km-rws{display:grid;grid-template-columns:1fr 1fr;gap:5px}
.km-rw{display:flex;align-items:flex-start;gap:7px;padding:7px 9px;
  background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.05);border-radius:4px}
.km-rw-ico{font-size:13px;flex-shrink:0;line-height:1.4}
.km-rw-body{flex:1;min-width:0}
.km-rw-lbl{font-size:7.5px;letter-spacing:.5px;text-transform:uppercase;color:rgba(196,168,48,.5);font-family:'Shippori Mincho',serif;margin-bottom:2px}
.km-rw-val{font-size:11px;color:#d4c8a8;font-weight:600;line-height:1.4;word-break:break-word}
.pos{color:#62d890}
.neg{color:#e06868}
/* CONSTRAINTS */
.km-cons{display:flex;flex-direction:column;gap:5px}
.km-con{display:flex;align-items:flex-start;gap:8px;padding:6px 9px;
  background:rgba(220,130,40,.05);border:1px solid rgba(220,130,40,.16);border-radius:4px}
.km-con-ico{color:rgba(220,130,40,.75);font-size:10px;flex-shrink:0;margin-top:2px}
.km-con-txt{font-size:11px;color:#c8a870;line-height:1.5}
/* FOOTER */
#kmfoot{border-top:1px solid rgba(255,255,255,.04);padding:6px 14px;
  font-family:'Shippori Mincho','Noto Serif JP',serif;font-size:7.5px;
  color:rgba(196,168,48,.38);text-align:center;letter-spacing:2.5px;
  text-transform:uppercase;background:#080604;position:relative}
#kmfoot::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(196,168,48,.18),transparent)}\
"""

JS = """\
(function(){
function g(id){return document.getElementById(id)}
function esc(v){if(v==null)return'';return String(v).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function hexRgb(h){var s=String(h||'').replace('#','');if(s.length===3)s=s[0]+s[0]+s[1]+s[1]+s[2]+s[2];var n=parseInt(s,16)||0xC4A830;return((n>>16)&255)+','+((n>>8)&255)+','+(n&255)}
function fmtNum(n){return Number(n).toLocaleString()}

var rawEl=g('kmraw');var d={};
try{if(rawEl&&rawEl.value.trim()){var dec=document.createElement('textarea');dec.innerHTML=rawEl.value.trim();d=JSON.parse(dec.value.trim())}}catch(e){}

var TH=(d.lang==='th');

// ── Difficulty ────────────────────────────────────────────────────────────────
var diffCol={S:'#FFD700',A:'#d870c8',B:'#5088d8',C:'#50b870',D:'#808080'};
var diff=(d.difficulty||'B').toUpperCase();
var col=diffCol[diff]||'#9a9080';
var rgb=hexRgb(col);
var diffEl=g('kmdiff');
if(diffEl){
  diffEl.textContent=diff;
  diffEl.style.color=col;
  diffEl.style.background='rgba('+rgb+',.1)';
  diffEl.style.border='1.5px solid rgba('+rgb+',.5)';
  diffEl.style.boxShadow='0 0 12px rgba('+rgb+',.2),inset 0 0 8px rgba('+rgb+',.06)';
}

// ── Title ─────────────────────────────────────────────────────────────────────
var ttl=g('kmttl');if(ttl)ttl.textContent=d.title||'—';

// ── Status bar ────────────────────────────────────────────────────────────────
var status=(d.status||'active').toLowerCase();
var stCfg={
  active:{lbl:TH?'▶ กำลังดำเนิน':'▶ ACTIVE',col:'#5088d8'},
  complete:{lbl:TH?'✓ สำเร็จ':'✓ COMPLETE',col:'#50c878'},
  failed:{lbl:TH?'✗ ล้มเหลว':'✗ FAILED',col:'#e06868'}
};
var sc=stCfg[status]||stCfg.active;
var stEl=g('kmst');if(stEl){stEl.textContent=sc.lbl;stEl.style.color=sc.col}

var typeMap={
  elimination:TH?'ปราบปราม':'Elimination',protection:TH?'คุ้มครอง':'Protection',
  investigation:TH?'สืบสวน':'Investigation',escort:TH?'คุ้มกัน':'Escort',
  retrieval:TH?'ค้นหา':'Retrieval',custom:TH?'ภารกิจพิเศษ':'Special'
};
var mtype=(d.type||'elimination').toLowerCase();
var tyEl=g('kmty');if(tyEl)tyEl.textContent=typeMap[mtype]||esc(d.type||'—');

var dlEl=g('kmdl');
if(dlEl)dlEl.textContent=d.deadline?(TH?'⏱ '+d.deadline:'⏱ '+d.deadline):(TH?'— ไม่จำกัดเวลา':'— No time limit');

// ── Body ──────────────────────────────────────────────────────────────────────
var body=g('kmbody');if(!body)return;
var h='';

// Location
if(d.location){
  h+='<div class="km-sec"><div class="km-lbl">📍 '+(TH?'สถานที่':'LOCATION')+'</div>'+
    '<div class="km-box">'+esc(d.location)+'</div></div>';
}

// Target
if(d.target){
  h+='<div class="km-sec"><div class="km-lbl">🎯 '+(TH?'เป้าหมาย':'TARGET')+'</div>'+
    '<div class="km-box">'+esc(d.target)+'</div></div>';
}

// Objectives
if(d.objectives&&d.objectives.length){
  h+='<div class="km-sec"><div class="km-lbl">◈ '+(TH?'วัตถุประสงค์':'OBJECTIVES')+'</div><div class="km-objs">';
  d.objectives.forEach(function(o){
    var req=o.required!==false;var done=o.done===true;
    var cls='km-obj'+(req?' req':' opt')+(done?' done':'');
    var ico=done?'✓':req?'◉':'◎';
    h+='<div class="'+cls+'">'+
      '<div class="km-obj-ico">'+ico+'</div>'+
      '<div class="km-obj-txt">'+esc(typeof o==='string'?o:o.text||'')+'</div>'+
      '<div class="km-tag '+(req?'req':'opt')+'">'+(req?(TH?'จำเป็น':'REQ'):(TH?'ตัวเลือก':'OPT'))+'</div>'+
    '</div>';
  });
  h+='</div></div>';
}

// Rewards
var rw=d.rewards||{};var cards=[];
if(rw.money)cards.push({ico:'💰',lbl:TH?'เงิน':'MONEY',val:fmtNum(rw.money)+' ryō',cls:''});
(rw.items||[]).forEach(function(it){
  var nm=typeof it==='string'?it:(it.name+(it.qty&&it.qty>1?' ×'+it.qty:''));
  cards.push({ico:'🎁',lbl:TH?'ของรางวัล':'ITEM',val:nm,cls:''});
});
(rw.fame||[]).forEach(function(f){
  var ch=f.change||f.value||0;
  cards.push({ico:'📍',lbl:TH?'ชื่อเสียง':'FAME',val:(ch>=0?'+':'')+ch+' '+esc(f.location||''),cls:ch>=0?'pos':'neg'});
});
(rw.relationship||[]).forEach(function(r){
  var ch=r.change||0;
  cards.push({ico:'🤝',lbl:TH?'ความสัมพันธ์':'RELATION',val:(ch>=0?'+':'')+ch+' '+esc(r.name||''),cls:ch>=0?'pos':'neg'});
});
(rw.other||[]).forEach(function(o){
  cards.push({ico:'⭐',lbl:TH?'อื่นๆ':'OTHER',val:esc(typeof o==='string'?o:(o.desc||o.name||'')),cls:''});
});
if(cards.length){
  h+='<div class="km-sec"><div class="km-lbl">✦ '+(TH?'รางวัล':'REWARDS')+'</div><div class="km-rws">';
  cards.forEach(function(c){
    h+='<div class="km-rw"><div class="km-rw-ico">'+c.ico+'</div><div class="km-rw-body">'+
      '<div class="km-rw-lbl">'+esc(c.lbl)+'</div>'+
      '<div class="km-rw-val '+c.cls+'">'+c.val+'</div>'+
    '</div></div>';
  });
  h+='</div></div>';
}

// Constraints
if(d.constraints&&d.constraints.length){
  h+='<div class="km-sec"><div class="km-lbl warn">⚠ '+(TH?'ข้อกำหนด':'CONSTRAINTS')+'</div><div class="km-cons">';
  d.constraints.forEach(function(c){
    h+='<div class="km-con"><div class="km-con-ico">▸</div>'+
      '<div class="km-con-txt">'+esc(typeof c==='string'?c:(c.text||c))+'</div></div>';
  });
  h+='</div></div>';
}

body.innerHTML=h;

// Footer
var ft=g('kmfoot');
if(ft)ft.textContent=TH?'鬼滅の刃 · ระบบภารกิจ · 任務命令':'鬼滅の刃 · MISSION SYSTEM · 任務命令';
})();\
"""

HTML = (
    '```\n'
    '<!DOCTYPE html>\n'
    '<html lang="ja">\n'
    '<head>\n'
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
    + FONTS + '\n'
    '<style>\n' + CSS + '\n'
    '</style>\n'
    '</head>\n'
    '<body>\n'
    '<textarea id="kmraw" style="display:none;position:absolute;left:-9999px">$1</textarea>\n'
    '<div id="kmwin">\n'
    '  <div id="kmhead">\n'
    '    <div id="kmcrow">鴉</div>\n'
    '    <div id="kmwm">任務</div>\n'
    '    <div id="kmhdtxt">\n'
    '      <div id="kmsub">鬼殺隊 · 任務命令</div>\n'
    '      <div id="kmttl">—</div>\n'
    '    </div>\n'
    '    <div id="kmdiff">B</div>\n'
    '  </div>\n'
    '  <div id="kmstatbar">\n'
    '    <div class="km-chip" id="kmst">▶ ACTIVE</div>\n'
    '    <div class="km-chip" id="kmty">Elimination</div>\n'
    '    <div class="km-chip" id="kmdl">—</div>\n'
    '  </div>\n'
    '  <div id="kmbody"></div>\n'
    '  <div id="kmfoot">鬼滅の刃 · MISSION SYSTEM · 任務命令</div>\n'
    '</div>\n'
    '<script>\n' + JS + '\n'
    '</script>\n'
    '</body>\n'
    '</html>\n'
    '```'
)

# ── Regex JSON ────────────────────────────────────────────────────────────────

regex_data = {
    "id": "kny-mission-log",
    "scriptName": "KNY Mission Log",
    "findRegex": r"/<KNY_MISSION>([\s\S]*?)<\/KNY_MISSION>/gm",
    "replaceString": HTML,
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

# ── Lorebook ──────────────────────────────────────────────────────────────────

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
## KNY MISSION SYSTEM

When {{user}}'s Kasugai Crow delivers a mission — whether from the Wisteria House, the Corps Master, or a civilian employer — output a mission block BEFORE the narrative, on its own line:

<KNY_MISSION>
{JSON}
</KNY_MISSION>

---

### MISSION JSON SCHEMA

```json
{
  "lang": "en",
  "title": "Hunt: The Silk Road Demon",
  "type": "Elimination",
  "difficulty": "B",
  "status": "active",
  "location": "Kōfu, Yamanashi — Silk Merchant District",
  "target": "Unnamed demon preying on traveling merchants along the old Silk Road.",
  "deadline": "3 days",
  "objectives": [
    {"text": "Eliminate the demon", "required": true, "done": false},
    {"text": "Protect merchant Goro and his cargo", "required": true, "done": false},
    {"text": "Retrieve stolen goods (bonus)", "required": false, "done": false}
  ],
  "rewards": {
    "money": 3000,
    "items": [
      {"name": "Wisteria Extract", "qty": 2}
    ],
    "fame": [
      {"location": "Kōfu", "change": 20}
    ],
    "relationship": [
      {"name": "Merchant Goro", "change": 15, "note": "For protecting his cargo"}
    ],
    "other": []
  },
  "constraints": [
    "No civilian casualties",
    "Protect merchant Goro at all costs"
  ]
}
```

---

### FIELD REFERENCE

| Field | Values / Notes |
|---|---|
| `lang` | "en" or "th" — match player preference |
| `type` | "Elimination" \| "Protection" \| "Investigation" \| "Escort" \| "Retrieval" \| "Custom" |
| `difficulty` | "S" \| "A" \| "B" \| "C" \| "D" |
| `status` | "active" \| "complete" \| "failed" |
| `deadline` | string e.g. "3 days", "Before dawn", or null if none |
| `objectives[].required` | true = primary (must complete); false = optional bonus |
| `objectives[].done` | true when the objective has been fulfilled |
| `rewards.money` | amount in ryō (integer) |
| `rewards.fame[].change` | positive = fame gain, negative = infamy |
| `rewards.relationship[].change` | positive or negative relationship points |
| `constraints` | list of restrictions: no-kill, must-protect, time-limit, etc. |

---

### RULES

**When to output the block**
• Crow delivers a new mission → output `<KNY_MISSION>` with `"status": "active"`.
• An objective is completed mid-scene → re-output the block with `done: true` on that objective.
• Mission ends (success or failure) → re-output with `"status": "complete"` or `"status": "failed"`.

**Difficulty guidelines**
• S — Demon Blood Art user, Upper Moon level threat or protecting many lives at once.
• A — Named demon, highly dangerous target, multiple threats.
• B — Mid-tier demon with some ability, moderate stakes.
• C — Weakened demon, straightforward hunt.
• D — Newly manifested demon, no confirmed ability, minimal risk.

**Rewards**
• Money comes from the Wisteria House standard rate or employer offer.
• Items are named specifically — no vague "medicine" entries.
• Fame change must name the specific location.
• Relationship rewards apply only when the mission is given by or involves a named character.
• Constraints apply only when the mission brief explicitly states restrictions; do not invent them.\
"""

lorebook = {
    "name": "KNY Mission Log",
    "entries": {
        "0": entry(0, "KNY Mission Log System", E0, 85)
    }
}

# ── Write ─────────────────────────────────────────────────────────────────────

for obj, fname, ind in [
    (regex_data, "regex_kny_mission.json",   4),
    (lorebook,   "kny_mission_lorebook.json", 2),
]:
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=ind)
    size = len(json.dumps(obj, ensure_ascii=False, indent=ind).encode("utf-8"))
    print(f"{fname} — {size:,} bytes ({size/1024:.1f} KB)")

print("Done!")
