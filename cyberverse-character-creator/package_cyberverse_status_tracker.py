import json

OUT = 'regex_cyberverse_status_tracker.json'
OUT_LB = 'cyberverse_status_lorebook.json'

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:transparent;font-family:'Rajdhani',system-ui,sans-serif;font-size:13px}
#cvwin{
  --acc:#00F0FF;--acc-rgb:0,240,255;--abg:rgba(0,240,255,.10);--abd:rgba(0,240,255,.28);
  --bg:#05060a;--bg2:#0a0c16;--bg3:#10131e;--bg4:#181c2a;--bg5:#222840;
  --tx:#dff6ff;--tx2:#8a96ac;--tx3:#4a5468;
  --bd:rgba(0,240,255,.25);--r:8px;--r2:4px;
  --fh:'Orbitron',sans-serif;--fm:'Share Tech Mono',monospace;
  background:linear-gradient(165deg,#0a0c16 0%,#05060a 100%);
  border:1px solid var(--bd);border-radius:var(--r);
  max-width:400px;margin:10px auto 8px;overflow:hidden;position:relative;
  box-shadow:0 8px 40px rgba(0,0,0,.85),0 0 28px rgba(var(--acc-rgb),.08),inset 0 1px 0 rgba(255,255,255,.04);
  color:var(--tx)
}
#cvwin::before{content:'';position:absolute;inset:0;pointer-events:none;z-index:6;opacity:.035;
  background:repeating-linear-gradient(0deg,#fff 0 1px,transparent 1px 3px)}
.cv-corner{position:absolute;width:11px;height:11px;z-index:7;pointer-events:none;opacity:.7}
.cv-corner-tl{top:0;left:0;border-top:1.5px solid var(--acc);border-left:1.5px solid var(--acc)}
.cv-corner-tr{top:0;right:0;border-top:1.5px solid var(--acc);border-right:1.5px solid var(--acc)}
/* HEAD */
#cvhead{position:relative;display:flex;align-items:center;gap:9px;padding:9px 12px;
  background:linear-gradient(160deg,#0c0f1c 0%,#080a12 60%);
  border-bottom:1px solid var(--bd);cursor:pointer;user-select:none}
#cvhead::after{content:'';position:absolute;bottom:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--acc),transparent);opacity:.4}
#cvsigil{width:30px;height:30px;flex-shrink:0;filter:drop-shadow(0 0 6px var(--acc))}
#cvhdtxt{flex:1;min-width:0}
#cvtitle{font-family:var(--fm);font-size:7px;letter-spacing:2.5px;text-transform:uppercase;color:var(--acc);opacity:.7;margin-bottom:2px}
#cvnm{font-family:var(--fh);font-size:13.5px;font-weight:700;color:#eafcff;letter-spacing:.5px;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-shadow:0 0 12px rgba(var(--acc-rgb),.5)}
#cvhandle{font-family:var(--fm);font-size:9px;color:#ff5fa8;letter-spacing:.5px;margin-top:1px;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#cvhdvit{display:flex;flex-direction:column;gap:3px;min-width:96px;flex-shrink:0}
.cv-hbar-row{display:flex;align-items:center;gap:4px}
.cv-hbar-lbl{font-size:6.5px;font-family:var(--fm);color:var(--tx3);width:20px;text-align:right;flex-shrink:0}
.cv-hbar-track{flex:1;height:4px;background:rgba(255,255,255,.06);border-radius:2px;overflow:hidden}
.cv-hbar-fill{height:100%;border-radius:2px}
.cv-hbar-hp{background:linear-gradient(90deg,#a8204a,#ff3b6e);box-shadow:0 0 5px rgba(255,60,110,.5)}
.cv-hbar-st{background:linear-gradient(90deg,#0a8aa0,#00f0ff);box-shadow:0 0 5px rgba(0,220,255,.5)}
.cv-hbar-val{font-size:6.5px;font-family:var(--fm);color:var(--tx3);min-width:32px;text-align:right;flex-shrink:0}
#cvlnbtn{font-family:var(--fm);font-size:7px;padding:3px 7px;border-radius:3px;cursor:pointer;
  background:rgba(255,255,255,.04);border:1px solid var(--bd);color:var(--tx3);letter-spacing:1.5px;
  user-select:none;flex-shrink:0;transition:all .2s}
#cvlnbtn:hover{color:var(--acc);border-color:var(--acc)}
#cvchev{font-size:12px;color:var(--tx3);transition:transform .3s;flex-shrink:0}
#cvwin.closed #cvchev{transform:rotate(180deg)}
/* BODY */
#cvbody{max-height:2200px;overflow:hidden;transition:max-height .4s ease}
#cvwin.closed #cvbody{max-height:0}
/* TABS */
#cvtabs{display:flex;background:var(--bg2);border-bottom:1px solid rgba(255,255,255,.05);overflow-x:auto;scrollbar-width:none}
#cvtabs::-webkit-scrollbar{display:none}
.cv-tab{flex:1;padding:8px 2px;text-align:center;font-family:var(--fm);font-size:7px;letter-spacing:.8px;
  text-transform:uppercase;color:var(--tx3);cursor:pointer;border-bottom:2px solid transparent;
  transition:all .2s;white-space:nowrap}
.cv-tab:hover{color:var(--tx2);background:rgba(255,255,255,.02)}
.cv-tab.active{color:var(--acc);border-bottom-color:var(--acc);background:linear-gradient(180deg,transparent,var(--abg));
  text-shadow:0 0 8px rgba(var(--acc-rgb),.6)}
/* PANELS */
.cv-panel{display:none;padding:10px 12px}
.cv-panel.active{display:block}
#cvwin ::-webkit-scrollbar{width:4px}
#cvwin ::-webkit-scrollbar-thumb{background:var(--bd);border-radius:2px}
/* SECTION HEADER */
.cv-sec{display:flex;align-items:center;gap:7px;margin-bottom:9px;margin-top:3px;font-family:var(--fm);
  font-size:7.5px;letter-spacing:2.5px;text-transform:uppercase;color:var(--acc)}
.cv-sec::before,.cv-sec::after{content:'';flex:1;height:1px}
.cv-sec::before{background:linear-gradient(90deg,transparent,var(--abd))}
.cv-sec::after{background:linear-gradient(90deg,var(--abd),transparent)}
.cv-sec.mt{margin-top:14px}
/* INFO GRID */
.cv-igrid{display:grid;grid-template-columns:1fr 1fr;gap:5px;margin-bottom:12px}
.cv-icard{background:var(--bg3);border:1px solid var(--bg4);border-radius:var(--r2);padding:6px 9px;
  border-left:2px solid var(--abd);transition:border-left-color .2s}
.cv-icard:hover{border-left-color:var(--acc)}
.cv-icard.full{grid-column:1/-1}
.cv-icard-l{font-family:var(--fm);font-size:7px;letter-spacing:1px;text-transform:uppercase;color:var(--tx3);margin-bottom:2px}
.cv-icard-v{font-size:11.5px;color:var(--tx);font-weight:600}
/* SITUATION */
.cv-sit-card{background:var(--bg3);border:1px solid var(--abd);border-left:3px solid var(--acc);
  border-radius:var(--r2);padding:8px 11px;margin-bottom:12px}
.cv-sit-txt{font-size:11px;color:var(--tx2);line-height:1.6;font-style:italic}
/* VITAL BARS */
.cv-bars{margin-bottom:12px}
.cv-bar-row{display:flex;align-items:center;gap:8px;margin-bottom:7px}
.cv-bar-lbl{font-family:var(--fm);font-size:7.5px;letter-spacing:.5px;color:var(--tx3);width:32px;text-align:right;flex-shrink:0}
.cv-bar-wrap{flex:1;display:flex;flex-direction:column;gap:3px}
.cv-bar-track{height:8px;background:rgba(255,255,255,.05);border-radius:4px;overflow:hidden;position:relative}
.cv-bar-fill{height:100%;border-radius:4px;transition:width .6s}
.cv-bar-hp{background:linear-gradient(90deg,#a8204a,#ff3b6e,#ff7fa8);box-shadow:0 0 7px rgba(255,60,110,.5)}
.cv-bar-st{background:linear-gradient(90deg,#0a6a80,#00c0e0,#5fe8ff);box-shadow:0 0 7px rgba(0,200,255,.45)}
.cv-bar-nums{display:flex;justify-content:flex-end}
.cv-bar-val{font-family:var(--fm);font-size:9px;color:var(--tx2);font-weight:600}
/* BADGES */
.cv-badges{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:11px}
.cv-badge{padding:3px 9px;border-radius:3px;font-size:10px;background:var(--bg4);border:1px solid var(--bg5);color:var(--tx2)}
.cv-badge.cond{border-color:rgba(255,182,39,.45);color:#ffb627;background:rgba(255,182,39,.08)}
.cv-badge.inj{border-color:rgba(255,80,80,.45);color:#ff5050;background:rgba(255,80,80,.08)}
.cv-badge.none{color:var(--tx3);font-style:italic;border-color:transparent;background:transparent}
/* CYBERWARE */
.cv-ware-group{margin-bottom:12px}
.cv-ware-lbl{font-family:var(--fm);font-size:7px;letter-spacing:2px;text-transform:uppercase;color:var(--acc);
  padding:3px 0;border-bottom:1px solid var(--abd);margin-bottom:7px;opacity:.85}
.cv-ware-card{background:var(--bg3);border:1px solid var(--bg4);border-left:2px solid var(--bg5);
  border-radius:var(--r2);padding:9px 10px;margin-bottom:6px;transition:border-color .2s}
.cv-ware-top{display:flex;align-items:flex-start;gap:8px;margin-bottom:5px}
.cv-ware-ico{width:24px;height:24px;border-radius:4px;background:var(--bg4);border:1px solid var(--bg5);
  display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.cv-ware-meta{flex:1;min-width:0}
.cv-ware-nm{font-size:11.5px;font-weight:700;color:var(--tx);margin-bottom:2px}
.cv-ware-mf{font-family:var(--fm);font-size:8px;color:var(--tx3)}
.cv-ware-tags{display:flex;gap:5px;flex-wrap:wrap;flex-shrink:0;align-items:flex-start}
.cv-tag{font-family:var(--fm);font-size:7px;padding:2px 6px;border-radius:3px;font-weight:700;letter-spacing:.5px;
  white-space:nowrap;border:1px solid currentColor}
.cv-ware-fx{font-size:10.5px;color:var(--tx2);line-height:1.5;margin-bottom:6px}
.cv-ware-foot{display:flex;align-items:center;justify-content:space-between;gap:8px}
.cv-ware-hc{font-family:var(--fm);font-size:8px;color:var(--tx3)}
.cv-ware-hc .v{color:#ff5fa8;font-weight:700}
/* CYBERPSYCHOSIS STRIP */
#cvpsy{position:relative;padding:9px 12px;background:var(--bg2);border-top:1px solid rgba(255,255,255,.05);
  border-bottom:1px solid rgba(255,255,255,.05)}
.cv-psy-row{display:flex;align-items:center;gap:9px;margin-bottom:6px}
.cv-psy-lbl{font-family:var(--fm);font-size:7px;letter-spacing:2px;text-transform:uppercase;color:var(--tx3);flex-shrink:0}
.cv-psy-state{font-family:var(--fh);font-size:9px;font-weight:700;letter-spacing:1.5px;flex:1;text-align:right}
.cv-psy-track{height:6px;background:rgba(255,255,255,.05);border-radius:4px;overflow:hidden;margin-bottom:6px}
.cv-psy-fill{height:100%;border-radius:4px;transition:width .6s}
.cv-psy-meta{display:flex;align-items:center;justify-content:space-between;font-family:var(--fm);font-size:8px;color:var(--tx3)}
.cv-psy-symptoms{display:flex;flex-wrap:wrap;gap:4px;margin-top:7px}
.cv-psy-sym{font-size:9px;padding:2px 7px;border-radius:3px;background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.08);color:var(--tx2)}
@keyframes cvGlitch{0%,100%{transform:translate(0,0)}20%{transform:translate(-1px,1px)}
  40%{transform:translate(1px,-1px)}60%{transform:translate(-1px,-1px)}80%{transform:translate(1px,1px)}}
.cv-glitch{animation:cvGlitch .25s infinite}
@keyframes cvPulse{0%,100%{opacity:1}50%{opacity:.45}}
.cv-pulse{animation:cvPulse 1.1s ease-in-out infinite}
/* ACCOUNT */
.cv-bal-row{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:12px}
.cv-bal-card{background:var(--bg3);border:1px solid var(--bg4);border-radius:var(--r2);padding:9px 11px}
.cv-bal-lbl{font-family:var(--fm);font-size:7px;letter-spacing:1.5px;text-transform:uppercase;color:var(--tx3);margin-bottom:4px}
.cv-bal-val{font-family:var(--fh);font-size:15px;font-weight:700;color:var(--acc);text-shadow:0 0 8px rgba(var(--acc-rgb),.4)}
.cv-ins-card{background:var(--bg3);border:1px solid var(--bg4);border-radius:var(--r2);padding:9px 11px;margin-bottom:8px}
.cv-ins-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:4px}
.cv-ins-name{font-size:12px;font-weight:700;color:var(--tx)}
.cv-ins-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0;display:inline-block;margin-right:5px}
.cv-ins-meta{font-family:var(--fm);font-size:8px;color:var(--tx3)}
.cv-debt-item{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:7px 10px;
  background:var(--bg3);border:1px solid var(--bg4);border-left:2px solid #ff5050;border-radius:var(--r2);margin-bottom:5px}
.cv-debt-info{flex:1;min-width:0}
.cv-debt-cred{font-size:11px;color:var(--tx);font-weight:600}
.cv-debt-note{font-size:9px;color:var(--tx3);margin-top:1px}
.cv-debt-amt{font-family:var(--fm);font-size:11px;color:#ff5050;font-weight:700;white-space:nowrap}
.cv-notes{font-size:10.5px;color:var(--tx2);line-height:1.6;background:var(--bg3);border:1px solid var(--bg4);
  border-radius:var(--r2);padding:8px 10px}
/* FAME / RELATIONSHIP CARDS */
.cv-fame-card,.cv-rel-card{background:var(--bg3);border:1px solid var(--bg4);border-radius:var(--r2);
  padding:9px 11px;margin-bottom:7px}
.cv-fame-top,.cv-rel-top{display:flex;align-items:center;gap:8px;margin-bottom:6px}
.cv-fame-nm,.cv-rel-nm{font-size:11.5px;font-weight:700;color:var(--tx);flex:1;font-family:var(--fh)}
.cv-stat-tag{font-size:7.5px;font-weight:700;padding:2px 8px;border-radius:3px;letter-spacing:.5px;white-space:nowrap}
.cv-fame-bar-wrap{height:6px;background:rgba(255,255,255,.05);border-radius:4px;overflow:hidden;position:relative;margin-bottom:5px}
.cv-fame-bar-center{position:absolute;top:0;left:50%;width:1px;height:100%;background:rgba(255,255,255,.15)}
.cv-fame-bar-fill{height:100%;border-radius:4px;position:absolute;top:0}
.cv-fame-bar-pos{background:linear-gradient(90deg,#0a8a60,#39ff8a);box-shadow:0 0 6px rgba(57,255,138,.4);left:50%}
.cv-fame-bar-neg{background:linear-gradient(90deg,#ff5050,#9a2020);box-shadow:0 0 6px rgba(255,80,80,.4);right:50%}
.cv-fame-meta{display:flex;align-items:center;justify-content:space-between}
.cv-fame-note,.cv-rel-note{font-size:9.5px;color:var(--tx3);line-height:1.4;flex:1}
.cv-fame-val{font-family:var(--fm);font-size:11px;font-weight:700;min-width:36px;text-align:right}
/* MISSION */
.cv-mis-card{background:var(--bg3);border:1px solid var(--abd);border-radius:var(--r2);padding:11px 12px;position:relative;overflow:hidden}
.cv-mis-top{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:8px}
.cv-mis-title{font-family:var(--fh);font-size:12.5px;font-weight:700;color:var(--tx);text-shadow:0 0 8px rgba(var(--acc-rgb),.3)}
.cv-mis-row{display:flex;gap:8px;margin-bottom:7px;font-size:11px}
.cv-mis-row .k{font-family:var(--fm);font-size:7.5px;letter-spacing:1px;text-transform:uppercase;color:var(--tx3);
  width:62px;flex-shrink:0;padding-top:1px}
.cv-mis-row .v{color:var(--tx2);flex:1;line-height:1.5}
.cv-mis-desc{font-size:10.5px;color:var(--tx2);line-height:1.6;background:var(--bg4);border-radius:var(--r2);
  padding:8px 10px;margin-bottom:9px}
.cv-mis-rewards{display:flex;flex-direction:column;gap:4px}
.cv-mis-reward{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--tx2)}
.cv-mis-reward::before{content:'◆';color:var(--acc);font-size:7px}
/* EMPTY STATE */
.cv-empty{text-align:center;padding:24px 0;color:var(--tx3);font-size:9px;letter-spacing:2px;font-family:var(--fm);text-transform:uppercase}
.cv-empty::before{content:'◇';display:block;font-size:16px;margin-bottom:7px;opacity:.3}
/* FOOTER */
#cvfoot{border-top:1px solid rgba(255,255,255,.05);padding:6px 13px;font-family:var(--fm);font-size:7px;
  color:var(--tx3);text-align:center;letter-spacing:2px;background:var(--bg2);text-transform:uppercase;position:relative}
"""

HTML_BODY = """
<textarea id="cvraw" style="display:none;position:absolute;left:-9999px">$1</textarea>
<div id="cvwin">
  <div class="cv-corner cv-corner-tl"></div>
  <div class="cv-corner cv-corner-tr"></div>
  <div id="cvhead">
    <svg id="cvsigil" viewBox="0 0 28 28" fill="none">
      <rect x="9" y="9" width="10" height="10" rx="1.5" stroke="currentColor" stroke-width="1.4" style="color:var(--acc)"/>
      <line x1="14" y1="2" x2="14" y2="9" stroke="currentColor" stroke-width="1.4" style="color:var(--acc)"/>
      <line x1="14" y1="19" x2="14" y2="26" stroke="currentColor" stroke-width="1.4" style="color:var(--acc)"/>
      <line x1="2" y1="14" x2="9" y2="14" stroke="currentColor" stroke-width="1.4" style="color:var(--acc)"/>
      <line x1="19" y1="14" x2="26" y2="14" stroke="currentColor" stroke-width="1.4" style="color:var(--acc)"/>
      <circle cx="14" cy="14" r="2.2" fill="currentColor" style="color:var(--acc)"/>
    </svg>
    <div id="cvhdtxt">
      <div id="cvtitle">NEURAL UPLINK // STATUS</div>
      <div id="cvnm">—</div>
      <div id="cvhandle">—</div>
    </div>
    <div id="cvhdvit"></div>
    <div id="cvlnbtn">EN</div>
    <div id="cvchev">▲</div>
  </div>
  <div id="cvbody">
    <div id="cvtabs"></div>
    <div id="cvpanes"></div>
  </div>
  <div id="cvpsy"></div>
  <div id="cvfoot">CYBERVERSE BIOMETRIC STATUS LINK</div>
</div>
"""

JS = """
(function(){
function g(id){return document.getElementById(id)}
function esc(v){if(v==null)return'';return String(v).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}
function pct(c,m){c=parseFloat(c);m=parseFloat(m);if(!(m>0))return 0;return Math.max(0,Math.min(100,Math.round(c/m*100)))}
function hexRgb(h){var s=String(h||'').replace('#','');if(s.length===3)s=s[0]+s[0]+s[1]+s[1]+s[2]+s[2];var n=parseInt(s,16)||0x00F0FF;return((n>>16)&255)+','+((n>>8)&255)+','+(n&255)}

var rawEl=g('cvraw');
var d={};
try{if(rawEl&&rawEl.value.trim()){var dec=document.createElement('textarea');dec.innerHTML=rawEl.value.trim();d=JSON.parse(dec.value.trim())}}catch(e){}
var TH=(d.lang==='th');

// ── LANGUAGE ──────────────────────────────────────────────────────────
var L={
  stat:['STAT','สถานะ'],cyberware:['CYBERWARE','ไซเบอร์แวร์'],account:['ACCOUNT','บัญชี'],
  fame:['FAME','ชื่อเสียง'],relations:['RELATIONS','ความสัมพันธ์'],mission:['MISSION','ภารกิจ'],
  char:['CHARACTER','ตัวละคร'],vital:['VITALS','ร่างกาย'],scene:['SCENE','สถานการณ์'],
  cond:['CONDITIONS','สภาพ'],inj:['INJURIES','บาดแผล'],norm:['Normal','ปกติ'],
  hp:['HP','HP'],stam:['STAM','สแตมินา'],
  noware:['No cyberware installed.','ยังไม่มีไซเบอร์แวร์'],
  neuralStability:['NEURAL STABILITY','เสถียรภาพประสาท'],humanity:['Humanity','ความเป็นมนุษย์'],
  bank:['Bank Balance','ยอดธนาคาร'],cash:['Cash on Hand','เงินสดติดตัว'],
  insurance:['Medical Insurance','ประกันสุขภาพ'],noins:['No active coverage.','ไม่มีประกัน'],
  debts:['Debts','หนี้สิน'],nodebt:['No outstanding debts.','ไม่มีหนี้สิน'],
  notes:['Notes','บันทึก'],nofame:['No factions recorded.','ยังไม่มีข้อมูลฝ่าย'],
  norel:['No relationships recorded.','ยังไม่มีความสัมพันธ์บันทึกไว้'],
  nomission:['No active mission.','ไม่มีภารกิจที่กำลังดำเนินการ'],
  employer:['Employer','ผู้ว่าจ้าง'],location:['Location','สถานที่'],deadline:['Deadline','กำหนดเวลา'],
  rewards:['Rewards','ค่าตอบแทน'],
  active:['ACTIVE','กำลังดำเนินการ'],complete:['COMPLETE','สำเร็จ'],failed:['FAILED','ล้มเหลว'],
  foot:['CYBERVERSE BIOMETRIC STATUS LINK','ลิงก์สถานะชีวภาพ CYBERVERSE']
};
function T(k){var a=L[k];if(!a)return k;return TH?a[1]:a[0]}

// ── HELPERS ──────────────────────────────────────────────────────────
function tierColor(t){
  var m={'Street':'#9090a8','Mid-Grade':'#5088d8','Premium':'#b070e0','Military Grade':'#ff8c42','Prototype':'#ff2079'};
  return m[t]||'#7898c8';
}
function wareStatusInfo(s){
  s=(s||'active').toLowerCase();
  var m={
    active:{color:'#39ff8a',label:'ACTIVE'},
    damaged:{color:'#ffb627',label:'DAMAGED'},
    offline:{color:'#707080',label:'OFFLINE'},
    malfunctioning:{color:'#ff3b3b',label:'MALFUNCTION'}
  };
  return m[s]||m.active;
}
var PSY_STATES={
  stable:{color:'#39ff8a',label:['STABLE','เสถียร'],pct:92},
  strained:{color:'#c8e639',label:['STRAINED','ตึงเครียด'],pct:68},
  unstable:{color:'#ffb627',label:['UNSTABLE','ไม่เสถียร'],pct:44},
  critical:{color:'#ff3b3b',label:['CRITICAL','วิกฤต'],pct:20},
  flatlined:{color:'#ff0040',label:['FLATLINED','หมดสภาพ'],pct:5}
};
var REL_COLORS={
  'Stranger':'#707080','Acquaintance':'#5088d8','Friend':'#39c8a0','Close Friend':'#39ff8a',
  'Ally':'#00f0ff','Romantic Interest':'#ff5fa8','Rival':'#ffb627','Enemy':'#ff5050','Nemesis':'#c81030'
};
function fameStatus(v){
  v=parseFloat(v)||0;
  if(v>=50)return{label:TH?'ไว้วางใจ':'Trusted',color:'#39ff8a'};
  if(v>=20)return{label:TH?'เป็นมิตร':'Friendly',color:'#5088d8'};
  if(v>=-19)return{label:TH?'เป็นกลาง':'Neutral',color:'#808090'};
  if(v>=-50)return{label:TH?'ระแวง':'Wary',color:'#ffb627'};
  return{label:TH?'เป็นศัตรู':'Hostile',color:'#ff5050'};
}
function missionStatusInfo(s){
  s=(s||'active').toLowerCase();
  var m={active:{color:'#00f0ff',k:'active'},complete:{color:'#39ff8a',k:'complete'},failed:{color:'#ff5050',k:'failed'}};
  return m[s]||m.active;
}

// ── PANEL: STAT ──────────────────────────────────────────────────
function pStat(){
  var hp=d.hp||{cur:100,max:100};
  var st=d.stamina||{cur:100,max:100};
  var hpP=pct(hp.cur,hp.max);var stP=pct(st.cur,st.max);

  var rows=[[TH?'ชื่อ':'Name',d.name],[TH?'ชื่อเล่น':'Handle',d.handle],
    [TH?'อายุ':'Age',d.age],[TH?'เพศ':'Gender',d.gender],[TH?'อาชีพ':'Role',d.role]];
  var gh='';
  rows.forEach(function(r,i){
    gh+='<div class="cv-icard'+(i>=4?' full':'')+'"><div class="cv-icard-l">'+esc(r[0])+'</div><div class="cv-icard-v">'+esc(r[1]||'—')+'</div></div>';
  });

  var barsH='<div class="cv-bar-row"><div class="cv-bar-lbl">'+T('hp')+'</div><div class="cv-bar-wrap"><div class="cv-bar-track"><div class="cv-bar-fill cv-bar-hp" style="width:'+hpP+'%"></div></div><div class="cv-bar-nums"><span class="cv-bar-val">'+esc(hp.cur)+' / '+esc(hp.max)+'</span></div></div></div>';
  barsH+='<div class="cv-bar-row"><div class="cv-bar-lbl">'+T('stam')+'</div><div class="cv-bar-wrap"><div class="cv-bar-track"><div class="cv-bar-fill cv-bar-st" style="width:'+stP+'%"></div></div><div class="cv-bar-nums"><span class="cv-bar-val">'+esc(st.cur)+' / '+esc(st.max)+'</span></div></div></div>';

  var conds=d.conditions||[];var injs=d.injuries||[];
  var cb='';
  if(!conds.length)cb='<span class="cv-badge none">'+esc(T('norm'))+'</span>';
  else conds.forEach(function(c){cb+='<span class="cv-badge cond">⚡ '+esc(c)+'</span>';});
  var ib='';
  if(!injs.length)ib='<span class="cv-badge none">'+esc(T('norm'))+'</span>';
  else injs.forEach(function(c){ib+='<span class="cv-badge inj">⚠ '+esc(c)+'</span>';});

  var sitH=d.situation?'<div class="cv-sec">'+T('scene')+'</div><div class="cv-sit-card"><div class="cv-sit-txt">'+esc(d.situation)+'</div></div>':'';
  return sitH+'<div class="cv-sec">'+T('char')+'</div>'+
    '<div class="cv-igrid">'+gh+'</div>'+
    '<div class="cv-sec mt">'+T('vital')+'</div>'+
    '<div class="cv-bars">'+barsH+'</div>'+
    '<div class="cv-sec mt">'+T('cond')+'</div><div class="cv-badges">'+cb+'</div>'+
    '<div class="cv-sec mt">'+T('inj')+'</div><div class="cv-badges">'+ib+'</div>';
}

// ── PANEL: CYBERWARE ────────────────────────────────────────────
function pCyberware(){
  var cw=d.cyberware||[];
  var h='<div class="cv-sec">'+T('cyberware')+'</div>';
  if(!cw.length)return h+'<div class="cv-empty">'+esc(T('noware'))+'</div>';
  var gr={};var order=[];
  cw.forEach(function(w){var c=w.category||(TH?'อื่นๆ':'Other');if(!gr[c]){gr[c]=[];order.push(c)}gr[c].push(w)});
  order.forEach(function(cat){
    h+='<div class="cv-ware-group"><div class="cv-ware-lbl">'+esc(cat)+'</div>';
    gr[cat].forEach(function(w){
      var tc=tierColor(w.tier);
      var si=wareStatusInfo(w.status);
      h+='<div class="cv-ware-card" style="border-left-color:'+tc+'66">'+
        '<div class="cv-ware-top">'+
          '<div class="cv-ware-ico">⚙</div>'+
          '<div class="cv-ware-meta">'+
            '<div class="cv-ware-nm">'+esc(w.name||'—')+'</div>'+
            (w.manufacturer?'<div class="cv-ware-mf">'+esc(w.manufacturer)+'</div>':'')+
          '</div>'+
          '<div class="cv-ware-tags">'+
            (w.tier?'<span class="cv-tag" style="color:'+tc+'">'+esc(w.tier)+'</span>':'')+
            '<span class="cv-tag" style="color:'+si.color+'">'+esc(si.label)+'</span>'+
          '</div>'+
        '</div>'+
        (w.effect?'<div class="cv-ware-fx">'+esc(w.effect)+'</div>':'')+
        '<div class="cv-ware-foot">'+
          '<div class="cv-ware-hc">'+(TH?'ค่าความเป็นมนุษย์':'Humanity Cost')+': <span class="v">−'+esc(w.humanityCost||0)+'</span></div>'+
        '</div>'+
      '</div>';
    });
    h+='</div>';
  });
  return h;
}

// ── CYBERPSYCHOSIS STRIP (always visible, not a tab) ──────────────
function renderPsy(){
  var el=g('cvpsy');if(!el)return;
  var psy=d.cyberpsychosis||{};
  var hu=psy.humanity||{cur:50,max:50};
  var st=(psy.state||'stable').toLowerCase();
  var info=PSY_STATES[st]||PSY_STATES.stable;
  var huP=pct(hu.cur,hu.max);
  var isCrit=(st==='critical'||st==='flatlined');
  var symH='';
  (psy.symptoms||[]).forEach(function(s){symH+='<span class="cv-psy-sym">'+esc(s)+'</span>';});
  el.innerHTML=
    '<div class="cv-psy-row">'+
      '<div class="cv-psy-lbl">'+T('neuralStability')+'</div>'+
      '<div class="cv-psy-state'+(isCrit?' cv-glitch':'')+'" style="color:'+info.color+';text-shadow:0 0 9px '+info.color+'88">'+esc(TH?info.label[1]:info.label[0])+'</div>'+
    '</div>'+
    '<div class="cv-psy-track"><div class="cv-psy-fill'+(st==='flatlined'?' cv-pulse':'')+'" style="width:'+huP+'%;background:'+info.color+';box-shadow:0 0 8px '+info.color+'77"></div></div>'+
    '<div class="cv-psy-meta"><span>'+T('humanity')+'</span><span>'+esc(hu.cur)+' / '+esc(hu.max)+'</span></div>'+
    (symH?'<div class="cv-psy-symptoms">'+symH+'</div>':'');
}

// ── PANEL: ACCOUNT ──────────────────────────────────────────────
function pAccount(){
  var ac=d.account||{};
  var cur=ac.currency||'€$';
  var h='<div class="cv-sec">'+T('account')+'</div>';
  h+='<div class="cv-bal-row">'+
    '<div class="cv-bal-card"><div class="cv-bal-lbl">'+T('bank')+'</div><div class="cv-bal-val">'+esc(cur)+esc((parseFloat(ac.bank)||0).toLocaleString())+'</div></div>'+
    '<div class="cv-bal-card"><div class="cv-bal-lbl">'+T('cash')+'</div><div class="cv-bal-val">'+esc(cur)+esc((parseFloat(ac.cash)||0).toLocaleString())+'</div></div>'+
  '</div>';

  h+='<div class="cv-sec mt">'+T('insurance')+'</div>';
  var ins=ac.insurance;
  if(!ins||!ins.provider){h+='<div class="cv-empty">'+esc(T('noins'))+'</div>';}
  else{
    var active=!!ins.active;
    h+='<div class="cv-ins-card">'+
      '<div class="cv-ins-top"><div class="cv-ins-name"><span class="cv-ins-dot" style="background:'+(active?'#39ff8a':'#ff5050')+';box-shadow:0 0 6px '+(active?'#39ff8a':'#ff5050')+'88"></span>'+esc(ins.provider)+'</div></div>'+
      '<div class="cv-ins-meta">'+(ins.tier?esc(ins.tier)+' · ':'')+(active?(TH?'ใช้งานอยู่':'Active'):(TH?'หมดอายุ':'Inactive'))+'</div>'+
    '</div>';
  }

  h+='<div class="cv-sec mt">'+T('debts')+'</div>';
  var debts=ac.debts||[];
  if(!debts.length)h+='<div class="cv-empty">'+esc(T('nodebt'))+'</div>';
  else debts.forEach(function(de){
    h+='<div class="cv-debt-item"><div class="cv-debt-info"><div class="cv-debt-cred">'+esc(de.creditor||'—')+'</div>'+
      (de.note?'<div class="cv-debt-note">'+esc(de.note)+'</div>':'')+'</div>'+
      '<div class="cv-debt-amt">'+esc(cur)+esc(de.amount||0)+'</div></div>';
  });

  if(ac.notes){
    h+='<div class="cv-sec mt">'+T('notes')+'</div><div class="cv-notes">'+esc(ac.notes)+'</div>';
  }
  return h;
}

// ── PANEL: FAME ─────────────────────────────────────────────────
function pFame(){
  var fame=d.fame||[];
  var h='<div class="cv-sec">'+T('fame')+'</div>';
  if(!fame.length)return h+'<div class="cv-empty">'+esc(T('nofame'))+'</div>';
  fame.forEach(function(f){
    var v=parseFloat(f.value)||0;
    var fs=fameStatus(v);
    var posW=v>0?Math.min(50,v/2)+'%':'0%';
    var negW=v<0?Math.min(50,-v/2)+'%':'0%';
    h+='<div class="cv-fame-card">'+
      '<div class="cv-fame-top">'+
        '<div class="cv-fame-nm">'+esc(f.faction||'—')+'</div>'+
        '<span class="cv-stat-tag" style="color:'+fs.color+';border:1px solid '+fs.color+'44;background:'+fs.color+'18">'+esc(fs.label)+'</span>'+
      '</div>'+
      '<div class="cv-fame-bar-wrap">'+
        '<div class="cv-fame-bar-center"></div>'+
        '<div class="cv-fame-bar-fill cv-fame-bar-pos" style="width:'+posW+'"></div>'+
        '<div class="cv-fame-bar-fill cv-fame-bar-neg" style="width:'+negW+'"></div>'+
      '</div>'+
      '<div class="cv-fame-meta">'+
        (f.note?'<div class="cv-fame-note">'+esc(f.note)+'</div>':'<div></div>')+
        '<div class="cv-fame-val" style="color:'+(v>=0?'#39ff8a':'#ff5050')+'">'+(v>0?'+':'')+v+'</div>'+
      '</div>'+
    '</div>';
  });
  return h;
}

// ── PANEL: RELATIONSHIPS ────────────────────────────────────────
function pRelationships(){
  var rel=d.relationships||[];
  var h='<div class="cv-sec">'+T('relations')+'</div>';
  if(!rel.length)return h+'<div class="cv-empty">'+esc(T('norel'))+'</div>';
  rel.forEach(function(r){
    var col=REL_COLORS[r.status]||'#7898c8';
    h+='<div class="cv-rel-card">'+
      '<div class="cv-rel-top">'+
        '<div class="cv-rel-nm">'+esc(r.name||'—')+'</div>'+
        '<span class="cv-stat-tag" style="color:'+col+';border:1px solid '+col+'44;background:'+col+'18">'+esc(r.status||'—')+'</span>'+
      '</div>'+
      (r.note?'<div class="cv-rel-note">'+esc(r.note)+'</div>':'')+
    '</div>';
  });
  return h;
}

// ── PANEL: MISSION ──────────────────────────────────────────────
function pMission(){
  var m=d.mission;
  var h='<div class="cv-sec">'+T('mission')+'</div>';
  if(!m||!m.title)return h+'<div class="cv-empty">'+esc(T('nomission'))+'</div>';
  var si=missionStatusInfo(m.status);
  var rewards=m.reward||[];
  if(typeof rewards==='string')rewards=[rewards];
  var rwH='';
  rewards.forEach(function(r){rwH+='<div class="cv-mis-reward">'+esc(r)+'</div>';});
  h+='<div class="cv-mis-card">'+
    '<div class="cv-mis-top">'+
      '<div class="cv-mis-title">'+esc(m.title)+'</div>'+
      '<span class="cv-stat-tag" style="color:'+si.color+';border:1px solid '+si.color+'44;background:'+si.color+'18">'+esc(T(si.k))+'</span>'+
    '</div>'+
    (m.employer?'<div class="cv-mis-row"><div class="k">'+T('employer')+'</div><div class="v">'+esc(m.employer)+'</div></div>':'')+
    (m.location?'<div class="cv-mis-row"><div class="k">'+T('location')+'</div><div class="v">'+esc(m.location)+'</div></div>':'')+
    (m.deadline?'<div class="cv-mis-row"><div class="k">'+T('deadline')+'</div><div class="v">'+esc(m.deadline)+'</div></div>':'')+
    (m.desc?'<div class="cv-mis-desc">'+esc(m.desc)+'</div>':'')+
    (rwH?'<div class="cv-sec" style="margin-top:2px;margin-bottom:7px">'+T('rewards')+'</div><div class="cv-mis-rewards">'+rwH+'</div>':'')+
  '</div>';
  return h;
}

// ── BUILD ───────────────────────────────────────────────────────
function build(){
  var acc=d.charColor||'#00F0FF';
  var rgb=hexRgb(acc);
  var win=g('cvwin');
  win.style.setProperty('--acc',acc);
  win.style.setProperty('--acc-rgb',rgb);
  win.style.setProperty('--abg','rgba('+rgb+',.10)');
  win.style.setProperty('--abd','rgba('+rgb+',.28)');
  win.style.setProperty('--bd','rgba('+rgb+',.25)');

  var nm=g('cvnm');if(nm)nm.textContent=d.name||'—';
  var hd=g('cvhandle');if(hd)hd.textContent=d.handle?(TH?'นามแฝง: ':'aka ')+d.handle:'—';
  var lb=g('cvlnbtn');if(lb)lb.textContent=TH?'TH':'EN';
  var ft=g('cvfoot');if(ft)ft.textContent=T('foot');

  var hv=g('cvhdvit');
  if(hv){
    var hp=d.hp||{cur:0,max:100};var st=d.stamina||{cur:0,max:100};
    hv.innerHTML=
      '<div class="cv-hbar-row"><span class="cv-hbar-lbl">HP</span><div class="cv-hbar-track"><div class="cv-hbar-fill cv-hbar-hp" style="width:'+pct(hp.cur,hp.max)+'%"></div></div><span class="cv-hbar-val">'+esc(hp.cur)+'/'+esc(hp.max)+'</span></div>'+
      '<div class="cv-hbar-row"><span class="cv-hbar-lbl">ST</span><div class="cv-hbar-track"><div class="cv-hbar-fill cv-hbar-st" style="width:'+pct(st.cur,st.max)+'%"></div></div><span class="cv-hbar-val">'+esc(st.cur)+'/'+esc(st.max)+'</span></div>';
  }

  var defs=[
    ['stat',T('stat'),pStat],
    ['cyberware',T('cyberware'),pCyberware],
    ['account',T('account'),pAccount],
    ['fame',T('fame'),pFame],
    ['relations',T('relations'),pRelationships],
    ['mission',T('mission'),pMission]
  ];
  var tabsH='',panesH='';
  defs.forEach(function(t,i){
    tabsH+='<div class="cv-tab'+(i===0?' active':'')+'" data-t="'+t[0]+'">'+esc(t[1])+'</div>';
    panesH+='<div class="cv-panel'+(i===0?' active':'')+'" data-p="'+t[0]+'">'+t[2]()+'</div>';
  });
  var tabs=g('cvtabs');if(tabs)tabs.innerHTML=tabsH;
  var panes=g('cvpanes');if(panes)panes.innerHTML=panesH;

  renderPsy();
}

build();

// ── EVENTS ───────────────────────────────────────────────────────
var head=g('cvhead');
if(head)head.addEventListener('click',function(){g('cvwin').classList.toggle('closed')});

var lnbtn=g('cvlnbtn');
if(lnbtn)lnbtn.addEventListener('click',function(e){e.stopPropagation();TH=!TH;build()});

var tabsEl=g('cvtabs');
if(tabsEl)tabsEl.addEventListener('click',function(e){
  var tab=e.target.closest('.cv-tab');if(!tab)return;
  var t=tab.getAttribute('data-t');
  Array.prototype.forEach.call(tabsEl.querySelectorAll('.cv-tab'),function(x){x.classList.toggle('active',x===tab)});
  var panes=g('cvpanes');
  if(panes)Array.prototype.forEach.call(panes.querySelectorAll('.cv-panel'),function(p){p.classList.toggle('active',p.getAttribute('data-p')===t)});
});
})();
"""

html = (
    '<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800;900'
    '&family=Rajdhani:wght@500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet"/>'
    '<style>' + CSS + '</style>'
    + HTML_BODY
    + '<script>' + JS + '</script>'
)

data = {
    "id": "cyberverse-status-tracker",
    "scriptName": "Cyberverse Status Tracker",
    "findRegex": r"/<CYBER_STATUS>([\s\S]*?)<\/CYBER_STATUS>/gm",
    "replaceString": "```\n<!DOCTYPE html>\n<html><head></head><body>" + html + "</body></html>\n```",
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

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
size = len(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))
print(f"{OUT} — {size:,} bytes ({size/1024:.1f} KB)")

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
## CYBERVERSE STATUS TRACKER SYSTEM

You are running the Cyberverse status tracking system. After EVERY response you write, append a status block on its own line with no extra text around it:

<CYBER_STATUS>
{JSON}
</CYBER_STATUS>

The JSON must be a complete, valid status object. Never omit the block, even in short replies.

---

### STATUS JSON SCHEMA

```json
{
  "lang": "en",
  "charColor": "#00F0FF",
  "name": "Kai Mercer",
  "handle": "Nightowl",
  "age": "29",
  "gender": "Male",
  "role": "Solo",
  "situation": "...",
  "hp": {"cur": 72, "max": 100},
  "stamina": {"cur": 50, "max": 100},
  "conditions": [],
  "injuries": [],
  "cyberware": [
    {
      "name": "Kerenzikov",
      "category": "Neuralware",
      "tier": "Military Grade",
      "manufacturer": "Zetatech",
      "effect": "Slows perceived time during combat reactions.",
      "humanityCost": 6,
      "status": "active"
    }
  ],
  "cyberpsychosis": {
    "humanity": {"cur": 34, "max": 50},
    "state": "strained",
    "symptoms": ["Emotional blunting", "Occasional auditory static"]
  },
  "account": {
    "currency": "€$",
    "bank": 15400,
    "cash": 320,
    "insurance": {"provider": "Trauma Team Intl.", "tier": "Gold", "active": true},
    "debts": [{"creditor": "Wakako Okada", "amount": 2000, "note": "Job advance"}],
    "notes": "..."
  },
  "fame": [
    {"faction": "Arasaka Corp", "value": -40, "note": "Sabotaged a shipment."}
  ],
  "relationships": [
    {"name": "Jackie", "status": "Ally", "note": "Ride-or-die partner."}
  ],
  "mission": {
    "title": "Ghost in the Tower",
    "employer": "Wakako Okada",
    "location": "Arasaka Tower, Corpo Plaza",
    "desc": "Extract a netrunner trapped behind ICE in the tower's sublevel.",
    "reward": ["€$5,000 upfront", "Cyberdeck: Tetratronic Rippler", "Wakako's favor"],
    "deadline": "48 hours",
    "status": "active"
  }
}
```

---

### FIELD REFERENCE

| Field | Notes |
|---|---|
| `lang` | "en" or "th" — match player preference |
| `charColor` | hex accent set at creation; never changes |
| `cyberware` | UNLIMITED array — list every installed piece of chrome in full detail, no count cap |
| `cyberware[].category` | groups the Cyberware tab — use: Neuralware, Cyberoptics, Cyberaudio, Cyberlimbs, Internal/Frame, Nanotech, Fashionware, or Other |
| `cyberware[].tier` | "Street" \| "Mid-Grade" \| "Premium" \| "Military Grade" \| "Prototype" |
| `cyberware[].status` | "active" \| "damaged" \| "offline" \| "malfunctioning" |
| `cyberpsychosis.state` | "stable" \| "strained" \| "unstable" \| "critical" \| "flatlined" — drives the always-visible neural stability strip at the bottom of the widget |
| `account.bank` / `account.cash` | plain numbers, no currency symbol — `currency` field supplies the symbol |
| `mission.reward` | array of strings — rewards are NOT always money; mix cash, items, favors, intel freely |
| `relationships[].status` | "Stranger" \| "Acquaintance" \| "Friend" \| "Close Friend" \| "Ally" \| "Romantic Interest" \| "Rival" \| "Enemy" \| "Nemesis" |

---

### OUTPUT RULES
• Copy the full JSON from the previous block and modify only changed fields.
• Never drop any key even if its value did not change.
• `situation` must be rewritten every response to reflect the current moment.
• `cyberware` has no installation limit — track every piece of chrome the character has, however many that is.
• Deduct `humanityCost` from `cyberpsychosis.humanity.cur` whenever new cyberware is installed.
• Update `cyberpsychosis.state` and `symptoms` to reflect cumulative humanity loss and recent narrative stress, not just a fixed threshold.

---

### CYBERPSYCHOSIS GUIDELINES
The strip at the bottom of the widget is always visible regardless of which tab is open — it is the player's early-warning system.

| State | Humanity range (guideline) | Narrative cues |
|---|---|---|
| stable | full / near-full | normal emotional range, no symptoms |
| strained | mild loss | occasional irritability, minor disconnection |
| unstable | moderate loss | mood swings, paranoia, blackout flashes |
| critical | heavy loss | violent impulses, dissociation, hallucinated threats |
| flatlined | humanity bottomed out | total psychotic break — character may go berserk or shut down emotionally; this is a major story event, not a background stat tick |

`symptoms` is a short array of present-tense effects ("Tremors in left hand", "Hears static under quiet sounds") — update it alongside `state`.

---

### CYBERWARE GUIDELINES
• Every implant the character has ever had installed and not removed should appear in the array — there is no cap.
• Give each entry a real `effect` description; do not leave entries as bare names.
• `humanityCost` is the one-time cost paid at installation, used to track cumulative humanity loss — do not re-deduct it every response.
• Mark obsolete/destroyed cyberware `status: "offline"` rather than deleting it, unless it was physically removed from the body (then delete the entry).

---

### ACCOUNT / FAME / RELATIONSHIP / MISSION RULES
• `account.insurance.active` should flip to `false` if premiums lapse or coverage is revoked in the story.
• `fame` tracks standing with gangs, corporations, and city institutions — value range roughly -100 to +100.
• `relationships` only includes named characters the player has actually interacted with — do not pre-populate.
• `mission` holds only the SINGLE current active job. When a job ends, set `status` to "complete" or "failed" for one response (so the player sees the outcome), then clear `mission` to `null` on the next response unless a new job is immediately accepted.\
"""

lorebook = {
    "name": "Cyberverse Status Tracker",
    "entries": {
        "0": entry(0, "Cyberverse Status Tracker System", E0, 89),
    }
}

with open(OUT_LB, 'w', encoding='utf-8') as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)
lb_size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode('utf-8'))
print(f"{OUT_LB} — {lb_size:,} bytes ({lb_size/1024:.1f} KB)")
print("Done!")
