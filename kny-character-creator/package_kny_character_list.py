import json

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

# ── Entry 0: Format Instructions ─────────────────────────────────────────────

E0 = """\
## KNY CHARACTER HEADER SYSTEM

### FORMAT
[KNY|catbox_code|Name (Form)|#hexcolor]

Place at the very start of your response — before narrative or dialogue — when speaking as or focusing on a listed character.

### FORM SELECTION
• Characters with multiple forms share the SAME hex color but may use different image codes.
• Match the form label to the current scene's timeline and character state.
• Always include the form label: "Kamado Tanjiro (Swordsmith Village)" not just "Tanjiro".
• Image codes are placeholders (_). Replace with your catbox.moe upload codes.

### UNLISTED CHARACTERS
Use [KNY|_|Name|#hex] with a consistent, sensible colour. The silhouette placeholder shows automatically.

### NAMING CONVENTIONS
• Japanese name order (family name first): Kamado Tanjiro, Kocho Shinobu, Agatsuma Zenitsu, etc.
• Akaza does NOT acknowledge the name "Hakuji" until his memories return in battle.
• Kokushibo's human past as Tsugikuni Michikatsu is revealed only in flashback; present scenes use only "Kokushibo."
• All demons address Muzan as "Muzan-sama." Humans who know his true identity almost never say it aloud.
• Names remain canonical regardless of the roleplay language.

### RULE
Use the header ONCE per response, at the very top. Never repeat mid-scene.\
"""

# ── Entry 1: Main Cast, Hashira, Allies ──────────────────────────────────────

E1 = """\
## KNY CHARACTER LIST — MAIN CAST & ALLIES

### MAIN CAST
1. Kamado Tanjiro (Taisho Arc) [_] — Water Breathing apprentice; checkered green haori; kindhearted, stubborn, exceptional scent. Early arcs through Mugen Train. (Hex: #C85A35)
2. Kamado Tanjiro (Swordsmith Village) [_] — Hinokami Kagura / Sun Breathing mastered; Demon Slayer Mark first appears; wielding Yoriichi-type blade. (Hex: #C85A35)
3. Kamado Tanjiro (Final Battle) [_] — Transparent World active; all 13 Sun Breathing forms; fights Muzan through sunrise. Peak form. (Hex: #C85A35)
4. Kamado Tanjiro (Demon) [_] — Briefly revived as demon by Muzan's dying blood; friends' voices and memories pull him back to humanity. (Hex: #C85A35)
5. Kamado Nezuko (Demon) [_] — Turned as a child; bamboo muzzle, hemp-pattern pink kimono; conquered sunlight without consuming humans. (Hex: #E8708C)
6. Kamado Nezuko (Awakened) [_] — Exploding Blood berserk mode; giant cracked-skin form; nearly loses herself to demon instinct. (Hex: #E8708C)
7. Kamado Nezuko (Human) [_] — Fully restored after Tamayo's drug; reunited with Tanjiro in time to share sunrise. (Hex: #E8708C)
8. Agatsuma Zenitsu [_] — Thunder Breathing; cowardly exterior; asleep-state reaches Godspeed; mastered one form to its absolute limit. (Hex: #F5C842)
9. Hashibira Inosuke [_] — Beast Breathing; boar mask; raised by boars on a mountain; hyper-acute tactile sense; fierce but surprisingly sensitive. (Hex: #5A9E6F)
10. Tsuyuri Kanao [_] — Flower / Insect Breathing hybrid; emotionless from trauma until freed by coin habit; Scarlet Spider Lily Eyes; Kanae's adoptive sister. (Hex: #C9A0DC)
11. Shinazugawa Genya [_] — Sanemi's younger brother; no breathing style; eats demons to borrow their regeneration and blood arts temporarily; gun + prayer-bead weapon. (Hex: #7A5848)

### HASHIRA (NINE PILLARS)
12. Tomioka Giyu (Water Hashira) [_] — Half-solid, half-checkered haori; stoic and misunderstood; Water Breathing 11th Form: Dead Calm. (Hex: #3A6EA5)
13. Kocho Shinobu (Insect Hashira) [_] — Butterfly haori; blade too thin to decapitate; laces every strike with wisteria poison; hid grief over Kanae behind a perpetual smile. (Hex: #7B5EA7)
14. Rengoku Kyojuro (Flame Hashira) [_] — Blazing passion and ironclad will; Flame Breathing 9th Form: Purgatory; died protecting passengers and Tanjiro from Akaza. (Hex: #E87030)
15. Uzui Tengen (Sound Hashira) [_] — Flamboyant ex-shinobi; dual cleaver blades; Sound Breathing; partner to three kunoichi wives; retires after Entertainment District. (Hex: #D4A800)
16. Kanroji Mitsuri (Love Hashira) [_] — Pink-and-lime hair; whip-thin blade suits her pliable body; Love Breathing; emotional and devastatingly powerful; loves Obanai. (Hex: #D4688A)
17. Tokito Muichiro (Mist Hashira) [_] — Youngest Hashira at 14; Mist Breathing; complete amnesia until Swordsmith Village reveals his Yoriichi bloodline. (Hex: #7AC8D8)
18. Shinazugawa Sanemi (Wind Hashira) [_] — Scarred, aggressive; Wind Breathing; rare marechi blood intoxicates demons; killed his own demon-turned mother to protect others. (Hex: #6A8A5A)
19. Himejima Gyomei (Stone Hashira) [_] — Strongest Hashira; blind; Stone Breathing; flail-and-axe chain; weeps constantly; utterly unbreakable in battle. (Hex: #6A5030)
20. Iguro Obanai (Serpent Hashira) [_] — White serpent Kaburamaru; mismatched eyes; cloth-wrapped lower face; Serpent Breathing; devoted to Mitsuri. (Hex: #4A7A6A)

### TEACHERS & MENTORS
21. Urokodaki Sakonji [_] — Former Water Hashira; Tanjiro's master; red tengu mask always on; Total Concentration Breathing teacher; deeply paternal toward his students. (Hex: #4A6880)
22. Kuwajima Jigoro [_] — Former Thunder Hashira; Zenitsu's harsh but loving master; committed seppuku from shame over Kaigaku's betrayal. (Hex: #8A7A3A)
23. Rengoku Shinjuro [_] — Former Flame Hashira; Kyojuro's father; spiralled into grief and alcoholism after his wife died; reclaimed by his son's legacy. (Hex: #8A5020)
24. Rengoku Senjuro [_] — Kyojuro's gentle younger brother; lacks the Rengoku flame gift; warmly supportive; preserves the family flame records. (Hex: #C87840)

### UBUYASHIKI CLAN
25. Ubuyashiki Kagaya [_] — 97th Corps Master; cursed bloodline shortens his life; serene and prophetic; self-detonates to weaken Muzan at Infinity Castle. (Hex: #8A7060)
26. Ubuyashiki Kiriya [_] — Kagaya's young son; becomes acting Corps commander after Infinity Castle; quiet authority for his age. (Hex: #7A6050)

### BUTTERFLY ESTATE & SUPPORT
27. Kocho Kanae (Flower Hashira) [_] — Shinobu's elder sister; warm and powerful; killed by Doma; her memory and plan shape Shinobu's entire revenge. (Hex: #C0A0C8)
28. Kanzaki Aoi [_] — Butterfly Estate medic; failed Final Selection but serves tirelessly as healer and trainer for slayers. (Hex: #C8A880)
29. Naho, Sumi, Kiyo [_] — Three young Butterfly Estate attendants who nurse injured Demon Slayers with cheerful devotion. (Hex: #D0C0A0)

### SWORDSMITHS
30. Haganezuka Hotaru (Masked) [_] — Hyottoko-masked obsessive; easily enraged; perfectionist swordsmith assigned to Tanjiro. (Hex: #8A6040)
31. Haganezuka Hotaru (Unmasked) [_] — Surprisingly handsome face revealed late in manga; eerily serene when polishing a blade even mid-crisis. (Hex: #8A6040)
32. Tecchikawahara Tecchin [_] — Stern chief of the Hidden Swordsmith Village; oversees all blade production for the Corps. (Hex: #6A5040)

### PAST ERA & ANCESTORS
33. Tsugikuni Yoriichi [_] — Creator of Sun Breathing and every derivative style; the most powerful demon slayer in recorded history; twin of Michikatsu; died of old age with Muzan unslain. (Hex: #C84040)
34. Tsugikuni Michikatsu (Human) [_] — Yoriichi's twin; skilled soldier-swordsman; envied his brother's gift; chose demonhood over mortality. Became Kokushibo. (Hex: #2A2050)
35. Sumiyoshi [_] — Tanjiro's ancestor; befriended Yoriichi in his old age; preserved the Hinokami Kagura dances that kept Sun Breathing alive through the Kamado lineage. (Hex: #C06040)
36. Suyako [_] — Sumiyoshi's warm wife; welcomed Yoriichi into their home; her joy gave his final years meaning. (Hex: #E8A880)
37. Sabito [_] — Urokodaki's late student; slew almost every demon at Final Selection alone; guides Tanjiro as a spirit during boulder training. (Hex: #7A9AAA)
38. Makomo [_] — Urokodaki's late student; gentle spirit who guides Tanjiro alongside Sabito. (Hex: #9AA0C0)\
"""

# ── Entry 2: Demons & Others ─────────────────────────────────────────────────

E2 = """\
## KNY CHARACTER LIST — DEMONS & OTHERS

### ROGUE DEMONS / ALLIES
39. Tamayo [_] — Doctor demon freed from Muzan; spent centuries developing a human-restoration drug; sacrificed herself to poison Muzan from within. (Hex: #8A7AAA)
40. Yushiro [_] — Tamayo's devoted demon attendant; Blindfold concealment technique; violently jealous of anyone near her. (Hex: #6A6A9A)
41. Kaigaku [_] — Zenitsu's bitter senior student; surrendered to Kokushibo to survive; became Lower Moon 1; destroyed by Zenitsu's Seventh Form: Flaming Thunder God. (Hex: #5A4A6A)

### KIBUTSUJI MUZAN
42. Kibutsuji Muzan (Human Disguise) [_] — Suave black-hatted man; first encountered in Asakusa; progenitor of all demons; controls them via his blood. (Hex: #3A0A1A)
43. Kibutsuji Muzan (Battle Form) [_] — Transformed in Infinity Castle; white-fleshed grotesque; multiple mouths and arms; absorbs Nezuko's blood to pursue sun resistance. (Hex: #3A0A1A)

### UPPER MOONS (TWELVE KIZUKI)
44. Kokushibo (Upper Moon 1 / Michikatsu) [_] — Moon Breathing; dozens of eyes across his face; Nichirin-blade wielder even as a demon; near-Yoriichi-class; fought Sanemi, Gyomei, Muichiro in Infinity Castle. (Hex: #2A2050)
45. Doma (Upper Moon 2) [_] — Hollow rainbow eyes that feel nothing; Eternal Paradise Faith cult; Ice Lotus Cryotherapy; killed Kanae; undone by Shinobu's wisteria-saturated body, finished by Kanao and Inosuke. (Hex: #5A9AAA)
46. Doma (Young Cult Leader) [_] — Past form; charismatic and hollow even as a young human cult leader before demonhood. (Hex: #5A9AAA)
47. Akaza (Upper Moon 3) [_] — Martial arts master; pink chrysanthemum markings; Destructive Death / Compass Needle; killed Rengoku; regained memories of Hakuji's human life and destroyed himself from within. (Hex: #C84080)
48. Akaza (Past / Hakuji) [_] — Human fighter Hakuji; tattooed arms; lived to protect a sick girl and her kind father; fell to grief and slaughtered a yakuza clan; turned by Muzan. (Hex: #C84080)
49. Hantengu (Upper Moon 4) [_] — Cowardly tiny main body; Blood Demon Art splits emotions into clones: Sekido (rage), Karaku (pleasure), Aizetsu (grief), Urogi (joy); true body hidden inside the combined clone Zohakuten. (Hex: #5A5030)
50. Nakime (Upper Moon 4 / Biwa Demon) [_] — Biwa-playing demon; controls the infinite architecture of the Infinity Castle; silent and lethal; elevated after Hantengu's death. (Hex: #3A3A5A)
51. Gyokko (Upper Moon 5) [_] — Ceramic-vase body; Myriad of Scales Blood Demon Art (fish-creature swarms, pottery traps); grotesquely proud of his "art"; slain by Muichiro after his Mark awakens. (Hex: #3A8A8A)
52. Gyutaro (Upper Moon 6 — Male) [_] — Gaunt, sickly; poison scythe Blood Demon Art: Flying Blood Sickles; fiercely protective of Daki; dominant soul of the pair. (Hex: #5A8030)
53. Daki (Upper Moon 6 — Female) [_] — Beautiful oiran; Obi Sash Manipulation; Gyutaro's younger sister; her body hosts both their souls; childlike and dependent on her brother. (Hex: #D4806A)

### LOWER MOONS & OTHER DEMONS
54. Enmu (Lower Moon 1) [_] — Dream manipulation via blood-written script; obsessed with Muzan's praise; fused himself to the Mugen Train to devour souls en masse. (Hex: #6A5A8A)
55. Rui (Lower Moon 5) [_] — Spider demon of Mt. Natagumo; Blood Demon Art: Cutting Thread; built a fake "family" from enslaved demons out of yearning for real bonds. (Hex: #6A4A5A)
56. Susamaru [_] — Six-armed temari demon; served Muzan before official Kizuki enrollment; killed by Tamayo's Blood Demon Art (Muzan's name-curse in her blood). (Hex: #D47060)
57. Yahaba [_] — Arrow demon partnered with Susamaru; Koketsu Arrow guides temari with directional wind; defeated by Tanjiro through Constant Flux. (Hex: #6A5060)
58. Hand Demon [_] — Ancient demon of Mt. Fujikasane; slaughtered dozens of Urokodaki's students including Sabito; apex threat of the Final Selection forest. (Hex: #4A3A3A)

### SPIDER DEMON FAMILY (MT. NATAGUMO)
59. Spider Demon Father [_] — Enormous forced-transformation; enslaved by Rui to play "father"; no will of his own left. (Hex: #5A4A3A)
60. Spider Demon Mother [_] — Thread user; compassionate even in Rui's control; destroyed her own threads to free captive slayers before Shinobu killed her. (Hex: #7A6A5A)
61. Spider Demon Sister [_] — Forced to train demon-controlled slayers; killed by Shinobu with Insect Breathing. (Hex: #9A7A6A)

### OTHER SUPPORTING
62. Kotoha Hashibira [_] — Inosuke's gentle late mother; fled Doma's cult carrying her infant; ultimately killed by Doma before escaping. (Hex: #C0A0A0)
63. Goto [_] — Wisteria House support member; quiet and dependable; handles transport and logistics for injured slayers after missions. (Hex: #7A7070)\
"""

lorebook = {
    "name": "KNY Character List",
    "entries": {
        "0": entry(0, "KNY Header System — Format Instructions", E0, 95),
        "1": entry(1, "KNY Character List — Main Cast & Allies",  E1, 94),
        "2": entry(2, "KNY Character List — Demons & Others",     E2, 93),
    }
}

out = "kny_character_list_lorebook.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)

size = len(json.dumps(lorebook, ensure_ascii=False, indent=2).encode("utf-8"))
print(f"Done! {out} — {size:,} bytes ({size/1024:.1f} KB)")
