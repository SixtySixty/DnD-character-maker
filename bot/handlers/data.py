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
        "age": [
            "under 70 ages",
            "70-200 ages",
            "over 350 ages"
        ],
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
        "age": [
            "under 70 ages",
            "70-200 ages",
            "over 350 ages"
        ],
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
            "Amakiir (Gemflower)", "Galanodel (Moonwhisper)", "Holimion (Diamonddew)", "Ilphelkiir (Gemblossom)",
            "Liadon (Silverfrond)", "Meliamne (Oakenheel)", "Nai'lo (Nightbreeze)", "Siannodel (Moonbrook)", "Xiloscient (Goldpetal)"
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["5'1\" (155 cm)", "99 lbs (45 kg)"],
            "medium": ["5'5\" (165 cm)", "119 lbs (54 kg)"],
            "big": ["5'11\" (180 cm)", "143 lbs (65 kg)"]
        },
        "size": "Medium",
        "age": [
            "under 120 ages",
            "120–250 ages",
            "over 750 ages"
        ],
        "language": ["Common", "Elvish", "One extra language (any)"],
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
        "age": [
            "under 120 ages",
            "120–250 ages",
            "over 750 ages"
        ],
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
        "age": [
            "under 120 ages",
            "120–250 ages",
            "over 750 ages"
        ],
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
        "image": "media/races/dnd_dark_elf.png"
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
        "age": [
            "under 35 ages",
            "35–80 ages",
            "over 150 ages"
        ],
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
        "age": [
            "under 35 ages",
            "35–80 ages",
            "over 150 ages"
        ],
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
            "Ander", "Brennen", "Darvin", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal"
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
        "age": [
            "under 20 ages",
            "20–40 ages",
            "over 60 ages"
        ],
        "language": ["Common", "One extra language (any)"],
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
        "age": [
            "under 12 ages",
            "12–30 ages",
            "over 80 ages"
        ],
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
        "age": [
            "under 60 ages",
            "60–120 ages",
            "over 350 ages"
        ],
        "language": ["Common", "Gnomish", "Speak with Small Beasts"],
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
        "age": [
            "under 60 ages",
            "60–120 ages",
            "over 350 ages"
        ],
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
            "Amakiir (Gemflower)", "Holimion (Diamonddew)", "Liadon (Silverfrond)", "Nai'lo (Nightbreeze)", "Xiloscient (Goldpetal)"
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["5'1\" (155 cm)", "106 lbs (48 kg)"],
            "medium": ["5'7\" (170 cm)", "143 lbs (65 kg)"],
            "big": ["6'1\" (185 cm)", "187 lbs (85 kg)"]
        },
        "size": "Medium",
        "age": [
            "under 30 ages",
            "30–70 ages",
            "over 180 ages"
        ],
        "language": ["Common", "Elvish", "Two extra languages (any)"],
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
        "age": [
            "under 20 ages",
            "20–40 ages",
            "over 75 ages"
        ],
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
        "age": [
            "under 25 ages",
            "25–40 ages",
            "over 80 ages"
        ],
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




# classes, their descriptions, characteristics and pictures

class_info = {
    "barbarian": {
        "title": "Barbarian",
        "description": "Barbarians are mighty warriors empowered by primal instincts and an indomitable will. Their Rage is a physical embodiment of primal fury, enabling them to shrug off blows and deal devastating attacks. Barbarians are fierce defenders, often at home in wild places and on the open road.",
        "detailed_description": (
            "Barbarians find power in a raw, primal connection to the wild—sometimes as tribal champions, lone wanderers, or unstoppable forces of nature. Their rage and resilience are legendary, allowing them to endure wounds that would fell other warriors. Fueled by freedom and a deep-rooted sense of self, barbarians are both feared for their ferocity and respected for their fierce loyalty."
        ),
        "features": "more info",
        "hit_die": "d12",
        "primary_ability": ["Strength"],
        "secondary_ability": ["Constitution"],
        "saving_throws": ["Strength", "Constitution"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields (no heavy armor)"],
        "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
        "tool_proficiencies": [],
        "skills_choices": [
            "Animal Handling", "Athletics", "Intimidation", "Nature",
            "Perception", "Survival"
        ],
        "skills_number": 2,
        "equipment_choices": [
            ["Greataxe", "Any martial melee weapon"],
            ["Two handaxes", "Any simple weapon"],
            ["Explorer's pack and four javelins"]
        ],
        "subclasses": [
            "Path of the Berserker",
            "Path of the Totem Warrior",
            "Path of the Battlerager",
            "Path of the Ancestral Guardian",
            "Path of the Storm Herald",
            "Path of the Zealot"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Rage", "Unarmored Defense"]},
            {"level": 2, "features": ["Reckless Attack", "Danger Sense"]},
            {"level": 3, "features": ["Primal Path", "Path Feature"]},
            {"level": 5, "features": ["Extra Attack", "Fast Movement"]},
            {"level": 7, "features": ["Feral Instinct"]},
            {"level": 9, "features": ["Brutal Critical (1 die)"]},
            {"level": 11, "features": ["Relentless Rage"]},
            {"level": 13, "features": ["Brutal Critical (2 dice)"]},
            {"level": 15, "features": ["Persistent Rage"]},
            {"level": 17, "features": ["Brutal Critical (3 dice)"]},
            {"level": 18, "features": ["Indomitable Might"]},
            {"level": 20, "features": ["Primal Champion"]}
        ],
        "characteristics": {
            "Strength": 15,
            "Dexterity": 13,
            "Constitution": 14,
            "Intelligence": 10,
            "Wisdom": 12,
            "Charisma": 8
        },
        "recommended_races": [
            "Half-Orc", "Mountain Dwarf", "Human", "Goliath"
        ],
        "image": "media/classes/dnd_barbarian.png"
    },
    "bard": {
        "title": "Bard",
        "description": "Bards are masters of song, speech, and the magic they contain. They weave spells through music and words, inspiring allies and manipulating reality through the power of performance.",
        "detailed_description": (
            "Bards are traveling performers, storytellers, and lorekeepers who use their charisma and magical abilities to inspire others. They gather knowledge from many sources, making them versatile spellcasters who can support their party in numerous ways. Whether lifting spirits with heroic ballads or cutting down enemies with vicious mockery, bards bring both art and arcane power to any adventure."
        ),
        "features": "more info",
        "hit_die": "d8",
        "primary_ability": ["Charisma"],
        "secondary_ability": ["Dexterity"],
        "saving_throws": ["Dexterity", "Charisma"],
        "armor_proficiencies": ["Light armor"],
        "weapon_proficiencies": ["Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"],
        "tool_proficiencies": ["Three musical instruments of your choice"],
        "skills_choices": ["Any three skills of your choice"],
        "skills_number": 3,
        "equipment_choices": [
            ["Rapier", "Longsword", "Any simple weapon"],
            ["Diplomat's pack", "Entertainer's pack"],
            ["Leather armor", "Dagger", "Simple weapon"]
        ],
        "subclasses": [
            "College of Lore",
            "College of Valor",
            "College of Glamour",
            "College of Whispers",
            "College of Swords",
            "College of Eloquence"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Bardic Inspiration", "Spellcasting"]},
            {"level": 2, "features": ["Jack of All Trades", "Song of Rest"]},
            {"level": 3, "features": ["Bard College", "Expertise"]},
            {"level": 4, "features": ["Ability Score Improvement"]},
            {"level": 5, "features": ["Bardic Inspiration (d8)", "Font of Inspiration"]},
            {"level": 6, "features": ["Countercharm", "Bard College feature"]},
            {"level": 10, "features": ["Bardic Inspiration (d10)", "Magical Secrets"]},
            {"level": 20, "features": ["Superior Inspiration"]}
        ],
        "characteristics": {
            "Strength": 8,
            "Dexterity": 14,
            "Constitution": 12,
            "Intelligence": 13,
            "Wisdom": 10,
            "Charisma": 15
        },
        "recommended_races": [
            "Half-Elf", "Tiefling", "Human", "Dragonborn"
        ],
        "image": "media/classes/dnd_bard.png"
    },

    "cleric": {
        "title": "Cleric",
        "description": "Clerics are intermediaries between the mortal world and the distant planes of the gods. They channel divine power to heal wounds, protect allies, and smite enemies.",
        "detailed_description": (
            "Clerics draw their power from divine sources, whether gods, forces of nature, or abstract ideals. They serve as healers, protectors, and champions of their faith. With access to both divine magic and martial prowess, clerics can adapt to fill many roles in an adventuring party while maintaining their sacred duties."
        ),
        "features": "more info",
        "hit_die": "d8",
        "primary_ability": ["Wisdom"],
        "secondary_ability": ["Constitution"],
        "saving_throws": ["Wisdom", "Charisma"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields"],
        "weapon_proficiencies": ["Simple weapons"],
        "tool_proficiencies": [],
        "skills_choices": [
            "History", "Insight", "Medicine", "Persuasion", "Religion"
        ],
        "skills_number": 2,
        "equipment_choices": [
            ["Scale mail", "Leather armor", "Chain mail if proficient"],
            ["Shield", "Any simple weapon"],
            ["Light crossbow and 20 bolts", "Any simple weapon"],
            ["Priest's pack", "Explorer's pack"]
        ],
        "subclasses": [
            "Life Domain",
            "Light Domain",
            "Knowledge Domain",
            "Nature Domain",
            "Tempest Domain",
            "Trickery Domain",
            "War Domain"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Spellcasting", "Divine Domain"]},
            {"level": 2, "features": ["Channel Divinity", "Turn Undead"]},
            {"level": 5, "features": ["Destroy Undead (CR 1/2)"]},
            {"level": 8, "features": ["Destroy Undead (CR 1)", "Divine Strike"]},
            {"level": 10, "features": ["Divine Intervention"]},
            {"level": 20, "features": ["Divine Intervention Improvement"]}
        ],
        "characteristics": {
            "Strength": 14,
            "Dexterity": 8,
            "Constitution": 13,
            "Intelligence": 10,
            "Wisdom": 15,
            "Charisma": 12
        },
        "recommended_races": [
            "Human", "Hill Dwarf", "Dragonborn", "Half-Elf"
        ],
        "image": "media/classes/dnd_cleric.png"
    },

    "druid": {
        "title": "Druid",
        "description": "Druids revere nature above all, gaining their spells and other magical powers from the force of nature itself or from a nature deity. They can transform into beasts and command the elements.",
        "detailed_description": (
            "Druids are guardians of the natural world, wielding primal magic that stems from nature itself. They can take the form of animals, control the weather, and heal with natural remedies. Druids often serve as protectors of sacred groves, mediators between civilization and the wild, and champions of the natural order."
        ),
        "features": "more info",
        "hit_die": "d8",
        "primary_ability": ["Wisdom"],
        "secondary_ability": ["Constitution"],
        "saving_throws": ["Intelligence", "Wisdom"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields (non-metal only)"],
        "weapon_proficiencies": ["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"],
        "tool_proficiencies": ["Herbalism kit"],
        "skills_choices": [
            "Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"
        ],
        "skills_number": 2,
        "equipment_choices": [
            ["Wooden shield", "Any simple melee weapon"],
            ["Scimitar", "Any simple melee weapon"],
            ["Leather armor", "Explorer's pack", "Dagger"]
        ],
        "subclasses": [
            "Circle of the Land",
            "Circle of the Moon",
            "Circle of Dreams",
            "Circle of the Shepherd",
            "Circle of Spores",
            "Circle of Stars"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Druidcraft", "Spellcasting"]},
            {"level": 2, "features": ["Wild Shape", "Druid Circle"]},
            {"level": 4, "features": ["Wild Shape improvement"]},
            {"level": 8, "features": ["Wild Shape improvement"]},
            {"level": 18, "features": ["Timeless Body", "Beast Spells"]},
            {"level": 20, "features": ["Archdruid"]}
        ],
        "characteristics": {
            "Strength": 8,
            "Dexterity": 12,
            "Constitution": 14,
            "Intelligence": 13,
            "Wisdom": 15,
            "Charisma": 10
        },
        "recommended_races": [
            "Wood Elf", "Forest Gnome", "Human", "Firbolg"
        ],
        "image": "media/classes/dnd_druid.png"
    },

    "fighter": {
        "title": "Fighter",
        "description": "Fighters are masters of martial combat, skilled with a variety of weapons and armor. They are well-acquainted with death, both meting it out and staring it defiantly in the face.",
        "detailed_description": (
            "Fighters learn the basics of all combat styles and can specialize in particular fighting techniques. They are the most diverse class, capable of excelling in any combat role from heavily armored tank to nimble archer. Their martial prowess and tactical knowledge make them invaluable in any conflict."
        ),
        "features": "more info",
        "hit_die": "d10",
        "primary_ability": ["Strength or Dexterity"],
        "secondary_ability": ["Constitution"],
        "saving_throws": ["Strength", "Constitution"],
        "armor_proficiencies": ["All armor", "Shields"],
        "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
        "tool_proficiencies": [],
        "skills_choices": [
            "Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"
        ],
        "skills_number": 2,
        "equipment_choices": [
            ["Chain mail", "Leather armor", "Studded leather"],
            ["Shield and any simple weapon", "Two martial weapons"],
            ["Light crossbow and 20 bolts", "Two handaxes"],
            ["Dungeoneer's pack", "Explorer's pack"]
        ],
        "subclasses": [
            "Champion",
            "Battle Master",
            "Eldritch Knight",
            "Arcane Archer",
            "Cavalier",
            "Samurai"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Fighting Style", "Second Wind"]},
            {"level": 2, "features": ["Action Surge"]},
            {"level": 3, "features": ["Martial Archetype"]},
            {"level": 5, "features": ["Extra Attack"]},
            {"level": 9, "features": ["Indomitable"]},
            {"level": 11, "features": ["Extra Attack (2)"]},
            {"level": 20, "features": ["Extra Attack (3)"]}
        ],
        "characteristics": {
            "Strength": 15,
            "Dexterity": 14,
            "Constitution": 13,
            "Intelligence": 8,
            "Wisdom": 10,
            "Charisma": 12
        },
        "recommended_races": [
            "Human", "Half-Orc", "Dragonborn", "Mountain Dwarf"
        ],
        "image": "media/classes/dnd_fighter.png"
    },

    "monk": {
        "title": "Monk",
        "description": "Monks harness inner power through discipline and training. They use ki to perform supernatural feats and fight with speed and precision rather than brute force.",
        "detailed_description": (
            "Monks are masters of martial arts, using their bodies as weapons and channeling mystical energy called ki. They seek perfection through meditation, training, and ascetic practices. Their speed, agility, and supernatural abilities make them formidable opponents who can strike multiple times and move with incredible swiftness."
        ),
        "features": "more info",
        "hit_die": "d8",
        "primary_ability": ["Dexterity"],
        "secondary_ability": ["Wisdom"],
        "saving_throws": ["Strength", "Dexterity"],
        "armor_proficiencies": [],
        "weapon_proficiencies": ["Simple weapons", "Shortswords"],
        "tool_proficiencies": ["One type of artisan's tools or one musical instrument"],
        "skills_choices": [
            "Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"
        ],
        "skills_number": 2,
        "equipment_choices": [
            ["Shortsword", "Any simple weapon"],
            ["Dungeoneer's pack", "Explorer's pack"],
            ["10 darts"]
        ],
        "subclasses": [
            "Way of the Open Hand",
            "Way of Shadow",
            "Way of the Four Elements",
            "Way of the Long Death",
            "Way of the Sun Soul",
            "Way of the Drunken Master"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Unarmored Defense", "Martial Arts"]},
            {"level": 2, "features": ["Ki", "Flurry of Blows", "Patient Defense", "Step of the Wind"]},
            {"level": 3, "features": ["Monastic Tradition", "Deflect Missiles"]},
            {"level": 4, "features": ["Slow Fall"]},
            {"level": 5, "features": ["Extra Attack", "Stunning Strike"]},
            {"level": 6, "features": ["Ki-Empowered Strikes"]},
            {"level": 7, "features": ["Evasion", "Stillness of Mind"]},
            {"level": 20, "features": ["Perfect Self"]}
        ],
        "characteristics": {
            "Strength": 12,
            "Dexterity": 15,
            "Constitution": 13,
            "Intelligence": 10,
            "Wisdom": 14,
            "Charisma": 8
        },
        "recommended_races": [
            "Human", "Wood Elf", "Halfling", "Variant Human"
        ],
        "image": "media/classes/dnd_monk.png"
    },

    "paladin": {
        "title": "Paladin",
        "description": "Paladins are holy warriors bound by sacred oaths. They fight for justice and righteousness, wielding divine magic alongside martial prowess to protect the innocent.",
        "detailed_description": (
            "Paladins are champions of justice who swear sacred oaths that grant them divine power. They serve as protectors of the weak, destroyers of evil, and beacons of hope in dark times. Their combination of martial skill, divine magic, and unwavering conviction makes them formidable allies and fearsome enemies of evil."
        ),
        "features": "more info",
        "hit_die": "d10",
        "primary_ability": ["Strength"],
        "secondary_ability": ["Charisma"],
        "saving_throws": ["Wisdom", "Charisma"],
        "armor_proficiencies": ["All armor", "Shields"],
        "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
        "tool_proficiencies": [],
        "skills_choices": [
            "Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"
        ],
        "skills_number": 2,
        "equipment_choices": [
            ["Chain mail", "Leather armor"],
            ["Shield and any simple weapon", "Two martial weapons"],
            ["Five javelins", "Any simple melee weapon"],
            ["Priest's pack", "Explorer's pack"]
        ],
        "subclasses": [
            "Oath of Devotion",
            "Oath of the Ancients",
            "Oath of Vengeance",
            "Oath of Conquest",
            "Oath of Redemption",
            "Oath of Glory"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Divine Sense", "Lay on Hands"]},
            {"level": 2, "features": ["Fighting Style", "Spellcasting", "Divine Smite"]},
            {"level": 3, "features": ["Divine Health", "Sacred Oath"]},
            {"level": 5, "features": ["Extra Attack"]},
            {"level": 6, "features": ["Aura of Protection"]},
            {"level": 10, "features": ["Aura of Courage"]},
            {"level": 20, "features": ["Sacred Oath feature"]}
        ],
        "characteristics": {
            "Strength": 15,
            "Dexterity": 10,
            "Constitution": 13,
            "Intelligence": 8,
            "Wisdom": 12,
            "Charisma": 14
        },
        "recommended_races": [
            "Human", "Dragonborn", "Aasimar", "Half-Elf"
        ],
        "image": "media/classes/dnd_paladin.png"
    },

    "ranger": {
        "title": "Ranger",
        "description": "Rangers are skilled hunters and trackers who protect the borders of civilization from the threats of the wild. They are warriors of the wilderness, skilled with bow and blade.",
        "detailed_description": (
            "Rangers are guardians of the wild places, skilled in hunting, tracking, and survival. They know the secrets of the wilderness and can navigate any terrain. With their combat expertise and nature magic, rangers serve as scouts, guides, and protectors of the natural world."
        ),
        "features": "more info",
        "hit_die": "d10",
        "primary_ability": ["Dexterity"],
        "secondary_ability": ["Wisdom"],
        "saving_throws": ["Strength", "Dexterity"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields"],
        "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
        "tool_proficiencies": [],
        "skills_choices": [
            "Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"
        ],
        "skills_number": 3,
        "equipment_choices": [
            ["Scale mail", "Leather armor"],
            ["Two shortswords", "Two simple melee weapons"],
            ["Dungeoneer's pack", "Explorer's pack"],
            ["Longbow and quiver of 20 arrows"]
        ],
        "subclasses": [
            "Beast Master",
            "Hunter",
            "Gloom Stalker",
            "Horizon Walker",
            "Monster Slayer",
            "Fey Wanderer"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Favored Enemy", "Natural Explorer"]},
            {"level": 2, "features": ["Fighting Style", "Spellcasting"]},
            {"level": 3, "features": ["Ranger Archetype", "Primeval Awareness"]},
            {"level": 5, "features": ["Extra Attack"]},
            {"level": 8, "features": ["Land's Stride"]},
            {"level": 14, "features": ["Vanish"]},
            {"level": 20, "features": ["Foe Slayer"]}
        ],
        "characteristics": {
            "Strength": 12,
            "Dexterity": 15,
            "Constitution": 13,
            "Intelligence": 8,
            "Wisdom": 14,
            "Charisma": 10
        },
        "recommended_races": [
            "Wood Elf", "Human", "Half-Elf", "Variant Human"
        ],
        "image": "media/classes/dnd_ranger.png"
    },

    "rogue": {
        "title": "Rogue",
        "description": "Rogues rely on skill, stealth, and their foes' vulnerabilities to get the upper hand in any situation. They excel at what others can't or won't do.",
        "detailed_description": (
            "Rogues are skilled in the arts of stealth, deception, and precision strikes. They prefer to work from the shadows, using cunning and expertise rather than brute force. Whether as thieves, spies, or assassins, rogues are masters of getting into places they shouldn't be and finding things that others have lost."
        ),
        "features": "more info",
        "hit_die": "d8",
        "primary_ability": ["Dexterity"],
        "secondary_ability": ["Intelligence"],
        "saving_throws": ["Dexterity", "Intelligence"],
        "armor_proficiencies": ["Light armor"],
        "weapon_proficiencies": ["Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"],
        "tool_proficiencies": ["Thieves' tools"],
        "skills_choices": [
            "Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"
        ],
        "skills_number": 4,
        "equipment_choices": [
            ["Rapier", "Shortsword"],
            ["Shortbow and quiver of 20 arrows", "Shortsword"],
            ["Burglar's pack", "Dungeoneer's pack", "Explorer's pack"],
            ["Leather armor", "Two daggers", "Thieves' tools"]
        ],
        "subclasses": [
            "Thief",
            "Assassin",
            "Arcane Trickster",
            "Mastermind",
            "Swashbuckler",
            "Inquisitive"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Expertise", "Sneak Attack", "Thieves' Cant"]},
            {"level": 2, "features": ["Cunning Action"]},
            {"level": 3, "features": ["Roguish Archetype"]},
            {"level": 5, "features": ["Uncanny Dodge"]},
            {"level": 7, "features": ["Evasion"]},
            {"level": 11, "features": ["Reliable Talent"]},
            {"level": 20, "features": ["Stroke of Luck"]}
        ],
        "characteristics": {
            "Strength": 12,
            "Dexterity": 15,
            "Constitution": 13,
            "Intelligence": 14,
            "Wisdom": 10,
            "Charisma": 8
        },
        "recommended_races": [
            "Half-Elf", "Lightfoot Halfling", "Human", "Variant Human"
        ],
        "image": "media/classes/dnd_rogue.png"
    },

    "sorcerer": {
        "title": "Sorcerer",
        "description": "Sorcerers have innate magical power from within themselves. They manipulate raw magic through will and instinct rather than study and preparation.",
        "detailed_description": (
            "Sorcerers are natural spellcasters who draw magic from within themselves rather than from external sources. Their power comes from their bloodline, exposure to magical forces, or otherworldly influences. They have fewer spells than wizards but can modify their magic in unique ways through metamagic."
        ),
        "features": "more info",
        "hit_die": "d6",
        "primary_ability": ["Charisma"],
        "secondary_ability": ["Constitution"],
        "saving_throws": ["Constitution", "Charisma"],
        "armor_proficiencies": [],
        "weapon_proficiencies": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"],
        "tool_proficiencies": [],
        "skills_choices": [
            "Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"
        ],
        "skills_number": 2,
        "equipment_choices": [
            ["Light crossbow and 20 bolts", "Any simple weapon"],
            ["Component pouch", "Arcane focus"],
            ["Dungeoneer's pack", "Explorer's pack"],
            ["Two daggers"]
        ],
        "subclasses": [
            "Draconic Bloodline",
            "Wild Magic",
            "Divine Soul",
            "Shadow Magic",
            "Storm Sorcery",
            "Aberrant Mind"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Spellcasting", "Sorcerous Origin"]},
            {"level": 2, "features": ["Font of Magic"]},
            {"level": 3, "features": ["Metamagic"]},
            {"level": 4, "features": ["Ability Score Improvement"]},
            {"level": 20, "features": ["Sorcerous Restoration"]}
        ],
        "characteristics": {
            "Strength": 10,
            "Dexterity": 13,
            "Constitution": 14,
            "Intelligence": 8,
            "Wisdom": 12,
            "Charisma": 15
        },
        "recommended_races": [
            "Dragonborn", "Tiefling", "Half-Elf", "Human"
        ],
        "image": "media/classes/dnd_sorcerer.png"
    },

        "warlock": {
        "title": "Warlock",
        "description": "Warlocks are seekers of knowledge hidden in fabric of the multiverse. They form pacts with mysterious beings to unlock magical power.",
        "detailed_description": (
            "Warlocks gain their powers through pacts with otherworldly entities. These patrons grant magical abilities in exchange for service or favors. Warlocks have fewer spell slots than other casters but regain them on short rests and can customize their abilities through eldritch invocations."
        ),
        "features": "more info",
        "hit_die": "d8",
        "primary_ability": ["Charisma"],
        "secondary_ability": ["Constitution"],
        "saving_throws": ["Wisdom", "Charisma"],
        "armor_proficiencies": ["Light armor"],
        "weapon_proficiencies": ["Simple weapons"],
        "tool_proficiencies": [],
        "skills_choices": [
            "Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"
        ],
        "skills_number": 2,
        "equipment_choices": [
            ["Light crossbow and 20 bolts", "Any simple weapon"],
            ["Component pouch", "Arcane focus"],
            ["Scholar's pack", "Dungeoneer's pack"],
            ["Leather armor", "Any simple weapon", "Two daggers"]
        ],
        "subclasses": [
            "The Fiend",
            "The Great Old One",
            "The Archfey",
            "The Celestial",
            "The Hexblade",
            "The Fathomless"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Otherworldly Patron", "Pact Magic"]},
            {"level": 2, "features": ["Eldritch Invocations"]},
            {"level": 3, "features": ["Pact Boon"]},
            {"level": 4, "features": ["Ability Score Improvement"]},
            {"level": 11, "features": ["Mystic Arcanum (6th level)"]},
            {"level": 20, "features": ["Eldritch Master"]}
        ],
        "characteristics": {
            "Strength": 8,
            "Dexterity": 14,
            "Constitution": 13,
            "Intelligence": 12,
            "Wisdom": 10,
            "Charisma": 15
        },
        "recommended_races": [
            "Tiefling", "Human", "Half-Elf", "Variant Human"
        ],
        "image": "media/classes/dnd_warlock.png"
    },

    "wizard": {
        "title": "Wizard",
        "description": "Wizards are supreme magic-users, defined by their quest to understand the universe through study and practice. They are the ultimate students of arcane magic.",
        "detailed_description": (
            "Wizards are scholarly magic-users capable of manipulating structures of reality through careful study and preparation. They have access to the largest selection of spells and can learn new ones by studying spellbooks, scrolls, and other sources. Their knowledge of magic is unparalleled among the classes."
        ),
        "features": "more info",
        "hit_die": "d6",
        "primary_ability": ["Intelligence"],
        "secondary_ability": ["Wisdom"],
        "saving_throws": ["Intelligence", "Wisdom"],
        "armor_proficiencies": [],
        "weapon_proficiencies": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"],
        "tool_proficiencies": [],
        "skills_choices": [
            "Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"
        ],
        "skills_number": 2,
        "equipment_choices": [
            ["Quarterstaff", "Dagger"],
            ["Component pouch", "Arcane focus"],
            ["Scholar's pack", "Explorer's pack"],
            ["Spellbook"]
        ],
        "subclasses": [
            "School of Abjuration",
            "School of Conjuration",
            "School of Divination",
            "School of Enchantment",
            "School of Evocation",
            "School of Illusion",
            "School of Necromancy",
            "School of Transmutation"
        ],
        "class_features_table": [
            {"level": 1, "features": ["Spellcasting", "Arcane Recovery"]},
            {"level": 2, "features": ["Arcane Tradition"]},
            {"level": 4, "features": ["Ability Score Improvement"]},
            {"level": 18, "features": ["Spell Mastery"]},
            {"level": 20, "features": ["Signature Spells"]}
        ],
        "characteristics": {
            "Strength": 8,
            "Dexterity": 12,
            "Constitution": 13,
            "Intelligence": 15,
            "Wisdom": 14,
            "Charisma": 10
        },
        "recommended_races": [
            "High Elf", "Human", "Rock Gnome", "Variant Human"
        ],
        "image": "media/classes/dnd_wizard.png"
    },

}



# worldviews and additional info about that

worldview_info = {
    "lawful_good": {
        "title": "Lawful Good",
        "description": (
            "Those of Lawful Good alignment are guided by honor, compassion, and a steadfast sense of duty. They believe in justice, order, and the greater good, striving to do what is right not just for themselves, but for their community and the world at large.\n\nSuch individuals often serve as beacons of hope and integrity, inspiring others through their noble deeds and unwavering principles.\n\nImagine a knight who refuses to abandon the innocent, a paladin who upholds their sacred oath even when tempted, or a ruler who places the needs of the people above personal gain. Their lives are stories of sacrifice, courage, and the pursuit of a just world."
        )
    },
    "neutral_good": {
        "title": "Neutral Good",
        "description": (
            "Neutral Good characters are guided by benevolence and empathy, doing what is right simply because it is right. They are not bound by laws or traditions, but rather by an inner moral compass that points toward kindness and fairness.\n\nWhether helping a stranger in need or standing up to injustice, they act selflessly, often bridging divides between order and chaos. \n\nPicture a healer who aids all, regardless of background, or a wise sage who seeks harmony in a divided land. Their goodness is genuine and universal, making them beloved by those around them."
        )
    },
    "chaotic_good": {
        "title": "Chaotic Good",
        "description": (
            "Chaotic Good individuals are free spirits who follow their conscience above all else. They believe in doing good, but refuse to let rules or authority stand in the way of compassion and justice.\n\nTheir actions are often bold and unconventional—perhaps a rebel who steals from the corrupt to feed the poor, or an adventurer who breaks unjust laws to free the oppressed.\n\nThese characters value freedom, individuality, and the power of personal choice, often becoming legends and folk heroes whose daring exploits inspire others to challenge the status quo."
        )
    },
    "lawful_neutral": {
        "title": "Lawful Neutral",
        "description": (
            "Lawful Neutral characters are the embodiment of order, discipline, and tradition. They believe in the importance of structure, rules, and codes—whether those are the laws of the land, the tenets of a faith, or a personal code of conduct.\n\nTheir actions are guided not by notions of good or evil, but by a commitment to stability and predictability.\n\nImagine a judge who applies the law impartially, a monk who follows a strict regimen, or a city official who values procedure above all else. Their steadfastness can be both reassuring and unyielding, making them pillars of their societies."
        )
    },
    "true_neutral": {
        "title": "True Neutral",
        "description": (
            "True Neutral characters seek balance in all things, often avoiding extremes and refusing to take sides in conflicts. They act according to the situation, sometimes helping, sometimes hindering, but always striving to maintain equilibrium.\n\nSuch individuals might be druids who protect the natural order, or wise mediators who see merit in every viewpoint.\n\nTheir perspective is broad, and their actions are guided by a desire to preserve harmony, making them unpredictable yet essential in a world of clashing ideals."
        )
    },
    "chaotic_neutral": {
        "title": "Chaotic Neutral",
        "description": (
            "Chaotic Neutral characters are driven by personal freedom and the pursuit of their own desires. They value spontaneity, independence, and the thrill of living life on their own terms. Their actions may seem erratic or whimsical to others, but to them, every day is an opportunity for new experiences.\n\nThink of a wandering bard who follows inspiration wherever it leads, or a rogue who acts on impulse, caring little for rules or consequences.\n\nTheir unpredictability can be both exhilarating and frustrating to those around them."
        )
    },
    "lawful_evil": {
        "title": "Lawful Evil",
        "description": (
            "Lawful Evil individuals use order, structure, and authority to achieve their own ends. They respect hierarchy and tradition, but twist these systems to serve selfish or ruthless ambitions.\n\nWhether a calculating tyrant who enforces harsh laws, a corrupt official exploiting their position, or a cunning villain who manipulates contracts and oaths, these characters are masters of using the rules against others.\n\nTheir evil is methodical and deliberate, making them formidable adversaries who inspire both fear and grudging respect."
        )
    },
    "neutral_evil": {
        "title": "Neutral Evil",
        "description": (
            "Neutral Evil characters are guided solely by self-interest. They will do whatever it takes to get what they want, unconcerned with laws, traditions, or the suffering of others.\n\nTheir actions are often cold and pragmatic, whether it’s an assassin who kills for gold, a traitor who betrays friends for power, or a mercenary who serves the highest bidder.\n\nTheir amorality makes them dangerous, as they are willing to cross any line if it benefits them."
        )
    },
    "chaotic_evil": {
        "title": "Chaotic Evil",
        "description": (
            "Chaotic Evil characters are agents of destruction and mayhem, acting on violent impulses and a desire for chaos. They care nothing for rules, order, or the well-being of others, and delight in causing pain, fear, and disorder.\n\nWhether a rampaging warlord, a sadistic cultist, or a demon reveling in suffering, their actions are unpredictable and often catastrophic.\n\nThey are the embodiment of pure evil, leaving ruin in their wake and inspiring dread wherever they go."
        )
    }
}
