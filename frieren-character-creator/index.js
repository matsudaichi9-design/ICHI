/* ══════════════════════════════════════════════════════════
   Frieren RPG Character Creator — SillyTavern Extension
   ══════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  // ── Constants ─────────────────────────────────────────────
  const RACES = [
    {
      id: 'human', icon: '👤',
      name: '人間 Human',
      desc: 'สายพันธุ์ที่ปรับตัวได้ดี มีความสามารถรอบด้าน',
      bonus: 'ค่าสถานะสมดุล / +2 ได้ 1 ค่า',
      statBonus: {}
    },
    {
      id: 'elf', icon: '🧝',
      name: 'エルフ Elf',
      desc: 'สายพันธุ์อายุยืนหลายศตวรรษ ทรงจำที่ยาวนาน เชี่ยวชาญเวทมนตร์',
      bonus: 'INT +3, WIS +2, STR −1',
      statBonus: { INT: 3, WIS: 2, STR: -1 }
    },
    {
      id: 'dwarf', icon: '⚒️',
      name: 'ドワーフ Dwarf',
      desc: 'สายพันธุ์นักรบอายุยืน ร่างกายแข็งแกร่ง เชี่ยวชาญงานฝีมือ',
      bonus: 'STR +3, CON +2, DEX −1',
      statBonus: { STR: 3, CON: 2, DEX: -1 }
    },
    {
      id: 'demon', icon: '👹',
      name: '魔族 Demon',
      desc: 'สายพันธุ์มีเวทมนตร์โดยกำเนิด ไม่มีอารมณ์แท้จริง อ่านใจมนุษย์ได้',
      bonus: 'INT +4, CHA +3, WIS −2',
      statBonus: { INT: 4, CHA: 3, WIS: -2 }
    },
    {
      id: 'half_elf', icon: '🧬',
      name: 'ハーフエルフ Half-Elf',
      desc: 'ลูกผสมระหว่างมนุษย์และเอลฟ์ รับคุณสมบัติทั้งสองสาย',
      bonus: 'INT +2, WIS +1, DEX +1',
      statBonus: { INT: 2, WIS: 1, DEX: 1 }
    },
    {
      id: 'spirit', icon: '✨',
      name: '精霊 Spirit',
      desc: 'สิ่งมีชีวิตทางเวทมนตร์ ผูกพันกับพลังธรรมชาติและโลกวิญญาณ',
      bonus: 'WIS +5, CON −2',
      statBonus: { WIS: 5, CON: -2 }
    }
  ];

  const CLASSES = [
    {
      id: 'mage', icon: '🔮',
      name: '魔法使い Mage',
      desc: 'เชี่ยวชาญเวทมนตร์ แต่ละคนมีเวทเอกลักษณ์เฉพาะตัว',
      subClasses: ['Offensive Mage', 'Defensive Mage', 'Support Mage', 'Ancient Magic User', 'Sage', 'Battle Mage'],
      ranks: ['見習い Apprentice', '登録 Registered Mage', '一級 First-Class Mage', '伝説 Legendary Mage']
    },
    {
      id: 'warrior', icon: '⚔️',
      name: '戦士 Warrior',
      desc: 'นักรบผู้เชี่ยวชาญการต่อสู้ใกล้ชิด สายกล้ามเนื้อและเทคนิค',
      subClasses: ['Sword Fighter', 'Great Sword', 'Shield Bearer', 'Berserker', 'Duelist', 'Spearman'],
      ranks: ['Novice', 'Fighter', 'Veteran Warrior', 'Legendary Hero']
    },
    {
      id: 'holy_warrior', icon: '🛡️',
      name: '聖騎士 Holy Warrior',
      desc: 'ผสมผสานทักษะการต่อสู้กับเวทมนตร์แสงศักดิ์สิทธิ์',
      subClasses: ['Paladin', 'Templar', 'Divine Knight', 'Inquisitor'],
      ranks: ['Squire', 'Knight', 'Holy Knight', 'Divine Champion']
    },
    {
      id: 'priest', icon: '⛪',
      name: '僧侶 Priest',
      desc: 'ผู้รักษาและผู้ปกป้อง ใช้เวทมนตร์แห่งความศักดิ์สิทธิ์เพื่อช่วยเหลือผู้อื่น',
      subClasses: ['Healer', 'Exorcist', 'Spirit Caller', 'Battle Priest', 'Archbishop'],
      ranks: ['Acolyte', 'Priest', 'High Priest', 'Archbishop']
    },
    {
      id: 'scout', icon: '🗡️',
      name: '斥候 Scout',
      desc: 'ผู้เชี่ยวชาญการลาดตระเวน โจมตีเร็ว และการเอาตัวรอด',
      subClasses: ['Rogue', 'Assassin', 'Ranger', 'Tracker', 'Spy'],
      ranks: ['Beginner', 'Scout', 'Shadow', 'Phantom']
    },
    {
      id: 'craftsman', icon: '🔨',
      name: '職人 Craftsman',
      desc: 'ผู้สร้างสิ่งของมหัศจรรย์ อาวุธและอุปกรณ์เวทมนตร์',
      subClasses: ['Blacksmith', 'Enchanter', 'Runesmith', 'Alchemist', 'Artificer'],
      ranks: ['Apprentice', 'Journeyman', 'Master Craftsman', 'Grandmaster']
    }
  ];

  const MAGIC_AFFINITIES = [
    { id: 'offensive',  icon: '💥', name: '攻撃魔法 Offensive',  desc: 'เวทโจมตีรูปแบบต่างๆ' },
    { id: 'defensive',  icon: '🛡️', name: '防壁魔法 Defensive',  desc: 'เวทป้องกันและกำแพง' },
    { id: 'healing',    icon: '💚', name: '回復魔法 Healing',     desc: 'เวทรักษาและฟื้นฟู' },
    { id: 'support',    icon: '⭐', name: '補助魔法 Support',    desc: 'เวทเสริมพลัง' },
    { id: 'illusion',   icon: '🌫️', name: '幻影魔法 Illusion',   desc: 'เวทหลอกประสาท' },
    { id: 'binding',    icon: '⛓️', name: '拘束魔法 Binding',    desc: 'เวทจับกุมและควบคุม' },
    { id: 'ancient',    icon: '📜', name: '古代魔法 Ancient',    desc: 'เวทยุคโบราณหายาก' },
    { id: 'nature',     icon: '🌿', name: '自然魔法 Nature',     desc: 'เวทควบคุมธรรมชาติ' },
    { id: 'necromancy', icon: '💀', name: '死霊魔法 Necromancy', desc: 'เวทแห่งความตาย' },
    { id: 'spatial',    icon: '🌀', name: '空間魔法 Spatial',    desc: 'เวทควบคุมพื้นที่-มิติ' }
  ];

  const PERSONALITIES = [
    'เงียบขรึม', 'อารมณ์ดี', 'ลึกลับ', 'ตรงไปตรงมา', 'ขี้อาย',
    'กล้าหาญ', 'รอบคอบ', 'อ่อนโยน', 'แข็งกร้าว', 'ช่างสังเกต',
    'ใจดี', 'เฉลียวฉลาด', 'ขี้เล่น', 'จริงจัง', 'ฉลาดแกมโกง',
    'ซื่อสัตย์', 'ทะเยอทะยาน', 'สุขุมเยือกเย็น', 'หุนหันพลันแล่น', 'อดทน',
    'เสียสละ', 'ชอบสำรวจ', 'ชอบอยู่คนเดียว', 'ชอบสังสรรค์', 'นักต่อสู้'
  ];

  const ORIGINS = [
    'เมืองหลวงราชอาณาจักร', 'หมู่บ้านชายแดน', 'ป่าเอลฟ์โบราณ',
    'เหมืองแร่ดวาร์ฟ', 'อาณาจักรมาร', 'เมืองท่าชายทะเล',
    'ที่ราบสูงกลางทวีป', 'ซากปรักหักพังโบราณ', 'อารามนักบวช',
    'หอคอยเวทมนตร์', 'เมืองพ่อค้า', 'ป่าลึกลับ',
    'ทะเลทราย', 'ภูเขาหิมะ', 'ไม่ทราบที่มา'
  ];

  const REL_TYPES = [
    'สมาชิกปาร์ตี้', 'ครู/อาจารย์', 'ศิษย์', 'เพื่อนสนิท',
    'คู่รัก', 'คู่แข่ง', 'ศัตรู', 'ญาติพี่น้อง',
    'ผู้อุปถัมภ์', 'เพื่อนเก่า', 'ผู้ล่วงลับ (ในความทรงจำ)'
  ];

  const STAT_META = {
    STR: { label: 'STR', full: 'Strength',     icon: '💪', cls: 'str' },
    INT: { label: 'INT', full: 'Intelligence',  icon: '🧠', cls: 'int' },
    WIS: { label: 'WIS', full: 'Wisdom',        icon: '👁️', cls: 'wis' },
    DEX: { label: 'DEX', full: 'Dexterity',     icon: '🏃', cls: 'dex' },
    CON: { label: 'CON', full: 'Constitution',  icon: '🛡️', cls: 'con' },
    CHA: { label: 'CHA', full: 'Charisma',      icon: '✨', cls: 'cha' }
  };

  const STEPS = [
    { title: 'ยินดีต้อนรับ',              icon: '⭐' },
    { title: 'ข้อมูลพื้นฐาน',             icon: '👤' },
    { title: 'คลาส & อาชีพ',             icon: '⚔️' },
    { title: 'เวทมนตร์ & ความสามารถ',    icon: '✨' },
    { title: 'ทักษะ & ความเชี่ยวชาญ',   icon: '📚' },
    { title: 'ค่าสถานะ',                  icon: '📊' },
    { title: 'ประวัติ & บุคลิก',          icon: '📖' },
    { title: 'ความสัมพันธ์',              icon: '🤝' },
    { title: 'อาวุธ & อุปกรณ์',          icon: '🗡️' },
    { title: 'สรุป & ส่งออก',            icon: '📜' }
  ];

  const TOTAL_POINTS = 72;
  const STAT_MIN = 5;
  const STAT_MAX = 20;

  // ── State ──────────────────────────────────────────────────
  let currentStep = 0;
  let char = {
    basic:    { name: '', age: '', gender: '', race: 'human', height: '', eyeColor: '', hairColor: '', appearance: '' },
    classInfo:{ cls: '', subClass: '', rank: '', guild: '', level: 1 },
    magic:    { affinity: [], signatureSpells: [], uniqueAbility: '', manaCapacity: 'normal' },
    skills:   [],
    stats:    { STR: 10, INT: 10, WIS: 10, DEX: 10, CON: 10, CHA: 10 },
    background:{ origin: '', backstory: '', personality: [], goals: '', fears: '' },
    relationships: [],
    equipment: { primaryWeapon: '', secondaryWeapon: '', armor: '', staff: '', accessories: '', specialItem: '' }
  };

  function usedPoints() {
    return Object.values(char.stats).reduce((a, b) => a + b, 0);
  }
  function remainingPoints() {
    return TOTAL_POINTS - usedPoints() + 60; // 60 = base (6 × 10)
  }

  // ── Init ───────────────────────────────────────────────────
  function init() {
    injectButton();
    injectModal();
    window.FrierenCreator = {
      open, close, navigate, goStep,
      updateChar, selectRace, selectClass, toggleAffinity,
      addSpell, removeSpell, updateSpell,
      addSkill, removeSkill,
      changeStat,
      togglePersonality,
      addRelationship, removeRelationship, updateRel,
      copySheet, sendToChat, downloadSheet,
      closeIfOverlay
    };
  }

  function injectButton() {
    const btn = document.createElement('div');
    btn.id = 'frieren-trigger';
    btn.innerHTML = '<span>✦</span> Frieren RPG';
    btn.title = 'สร้างตัวละคร Frieren RPG';
    btn.onclick = open;

    const targets = [
      '#extensionsMenuButton',
      '#extension_floating_menu',
      '#top-bar',
      '.flex-container.flexGap5',
      '#leftSendForm',
      'body'
    ];
    let placed = false;
    for (const sel of targets) {
      const el = document.querySelector(sel);
      if (el && el !== document.body) {
        el.appendChild(btn);
        placed = true;
        break;
      }
    }
    if (!placed) {
      btn.style.cssText = 'position:fixed;top:10px;right:10px;z-index:9998;';
      document.body.appendChild(btn);
    }
  }

  function injectModal() {
    const wrap = document.createElement('div');
    wrap.id = 'frieren-creator-modal';
    wrap.style.display = 'none';
    wrap.innerHTML = buildModalHTML();
    document.body.appendChild(wrap);
  }

  function buildModalHTML() {
    const dots = STEPS.map((s, i) => `
      <div class="step-dot ${i === 0 ? 'active' : ''}" data-step="${i}">
        <div class="step-dot-inner">${s.icon}</div>
        <span class="step-dot-label">${s.title}</span>
      </div>
      ${i < STEPS.length - 1 ? '<div class="step-line" id="step-line-' + i + '"></div>' : ''}
    `).join('');

    return `
    <div id="frieren-overlay" onclick="window.FrierenCreator.closeIfOverlay(event)">
      <div id="frieren-creator">
        <button class="frieren-close" onclick="window.FrierenCreator.close()">✕</button>
        <div class="frieren-header">
          <div class="header-runes">ᚠᚱᛁᛖᚱᛖᚾ · ᛒᛖᛃᛟᚾᛞ · ᛃᛟᚢᚱᚾᛖᛃ᛫ᛊ · ᛖᚾᛞ</div>
          <h1>Sousou no Frieren</h1>
          <p>葬送のフリーレン — RPG Character Creator</p>
        </div>
        <div class="step-progress">${dots}</div>
        <div class="step-title-bar"><h3 id="frieren-step-title">${STEPS[0].title}</h3></div>
        <div class="step-content" id="frieren-step-content"></div>
        <div class="frieren-nav">
          <button id="frieren-back" class="nav-btn back-btn" onclick="window.FrierenCreator.navigate(-1)">← กลับ</button>
          <span class="step-counter" id="frieren-step-counter">1 / ${STEPS.length}</span>
          <button id="frieren-next" class="nav-btn next-btn" onclick="window.FrierenCreator.navigate(1)">ถัดไป →</button>
        </div>
      </div>
    </div>`;
  }

  // ── Open / Close ───────────────────────────────────────────
  function open() {
    const m = document.getElementById('frieren-creator-modal');
    if (m) { m.style.display = 'block'; renderCurrentStep(); }
  }
  function close() {
    const m = document.getElementById('frieren-creator-modal');
    if (m) m.style.display = 'none';
  }
  function closeIfOverlay(e) {
    if (e.target.id === 'frieren-overlay') close();
  }

  // ── Navigation ─────────────────────────────────────────────
  function navigate(dir) {
    const next = currentStep + dir;
    if (next < 0 || next >= STEPS.length) return;
    goStep(next);
  }

  function goStep(n) {
    currentStep = n;
    renderCurrentStep();
    updateProgressUI();
  }

  function updateProgressUI() {
    const dots = document.querySelectorAll('.step-dot');
    dots.forEach((d, i) => {
      d.classList.toggle('active', i === currentStep);
      d.classList.toggle('completed', i < currentStep);
    });
    for (let i = 0; i < STEPS.length - 1; i++) {
      const line = document.getElementById('step-line-' + i);
      if (line) line.classList.toggle('completed', i < currentStep);
    }
    const titleEl = document.getElementById('frieren-step-title');
    if (titleEl) titleEl.textContent = STEPS[currentStep].title;

    const counterEl = document.getElementById('frieren-step-counter');
    if (counterEl) counterEl.textContent = `${currentStep + 1} / ${STEPS.length}`;

    const back = document.getElementById('frieren-back');
    const next = document.getElementById('frieren-next');
    if (back) back.style.visibility = currentStep === 0 ? 'hidden' : 'visible';
    if (next) {
      next.textContent = currentStep === STEPS.length - 1 ? '✦ เสร็จสิ้น' : 'ถัดไป →';
      next.className = 'nav-btn next-btn' + (currentStep === STEPS.length - 1 ? ' finish-btn' : '');
    }
  }

  function renderCurrentStep() {
    const el = document.getElementById('frieren-step-content');
    if (!el) return;
    el.innerHTML = '';
    const panel = document.createElement('div');
    panel.className = 'step-panel';
    panel.innerHTML = getStepHTML(currentStep);
    el.appendChild(panel);
    attachStepListeners(currentStep);
    updateProgressUI();
  }

  // ── Step HTML Generators ───────────────────────────────────
  function getStepHTML(step) {
    switch (step) {
      case 0: return stepWelcome();
      case 1: return stepBasicInfo();
      case 2: return stepClass();
      case 3: return stepMagic();
      case 4: return stepSkills();
      case 5: return stepStats();
      case 6: return stepBackground();
      case 7: return stepRelationships();
      case 8: return stepEquipment();
      case 9: return stepSummary();
      default: return '';
    }
  }

  function stepWelcome() {
    return `
    <div class="welcome-screen">
      <div class="magic-circle">
        <div class="magic-ring r1"></div>
        <div class="magic-ring r2"></div>
        <div class="magic-ring r3"></div>
        <div class="magic-center">✦</div>
      </div>
      <h2>ยินดีต้อนรับสู่โลกของ Frieren</h2>
      <p class="welcome-quote">"เวทมนตร์คือสิ่งที่คุณสามารถพัฒนาได้เรื่อยๆ ไม่ว่าจะผ่านไปกี่ร้อยปี..."<br><em>— Frieren, Arch-Mage</em></p>
      <p class="welcome-desc">
        สร้างตัวละครของคุณในโลกแฟนตาซีของ <strong style="color:var(--fr-gold)">葬送のフリーレン</strong><br>
        ระบบนี้ครอบคลุมทุกด้านของตัวละคร ตั้งแต่เผ่าพันธุ์ คลาส เวทมนตร์เฉพาะตัว<br>
        ไปจนถึงประวัติชีวิต บุคลิกภาพ และความสัมพันธ์กับผู้อื่น
      </p>
      <div class="welcome-features">
        <div class="welcome-feature">👤 ตัวตนเฉพาะตัว</div>
        <div class="welcome-feature">✨ เวทมนตร์ไม่ซ้ำใคร</div>
        <div class="welcome-feature">📊 ระบบค่าสถานะ</div>
        <div class="welcome-feature">📖 เรื่องราวชีวิต</div>
        <div class="welcome-feature">🤝 ความสัมพันธ์</div>
        <div class="welcome-feature">📜 Export ทุกรูปแบบ</div>
      </div>
    </div>`;
  }

  function stepBasicInfo() {
    const raceCards = RACES.map(r => `
      <div class="race-card ${char.basic.race === r.id ? 'selected' : ''}"
           onclick="window.FrierenCreator.selectRace('${r.id}', this)">
        <div class="race-icon">${r.icon}</div>
        <div class="race-name">${r.name}</div>
        <div class="race-desc">${r.desc}</div>
        <div class="race-bonus">✦ ${r.bonus}</div>
      </div>`).join('');

    return `
    <div class="form-section">
      <div class="form-row">
        <div class="form-group">
          <label>ชื่อ <span class="required">*</span></label>
          <input id="fi-name" type="text" class="frieren-input" placeholder="ชื่อตัวละคร..." value="${esc(char.basic.name)}">
        </div>
        <div class="form-group">
          <label>อายุ</label>
          <input id="fi-age" type="text" class="frieren-input" placeholder="เช่น 28 หรือ ~1200 (เอลฟ์)" value="${esc(char.basic.age)}">
        </div>
      </div>

      <div class="form-group">
        <label>เพศ</label>
        <div class="gender-options">
          ${['ชาย','หญิง','ไม่ระบุ','อื่นๆ'].map(g => `
            <label class="radio-card ${char.basic.gender === g ? 'selected' : ''}">
              <input type="radio" name="fi-gender" value="${g}" ${char.basic.gender === g ? 'checked' : ''}>${g}
            </label>`).join('')}
        </div>
      </div>

      <div class="form-group">
        <label>เผ่าพันธุ์ <span class="required">*</span></label>
        <div class="race-grid">${raceCards}</div>
      </div>

      <div class="form-row">
        <div class="form-group">
          <label>ส่วนสูง</label>
          <input id="fi-height" type="text" class="frieren-input" placeholder="เช่น 165 ซม." value="${esc(char.basic.height)}">
        </div>
        <div class="form-group">
          <label>สีตา</label>
          <input id="fi-eye" type="text" class="frieren-input" placeholder="เช่น ฟ้าอมเขียว" value="${esc(char.basic.eyeColor)}">
        </div>
        <div class="form-group">
          <label>สีผม</label>
          <input id="fi-hair" type="text" class="frieren-input" placeholder="เช่น เงิน/ขาว" value="${esc(char.basic.hairColor)}">
        </div>
      </div>

      <div class="form-group">
        <label>รูปลักษณ์ภายนอก</label>
        <textarea id="fi-appearance" class="frieren-textarea" placeholder="บรรยายลักษณะที่มองเห็น เช่น เสื้อผ้า รอยแผลเป็น สัญลักษณ์พิเศษ..." rows="3">${esc(char.basic.appearance)}</textarea>
      </div>
    </div>`;
  }

  function stepClass() {
    const classCards = CLASSES.map(c => `
      <div class="class-card ${char.classInfo.cls === c.id ? 'selected' : ''}"
           onclick="window.FrierenCreator.selectClass('${c.id}', this)">
        <div class="class-icon">${c.icon}</div>
        <div class="class-name">${c.name}</div>
        <div class="class-desc">${c.desc}</div>
      </div>`).join('');

    const selClass = CLASSES.find(c => c.id === char.classInfo.cls);
    const showDetail = !!selClass;

    return `
    <div class="form-section">
      <div class="form-group">
        <label>เลือกคลาส / อาชีพ <span class="required">*</span></label>
        <div class="class-grid">${classCards}</div>
      </div>

      <div id="class-detail-panel" class="class-details-panel" style="${showDetail ? '' : 'display:none'}">
        <div class="form-row">
          <div class="form-group">
            <label>ความเชี่ยวชาญ / สายย่อย</label>
            <select id="ci-subclass" class="frieren-select">
              <option value="">-- เลือกความเชี่ยวชาญ --</option>
              ${(selClass?.subClasses || []).map(s => `<option value="${s}" ${char.classInfo.subClass === s ? 'selected' : ''}>${s}</option>`).join('')}
            </select>
          </div>
          <div class="form-group">
            <label>ยศ / ระดับ</label>
            <select id="ci-rank" class="frieren-select">
              <option value="">-- เลือกยศ --</option>
              ${(selClass?.ranks || []).map(r => `<option value="${r}" ${char.classInfo.rank === r ? 'selected' : ''}>${r}</option>`).join('')}
            </select>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>กิลด์ / สังกัด / สังกัดราชการ</label>
            <input id="ci-guild" type="text" class="frieren-input" placeholder="เช่น Magic Guild ประจำเมือง Äußerst" value="${esc(char.classInfo.guild)}">
          </div>
          <div class="form-group">
            <label>ระดับ (Level)</label>
            <input id="ci-level" type="number" class="frieren-input" min="1" max="100" value="${char.classInfo.level}">
          </div>
        </div>
      </div>
    </div>`;
  }

  function stepMagic() {
    const affCards = MAGIC_AFFINITIES.map(a => `
      <div class="affinity-card ${char.magic.affinity.includes(a.id) ? 'selected' : ''}"
           onclick="window.FrierenCreator.toggleAffinity('${a.id}', this)">
        <div class="aff-icon">${a.icon}</div>
        <div class="aff-info">
          <div class="aff-name">${a.name}</div>
          <div class="aff-desc">${a.desc}</div>
        </div>
      </div>`).join('');

    const spellLevels = ['E','D','C','B','A','S','SS'];
    const spellItems = char.magic.signatureSpells.map((sp, i) => `
      <div class="spell-item" id="spell-${i}">
        <div class="spell-item-header">
          <div class="spell-number">${i + 1}</div>
          <input type="text" class="frieren-input" style="flex:1" placeholder="ชื่อเวทมนตร์ เช่น Zoltraak" value="${esc(sp.name)}"
                 onchange="window.FrierenCreator.updateSpell(${i},'name',this.value)">
          <select class="frieren-select spell-level-select"
                  onchange="window.FrierenCreator.updateSpell(${i},'level',this.value)">
            ${spellLevels.map(l => `<option value="${l}" ${sp.level === l ? 'selected' : ''}>Rank ${l}</option>`).join('')}
          </select>
          <button class="spell-remove" onclick="window.FrierenCreator.removeSpell(${i})">✕</button>
        </div>
        <textarea class="frieren-textarea" rows="2" placeholder="อธิบายผลของเวทมนตร์..."
                  onchange="window.FrierenCreator.updateSpell(${i},'desc',this.value)">${esc(sp.desc)}</textarea>
      </div>`).join('');

    return `
    <div class="form-section">
      <div class="info-note">💡 ในโลกของ Frieren เวทมนตร์แต่ละอย่างมีเอกลักษณ์ของผู้ใช้ ตัวละครที่ดีมักมี <strong>เวทเฉพาะตัว</strong> ที่ไม่ซ้ำใคร แม้จะใช้ชื่อเดียวกัน</div>

      <div class="form-group">
        <label>ความถนัดทางเวทมนตร์ (เลือกได้หลายอย่าง)</label>
        <div class="affinity-grid">${affCards}</div>
      </div>

      <div class="section-divider"></div>

      <div class="form-group">
        <label>เวทมนตร์ประจำตัว / Signature Spells</label>
        <div id="spell-list">${spellItems}</div>
        <button class="add-btn" onclick="window.FrierenCreator.addSpell()">+ เพิ่มเวทมนตร์</button>
      </div>

      <div class="section-divider"></div>

      <div class="form-group">
        <label>ความสามารถพิเศษ / Unique Ability</label>
        <textarea id="mg-unique" class="frieren-textarea" rows="3"
          placeholder="ความสามารถที่เป็นเอกลักษณ์เฉพาะตัว เช่น ความสามารถในการดูดซับเวทของศัตรู หรือตา Sense Magic...">${esc(char.magic.uniqueAbility)}</textarea>
      </div>

      <div class="form-group">
        <label>ขนาดแหล่งพลังงานเวทมนตร์ (Mana Pool)</label>
        <select id="mg-mana" class="frieren-select">
          <option value="tiny" ${char.magic.manaCapacity==='tiny'?'selected':''}>น้อยมาก (ใช้ได้ไม่กี่ครั้ง)</option>
          <option value="small" ${char.magic.manaCapacity==='small'?'selected':''}>น้อย (ต่ำกว่าเฉลี่ย)</option>
          <option value="normal" ${char.magic.manaCapacity==='normal'?'selected':''}>ปกติ (เฉลี่ยมนุษย์)</option>
          <option value="large" ${char.magic.manaCapacity==='large'?'selected':''}>มาก (นักเวทมนตร์ชำนาญ)</option>
          <option value="massive" ${char.magic.manaCapacity==='massive'?'selected':''}>มหาศาล (ระดับตำนาน)</option>
          <option value="bottomless" ${char.magic.manaCapacity==='bottomless'?'selected':''}>ไร้ขีดจำกัด (ระดับเทพ)</option>
        </select>
      </div>
    </div>`;
  }

  function stepSkills() {
    const tags = char.skills.map((sk, i) => `
      <div class="skill-tag">
        ${esc(sk)}
        <button class="skill-tag-remove" onclick="window.FrierenCreator.removeSkill(${i})">×</button>
      </div>`).join('');

    return `
    <div class="form-section">
      <div class="info-note">📚 ทักษะและความเชี่ยวชาญที่สะสมมาจากประสบการณ์จริง ทั้งการต่อสู้ การเอาตัวรอด และทักษะชีวิต</div>

      <div class="form-group">
        <label>เพิ่มทักษะ</label>
        <div class="skill-input-row">
          <input id="skill-input" type="text" class="frieren-input" placeholder="เช่น การใช้ดาบสองมือ, ร่ายเวทขณะวิ่ง, ปีนป่าย..."
                 onkeydown="if(event.key==='Enter'){window.FrierenCreator.addSkill();event.preventDefault()}">
          <button class="add-skill-btn" onclick="window.FrierenCreator.addSkill()">+</button>
        </div>
        <div id="skill-tags" class="skill-tags" style="margin-top:10px">${tags}</div>
      </div>

      <div class="section-divider"></div>

      <div class="info-note" style="margin-top:0">
        💡 ตัวอย่างทักษะ: การตรวจสอบกับดัก | การวางแผนเส้นทาง | การเจรจาต่อรอง | การรักษาบาดแผล | การอ่านเวทโบราณ | การทำอาหารในป่า
      </div>
    </div>`;
  }

  function stepStats() {
    const rem = remainingPoints();
    const statRows = Object.entries(STAT_META).map(([key, m]) => {
      const val = char.stats[key];
      const pct = ((val - STAT_MIN) / (STAT_MAX - STAT_MIN)) * 100;
      return `
      <div class="stat-row">
        <div class="stat-icon">${m.icon}</div>
        <div class="stat-label"><strong>${m.label}</strong><span>${m.full}</span></div>
        <div class="stat-controls">
          <button class="stat-btn minus" onclick="window.FrierenCreator.changeStat('${key}',-1)">−</button>
          <div class="stat-value" id="sv-${key}">${val}</div>
          <button class="stat-btn plus" onclick="window.FrierenCreator.changeStat('${key}',1)">+</button>
          <div class="stat-bar-wrap">
            <div class="stat-bar ${m.cls}" id="sb-${key}" style="width:${pct}%"></div>
          </div>
        </div>
      </div>`;
    }).join('');

    const race = RACES.find(r => r.id === char.basic.race);
    const bonusText = race ? Object.entries(race.statBonus)
      .map(([k, v]) => `${k} ${v > 0 ? '+' : ''}${v}`).join(', ') : '';

    const hp  = char.stats.CON * 10 + char.stats.STR * 2;
    const mp  = char.stats.INT * 8  + char.stats.WIS * 5;
    const spd = char.stats.DEX * 3  + char.stats.STR;

    return `
    <div class="form-section">
      <div class="stats-header">
        <span class="points-pool">จุดที่เหลือ (Point Pool)</span>
        <span class="points-count" id="points-left">${rem}</span>
      </div>
      ${bonusText ? `<div class="info-note">✦ โบนัสเผ่า ${race.name}: <strong>${bonusText}</strong> (นับนอกเหนือจาก base stats)</div>` : ''}
      <div class="stats-grid">${statRows}</div>
      <div class="derived-stats">
        <div class="derived-stat"><span class="d-label">❤️ HP</span><div class="d-value" id="derived-hp">${hp}</div></div>
        <div class="derived-stat"><span class="d-label">💙 MP</span><div class="d-value" id="derived-mp">${mp}</div></div>
        <div class="derived-stat"><span class="d-label">⚡ Speed</span><div class="d-value" id="derived-spd">${spd}</div></div>
      </div>
    </div>`;
  }

  function stepBackground() {
    const persTags = PERSONALITIES.map(p => `
      <div class="pers-tag ${char.background.personality.includes(p) ? 'selected' : ''}"
           onclick="window.FrierenCreator.togglePersonality('${p}', this)">${p}</div>`).join('');

    return `
    <div class="form-section">
      <div class="form-row">
        <div class="form-group">
          <label>ต้นกำเนิด / บ้านเกิด</label>
          <select id="bg-origin" class="frieren-select">
            <option value="">-- เลือกที่มา --</option>
            ${ORIGINS.map(o => `<option value="${o}" ${char.background.origin===o?'selected':''}>${o}</option>`).join('')}
          </select>
        </div>
      </div>

      <div class="form-group">
        <label>บุคลิกลักษณะ (เลือกได้หลายอย่าง)</label>
        <div class="personality-grid">${persTags}</div>
      </div>

      <div class="form-group">
        <label>เป้าหมายในชีวิต</label>
        <textarea id="bg-goals" class="frieren-textarea" rows="2"
          placeholder="เช่น ต้องการรวบรวมเวทมนตร์ทุกอย่างที่มีอยู่บนโลก...">${esc(char.background.goals)}</textarea>
      </div>

      <div class="form-group">
        <label>จุดอ่อน / สิ่งที่กลัว</label>
        <textarea id="bg-fears" class="frieren-textarea" rows="2"
          placeholder="เช่น กลัวการสูญเสียเพื่อนที่มีอายุสั้นกว่า, อ่อนแอต่อเวทมนตร์ไฟ...">${esc(char.background.fears)}</textarea>
      </div>

      <div class="form-group">
        <label>เรื่องราวชีวิต / ประวัติ</label>
        <textarea id="bg-backstory" class="frieren-textarea" rows="5"
          placeholder="เล่าเรื่องราวชีวิตของตัวละคร จุดเปลี่ยนสำคัญ เหตุการณ์ที่หล่อหลอมตัวตน...">${esc(char.background.backstory)}</textarea>
      </div>
    </div>`;
  }

  function stepRelationships() {
    const items = char.relationships.map((r, i) => `
      <div class="rel-item">
        <div class="rel-item-header">
          <span class="rel-number">ความสัมพันธ์ที่ ${i + 1}</span>
          <button class="rel-remove" onclick="window.FrierenCreator.removeRelationship(${i})">✕ ลบ</button>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>ชื่อ</label>
            <input type="text" class="frieren-input" placeholder="ชื่อบุคคล..." value="${esc(r.name)}"
                   onchange="window.FrierenCreator.updateRel(${i},'name',this.value)">
          </div>
          <div class="form-group">
            <label>ประเภทความสัมพันธ์</label>
            <select class="frieren-select" onchange="window.FrierenCreator.updateRel(${i},'type',this.value)">
              <option value="">-- เลือก --</option>
              ${REL_TYPES.map(t => `<option value="${t}" ${r.type===t?'selected':''}>${t}</option>`).join('')}
            </select>
          </div>
        </div>
        <div class="form-group">
          <label>รายละเอียดความสัมพันธ์</label>
          <textarea class="frieren-textarea" rows="2"
            placeholder="บอกเล่าความสัมพันธ์ ประวัติร่วมกัน หรือสภาวะปัจจุบัน..."
            onchange="window.FrierenCreator.updateRel(${i},'desc',this.value)">${esc(r.desc)}</textarea>
        </div>
      </div>`).join('');

    return `
    <div class="form-section">
      <div class="info-note">🤝 บุคคลสำคัญในชีวิตของตัวละคร ทั้งพันธมิตร ศัตรู คนรัก หรือผู้ที่จากไปแล้ว</div>
      <div id="rel-list">${items}</div>
      <button class="add-btn" onclick="window.FrierenCreator.addRelationship()">+ เพิ่มความสัมพันธ์</button>
    </div>`;
  }

  function stepEquipment() {
    return `
    <div class="form-section">
      <div class="equip-section">
        <h4>⚔️ อาวุธ</h4>
        <div class="form-row">
          <div class="form-group">
            <label>อาวุธหลัก</label>
            <input id="eq-primary" type="text" class="frieren-input" placeholder="เช่น ดาบหนึ่งมือ Dübelritter" value="${esc(char.equipment.primaryWeapon)}">
          </div>
          <div class="form-group">
            <label>อาวุธรอง</label>
            <input id="eq-secondary" type="text" class="frieren-input" placeholder="เช่น มีดสั้น, โล่..." value="${esc(char.equipment.secondaryWeapon)}">
          </div>
        </div>
      </div>

      <div class="equip-section">
        <h4>🛡️ เกราะ & ผ้าคลุม</h4>
        <div class="form-group">
          <label>ชุดเกราะ / เสื้อผ้าสู้รบ</label>
          <input id="eq-armor" type="text" class="frieren-input" placeholder="เช่น เสื้อคลุมผ้าสีดำเสริมเวทมนตร์..." value="${esc(char.equipment.armor)}">
        </div>
      </div>

      <div class="equip-section">
        <h4>🔮 ไม้เท้า / ตัวเร่งเวทมนตร์</h4>
        <div class="form-group">
          <label>Staff / Wand / Catalyst (สำหรับนักเวท)</label>
          <input id="eq-staff" type="text" class="frieren-input" placeholder="เช่น ไม้เท้าโบราณเก็บเกี่ยวจากป่าเอลฟ์..." value="${esc(char.equipment.staff)}">
        </div>
      </div>

      <div class="equip-section">
        <h4>💍 ของวิเศษ & อุปกรณ์พิเศษ</h4>
        <div class="form-group">
          <label>แหวน สร้อย ของเสริม ฯลฯ</label>
          <textarea id="eq-accessories" class="frieren-textarea" rows="2"
            placeholder="เช่น แหวนป้องกันเวทมนตร์มืด, หินสีน้ำเงินที่เก็บรักษาความทรงจำ...">${esc(char.equipment.accessories)}</textarea>
        </div>
        <div class="form-group">
          <label>ไอเทมพิเศษ / สิ่งที่พกติดตัวเสมอ</label>
          <textarea id="eq-special" class="frieren-textarea" rows="2"
            placeholder="เช่น หนังสือจดบันทึกเวทเก่า, จดหมายจากอาจารย์, ตุ๊กตาผ้าที่เพื่อนทำให้...">${esc(char.equipment.specialItem)}</textarea>
        </div>
      </div>
    </div>`;
  }

  function stepSummary() {
    const sheet = generateCharacterSheet();
    return `
    <div class="form-section">
      <div class="info-note">📜 ตรวจสอบข้อมูลตัวละครของคุณ แล้วส่งออกเพื่อใช้งานใน SillyTavern</div>
      <div class="character-sheet-preview" id="char-sheet-preview">${esc(sheet)}</div>
      <div class="export-actions">
        <button class="export-btn copy" onclick="window.FrierenCreator.copySheet()">📋 คัดลอก</button>
        <button class="export-btn send" onclick="window.FrierenCreator.sendToChat()">💬 ส่งเข้า Chat</button>
        <button class="export-btn download" onclick="window.FrierenCreator.downloadSheet()">⬇️ ดาวน์โหลด</button>
      </div>
      <div class="export-success" id="export-success">✓ คัดลอกแล้ว!</div>
    </div>`;
  }

  // ── Attach Listeners Per Step ──────────────────────────────
  function attachStepListeners(step) {
    if (step === 1) {
      bind('fi-name',       v => char.basic.name       = v);
      bind('fi-age',        v => char.basic.age        = v);
      bind('fi-height',     v => char.basic.height     = v);
      bind('fi-eye',        v => char.basic.eyeColor   = v);
      bind('fi-hair',       v => char.basic.hairColor  = v);
      bind('fi-appearance', v => char.basic.appearance = v);
      document.querySelectorAll('input[name="fi-gender"]').forEach(r =>
        r.addEventListener('change', function () {
          char.basic.gender = this.value;
          document.querySelectorAll('.gender-options .radio-card').forEach(c => c.classList.remove('selected'));
          this.closest('.radio-card').classList.add('selected');
        }));
    }
    if (step === 2) {
      bind('ci-subclass', v => char.classInfo.subClass = v);
      bind('ci-rank',     v => char.classInfo.rank     = v);
      bind('ci-guild',    v => char.classInfo.guild    = v);
      bind('ci-level',    v => char.classInfo.level    = parseInt(v) || 1);
    }
    if (step === 3) {
      bind('mg-unique', v => char.magic.uniqueAbility  = v);
      bind('mg-mana',   v => char.magic.manaCapacity   = v);
    }
    if (step === 6) {
      bind('bg-origin',    v => char.background.origin    = v);
      bind('bg-goals',     v => char.background.goals     = v);
      bind('bg-fears',     v => char.background.fears     = v);
      bind('bg-backstory', v => char.background.backstory = v);
    }
    if (step === 8) {
      bind('eq-primary',     v => char.equipment.primaryWeapon   = v);
      bind('eq-secondary',   v => char.equipment.secondaryWeapon = v);
      bind('eq-armor',       v => char.equipment.armor           = v);
      bind('eq-staff',       v => char.equipment.staff           = v);
      bind('eq-accessories', v => char.equipment.accessories     = v);
      bind('eq-special',     v => char.equipment.specialItem     = v);
    }
  }

  function bind(id, setter) {
    const el = document.getElementById(id);
    if (!el) return;
    el.addEventListener('change', () => setter(el.value));
    el.addEventListener('input',  () => setter(el.value));
  }

  // ── Public Methods ─────────────────────────────────────────
  function updateChar(section, key, value) {
    if (char[section] !== undefined) char[section][key] = value;
  }

  function selectRace(id, el) {
    char.basic.race = id;
    document.querySelectorAll('.race-card').forEach(c => c.classList.remove('selected'));
    if (el) el.classList.add('selected');
  }

  function selectClass(id, el) {
    char.classInfo.cls = id;
    char.classInfo.subClass = '';
    char.classInfo.rank = '';
    document.querySelectorAll('.class-card').forEach(c => c.classList.remove('selected'));
    if (el) el.classList.add('selected');

    const panel = document.getElementById('class-detail-panel');
    const cls = CLASSES.find(c => c.id === id);
    if (panel && cls) {
      panel.style.display = '';
      const subSel = document.getElementById('ci-subclass');
      const rankSel = document.getElementById('ci-rank');
      if (subSel) subSel.innerHTML = '<option value="">-- เลือกความเชี่ยวชาญ --</option>' +
        cls.subClasses.map(s => `<option value="${s}">${s}</option>`).join('');
      if (rankSel) rankSel.innerHTML = '<option value="">-- เลือกยศ --</option>' +
        cls.ranks.map(r => `<option value="${r}">${r}</option>`).join('');
    }
  }

  function toggleAffinity(id, el) {
    const idx = char.magic.affinity.indexOf(id);
    if (idx >= 0) { char.magic.affinity.splice(idx, 1); if (el) el.classList.remove('selected'); }
    else          { char.magic.affinity.push(id);        if (el) el.classList.add('selected'); }
  }

  function addSpell() {
    char.magic.signatureSpells.push({ name: '', desc: '', level: 'C' });
    const list = document.getElementById('spell-list');
    if (!list) return;
    const i = char.magic.signatureSpells.length - 1;
    const div = document.createElement('div');
    div.className = 'spell-item';
    div.id = `spell-${i}`;
    div.innerHTML = `
      <div class="spell-item-header">
        <div class="spell-number">${i + 1}</div>
        <input type="text" class="frieren-input" style="flex:1" placeholder="ชื่อเวทมนตร์..."
               onchange="window.FrierenCreator.updateSpell(${i},'name',this.value)">
        <select class="frieren-select spell-level-select"
                onchange="window.FrierenCreator.updateSpell(${i},'level',this.value)">
          ${['E','D','C','B','A','S','SS'].map(l => `<option value="${l}" ${l==='C'?'selected':''}>${l}</option>`).join('')}
        </select>
        <button class="spell-remove" onclick="window.FrierenCreator.removeSpell(${i})">✕</button>
      </div>
      <textarea class="frieren-textarea" rows="2" placeholder="อธิบายผลของเวทมนตร์..."
                onchange="window.FrierenCreator.updateSpell(${i},'desc',this.value)"></textarea>`;
    list.appendChild(div);
  }

  function removeSpell(i) {
    char.magic.signatureSpells.splice(i, 1);
    rerenderSpells();
  }

  function updateSpell(i, field, value) {
    if (char.magic.signatureSpells[i]) char.magic.signatureSpells[i][field] = value;
  }

  function rerenderSpells() {
    const list = document.getElementById('spell-list');
    if (!list) return;
    const spellLevels = ['E','D','C','B','A','S','SS'];
    list.innerHTML = char.magic.signatureSpells.map((sp, i) => `
      <div class="spell-item" id="spell-${i}">
        <div class="spell-item-header">
          <div class="spell-number">${i+1}</div>
          <input type="text" class="frieren-input" style="flex:1" placeholder="ชื่อเวทมนตร์..." value="${esc(sp.name)}"
                 onchange="window.FrierenCreator.updateSpell(${i},'name',this.value)">
          <select class="frieren-select spell-level-select"
                  onchange="window.FrierenCreator.updateSpell(${i},'level',this.value)">
            ${spellLevels.map(l => `<option value="${l}" ${sp.level===l?'selected':''}>${l}</option>`).join('')}
          </select>
          <button class="spell-remove" onclick="window.FrierenCreator.removeSpell(${i})">✕</button>
        </div>
        <textarea class="frieren-textarea" rows="2" placeholder="อธิบายผลของเวทมนตร์..."
                  onchange="window.FrierenCreator.updateSpell(${i},'desc',this.value)">${esc(sp.desc)}</textarea>
      </div>`).join('');
  }

  function addSkill() {
    const inp = document.getElementById('skill-input');
    if (!inp) return;
    const val = inp.value.trim();
    if (!val) return;
    char.skills.push(val);
    inp.value = '';
    const tags = document.getElementById('skill-tags');
    if (tags) {
      const i = char.skills.length - 1;
      const tag = document.createElement('div');
      tag.className = 'skill-tag';
      tag.innerHTML = `${esc(val)}<button class="skill-tag-remove" onclick="window.FrierenCreator.removeSkill(${i})">×</button>`;
      tags.appendChild(tag);
    }
  }

  function removeSkill(i) {
    char.skills.splice(i, 1);
    const tags = document.getElementById('skill-tags');
    if (tags) tags.innerHTML = char.skills.map((sk, idx) => `
      <div class="skill-tag">${esc(sk)}
        <button class="skill-tag-remove" onclick="window.FrierenCreator.removeSkill(${idx})">×</button>
      </div>`).join('');
  }

  function changeStat(stat, delta) {
    const cur = char.stats[stat];
    const rem = remainingPoints();
    if (delta > 0 && (cur >= STAT_MAX || rem <= 0)) return;
    if (delta < 0 && cur <= STAT_MIN) return;
    char.stats[stat] = cur + delta;

    const valEl = document.getElementById(`sv-${stat}`);
    const barEl = document.getElementById(`sb-${stat}`);
    if (valEl) valEl.textContent = char.stats[stat];
    if (barEl) barEl.style.width = ((char.stats[stat] - STAT_MIN) / (STAT_MAX - STAT_MIN) * 100) + '%';

    const ptEl = document.getElementById('points-left');
    if (ptEl) ptEl.textContent = remainingPoints();

    const hp  = char.stats.CON * 10 + char.stats.STR * 2;
    const mp  = char.stats.INT * 8  + char.stats.WIS * 5;
    const spd = char.stats.DEX * 3  + char.stats.STR;
    const hpEl  = document.getElementById('derived-hp');
    const mpEl  = document.getElementById('derived-mp');
    const spdEl = document.getElementById('derived-spd');
    if (hpEl)  hpEl.textContent  = hp;
    if (mpEl)  mpEl.textContent  = mp;
    if (spdEl) spdEl.textContent = spd;
  }

  function togglePersonality(trait, el) {
    const idx = char.background.personality.indexOf(trait);
    if (idx >= 0) { char.background.personality.splice(idx, 1); if (el) el.classList.remove('selected'); }
    else          { char.background.personality.push(trait);     if (el) el.classList.add('selected'); }
  }

  function addRelationship() {
    char.relationships.push({ name: '', type: '', desc: '' });
    const list = document.getElementById('rel-list');
    if (!list) return;
    const i = char.relationships.length - 1;
    const div = document.createElement('div');
    div.className = 'rel-item';
    div.innerHTML = `
      <div class="rel-item-header">
        <span class="rel-number">ความสัมพันธ์ที่ ${i + 1}</span>
        <button class="rel-remove" onclick="window.FrierenCreator.removeRelationship(${i})">✕ ลบ</button>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label>ชื่อ</label>
          <input type="text" class="frieren-input" placeholder="ชื่อบุคคล..."
                 onchange="window.FrierenCreator.updateRel(${i},'name',this.value)">
        </div>
        <div class="form-group">
          <label>ประเภท</label>
          <select class="frieren-select" onchange="window.FrierenCreator.updateRel(${i},'type',this.value)">
            <option value="">-- เลือก --</option>
            ${REL_TYPES.map(t => `<option value="${t}">${t}</option>`).join('')}
          </select>
        </div>
      </div>
      <div class="form-group">
        <label>รายละเอียด</label>
        <textarea class="frieren-textarea" rows="2" placeholder="รายละเอียดความสัมพันธ์..."
                  onchange="window.FrierenCreator.updateRel(${i},'desc',this.value)"></textarea>
      </div>`;
    list.appendChild(div);
  }

  function removeRelationship(i) {
    char.relationships.splice(i, 1);
    const list = document.getElementById('rel-list');
    if (list) list.innerHTML = char.relationships.map((r, idx) => `
      <div class="rel-item">
        <div class="rel-item-header">
          <span class="rel-number">ความสัมพันธ์ที่ ${idx + 1}</span>
          <button class="rel-remove" onclick="window.FrierenCreator.removeRelationship(${idx})">✕ ลบ</button>
        </div>
        <div class="form-row">
          <div class="form-group"><label>ชื่อ</label>
            <input type="text" class="frieren-input" value="${esc(r.name)}"
                   onchange="window.FrierenCreator.updateRel(${idx},'name',this.value)"></div>
          <div class="form-group"><label>ประเภท</label>
            <select class="frieren-select" onchange="window.FrierenCreator.updateRel(${idx},'type',this.value)">
              <option value="">-- เลือก --</option>
              ${REL_TYPES.map(t => `<option value="${t}" ${r.type===t?'selected':''}>${t}</option>`).join('')}
            </select></div>
        </div>
        <div class="form-group"><label>รายละเอียด</label>
          <textarea class="frieren-textarea" rows="2"
                    onchange="window.FrierenCreator.updateRel(${idx},'desc',this.value)">${esc(r.desc)}</textarea></div>
      </div>`).join('');
  }

  function updateRel(i, field, value) {
    if (char.relationships[i]) char.relationships[i][field] = value;
  }

  // ── Export ─────────────────────────────────────────────────
  function generateCharacterSheet() {
    const b    = char.basic;
    const ci   = char.classInfo;
    const mg   = char.magic;
    const st   = char.stats;
    const bg   = char.background;
    const eq   = char.equipment;
    const race = RACES.find(r => r.id === b.race);
    const cls  = CLASSES.find(c => c.id === ci.cls);
    const affs = mg.affinity.map(id => MAGIC_AFFINITIES.find(a => a.id === id)?.name || id);

    const hp  = st.CON * 10 + st.STR * 2;
    const mp  = st.INT * 8  + st.WIS * 5;
    const spd = st.DEX * 3  + st.STR;

    let sheet = '';
    sheet += `═══════════════════════════════════════════════\n`;
    sheet += `       【キャラクターシート / Character Sheet】\n`;
    sheet += `           ✦ ${b.name || '(ยังไม่ได้ตั้งชื่อ)'} ✦\n`;
    sheet += `═══════════════════════════════════════════════\n\n`;

    sheet += `■ 基本情報 / Basic Information\n`;
    sheet += `名前 (Name)    : ${b.name || '—'}\n`;
    sheet += `年齢 (Age)     : ${b.age  || '—'}\n`;
    sheet += `性別 (Gender)  : ${b.gender || '—'}\n`;
    sheet += `種族 (Race)    : ${race?.name || b.race || '—'}\n`;
    sheet += `身長 (Height)  : ${b.height    || '—'}\n`;
    sheet += `瞳の色 (Eyes)  : ${b.eyeColor  || '—'}\n`;
    sheet += `髪の色 (Hair)  : ${b.hairColor || '—'}\n`;
    if (b.appearance) sheet += `外見 (Appearance) :\n${b.appearance}\n`;

    sheet += `\n■ クラス・ランク / Class & Rank\n`;
    sheet += `職業 (Class)    : ${cls?.name || ci.cls || '—'}\n`;
    sheet += `専門 (Subclass) : ${ci.subClass || '—'}\n`;
    sheet += `ランク (Rank)   : ${ci.rank  || '—'}\n`;
    sheet += `ギルド (Guild)  : ${ci.guild || '—'}\n`;
    sheet += `レベル (Level)  : ${ci.level}\n`;

    sheet += `\n■ 魔法・能力 / Magic & Abilities\n`;
    sheet += `魔法親和性 (Affinity) : ${affs.length ? affs.join(', ') : '—'}\n`;
    sheet += `マナ (Mana Pool)      : ${mg.manaCapacity}\n`;
    if (mg.signatureSpells.length > 0) {
      sheet += `\n【固有魔法 / Signature Spells】\n`;
      mg.signatureSpells.forEach((sp, i) => {
        sheet += `  ${i+1}. ${sp.name || '(ไม่มีชื่อ)'} [Rank ${sp.level}]\n`;
        if (sp.desc) sheet += `     └ ${sp.desc}\n`;
      });
    }
    if (mg.uniqueAbility) sheet += `\n【特殊能力 / Unique Ability】\n${mg.uniqueAbility}\n`;

    if (char.skills.length > 0) {
      sheet += `\n■ スキル / Skills\n`;
      char.skills.forEach(sk => { sheet += `  • ${sk}\n`; });
    }

    sheet += `\n■ ステータス / Statistics\n`;
    sheet += `  STR ${String(st.STR).padStart(2)}  |  INT ${String(st.INT).padStart(2)}  |  WIS ${String(st.WIS).padStart(2)}\n`;
    sheet += `  DEX ${String(st.DEX).padStart(2)}  |  CON ${String(st.CON).padStart(2)}  |  CHA ${String(st.CHA).padStart(2)}\n`;
    sheet += `  HP: ${hp}  |  MP: ${mp}  |  Speed: ${spd}\n`;
    if (race && Object.keys(race.statBonus).length) {
      const b2 = Object.entries(race.statBonus).map(([k,v])=>`${k}${v>0?'+':''}${v}`).join(', ');
      sheet += `  (Racial Bonus: ${b2})\n`;
    }

    sheet += `\n■ 性格・バックグラウンド / Personality & Background\n`;
    if (bg.personality.length) sheet += `性格 (Personality) : ${bg.personality.join('・')}\n`;
    if (bg.origin)             sheet += `出身地 (Origin)    : ${bg.origin}\n`;
    if (bg.goals)              sheet += `目標 (Goals)       : ${bg.goals}\n`;
    if (bg.fears)              sheet += `弱点・恐れ (Fears) : ${bg.fears}\n`;
    if (bg.backstory) {
      sheet += `\n【生い立ち・経歴 / Backstory】\n${bg.backstory}\n`;
    }

    if (char.relationships.length > 0) {
      sheet += `\n■ 人間関係 / Relationships\n`;
      char.relationships.forEach((r, i) => {
        if (!r.name && !r.type) return;
        sheet += `  ${i+1}. ${r.name || '?'} [${r.type || '—'}]\n`;
        if (r.desc) sheet += `     └ ${r.desc}\n`;
      });
    }

    sheet += `\n■ 装備 / Equipment\n`;
    if (eq.primaryWeapon)   sheet += `  武器 (Primary)   : ${eq.primaryWeapon}\n`;
    if (eq.secondaryWeapon) sheet += `  武器 (Secondary) : ${eq.secondaryWeapon}\n`;
    if (eq.armor)           sheet += `  防具 (Armor)     : ${eq.armor}\n`;
    if (eq.staff)           sheet += `  杖/触媒 (Staff)  : ${eq.staff}\n`;
    if (eq.accessories)     sheet += `  装飾品 (Accessories) : ${eq.accessories}\n`;
    if (eq.specialItem)     sheet += `  特殊アイテム (Special) : ${eq.specialItem}\n`;

    sheet += `\n═══════════════════════════════════════════════\n`;
    sheet += `Generated by Frieren RPG Character Creator\n`;
    sheet += `葬送のフリーレン — Beyond Journey's End\n`;
    sheet += `═══════════════════════════════════════════════`;
    return sheet;
  }

  function copySheet() {
    const sheet = generateCharacterSheet();
    navigator.clipboard.writeText(sheet).then(() => {
      const el = document.getElementById('export-success');
      if (el) { el.style.display = 'block'; setTimeout(() => { el.style.display = 'none'; }, 3000); }
    }).catch(() => {
      const ta = document.createElement('textarea');
      ta.value = sheet;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      const el = document.getElementById('export-success');
      if (el) { el.style.display = 'block'; setTimeout(() => { el.style.display = 'none'; }, 3000); }
    });
  }

  function sendToChat() {
    const sheet = generateCharacterSheet();
    const selectors = ['#send_textarea', '#chat-input', '.send_textarea', '#user-input'];
    for (const sel of selectors) {
      const el = document.querySelector(sel);
      if (el) {
        el.value = `[Character Sheet]\n${sheet}`;
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
    const sheet = generateCharacterSheet();
    const name  = (char.basic.name || 'character').replace(/\s+/g, '_');
    const blob  = new Blob([sheet], { type: 'text/plain;charset=utf-8' });
    const url   = URL.createObjectURL(blob);
    const a     = document.createElement('a');
    a.href      = url;
    a.download  = `${name}_frieren_rpg.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  // ── Utility ────────────────────────────────────────────────
  function esc(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // ── Bootstrap ──────────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    setTimeout(init, 500);
  }
})();
