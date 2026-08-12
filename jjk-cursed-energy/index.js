/* ══════════════════════════════════════════════════════════
   JJK Cursed Energy System — SillyTavern Extension
   Theme: Jujutsu Kaisen — Cursed Energy / Domain Expansion
   ══════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  // ── Constants ─────────────────────────────────────────────
  const GRADES = [
    { id: 'grade4',  name: '4級 Grade 4',            desc: 'ระดับต่ำสุด รับงานทั่วไป จัดการคำสาปหางแถวได้' },
    { id: 'grade3',  name: '3級 Grade 3',            desc: 'มีประสบการณ์พอสมควร เริ่มออกภาคสนามจริง' },
    { id: 'grade2',  name: '2級 Grade 2',            desc: 'จัดการคำสาประดับกลางได้ด้วยตัวเอง' },
    { id: 'semi1',   name: '準1級 Semi-Grade 1',     desc: 'ฝีมือใกล้ระดับสูงสุด แต่ยังไม่ได้รับการรับรองเต็มตัว' },
    { id: 'grade1',  name: '1級 Grade 1',            desc: 'นักไล่ล่าคำสาปฝีมือดีเยี่ยม รับมืองานอันตรายได้' },
    { id: 'special', name: '特級 Special Grade',      desc: 'ระดับสูงสุด หายากมาก พลังทำลายล้างมหาศาล' }
  ];

  const TECH_TYPES = [
    { id: 'offensive', label: '⚔️ โจมตี (Offensive)' },
    { id: 'defensive', label: '🛡️ ป้องกัน (Defensive)' },
    { id: 'support',   label: '⭐ เสริม (Support)' },
    { id: 'binding',   label: '⛓️ ผูกมัด (Binding)' },
    { id: 'domain',    label: '🔮 เกี่ยวกับอาณาเขต' },
    { id: 'reversal',  label: '💚 เยียวยา (Reverse Technique)' }
  ];

  const DOMAIN_TYPES = [
    { id: 'expansion', label: '領域展開 Domain Expansion (เต็มรูปแบบ)' },
    { id: 'simple',    label: '簡易領域 Simple Domain (พื้นฐาน)' }
  ];

  const RCT_LEVELS = [
    { id: 'weak',   label: 'อ่อน — รักษาบาดแผลเล็กน้อย' },
    { id: 'medium', label: 'ปานกลาง — รักษาบาดแผลสาหัส' },
    { id: 'strong', label: 'แข็งแกร่ง — ต่อกระดูก/อวัยวะ' },
    { id: 'full',   label: '完全体 Full-Body Regeneration' }
  ];

  const TABS = [
    { id: 'profile',    icon: '👤', label: 'ข้อมูล' },
    { id: 'energy',     icon: '🌀', label: 'พลังจิต' },
    { id: 'techniques', icon: '🖐️', label: 'เทคนิค' },
    { id: 'domain',     icon: '🔮', label: 'อาณาเขต' },
    { id: 'vows',       icon: '⛓️', label: 'คำสาบาน' },
    { id: 'combat',     icon: '⚡', label: 'การต่อสู้' },
    { id: 'summary',    icon: '📜', label: 'สรุป' }
  ];

  const STORAGE_PREFIX = 'jjk_ces_';

  // ── Default State ─────────────────────────────────────────
  function defaultState() {
    return {
      profile: {
        name: '', title: '', school: '', grade: 'grade3',
        innateName: '', innateDesc: '', appearance: ''
      },
      energy: { current: 100, max: 100, regen: 10 },
      techniques: [],
      domain: {
        name: '', desc: '', type: 'expansion', sureHit: false,
        energyCost: 40, cooldownMax: 5, cooldownRemaining: 0, active: false
      },
      vows: [],
      combat: {
        blackFlash: 0, blackFlashStreak: 0,
        rctActive: false, rctLevel: 'weak', rctNote: '',
        log: ''
      }
    };
  }

  let state = defaultState();
  let currentTab = 'profile';
  let idSeq = 1;
  function genId() { return 'i' + (idSeq++) + '_' + Date.now().toString(36); }

  // ── Persistence ───────────────────────────────────────────
  function getScopeKey() {
    try {
      const ctx = (typeof SillyTavern !== 'undefined' && SillyTavern.getContext)
        ? SillyTavern.getContext()
        : (typeof getContext === 'function' ? getContext() : null);
      if (ctx) {
        if (ctx.characterId !== undefined && ctx.characters && ctx.characters[ctx.characterId]) {
          const c = ctx.characters[ctx.characterId];
          return STORAGE_PREFIX + (c.avatar || c.name || 'default');
        }
        if (ctx.name2) return STORAGE_PREFIX + ctx.name2;
      }
    } catch (e) { /* ignore, fall back below */ }
    return STORAGE_PREFIX + 'default';
  }

  function loadState() {
    try {
      const raw = localStorage.getItem(getScopeKey());
      if (!raw) { state = defaultState(); return; }
      const parsed = JSON.parse(raw);
      const def = defaultState();
      state = {
        profile: Object.assign(def.profile, parsed.profile || {}),
        energy: Object.assign(def.energy, parsed.energy || {}),
        techniques: Array.isArray(parsed.techniques) ? parsed.techniques : [],
        domain: Object.assign(def.domain, parsed.domain || {}),
        vows: Array.isArray(parsed.vows) ? parsed.vows : [],
        combat: Object.assign(def.combat, parsed.combat || {})
      };
    } catch (e) {
      state = defaultState();
    }
  }

  function saveState() {
    try { localStorage.setItem(getScopeKey(), JSON.stringify(state)); } catch (e) { /* storage full/unavailable */ }
  }

  function clamp(v, min, max) { return Math.min(max, Math.max(min, v)); }

  // ── Init ──────────────────────────────────────────────────
  function init() {
    loadState();
    injectButton();
    injectModal();
    window.JJKCursedEnergy = {
      open, close, closeIfOverlay, switchTab,
      updateProfile, selectGrade,
      energyDelta, updateEnergyField,
      addTechnique, removeTechnique, updateTechnique,
      updateDomainField, openDomain, closeDomain, tickDomain,
      addVow, removeVow, updateVow, toggleVowActive,
      blackFlashDelta, resetBlackFlashStreak, updateCombatField,
      copySheet, sendToChat, downloadSheet, resetAll
    };
  }

  function injectButton() {
    const btn = document.createElement('div');
    btn.id = 'jce-trigger';
    btn.innerHTML = '<span>呪</span> Cursed Energy';
    btn.title = 'เปิด JJK Cursed Energy System';
    btn.onclick = open;

    const targets = [
      '#extensionsMenuButton', '#extension_floating_menu',
      '#top-bar', '.flex-container.flexGap5', '#leftSendForm', 'body'
    ];
    let placed = false;
    for (const sel of targets) {
      const el = document.querySelector(sel);
      if (el && el !== document.body) { el.appendChild(btn); placed = true; break; }
    }
    if (!placed) {
      btn.style.cssText = 'position:fixed;top:10px;right:10px;z-index:9998;';
      document.body.appendChild(btn);
    }
  }

  function injectModal() {
    const wrap = document.createElement('div');
    wrap.id = 'jce-modal';
    wrap.style.display = 'none';
    wrap.innerHTML = buildModalHTML();
    document.body.appendChild(wrap);
  }

  function buildModalHTML() {
    const tabBtns = TABS.map(t => `
      <button class="jce-tab-btn ${t.id === currentTab ? 'active' : ''}" data-tab="${t.id}"
              onclick="window.JJKCursedEnergy.switchTab('${t.id}')">
        <span class="jce-tab-icon">${t.icon}</span><span class="jce-tab-label">${t.label}</span>
      </button>`).join('');

    return `
    <div id="jce-overlay" onclick="window.JJKCursedEnergy.closeIfOverlay(event)">
      <div id="jce-panel">
        <button class="jce-close" onclick="window.JJKCursedEnergy.close()">✕</button>
        <div class="jce-header">
          <div class="jce-header-glyph">呪術廻戦 ▪ 領域展開 ▪ 反転術式</div>
          <h1>Cursed Energy System</h1>
          <p>ระบบพลังจิต & เทคนิคคำสาปสำหรับโรลเพลย์ Jujutsu Kaisen</p>
          <div class="jce-header-bar" id="jce-header-bar"></div>
        </div>
        <div class="jce-tabs">${tabBtns}</div>
        <div class="jce-content" id="jce-content"></div>
      </div>
    </div>`;
  }

  // ── Open / Close ──────────────────────────────────────────
  function open() {
    const m = document.getElementById('jce-modal');
    if (!m) return;
    loadState();
    m.style.display = 'block';
    renderTabs();
    renderCurrentTab();
  }
  function close() {
    const m = document.getElementById('jce-modal');
    if (m) m.style.display = 'none';
  }
  function closeIfOverlay(e) { if (e.target.id === 'jce-overlay') close(); }

  function switchTab(id) {
    currentTab = id;
    renderTabs();
    renderCurrentTab();
  }
  function renderTabs() {
    document.querySelectorAll('.jce-tab-btn').forEach(b => b.classList.toggle('active', b.dataset.tab === currentTab));
  }

  function renderCurrentTab() {
    const el = document.getElementById('jce-content');
    if (!el) return;
    el.innerHTML = '';
    const panel = document.createElement('div');
    panel.className = 'jce-panel-inner';
    panel.innerHTML = getTabHTML(currentTab);
    el.appendChild(panel);
    attachTabListeners(currentTab);
    updateHeaderBar();
  }

  function updateHeaderBar() {
    const bar = document.getElementById('jce-header-bar');
    if (!bar) return;
    const pct = clamp(Math.round((state.energy.current / Math.max(1, state.energy.max)) * 100), 0, 100);
    const cls = pct > 60 ? 'high' : pct > 30 ? 'mid' : 'low';
    bar.innerHTML = `
      <div class="jce-mini-label">呪力 ${state.energy.current} / ${state.energy.max}</div>
      <div class="jce-mini-track"><div class="jce-mini-fill ${cls}" style="width:${pct}%"></div></div>
      ${state.domain.active ? '<div class="jce-mini-domain">🔮 อาณาเขตเปิดใช้งานอยู่</div>' : ''}
    `;
  }

  // ── Tab HTML ──────────────────────────────────────────────
  function getTabHTML(id) {
    switch (id) {
      case 'profile':    return tabProfile();
      case 'energy':     return tabEnergy();
      case 'techniques': return tabTechniques();
      case 'domain':     return tabDomain();
      case 'vows':       return tabVows();
      case 'combat':     return tabCombat();
      case 'summary':    return tabSummary();
      default: return '';
    }
  }

  function tabProfile() {
    const p = state.profile;
    const gradeCards = GRADES.map(g => `
      <div class="grade-card ${p.grade === g.id ? 'selected' : ''}" onclick="window.JJKCursedEnergy.selectGrade('${g.id}', this)">
        <div class="grade-name">${g.name}</div>
        <div class="grade-desc">${g.desc}</div>
      </div>`).join('');

    return `
    <div class="jce-form">
      <div class="jce-row">
        <div class="jce-group">
          <label>ชื่อตัวละคร <span class="req">*</span></label>
          <input id="jp-name" type="text" class="jce-input" placeholder="ชื่อนักไล่ล่าคำสาป..." value="${esc(p.name)}">
        </div>
        <div class="jce-group">
          <label>ฉายา / ตำแหน่ง</label>
          <input id="jp-title" type="text" class="jce-input" placeholder="เช่น ผู้แข็งแกร่งที่สุด..." value="${esc(p.title)}">
        </div>
      </div>
      <div class="jce-group">
        <label>สังกัด / โรงเรียนเวทมนตร์</label>
        <input id="jp-school" type="text" class="jce-input" placeholder="เช่น โรงเรียนเวทมนตร์คำสาปโตเกียว, เกียวโต..." value="${esc(p.school)}">
      </div>
      <div class="jce-group">
        <label>เกรดนักไล่ล่าคำสาป <span class="req">*</span></label>
        <div class="grade-grid">${gradeCards}</div>
      </div>
      <div class="jce-divider"></div>
      <div class="jce-group">
        <label>เทคนิคกำเนิด (Innate Technique) — ชื่อ</label>
        <input id="jp-innate-name" type="text" class="jce-input" placeholder="ชื่อเทคนิคเฉพาะตัว..." value="${esc(p.innateName)}">
      </div>
      <div class="jce-group">
        <label>รายละเอียดเทคนิคกำเนิด</label>
        <textarea id="jp-innate-desc" class="jce-textarea" rows="3" placeholder="อธิบายกลไก/ข้อจำกัดของเทคนิคที่ติดตัวมาแต่กำเนิด...">${esc(p.innateDesc)}</textarea>
      </div>
      <div class="jce-group">
        <label>รูปลักษณ์ / ลักษณะเด่น</label>
        <textarea id="jp-appearance" class="jce-textarea" rows="3" placeholder="ลักษณะภายนอก เครื่องแบบ รอยสัก เครื่องหมายคำสาป...">${esc(p.appearance)}</textarea>
      </div>
    </div>`;
  }

  function tabEnergy() {
    const e = state.energy;
    const pct = clamp(Math.round((e.current / Math.max(1, e.max)) * 100), 0, 100);
    const cls = pct > 60 ? 'high' : pct > 30 ? 'mid' : 'low';
    return `
    <div class="jce-form">
      <div class="info-note">🌀 พลังจิต (Cursed Energy) คือแหล่งพลังที่ใช้ขับเคลื่อนเทคนิคคำสาปและอาณาเขต — หมดแล้วใช้เทคนิคไม่ได้จนกว่าจะฟื้นตัว</div>

      <div class="energy-display">
        <div class="energy-value"><span id="jce-e-current">${e.current}</span> / <span id="jce-e-max">${e.max}</span></div>
        <div class="energy-track"><div class="energy-fill ${cls}" id="jce-e-fill" style="width:${pct}%"></div></div>
      </div>

      <div class="energy-quick-actions">
        <button class="jce-btn danger" onclick="window.JJKCursedEnergy.energyDelta(-25)">−25 (ใช้เทคนิค)</button>
        <button class="jce-btn danger" onclick="window.JJKCursedEnergy.energyDelta(-10)">−10</button>
        <button class="jce-btn ghost" onclick="window.JJKCursedEnergy.energyDelta(10)">+10</button>
        <button class="jce-btn success" onclick="window.JJKCursedEnergy.energyDelta(9999)">เติมเต็ม</button>
      </div>

      <div class="jce-row">
        <div class="jce-group">
          <label>พลังจิตสูงสุด (Max)</label>
          <input id="je-max" type="number" min="1" class="jce-input" value="${e.max}">
        </div>
        <div class="jce-group">
          <label>ฟื้นฟูต่อเทิร์น (Regen/Turn)</label>
          <input id="je-regen" type="number" min="0" class="jce-input" value="${e.regen}">
        </div>
      </div>
      <button class="jce-btn ghost full" onclick="window.JJKCursedEnergy.energyDelta(0)">↻ อัปเดตค่า</button>
    </div>`;
  }

  function tabTechniques() {
    const items = state.techniques.map(t => `
      <div class="tech-item" id="tech-${t.id}">
        <div class="tech-item-header">
          <input type="text" class="jce-input" style="flex:1" placeholder="ชื่อเทคนิค..." value="${esc(t.name)}"
                 onchange="window.JJKCursedEnergy.updateTechnique('${t.id}','name',this.value)">
          <select class="jce-select tech-type-select" onchange="window.JJKCursedEnergy.updateTechnique('${t.id}','type',this.value)">
            ${TECH_TYPES.map(ty => `<option value="${ty.id}" ${t.type === ty.id ? 'selected' : ''}>${ty.label}</option>`).join('')}
          </select>
          <input type="number" class="jce-input" style="width:80px" placeholder="ต้นทุน" value="${t.cost || 0}"
                 onchange="window.JJKCursedEnergy.updateTechnique('${t.id}','cost',this.value)">
          <button class="tech-remove" onclick="window.JJKCursedEnergy.removeTechnique('${t.id}')">✕</button>
        </div>
        <textarea class="jce-textarea" rows="2" placeholder="อธิบายผลของเทคนิค..."
                  onchange="window.JJKCursedEnergy.updateTechnique('${t.id}','desc',this.value)">${esc(t.desc)}</textarea>
      </div>`).join('');

    return `
    <div class="jce-form">
      <div class="info-note">🖐️ บันทึกเทคนิคคำสาปที่ตัวละครใช้ได้ พร้อมประเภทและต้นทุนพลังจิตโดยประมาณ</div>
      <div id="tech-list">${items || '<div class="jce-empty">ยังไม่มีเทคนิคที่บันทึกไว้</div>'}</div>
      <button class="add-btn" onclick="window.JJKCursedEnergy.addTechnique()">+ เพิ่มเทคนิคคำสาป</button>
    </div>`;
  }

  function tabDomain() {
    const d = state.domain;
    const status = d.active ? { label: 'เปิดใช้งานอยู่', cls: 'active' }
      : d.cooldownRemaining > 0 ? { label: `พักฟื้น (เหลือ ${d.cooldownRemaining} เทิร์น)`, cls: 'cooldown' }
      : { label: 'พร้อมใช้งาน', cls: 'ready' };

    return `
    <div class="jce-form">
      <div class="info-note">🔮 การขยายอาณาเขต (Domain Expansion) สร้างพื้นที่ปิดตายที่ใส่เทคนิคเฉพาะตัวลงไปโดยตรง — ปกติแล้วให้ผลโจมตีแบบมั่นใจ (Sure-Hit) กับผู้ที่ไม่มีอาณาเขต/เกราะป้องกันของตัวเอง</div>

      <div class="domain-status ${status.cls}">${status.label}</div>

      <div class="jce-group">
        <label>ชื่ออาณาเขต</label>
        <input id="jd-name" type="text" class="jce-input" placeholder="เช่น Unlimited Void, Malevolent Shrine, Chimera Shadow Garden..." value="${esc(d.name)}">
      </div>
      <div class="jce-group">
        <label>ผลของอาณาเขต / คำอธิบาย</label>
        <textarea id="jd-desc" class="jce-textarea" rows="3" placeholder="อธิบายภาพลักษณ์และผลกระทบต่อผู้ที่ถูกกักไว้ข้างใน...">${esc(d.desc)}</textarea>
      </div>
      <div class="jce-row">
        <div class="jce-group">
          <label>ประเภท</label>
          <select id="jd-type" class="jce-select">
            ${DOMAIN_TYPES.map(t => `<option value="${t.id}" ${d.type === t.id ? 'selected' : ''}>${t.label}</option>`).join('')}
          </select>
        </div>
        <div class="jce-group">
          <label class="jce-checkbox-label">
            <input id="jd-surehit" type="checkbox" ${d.sureHit ? 'checked' : ''}> โจมตีมั่นใจ (Sure-Hit)
          </label>
        </div>
      </div>
      <div class="jce-row">
        <div class="jce-group">
          <label>ต้นทุนพลังจิตในการเปิด</label>
          <input id="jd-cost" type="number" min="0" class="jce-input" value="${d.energyCost}">
        </div>
        <div class="jce-group">
          <label>ระยะพักฟื้น (เทิร์น)</label>
          <input id="jd-cooldown" type="number" min="0" class="jce-input" value="${d.cooldownMax}">
        </div>
      </div>

      <div class="domain-actions">
        <button class="jce-btn success" onclick="window.JJKCursedEnergy.openDomain()" ${d.active || d.cooldownRemaining > 0 ? 'disabled' : ''}>🔮 เปิดอาณาเขต</button>
        <button class="jce-btn danger" onclick="window.JJKCursedEnergy.closeDomain()" ${d.active ? '' : 'disabled'}>ปิดอาณาเขต</button>
        <button class="jce-btn ghost" onclick="window.JJKCursedEnergy.tickDomain()">⏭ ผ่านไป 1 เทิร์น</button>
      </div>
    </div>`;
  }

  function tabVows() {
    const items = state.vows.map(v => `
      <div class="vow-item ${v.active ? 'active' : ''}" id="vow-${v.id}">
        <div class="vow-item-header">
          <label class="jce-checkbox-label">
            <input type="checkbox" ${v.active ? 'checked' : ''} onchange="window.JJKCursedEnergy.toggleVowActive('${v.id}')"> ใช้งานอยู่
          </label>
          <button class="tech-remove" onclick="window.JJKCursedEnergy.removeVow('${v.id}')">✕</button>
        </div>
        <input type="text" class="jce-input" placeholder="ชื่อคำสาบาน..." value="${esc(v.name)}"
               onchange="window.JJKCursedEnergy.updateVow('${v.id}','name',this.value)">
        <div class="jce-row" style="margin-top:8px">
          <div class="jce-group">
            <label>ข้อจำกัด (Restriction)</label>
            <textarea class="jce-textarea" rows="2" placeholder="สิ่งที่ต้องเสียสละ/ห้ามทำ..."
                      onchange="window.JJKCursedEnergy.updateVow('${v.id}','restriction',this.value)">${esc(v.restriction)}</textarea>
          </div>
          <div class="jce-group">
            <label>ผลตอบแทน (Benefit)</label>
            <textarea class="jce-textarea" rows="2" placeholder="พลังที่เพิ่มขึ้นแลกกับข้อจำกัด..."
                      onchange="window.JJKCursedEnergy.updateVow('${v.id}','benefit',this.value)">${esc(v.benefit)}</textarea>
          </div>
        </div>
      </div>`).join('');

    return `
    <div class="jce-form">
      <div class="info-note">⛓️ คำสาบานผูกมัด (Binding Vow) คือข้อตกลงที่ยอมสละบางสิ่งเพื่อแลกพลังที่มากขึ้น — ยิ่งเสียสละมาก ยิ่งได้ผลตอบแทนสูง</div>
      <div id="vow-list">${items || '<div class="jce-empty">ยังไม่มีคำสาบานที่บันทึกไว้</div>'}</div>
      <button class="add-btn" onclick="window.JJKCursedEnergy.addVow()">+ เพิ่มคำสาบาน</button>
    </div>`;
  }

  function tabCombat() {
    const c = state.combat;
    return `
    <div class="jce-form">
      <div class="info-note">⚡ บันทึกสถิติการต่อสู้ — ลำแสงมืด (Black Flash) และเทคนิคย้อนกลับ (Reverse Cursed Technique)</div>

      <div class="combat-block">
        <h4>黒閃 Black Flash</h4>
        <div class="combat-counters">
          <div class="combat-counter">
            <span class="cc-label">รวมทั้งหมด</span>
            <div class="cc-controls">
              <button class="jce-btn ghost sm" onclick="window.JJKCursedEnergy.blackFlashDelta(-1,'blackFlash')">−</button>
              <span class="cc-value" id="jce-bf-total">${c.blackFlash}</span>
              <button class="jce-btn ghost sm" onclick="window.JJKCursedEnergy.blackFlashDelta(1,'blackFlash')">+</button>
            </div>
          </div>
          <div class="combat-counter">
            <span class="cc-label">สตรีคต่อเนื่อง</span>
            <div class="cc-controls">
              <button class="jce-btn ghost sm" onclick="window.JJKCursedEnergy.blackFlashDelta(-1,'blackFlashStreak')">−</button>
              <span class="cc-value" id="jce-bf-streak">${c.blackFlashStreak}</span>
              <button class="jce-btn ghost sm" onclick="window.JJKCursedEnergy.blackFlashDelta(1,'blackFlashStreak')">+</button>
            </div>
          </div>
        </div>
        <button class="jce-btn ghost full" onclick="window.JJKCursedEnergy.resetBlackFlashStreak()">↻ รีเซ็ตสตรีค</button>
      </div>

      <div class="jce-divider"></div>

      <div class="combat-block">
        <h4>反転術式 Reverse Cursed Technique</h4>
        <label class="jce-checkbox-label">
          <input id="jc-rct-active" type="checkbox" ${c.rctActive ? 'checked' : ''}> กำลังใช้งานอยู่
        </label>
        <div class="jce-group" style="margin-top:10px">
          <label>ระดับ</label>
          <select id="jc-rct-level" class="jce-select">
            ${RCT_LEVELS.map(l => `<option value="${l.id}" ${c.rctLevel === l.id ? 'selected' : ''}>${l.label}</option>`).join('')}
          </select>
        </div>
        <div class="jce-group">
          <label>บันทึก</label>
          <textarea id="jc-rct-note" class="jce-textarea" rows="2" placeholder="รายละเอียดอาการบาดเจ็บที่กำลังรักษา...">${esc(c.rctNote)}</textarea>
        </div>
      </div>

      <div class="jce-divider"></div>

      <div class="jce-group">
        <label>บันทึกการต่อสู้ล่าสุด (สำหรับอ้างอิง)</label>
        <textarea id="jc-log" class="jce-textarea" rows="4" placeholder="สรุปเหตุการณ์การต่อสู้ล่าสุด...">${esc(c.log)}</textarea>
      </div>
    </div>`;
  }

  function tabSummary() {
    const sheet = generateSheet();
    return `
    <div class="jce-form">
      <div class="info-note">📜 สรุปสถานะทั้งหมด — ใช้ส่งเข้าแชทเพื่อให้บอท/ผู้เล่นคนอื่นเห็นสถานะปัจจุบัน</div>
      <div class="sheet-preview" id="sheet-preview">${esc(sheet)}</div>
      <div class="export-actions">
        <button class="export-btn copy" onclick="window.JJKCursedEnergy.copySheet()">📋 คัดลอก</button>
        <button class="export-btn send" onclick="window.JJKCursedEnergy.sendToChat()">💬 ส่งเข้า Chat</button>
        <button class="export-btn download" onclick="window.JJKCursedEnergy.downloadSheet()">⬇️ ดาวน์โหลด</button>
      </div>
      <div class="export-success" id="export-success">✓ คัดลอกแล้ว!</div>
      <button class="jce-btn danger full" style="margin-top:16px" onclick="window.JJKCursedEnergy.resetAll()">🗑 รีเซ็ตข้อมูลทั้งหมด</button>
    </div>`;
  }

  // ── Listeners ─────────────────────────────────────────────
  function attachTabListeners(tab) {
    if (tab === 'profile') {
      bind('jp-name',         v => state.profile.name = v);
      bind('jp-title',        v => state.profile.title = v);
      bind('jp-school',       v => state.profile.school = v);
      bind('jp-innate-name',  v => state.profile.innateName = v);
      bind('jp-innate-desc',  v => state.profile.innateDesc = v);
      bind('jp-appearance',   v => state.profile.appearance = v);
    }
    if (tab === 'energy') {
      bind('je-max',   v => { state.energy.max = Math.max(1, parseInt(v) || 1); afterEnergyChange(); });
      bind('je-regen', v => { state.energy.regen = Math.max(0, parseInt(v) || 0); saveState(); });
    }
    if (tab === 'domain') {
      bind('jd-name', v => { state.domain.name = v; saveState(); });
      bind('jd-desc', v => { state.domain.desc = v; saveState(); });
      bind('jd-type', v => { state.domain.type = v; saveState(); });
      bind('jd-cost', v => { state.domain.energyCost = Math.max(0, parseInt(v) || 0); saveState(); });
      bind('jd-cooldown', v => { state.domain.cooldownMax = Math.max(0, parseInt(v) || 0); saveState(); });
      const sh = document.getElementById('jd-surehit');
      if (sh) sh.addEventListener('change', () => { state.domain.sureHit = sh.checked; saveState(); });
    }
    if (tab === 'combat') {
      bind('jc-rct-note', v => { state.combat.rctNote = v; saveState(); });
      bind('jc-log',      v => { state.combat.log = v; saveState(); });
      const act = document.getElementById('jc-rct-active');
      if (act) act.addEventListener('change', () => { state.combat.rctActive = act.checked; saveState(); });
      const lvl = document.getElementById('jc-rct-level');
      if (lvl) lvl.addEventListener('change', () => { state.combat.rctLevel = lvl.value; saveState(); });
    }
  }

  function bind(id, setter) {
    const el = document.getElementById(id);
    if (!el) return;
    el.addEventListener('change', () => setter(el.value));
    el.addEventListener('input',  () => setter(el.value));
  }

  // ── Profile ───────────────────────────────────────────────
  function updateProfile(key, value) { state.profile[key] = value; saveState(); }
  function selectGrade(id, el) {
    state.profile.grade = id;
    document.querySelectorAll('.grade-card').forEach(c => c.classList.remove('selected'));
    if (el) el.classList.add('selected');
    saveState();
  }

  // ── Energy ────────────────────────────────────────────────
  function afterEnergyChange() {
    state.energy.current = clamp(state.energy.current, 0, state.energy.max);
    saveState();
    refreshEnergyUI();
  }
  function energyDelta(amount) {
    state.energy.current = clamp(state.energy.current + amount, 0, state.energy.max);
    afterEnergyChange();
  }
  function updateEnergyField() { afterEnergyChange(); }
  function refreshEnergyUI() {
    const pct = clamp(Math.round((state.energy.current / Math.max(1, state.energy.max)) * 100), 0, 100);
    const cls = pct > 60 ? 'high' : pct > 30 ? 'mid' : 'low';
    const cur = document.getElementById('jce-e-current');
    const max = document.getElementById('jce-e-max');
    const fill = document.getElementById('jce-e-fill');
    if (cur) cur.textContent = state.energy.current;
    if (max) max.textContent = state.energy.max;
    if (fill) { fill.style.width = pct + '%'; fill.className = 'energy-fill ' + cls; }
    updateHeaderBar();
  }

  // ── Techniques ────────────────────────────────────────────
  function addTechnique() {
    state.techniques.push({ id: genId(), name: '', type: 'offensive', cost: 10, desc: '' });
    saveState();
    renderCurrentTab();
  }
  function removeTechnique(id) {
    state.techniques = state.techniques.filter(t => t.id !== id);
    saveState();
    renderCurrentTab();
  }
  function updateTechnique(id, field, value) {
    const t = state.techniques.find(t => t.id === id);
    if (!t) return;
    t[field] = field === 'cost' ? (parseInt(value) || 0) : value;
    saveState();
  }

  // ── Domain ────────────────────────────────────────────────
  function openDomain() {
    const d = state.domain;
    if (d.active || d.cooldownRemaining > 0) return;
    if (state.energy.current < d.energyCost) {
      alert('พลังจิตไม่พอสำหรับเปิดอาณาเขต (ต้องการ ' + d.energyCost + ')');
      return;
    }
    state.energy.current = clamp(state.energy.current - d.energyCost, 0, state.energy.max);
    d.active = true;
    d.cooldownRemaining = d.cooldownMax;
    saveState();
    renderCurrentTab();
  }
  function closeDomain() {
    state.domain.active = false;
    saveState();
    renderCurrentTab();
  }
  function tickDomain() {
    const d = state.domain;
    if (d.cooldownRemaining > 0) d.cooldownRemaining -= 1;
    state.energy.current = clamp(state.energy.current + state.energy.regen, 0, state.energy.max);
    saveState();
    renderCurrentTab();
  }

  // ── Vows ──────────────────────────────────────────────────
  function addVow() {
    state.vows.push({ id: genId(), name: '', restriction: '', benefit: '', active: false });
    saveState();
    renderCurrentTab();
  }
  function removeVow(id) {
    state.vows = state.vows.filter(v => v.id !== id);
    saveState();
    renderCurrentTab();
  }
  function updateVow(id, field, value) {
    const v = state.vows.find(v => v.id === id);
    if (v) { v[field] = value; saveState(); }
  }
  function toggleVowActive(id) {
    const v = state.vows.find(v => v.id === id);
    if (v) { v.active = !v.active; saveState(); renderCurrentTab(); }
  }

  // ── Combat ────────────────────────────────────────────────
  function blackFlashDelta(delta, field) {
    state.combat[field] = Math.max(0, (state.combat[field] || 0) + delta);
    saveState();
    const totalEl = document.getElementById('jce-bf-total');
    const streakEl = document.getElementById('jce-bf-streak');
    if (totalEl) totalEl.textContent = state.combat.blackFlash;
    if (streakEl) streakEl.textContent = state.combat.blackFlashStreak;
  }
  function resetBlackFlashStreak() {
    state.combat.blackFlashStreak = 0;
    saveState();
    renderCurrentTab();
  }
  function updateCombatField(field, value) { state.combat[field] = value; saveState(); }

  // ── Export ────────────────────────────────────────────────
  function generateSheet() {
    const p = state.profile, e = state.energy, d = state.domain, c = state.combat;
    const grade = GRADES.find(g => g.id === p.grade);
    const pct = clamp(Math.round((e.current / Math.max(1, e.max)) * 100), 0, 100);
    const domainType = DOMAIN_TYPES.find(t => t.id === d.type);

    let s = '';
    s += `═══════════════════════════════════════════\n`;
    s += `   【呪術師ステータス / Jujutsu Sorcerer Status】\n`;
    s += `           ✦ ${p.name || '(ยังไม่ได้ตั้งชื่อ)'} ✦\n`;
    s += `═══════════════════════════════════════════\n\n`;

    s += `■ 基本情報 / Basic Info\n`;
    s += `名前 (Name)      : ${p.name || '—'}\n`;
    s += `称号 (Title)     : ${p.title || '—'}\n`;
    s += `所属 (School)    : ${p.school || '—'}\n`;
    s += `等級 (Grade)     : ${grade ? grade.name : p.grade}\n`;
    if (p.innateName) s += `固有術式 (Innate) : ${p.innateName}${p.innateDesc ? ' — ' + p.innateDesc : ''}\n`;
    if (p.appearance) s += `外見 (Appearance) :\n${p.appearance}\n`;

    s += `\n■ 呪力 / Cursed Energy\n`;
    s += `現在値 (Current)   : ${e.current} / ${e.max} (${pct}%)\n`;
    s += `自然回復 (Regen)   : +${e.regen} / เทิร์น\n`;

    if (state.techniques.length > 0) {
      s += `\n■ 術式 / Cursed Techniques\n`;
      state.techniques.forEach((t, i) => {
        const type = TECH_TYPES.find(ty => ty.id === t.type);
        s += `  ${i + 1}. ${t.name || '(ไม่มีชื่อ)'} [${type ? type.label : t.type}] (ต้นทุน ${t.cost || 0})\n`;
        if (t.desc) s += `     └ ${t.desc}\n`;
      });
    }

    s += `\n■ 領域展開 / Domain\n`;
    s += `名前 (Name)        : ${d.name || '—'}\n`;
    s += `種類 (Type)        : ${domainType ? domainType.label : d.type}\n`;
    s += `必中効果 (Sure-Hit) : ${d.sureHit ? 'ใช่' : 'ไม่ใช่'}\n`;
    s += `消費呪力 (Cost)     : ${d.energyCost}\n`;
    s += `状態 (Status)       : ${d.active ? 'เปิดใช้งานอยู่' : d.cooldownRemaining > 0 ? `พักฟื้น (${d.cooldownRemaining}/${d.cooldownMax} เทิร์น)` : 'พร้อมใช้งาน'}\n`;
    if (d.desc) s += `説明 (Effect)       :\n${d.desc}\n`;

    if (state.vows.length > 0) {
      s += `\n■ 縛り / Binding Vows\n`;
      state.vows.forEach((v, i) => {
        if (!v.name) return;
        s += `  ${i + 1}. ${v.name} [${v.active ? 'ใช้งานอยู่' : 'ไม่ได้ใช้งาน'}]\n`;
        if (v.restriction) s += `     ข้อจำกัด : ${v.restriction}\n`;
        if (v.benefit)     s += `     ผลตอบแทน: ${v.benefit}\n`;
      });
    }

    s += `\n■ 戦績 / Combat Stats\n`;
    s += `黒閃 (Black Flash) : รวม ${c.blackFlash} ครั้ง (สตรีคปัจจุบัน ${c.blackFlashStreak})\n`;
    const rctLevel = RCT_LEVELS.find(l => l.id === c.rctLevel);
    s += `反転術式 (RCT)      : ${c.rctActive ? 'กำลังใช้งาน' : 'ไม่ได้ใช้งาน'}${c.rctActive && rctLevel ? ' — ' + rctLevel.label : ''}\n`;
    if (c.rctNote) s += `  └ ${c.rctNote}\n`;
    if (c.log) s += `\n【บันทึกการต่อสู้ล่าสุด】\n${c.log}\n`;

    s += `\n═══════════════════════════════════════════\n`;
    s += `Generated by JJK Cursed Energy System\n`;
    s += `呪術廻戦 — 領域展開\n`;
    s += `═══════════════════════════════════════════`;
    return s;
  }

  function copySheet() {
    const sheet = generateSheet();
    navigator.clipboard.writeText(sheet).then(showCopySuccess).catch(() => {
      const ta = document.createElement('textarea');
      ta.value = sheet;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      showCopySuccess();
    });
  }
  function showCopySuccess() {
    const el = document.getElementById('export-success');
    if (el) { el.style.display = 'block'; setTimeout(() => { el.style.display = 'none'; }, 3000); }
  }

  function sendToChat() {
    const sheet = generateSheet();
    const selectors = ['#send_textarea', '#chat-input', '.send_textarea', '#user-input'];
    for (const sel of selectors) {
      const el = document.querySelector(sel);
      if (el) {
        el.value = `[Cursed Energy Status]\n${sheet}`;
        el.dispatchEvent(new Event('input', { bubbles: true }));
        el.focus();
        close();
        return;
      }
    }
    copySheet();
    alert('ไม่พบช่องข้อความของ SillyTavern — คัดลอกไปยัง clipboard แล้ว วางในช่องข้อความด้วยตนเอง');
  }

  function downloadSheet() {
    const sheet = generateSheet();
    const name = (state.profile.name || 'sorcerer').replace(/\s+/g, '_');
    const blob = new Blob([sheet], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${name}_cursed_energy.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  function resetAll() {
    if (!confirm('ลบข้อมูลทั้งหมดของตัวละครนี้และเริ่มใหม่?')) return;
    state = defaultState();
    saveState();
    renderCurrentTab();
  }

  // ── Utility ───────────────────────────────────────────────
  function esc(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // ── Bootstrap ─────────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    setTimeout(init, 500);
  }
})();
