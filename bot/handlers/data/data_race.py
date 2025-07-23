# races, their descriptions, bonuses and pictures


race_info = {
    "hill_dwarf": {
        "title": "Hill Dwarf",
        "description": "Hill dwarves are tough, wise, and deeply connected to their clans, known for their resilience, sense of tradition, and strong community bonds.",
        "detailed_description": (
            "Hill dwarves are native to deep mountain strongholds and ancient subterranean halls. They are slightly shorter and stockier than their mountain cousins. Renowned for their wisdom and endurance, hill dwarves are stoic in adversity and slow to trust outsiders. Community, clan loyalty, craftsmanship, and the worship of their deities form the backbone of their culture."
        ),
        "features": "some more info",
        "male_names": [
            "Adrik", "Baern", "Barendd", "Brottor", "Dain", "Eberk", "Fargrim", "Harbek", "Orsik"
        ],
        "female_names": [
            "Artin", "Bardryn", "Dagnal", "Eldeth", "Gunnloda", "Hiln", "Kathra", "Kristryd", "Riswynn"
        ],
        "surnames": [
            "Balderk", "Fireforge", "Ironfist", "Loderr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"
        ],
        "speed": "25 feet",
        "body_size": {
            "small": ["3'9\" (115 cm)", "121 lbs (55 kg)"],
            "medium": ["4'1\" (125 cm)", "148 lbs (67 kg)"],
            "big": ["4'5\" (135 cm)", "176 lbs (80 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": "under 70 ages",
            "mature": "70-200 ages",
            "old": "over 350 ages"
        },
        "language": ["Common", "Dwarvish"],
        "recommended_worldview": "Lawful Good",
        "height_range": "4'0\"-5'0\" (120-150 cm)",
        "weight_range": "120-170 lbs (54-77 kg)",
        "recommended_classes": [
            "Cleric", "Fighter", "Paladin", "Ranger"
        ],
        "abilities": [
            {
                "name": "Dwarven Resilience",
                "description": "You have advantage on saving throws against poison, and you have resistance against poison damage."
            },
            {
                "name": "Dwarven Toughness",
                "description": "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
            },
            {
                "name": "Dwarven Combat Training",
                "description": "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."
            },
            {
                "name": "Tool Proficiency",
                "description": "You gain proficiency with one type of artisan's tools: smith's tools, brewer's supplies, or mason's tools."
            },
            {
                "name": "Stonecunning",
                "description": "Whenever you make a History check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 2,
            "Intelligence": 0,
            "Wisdom": 1,
            "Charisma": 0
        },
        "proficiencies": {
            "weapons": ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"],
            "tools": ["Smith's tools (choose one)", "Brewer's supplies (choose one)", "Mason's tools (choose one)"],
            "skills": []
        },
        "resistances": [
            "Poison (resistance and advantage on saves)"
        ],
        "saving_throw_advantages": [
            "Poison"
        ],
        "unique_traits": [
            "Hit point maximum increases by 1 per level (Dwarven Toughness)",
            "Double proficiency on History checks about stonework (Stonecunning)"
        ],
        "image": "media/races/dnd_hill_dwarf.png"
    },

    "mountain_dwarf": {
        "title": "Mountain Dwarf",
        "description": "Mountain dwarves are hardy and strong, with an unyielding spirit and martial traditions. Their culture is steeped in proud craftsmanship, ancient stone keeps, and battlefield honor.",
        "detailed_description": (
            "Mountain dwarves are outstanding smiths and warriors. They value clans and history, pride themselves on their martial prowess, and are stubborn in the face of adversity. Living in ancient mountain fortresses, they are tireless defenders of their homes and heritage."
        ),
        "features": "some more info",
        "male_names": [
            "Adrik", "Baern", "Barendd", "Brottor", "Dain", "Eberk", "Fargrim", "Harbek", "Orsik"
        ],
        "female_names": [
            "Artin", "Bardryn", "Dagnal", "Eldeth", "Gunnloda", "Hiln", "Kathra", "Kristryd", "Riswynn"
        ],
        "surnames": [
            "Balderk", "Fireforge", "Ironfist", "Loderr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"
        ],
        "speed": "25 feet",
        "body_size": {
            "small": ["3'11\" (120 cm)", "132 lbs (60 kg)"],
            "medium": ["4'5\" (135 cm)", "176 lbs (80 kg)"],
            "big": ["4'9\" (145 cm)", "209 lbs (95 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": "under 70 ages",
            "mature": "70-200 ages",
            "old": "over 350 ages"
        },
        "language": ["Common", "Dwarvish"],
        "recommended_worldview": "Lawful Good",
        "height_range": "4'0\"-5'0\" (120-150 cm)",
        "weight_range": "120-180 lbs (54-82 kg)",
        "recommended_classes": [
            "Fighter", "Paladin", "Barbarian"
        ],
        "abilities": [
            {
                "name": "Dwarven Resilience",
                "description": "You have advantage on saving throws against poison, and you have resistance against poison damage."
            },
            {
                "name": "Dwarven Armor Training",
                "description": "You are proficient with light and medium armor."
            },
            {
                "name": "Dwarven Combat Training",
                "description": "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."
            },
            {
                "name": "Tool Proficiency",
                "description": "You gain proficiency with one type of artisan's tools: smith's tools, brewer's supplies, or mason's tools."
            },
            {
                "name": "Stonecunning",
                "description": "Whenever you make a History check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 2,
            "Dexterity": 0,
            "Constitution": 2,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        },
        "proficiencies": {
            "weapons": ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"],
            "tools": ["Smith's tools (choose one)", "Brewer's supplies (choose one)", "Mason's tools (choose one)"],
            "skills": []
        },
        "resistances": [
            "Poison (resistance and advantage on saves)"
        ],
        "saving_throw_advantages": [
            "Poison"
        ],
        "unique_traits": [
            "Armor proficiency (light and medium) from race",
            "Double proficiency on History checks about stonework (Stonecunning)"
        ],
        "image": "media/races/dnd_mountain_dwarf.png"
    },

    "high_elf": {
        "title": "High Elf",
        "description": "High elves are a refined and proud race, known for their keen intellect, mastery of magic, and artistic flair. They live longer than other elves, have refined manners, and are often considered arrogant, but they also strive for harmony and perfection. High elves value knowledge, independence, and have an innate talent for the study of magic.",
        "detailed_description": (
            "High elves typically hail from ancient, hidden forests or luminous cities protected by powerful magic. They embrace both cerebral and aesthetic pursuits, spending years—sometimes decades—perfecting their skills in art, arcane study, and swordplay. While outsiders may see them as aloof or proud, high elves often feel a responsibility to preserve knowledge and guard the balance between the mundane and the mystical. Their lives are marked by a quest for excellence and the pursuit of beauty in all things."
        ),
        "features": "some more info",
        "male_names": [
            "Adran", "Aramil", "Arannis", "Aust", "Enialis", "Heian", "Paelias", "Quarion", "Soveliss"
        ],
        "female_names": [
            "Adrie", "Drusilia", "Felosial", "Ielenia", "Lia", "Mialee", "Naivara", "Quelenna", "Thia"
        ],
        "surnames": [
            "Amakiir", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Nai'lo", "Siannodel", "Xiloscient"
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["5'1\" (155 cm)", "99 lbs (45 kg)"],
            "medium": ["5'5\" (165 cm)", "119 lbs (54 kg)"],
            "big": ["5'11\" (180 cm)", "143 lbs (65 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": "under 120 ages",
            "mature": "120–250 ages",
            "old": "over 750 ages"
        },
        "language": ["Common", "Elvish"],
        "extra_language": 1,
        "recommended_worldview": "Chaotic Good",
        "height_range": "5'0\"–6'0\" (150–180 cm)",
        "weight_range": "90–145 lbs (41–66 kg)",
        "recommended_classes": [
            "Wizard", "Ranger", "Fighter"
        ],
        "abilities": [
            {
                "name": "Darkvision",
                "description": "You can see in darkness (shades of gray) up to 60 feet."
            },
            {
                "name": "Fey Ancestry",
                "description": "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."
            },
            {
                "name": "Trance",
                "description": "You do not need to sleep. Instead, you meditate deeply for 4 hours a day and remain semiconscious."
            },
            {
                "name": "Elf Weapon Training",
                "description": "You have proficiency with longswords, shortswords, shortbows, and longbows."
            },
            {
                "name": "Cantrip",
                "description": "You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it."
            },
            {
                "name": "Extra Language",
                "description": "You can speak, read, and write one additional language of your choice."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 0,
            "Dexterity": 2,
            "Constitution": 0,
            "Intelligence": 1,
            "Wisdom": 0,
            "Charisma": 0
        },
        "proficiencies": {
            "weapons": ["Longsword", "Shortsword", "Shortbow", "Longbow"],
            "tools": [],
            "skills": []
        },
        "resistances": [],
        "saving_throw_advantages": [
            "Charm"
        ],
        "unique_traits": [
            "Immunity to magical sleep",
            "Only need 4 hours of trance instead of sleep each day"
        ],
        "image": "media/races/dnd_high_elf.png"
    },
    "wood_elf": {
        "title": "Wood Elf",
        "description": "Wood elves are graceful, attuned to nature, and gifted hunters. They are known for keen senses, speed, and a deep bond with the wilderness.",
        "detailed_description": (
            "Wood elves dwell in ancient forests, living in harmony with the land and its cycles. They are elusive, rarely leaving a trace, and are swift runners and skilled archers. Their culture centers around freedom, adaptability, and the protection of untouched wilds. Many outsiders see them as mysterious and wild, but within their communities, they value compassion and respect for all living things."
        ),
        "features": "some more info",
        "male_names": [
            "Adran", "Aramil", "Aust", "Carric", "Erevan", "Galinndan", "Himo", "Ivellios", "Laucian"
        ],
        "female_names": [
            "Briana", "Caelynn", "Drusilia", "Felosial", "Keyleth", "Leshanna", "Shanairra", "Thia", "Valanthe"
        ],
        "surnames": [
            "Amakiir (Gemflower)", "Galanodel (Moonwhisper)", "Holimion (Diamonddew)",
            "Liadon (Silverfrond)", "Meliamne (Oakenheel)", "Nai'lo (Nightbreeze)",
            "Siannodel (Moonbrook)", "Xiloscient (Goldpetal)"
        ],
        "speed": "35 feet",
        "body_size": {
            "small": ["4'11\" (150 cm)", "95 lbs (43 kg)"],
            "medium": ["5'3\" (160 cm)", "115 lbs (52 kg)"],
            "big": ["5'9\" (175 cm)", "137 lbs (62 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": "under 120 ages",
            "mature": "120–250 ages",
            "old": "over 750 ages"
        },
        "language": ["Common", "Elvish"],
        "recommended_worldview": "Chaotic Good",
        "height_range": "5'0\"–6'0\" (150–180 cm)",
        "weight_range": "90–145 lbs (41–66 kg)",
        "recommended_classes": [
            "Ranger", "Rogue", "Druid"
        ],
        "abilities": [
            {
                "name": "Darkvision",
                "description": "You can see in darkness (shades of gray) up to 60 feet."
            },
            {
                "name": "Fey Ancestry",
                "description": "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."
            },
            {
                "name": "Trance",
                "description": "You do not need to sleep. Instead, you meditate deeply for 4 hours a day and remain semiconscious."
            },
            {
                "name": "Elf Weapon Training",
                "description": "You have proficiency with longswords, shortswords, shortbows, and longbows."
            },
            {
                "name": "Fleet of Foot",
                "description": "Your base walking speed is 35 feet."
            },
            {
                "name": "Mask of the Wild",
                "description": "You can attempt to hide even when only lightly obscured by natural phenomena."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 0,
            "Dexterity": 2,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 1,
            "Charisma": 0
        },
        "proficiencies": {
            "weapons": ["Longsword", "Shortsword", "Shortbow", "Longbow"],
            "tools": [],
            "skills": []
        },
        "resistances": [],
        "saving_throw_advantages": [
            "Charm"
        ],
        "unique_traits": [
            "Immunity to magical sleep",
            "Only need 4 hours of trance instead of sleep each day"
        ],
        "image": "media/races/dnd_wood_elf.png"
    },

    "dark_elf": {
        "title": "Dark Elf (Drow)",
        "description": "Drow are mysterious and feared elves from the Underdark, known for their striking appearance, innate magic, and deadly cunning.",
        "detailed_description": (
            "Drow society thrives in the deep realms beneath the surface, ruled by powerful matriarchs and the ever-present threat of betrayal. Their obsidian skin, silvery or white hair, and violet eyes set them apart. Drow are masters of stealth, magic, and intrigue. Despite their reputation for cruelty and ambition, individual drow may seek redemption or a different path on the surface world."
        ),
        "features": "some more info",
        "male_names": [
            "Drizzt", "Jarlaxle", "Pharaun", "Ryld", "Solaufein", "Zaknafein"
        ],
        "female_names": [
            "Briza", "Eclavdra", "Liriel", "Quenthel", "Sos’Umptu", "Vierna"
        ],
        "surnames": [
            "Baenre", "Barrison", "Del'Armgo", "Do'Urden", "Hun'ett", "Mizzrym", "Oblodra", "Ssrune"
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["4'7\" (140 cm)", "84 lbs (38 kg)"],
            "medium": ["4'11\" (150 cm)", "99 lbs (45 kg)"],
            "big": ["5'3\" (160 cm)", "117 lbs (53 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": "under 120 ages",
            "mature": "120–250 ages",
            "old": "over 750 ages"
        },
        "language": ["Common", "Elvish", "Undercommon"],
        "recommended_worldview": "Chaotic Evil",
        "height_range": "4'5\"–5'5\" (135–165 cm)",
        "weight_range": "75–120 lbs (34–55 kg)",
        "recommended_classes": [
            "Rogue", "Wizard", "Cleric"
        ],
        "abilities": [
            {
                "name": "Superior Darkvision",
                "description": "You can see in darkness (shades of gray) up to 120 feet."
            },
            {
                "name": "Sunlight Sensitivity",
                "description": "You have disadvantage on attack rolls and Perception checks relying on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight."
            },
            {
                "name": "Fey Ancestry",
                "description": "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."
            },
            {
                "name": "Trance",
                "description": "You do not need to sleep. Instead, you meditate deeply for 4 hours a day and remain semiconscious."
            },
            {
                "name": "Drow Magic",
                "description": "You know the Dancing Lights cantrip. At 3rd level, you can cast Faerie Fire once per long rest; at 5th level, you can also cast Darkness once per long rest. Charisma is your spellcasting ability."
            },
            {
                "name": "Drow Weapon Training",
                "description": "Proficiency with rapiers, shortswords, and hand crossbows."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 0,
            "Dexterity": 2,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 1
        },
        "proficiencies": {
            "weapons": ["Rapier", "Shortsword", "Hand Crossbow"],
            "tools": [],
            "skills": []
        },
        "resistances": [],
        "saving_throw_advantages": [
            "Charm"
        ],
        "unique_traits": [
            "Immunity to magical sleep",
            "Sunlight Sensitivity"
        ],
        "image": "media/races/dnd_drow.png"
    },

    "lightfoot_halfling": {
        "title": "Lightfoot Halfling",
        "description": "Lightfoot halflings are friendly, quick, and unassuming. They thrive on curiosity, luck, and a knack for remaining unseen.",
        "detailed_description": (
            "Lightfoot halflings enjoy the comforts of home, the pleasures of food and song, and the thrill of adventure. Whether in bustling city quarters or peaceful farmlands, they blend into societies easily, charming friends and eluding danger through agility and stealth. They rarely seek out conflict but will defend their homes with surprising courage and cunning."
        ),
        "features": "some more info",
        "male_names": [
            "Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lyle"
        ],
        "female_names": [
            "Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Vani"
        ],
        "surnames": [
            "Brushgather", "Goodbarrel", "Greenbottle", "High-hill", "Hilltopple", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"
        ],
        "speed": "25 feet",
        "body_size": {
            "small": ["2'5\" (75 cm)", "40 lbs (18 kg)"],
            "medium": ["2'11\" (90 cm)", "53 lbs (24 kg)"],
            "big": ["3'5\" (105 cm)", "66 lbs (30 kg)"]
        },
        "size": "Small",
        "age": {
            "young": "under 35 ages",
            "mature": "35–80 ages",
            "old": "over 150 ages"
        },
        "language": ["Common", "Halfling"],
        "recommended_worldview": "Lawful Good",
        "height_range": "2'5\"–3'5\" (75–105 cm)",
        "weight_range": "40–66 lbs (18–30 kg)",
        "recommended_classes": [
            "Rogue", "Bard"
        ],
        "abilities": [
            {
                "name": "Lucky",
                "description": "When you roll a 1 on a d20 for an attack, ability check, or saving throw, you can reroll, and must use the new roll."
            },
            {
                "name": "Brave",
                "description": "You have advantage on saving throws against being frightened."
            },
            {
                "name": "Halfling Nimbleness",
                "description": "You can move through the space of any creature that is of a size larger than yours."
            },
            {
                "name": "Naturally Stealthy",
                "description": "You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 0,
            "Dexterity": 2,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 1
        },
        "proficiencies": {
            "weapons": [],
            "tools": [],
            "skills": []
        },
        "resistances": [],
        "saving_throw_advantages": [
            "Frightened"
        ],
        "unique_traits": [
            "Can move through spaces of larger creatures",
            "Excellent at blending into crowds"
        ],
        "image": "media/races/dnd_lightfoot_halfling.png"
    },

    "stout_halfling": {
        "title": "Stout Halfling",
        "description": "Stout halflings are hardier and braver than their cousins, with a resilience that often surprises larger folk.",
        "detailed_description": (
            "Stout halflings are the most robust of their race, enduring both hardship and adversity with cheerful resolve. Many believe they have dwarven ancestry, sharing a knack for resisting poison and a love of hearth and home. Their courage and toughness make them valued companions and formidable survivors."
        ),
        "features": "some more info",
        "male_names": [
            "Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lyle"
        ],
        "female_names": [
            "Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Vani"
        ],
        "surnames": [
            "Brushgather", "Goodbarrel", "Greenbottle", "High-hill", "Hilltopple", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"
        ],
        "speed": "25 feet",
        "body_size": {
            "small": ["2'7\" (80 cm)", "44 lbs (20 kg)"],
            "medium": ["3'1\" (95 cm)", "57 lbs (26 kg)"],
            "big": ["3'7\" (110 cm)", "71 lbs (32 kg)"]
        },
        "size": "Small",
        "age": {
            "young": "under 35 ages",
            "mature": "35–80 ages",
            "old": "over 150 ages"
        },
        "language": ["Common", "Halfling"],
        "recommended_worldview": "Lawful Good",
        "height_range": "2'7\"–3'7\" (80–110 cm)",
        "weight_range": "44–71 lbs (20–32 kg)",
        "recommended_classes": [
            "Rogue", "Fighter"
        ],
        "abilities": [
            {
                "name": "Lucky",
                "description": "When you roll a 1 on a d20 for an attack, ability check, or saving throw, you can reroll, and must use the new roll."
            },
            {
                "name": "Brave",
                "description": "You have advantage on saving throws against being frightened."
            },
            {
                "name": "Halfling Nimbleness",
                "description": "You can move through the space of any creature that is of a size larger than yours."
            },
            {
                "name": "Stout Resilience",
                "description": "You have advantage on saving throws against poison, and you have resistance to poison damage."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 0,
            "Dexterity": 2,
            "Constitution": 1,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        },
        "proficiencies": {
            "weapons": [],
            "tools": [],
            "skills": []
        },
        "resistances": [
            "Poison (resistance and advantage on saves)"
        ],
        "saving_throw_advantages": [
            "Frightened", "Poison"
        ],
        "unique_traits": [
            "More resistant to poison than other halflings"
        ],
        "image": "media/races/dnd_stout_halfling.png"
    },

    "human": {
        "title": "Human",
        "description": "Humans are the most adaptable and ambitious people among the common races. Their diversity gives rise to varied cultures, talents, and worldviews.",
        "detailed_description": (
            "Humans dominate much of the world, with settlements in every environment. Their lifespans are short by the standards of other races, but their drive to achieve leads to rapid social and technological advancement. Humans can be warriors, wizards, or everything in between, and their variety makes them both unpredictable and endlessly fascinating."
        ),
        "features": "some more info",
        "male_names": [
            "Ander", "Brennen", "Darvin", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn"
        ],
        "female_names": [
            "Arveene", "Esvele", "Jhessail", "Kerri", "Lureene", "Miri", "Rowan", "Shandri", "Tessele"
        ],
        "surnames": [
            "Brightwood", "Helder", "Hornraven", "Lackman", "Stormwind", "Windrivver"
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["4'9\" (145 cm)", "99 lbs (45 kg)"],
            "medium": ["5'7\" (170 cm)", "154 lbs (70 kg)"],
            "big": ["6'5\" (195 cm)", "220 lbs (100 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": "under 20 ages",
            "mature": "20–40 ages",
            "old": "over 60 ages"
        },
        "language": ["Common"],
        "extra_language": 1,
        "recommended_worldview": "All worldviews",
        "height_range": "4'9\"–6'5\" (145–195 cm)",
        "weight_range": "99–220 lbs (45–100 kg)",
        "recommended_classes": [
            "Any"
        ],
        "abilities": [
            {
                "name": "Versatile",
                "description": "Each ability score increases by 1."
            },
            {
                "name": "Extra Language",
                "description": "You can speak, read, and write one extra language of your choice."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 1,
            "Dexterity": 1,
            "Constitution": 1,
            "Intelligence": 1,
            "Wisdom": 1,
            "Charisma": 1
        },
        "proficiencies": {
            "weapons": [],
            "tools": [],
            "skills": []
        },
        "resistances": [],
        "saving_throw_advantages": [],
        "unique_traits": [
            "Highly flexible racial bonuses"
        ],
        "image": "media/races/dnd_human.png"
    },
    "dragonborn": {
        "title": "Dragonborn",
        "description": "Dragonborn are proud, honorable, and driven by a strong sense of self-improvement and legacy derived from their draconic heritage. They are tall, powerful, and marked by scales and iconic breath weapons.",
        "detailed_description": (
            "Descended from dragons, dragonborn strive to emulate their ancestors' greatness and honor. They live by strict codes of conduct, value personal achievement, and tend to be loyal and steadfast. Few match a dragonborn's drive for glory and self-mastery, while their imposing presence and breath weapon make them fearsome in battle."
        ),
        "features": "some more info",
        "male_names": [
            "Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Raiann", "Shamash"
        ],
        "female_names": [
            "Akra", "Biri", "Daar", "Farideh", "Harann", "Havilar", "Kava", "Korinn", "Mishann", "Sora"
        ],
        "surnames": [
            "Clethtinthiallor", "Daardendrian", "Delmirev", "Drachedandion", "Fenkenkabradon", "Kepeshkmolik", "Kerrhylon", "Turnuroth"
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["5'7\" (170 cm)", "154 lbs (70 kg)"],
            "medium": ["6'1\" (185 cm)", "220 lbs (100 kg)"],
            "big": ["6'7\" (200 cm)", "287 lbs (130 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": "under 12 ages",
            "mature": "12–30 ages",
            "old": "over 80 ages"
        },
        "language": ["Common", "Draconic"],
        "recommended_worldview": "Lawful Good",
        "height_range": "6'0\"–6'8\" (183–203 cm)",
        "weight_range": "220–350 lbs (100–159 kg)",
        "recommended_classes": [
            "Paladin", "Sorcerer", "Fighter"
        ],
        "abilities": [
            {
                "name": "Draconic Ancestry",
                "description": "Choose a dragon type, which determines the breath weapon and damage resistance."
            },
            {
                "name": "Breath Weapon",
                "description": "You can use an action to exhale destructive energy; specifics depend on your draconic ancestry."
            },
            {
                "name": "Damage Resistance",
                "description": "You have resistance to the damage type associated with your draconic ancestry."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 2,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 1
        },
        "proficiencies": {
            "weapons": [],
            "tools": [],
            "skills": []
        },
        "resistances": [
            "Depends on draconic ancestry (fire, cold, lightning, etc.)"
        ],
        "saving_throw_advantages": [],
        "unique_traits": [
            "Breath Weapon attack as an action",
            "Choice of resistance and weapon shape based on ancestry"
        ],
        "image": "media/races/dnd_dragonborn.png"
},

    "forest_gnome": {
        "title": "Forest Gnome",
        "description": "Forest gnomes are shy, good-natured, and mischievous woodland folk known for their love of animals, protective magical abilities, and stealth.",
        "detailed_description": (
            "Rarely seen by outsiders, forest gnomes are reclusive but deeply magical members of woodland communities. They prefer cleverness over confrontation, communicate with small animals, and use illusory magic to avoid trouble. Their lighthearted humor and creativity make them skilled musicians and craftsmen."
        ),
        "features": "some more info",
        "male_names": [
            "Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin"
        ],
        "female_names": [
            "Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ellyjobell", "Ellywick", "Loopmottin"
        ],
        "surnames": [
            "Beren", "Daergel", "Folkor", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Timbers", "Turen"
        ],
        "speed": "25 feet",
        "body_size": {
            "small": ["2'9\" (85 cm)", "40 lbs (18 kg)"],
            "medium": ["3'3\" (100 cm)", "49 lbs (22 kg)"],
            "big": ["3'9\" (115 cm)", "60 lbs (27 kg)"]
        },
        "size": "Small",
        "age": {
            "young": "under 60 ages",
            "mature": "60–120 ages",
            "old": "over 350 ages"
        },
        "language": ["Common", "Gnomish"],
        "recommended_worldview": "Neutral Good",
        "height_range": "2'9\"–3'9\" (85–115 cm)",
        "weight_range": "40–60 lbs (18–27 kg)",
        "recommended_classes": [
            "Wizard", "Rogue"
        ],
        "abilities": [
            {
                "name": "Darkvision",
                "description": "You can see in darkness (shades of gray) up to 60 feet."
            },
            {
                "name": "Gnome Cunning",
                "description": "Advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
            },
            {
                "name": "Natural Illusionist",
                "description": "You know the minor illusion cantrip. Intelligence is your spellcasting ability."
            },
            {
                "name": "Speak with Small Beasts",
                "description": "You can communicate simple ideas with Small or smaller beasts."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 0,
            "Dexterity": 1,
            "Constitution": 0,
            "Intelligence": 2,
            "Wisdom": 0,
            "Charisma": 0
        },
        "proficiencies": {
            "weapons": [],
            "tools": [],
            "skills": []
        },
        "resistances": [],
        "saving_throw_advantages": [
            "All saves against magic (Int, Wis, Cha)"
        ],
        "unique_traits": [
            "Ability to communicate with small woodland creatures",
            "Minor illusion as a cantrip"
        ],
        "image": "media/races/dnd_forest_gnome.png"
    },

    "rock_gnome": {
        "title": "Rock Gnome",
        "description": "Rock gnomes are curious, intelligent, and naturally inventive. Their love of machines, alchemy, and lore makes them skilled craftsmen and tinkerers.",
        "detailed_description": (
            "Rock gnomes are the most common gnome subrace and are renowned for their natural inventiveness and technical skill. They often delight in creating small wonders, gadgets, or clever tricks, filling their homes with mechanical marvels and fantastical tools. Cheerful and energetic, they cherish family, tradition, and discovery."
        ),
        "features": "some more info",
        "male_names": [
            "Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin"
        ],
        "female_names": [
            "Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ellyjobell", "Ellywick", "Loopmottin"
        ],
        "surnames": [
            "Beren", "Daergel", "Folkor", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Timbers", "Turen"
        ],
        "speed": "25 feet",
        "body_size": {
            "small": ["2'11\" (90 cm)", "44 lbs (20 kg)"],
            "medium": ["3'5\" (105 cm)", "55 lbs (25 kg)"],
            "big": ["3'11\" (120 cm)", "66 lbs (30 kg)"]
        },
        "size": "Small",
        "age": {
            "young": "under 60 ages",
            "mature": "60–120 ages",
            "old": "over 350 ages"
        },
        "language": ["Common", "Gnomish"],
        "recommended_worldview": "Neutral Good",
        "height_range": "2'11\"–3'11\" (90–120 cm)",
        "weight_range": "44–66 lbs (20–30 kg)",
        "recommended_classes": [
            "Artificer", "Wizard"
        ],
        "abilities": [
            {
                "name": "Darkvision",
                "description": "You can see in darkness (shades of gray) up to 60 feet."
            },
            {
                "name": "Gnome Cunning",
                "description": "Advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
            },
            {
                "name": "Artificer’s Lore",
                "description": "Add twice proficiency bonus to History checks related to magic items, alchemical objects, or technological devices."
            },
            {
                "name": "Tinker",
                "description": "Proficiency with artisan’s tools; can construct tiny clockwork devices."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 0,
            "Dexterity": 1,
            "Constitution": 0,
            "Intelligence": 2,
            "Wisdom": 0,
            "Charisma": 0
        },
        "proficiencies": {
            "weapons": [],
            "tools": ["Tinker’s tools", "Artisan’s tools (choose one)"],
            "skills": []
        },
        "resistances": [],
        "saving_throw_advantages": [
            "All saves against magic (Int, Wis, Cha)"
        ],
        "unique_traits": [
            "Expertise in magical, alchemical, and technical History",
            "Ability to make clockwork inventions"
        ],
        "image": "media/races/dnd_rock_gnome.png"
    },

    "half_elf": {
        "title": "Half-Elf",
        "description": "Half-elves blend the best of human versatility and elven grace. They often act as diplomats or wanderers, well-suited to a life between worlds.",
        "detailed_description": (
            "Blessed with elven longevity and charm as well as human adaptability, half-elves have no true homeland. They thrive in both human societies and among elves, though they don’t always feel they belong in either. Charismatic and perceptive, many half-elves find themselves as natural mediators and leaders."
        ),
        "features": "some more info",
        "male_names": [
            "Adran", "Aramil", "Carric", "Erevan", "Ivellios", "Laucian", "Quarion", "Soveliss", "Varis"
        ],
        "female_names": [
            "Adrie", "Drusilia", "Felosial", "Keyleth", "Naivara", "Shanairra", "Thia", "Valanthe", "Xanaphia"
        ],
        "surnames": [
            "Amakiir", "Holimion", "Liadon", "Nai'lo", "Xiloscient"
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["5'1\" (155 cm)", "106 lbs (48 kg)"],
            "medium": ["5'7\" (170 cm)", "143 lbs (65 kg)"],
            "big": ["6'1\" (185 cm)", "187 lbs (85 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": "under 30 ages",
            "mature": "30–70 ages",
            "old": "over 180 ages"
        },
        "language": ["Common", "Elvish"],
        "extra_language": 2,
        "recommended_worldview": "Chaotic Good",
        "height_range": "5'0\"–6'2\" (150–188 cm)",
        "weight_range": "100–190 lbs (45–86 kg)",
        "recommended_classes": [
            "Bard", "Sorcerer", "Warlock"
        ],
        "abilities": [
            {
                "name": "Darkvision",
                "description": "You can see in darkness (shades of gray) up to 60 feet."
            },
            {
                "name": "Fey Ancestry",
                "description": "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."
            },
            {
                "name": "Skill Versatility",
                "description": "You gain proficiency in two skills of your choice."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 0,
            "Dexterity": 1,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 2
        },
        "proficiencies": {
            "weapons": [],
            "tools": [],
            "skills": ["Any two skills"]
        },
        "resistances": [],
        "saving_throw_advantages": [
            "Charm"
        ],
        "unique_traits": [
            "Immunity to magical sleep",
            "Receive proficiency in two skills of your choice"
        ],
        "image": "media/races/dnd_half_elf.png"
    },

    "half_orc": {
        "title": "Half-Orc",
        "description": "Half-orcs are fierce, powerful, and energetic, often caught between the civilized world and the savage traditions of orc tribes.",
        "detailed_description": (
            "The children of human and orc unions, half-orcs frequently face prejudice but also earn respect for their physical prowess and determination. They excel in harsh environments and arduous tasks, and are often proud of their ability to endure and overcome."
        ),
        "features": "some more info",
        "male_names": [
            "Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Ront"
        ],
        "female_names": [
            "Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha"
        ],
        "surnames": [
            "No family names; half-orc names are typically chosen to inspire fear or valor."
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["5'1\" (155 cm)", "132 lbs (60 kg)"],
            "medium": ["5'11\" (180 cm)", "198 lbs (90 kg)"],
            "big": ["6'7\" (200 cm)", "265 lbs (120 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": "under 20 ages",
            "mature": "20–40 ages",
            "old": "over 75 ages"
        },
        "language": ["Common", "Orc"],
        "recommended_worldview": "Chaotic Neutral",
        "height_range": "5'0\"–7'0\" (150–215 cm)",
        "weight_range": "125–300 lbs (57–136 kg)",
        "recommended_classes": [
            "Barbarian", "Fighter"
        ],
        "abilities": [
            {
                "name": "Darkvision",
                "description": "You can see in darkness (shades of gray) up to 60 feet."
            },
            {
                "name": "Menacing",
                "description": "You gain proficiency in the Intimidation skill."
            },
            {
                "name": "Relentless Endurance",
                "description": "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest."
            },
            {
                "name": "Savage Attacks",
                "description": "When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 2,
            "Dexterity": 0,
            "Constitution": 1,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        },
        "proficiencies": {
            "weapons": [],
            "tools": [],
            "skills": ["Intimidation"]
        },
        "resistances": [],
        "saving_throw_advantages": [],
        "unique_traits": [
            "Drop to 1 hit point once per long rest (Relentless Endurance)",
            "High critical hit damage with melee weapons (Savage Attacks)"
        ],
        "image": "media/races/dnd_half_orc.png"
    },

    "tiefling": {
        "title": "Tiefling",
        "description": "Tieflings are marked by their infernal heritage, manifesting physical traits such as horns, tails, and glowing eyes, as well as an innate gift for arcane magic and resistance to fire.",
        "detailed_description": (
            "Bearing the legacy of a fiendish bloodline, tieflings often face suspicion and prejudice, yet they possess a powerful will and resilience. Clever, adaptable, and mysterious, tieflings balance struggle with ambition and frequently walk the line between darkness and virtue."
        ),
        "features": "some more info",
        "male_names": [
            "Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Melech"
        ],
        "female_names": [
            "Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria"
        ],
        "surnames": [
            "No family names; tieflings often use given names only or invent surnames."
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["4'9\" (145 cm)", "88 lbs (40 kg)"],
            "medium": ["5'5\" (165 cm)", "121 lbs (55 kg)"],
            "big": ["6'1\" (185 cm)", "154 lbs (70 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": "under 25 ages",
            "mature": "25–40 ages",
            "old": "over 80 ages"
        },
        "language": ["Common", "Infernal"],
        "recommended_worldview": "Chaotic Evil",
        "height_range": "4'9\"–6'1\" (145–185 cm)",
        "weight_range": "88–154 lbs (40–70 kg)",
        "recommended_classes": [
            "Warlock", "Rogue", "Sorcerer"
        ],
        "abilities": [
            {
                "name": "Darkvision",
                "description": "You can see in darkness (shades of gray) up to 60 feet."
            },
            {
                "name": "Hellish Resistance",
                "description": "You have resistance to fire damage."
            },
            {
                "name": "Infernal Legacy",
                "description": "You know the Thaumaturgy cantrip. At 3rd level, you can cast Hellish Rebuke once per long rest. At 5th level, you can also cast Darkness once per long rest. Charisma is your spellcasting ability."
            }
        ],
        "characteristic_bonuses": {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 1,
            "Wisdom": 0,
            "Charisma": 2
        },
        "proficiencies": {
            "weapons": [],
            "tools": [],
            "skills": []
        },
        "resistances": [
            "Fire"
        ],
        "saving_throw_advantages": [],
        "unique_traits": [
            "Natural talent for infernal magic",
            "Innate resistance to fire"
        ],
        "image": "media/races/dnd_tiefling.png"
    }
}