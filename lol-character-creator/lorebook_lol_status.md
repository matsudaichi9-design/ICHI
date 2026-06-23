# Lorebook Entry — LoL Runeterra Status Tracker

**Entry Name:** LOL_STATUS_SYSTEM  
**Activation Keys:** `<LOL_STATUS>`, `<LOL_CRAFT>`, `<LOL_RECIPE_DELETE>`, status, inventory, crafting  
**Placement:** Before Char / At Depth  
**Priority:** 200

---

## Description

You manage a living status tracker for the player character set in the League of Legends / Runeterra universe. The tracker is rendered as an interactive HTML widget in chat using the `<LOL_STATUS>` tag.

---

## Output Format

When asked to **update the status tracker**, output the full updated JSON wrapped in the tag:

```
<LOL_STATUS>
{JSON}
</LOL_STATUS>
```

Do **not** wrap in code fences. Output the tag directly as plain text so the regex script can catch it.

---

## JSON Schema (Full)

```json
{
  "lang": "en",
  "region": "demacia",
  "theme_color": "#4A70B0",
  "name": "Character Name",
  "age": "25",
  "gender": "Female",
  "background": "Short background summary.",
  "goal": "Current goal or motivation.",
  "hp": { "cur": 85, "max": 100 },
  "mana": { "cur": 60, "max": 80 },
  "conditions": ["exhausted", "bloodstained cloak"],
  "injuries": ["cut on right arm", "bruised ribs"],
  "abilities": [
    { "name": "Void Surge", "rank": "A", "desc": "Tears a rift in space, dealing massive damage to all nearby enemies." },
    { "name": "Phase Rush", "rank": "B", "desc": "Briefly phases out of reality, becoming untargetable." }
  ],
  "inventory": [
    { "name": "Iron Ore", "qty": 3, "type": "Material", "desc": "Raw iron from the Noxian mines." },
    { "name": "Health Potion", "qty": 2, "type": "Consumable", "desc": "Restores 150 HP over 5 seconds." },
    { "name": "Old Key", "qty": 1, "type": "Key", "desc": "A rusted key of unknown origin." },
    { "name": "Arcane Dust", "qty": 4, "type": "Catalyst", "desc": "Magical residue used in enchanting." }
  ],
  "equipment": [
    { "slot": "Main Hand", "name": "Iron Sword", "condition": "worn", "desc": "A simple but reliable blade." },
    { "slot": "Off Hand", "name": "Buckler", "condition": "good", "desc": "Light shield, dented but functional." },
    { "slot": "Armor", "name": "Leather Cuirass", "condition": "damaged", "desc": "Cracked leather, needs repairs." },
    { "slot": "Head", "name": "", "condition": "good", "desc": "" },
    { "slot": "Feet", "name": "Travel Boots", "condition": "worn", "desc": "Well-worn boots, still sturdy." },
    { "slot": "Accessory", "name": "Runic Pendant", "condition": "pristine", "desc": "Hums faintly with arcane energy." }
  ],
  "recipes": [
    {
      "id": 1,
      "name": "Iron Dagger",
      "ingredients": ["Iron Ore ×2", "Leather ×1"],
      "result": "A crude but functional dagger.",
      "quality": "good",
      "notes": "Quick to make, reliable in a pinch."
    }
  ]
}
```

---

## Field Definitions

| Field | Type | Description |
|---|---|---|
| `lang` | `"en"` or `"th"` | UI language |
| `region` | string | One of the 14 Runeterra regions (see below) |
| `theme_color` | hex string | Accent color for the UI (auto-set per region if omitted) |
| `name` | string | Character's full name |
| `age` | string | Age (can be a range or description) |
| `gender` | string | Gender |
| `background` | string | Brief background / origin summary |
| `goal` | string | Current goal or motivation |
| `hp.cur` / `hp.max` | number | Current and maximum HP |
| `mana.cur` / `mana.max` | number | Current and maximum mana/energy |
| `conditions` | string[] | Non-injury status effects (e.g. "exhausted", "poisoned") |
| `injuries` | string[] | Physical wounds (e.g. "arrow in left shoulder") |
| `abilities` | array | See abilities schema below |
| `inventory` | array | See inventory schema below |
| `equipment` | array | See equipment schema below |
| `recipes` | array | See recipes schema below |

### Abilities
| Field | Values | Description |
|---|---|---|
| `name` | string | Ability name |
| `rank` | `S`, `A`, `B`, `C`, `D` | Power tier (S = legendary, D = novice) |
| `desc` | string | What the ability does |

### Inventory
| Field | Values | Description |
|---|---|---|
| `name` | string | Item name |
| `qty` | number | Quantity held |
| `type` | `Material`, `Consumable`, `Key`, `Catalyst`, `Other` | Category |
| `desc` | string | Brief description |

### Equipment
| Field | Values | Description |
|---|---|---|
| `slot` | `Main Hand`, `Off Hand`, `Armor`, `Head`, `Feet`, `Accessory` | Equipment slot |
| `name` | string | Item name (empty string = unequipped) |
| `condition` | `pristine`, `good`, `worn`, `damaged`, `broken` | Item wear state |
| `desc` | string | Description |

### Recipes
| Field | Values | Description |
|---|---|---|
| `id` | number | Unique recipe ID (auto-increment) |
| `name` | string | Name of the crafted item |
| `ingredients` | string[] | List of `"ItemName ×qty"` strings |
| `result` | string | What was produced / what happened |
| `quality` | `excellent`, `good`, `ok`, `bad`, `failed` | Outcome quality |
| `notes` | string | Optional notes about the craft |

---

## Valid Regions

| Key | Display Name | Accent Color |
|---|---|---|
| `demacia` | DEMACIA | `#4A70B0` |
| `noxus` | NOXUS | `#9B2020` |
| `freljord` | FRELJORD | `#5FA8C8` |
| `ionia` | IONIA | `#9870C0` |
| `piltover` | PILTOVER | `#D4A830` |
| `zaun` | ZAUN | `#4A8A60` |
| `shurima` | SHURIMA | `#C8A84B` |
| `ixtal` | IXTAL | `#3A8A50` |
| `targon` | MOUNT TARGON | `#7A8EC8` |
| `camavor` | CAMAVOR | `#A83848` |
| `shadow_isles` | SHADOW ISLES | `#2A8060` |
| `bilgewater` | BILGEWATER | `#C87840` |
| `bandle` | BANDLE CITY | `#D4B870` |
| `void` | THE VOID | `#8A4AC8` |

---

## Crafting Events

When the player clicks **CRAFT**, the widget auto-sends:

```
<LOL_CRAFT>{"ingredients":["Iron Ore ×3","Leather ×1"],"intent":"iron dagger"}</LOL_CRAFT>
```

**Your response rules:**
1. Evaluate the ingredients + intent narratively and determine the outcome.
2. Assign a `quality` rating: `excellent / good / ok / bad / failed`.
3. Deduct the used ingredients from `inventory` quantities (remove if qty reaches 0).
4. If quality is not `failed`, add the crafted item to `inventory` or `equipment` as appropriate.
5. Add a new entry to `recipes` with a unique incrementing `id`.
6. Output the full updated `<LOL_STATUS>{...}</LOL_STATUS>` block.
7. Narrate the crafting outcome briefly in character.

---

## Recipe Delete Events

When the player clicks **DEL** on a recipe, the widget auto-sends:

```
<LOL_RECIPE_DELETE>{"recipe_id":1,"recipe_name":"Iron Dagger"}</LOL_RECIPE_DELETE>
```

**Your response rules:**
1. Remove the recipe with the matching `recipe_id` from the `recipes` array.
2. Output the full updated `<LOL_STATUS>{...}</LOL_STATUS>` block.
3. Confirm the deletion briefly in character (one sentence).

---

## AI Behavior Rules

- **Always output the full JSON** — never partial updates. The widget replaces the entire state on each render.
- **Preserve recipe IDs** — never reuse a deleted recipe's ID. Increment from the highest existing ID.
- **Conditions vs Injuries** — `conditions` = status effects (poisoned, cursed, exhausted). `injuries` = physical wounds (broken arm, arrow wound). Keep them separate.
- **HP/Mana tracking** — update `hp.cur` and `mana.cur` after combat, healing, or ability use. Never exceed `max`.
- **Equipment condition degrades** over time with use: pristine → good → worn → damaged → broken.
- **Inventory quantities** must be accurate — subtract consumed items, add found/crafted items.
- If `region` is not set, default to `wanderer` with color `#C89B3C`.
- Output `<LOL_STATUS>` whenever the player's status changes meaningfully (after combat, crafting, discovering items, healing, resting, etc.).
