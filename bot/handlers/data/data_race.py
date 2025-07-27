# races, their descriptions, bonuses and pictures


race_info = {
    "hill_dwarf": {
        "title": "Hill Dwarf",
        "description": (
            "Hill dwarves are sturdy and wise, known for their resilience and keen insight. Living in tight-knit clans beneath rolling hills, they have earthy skin tones and cherish their long beards.\n\nThey value tradition and family ties, possess a strong sense of honor, and are driven by loyalty and inherited wisdom.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Dwarvish\n"
            "- *Height range*: 4'0\"-5'0\" (120-150 cm)\n"
            "- *Weight range*: 120-170 lbs (54-77 kg)\n"
            "- *Weapons*: Battleaxe, Handaxe, Light Hammer, Warhammer\n"
            "- *Duration of life*: up to 350 ages\n"
            "- *Recommended classes*: Cleric, Fighter, Paladin, Ranger\n"),
        "detailed_description": (
            "Dwarves are sturdy warriors, miners, stoneworkers, and smiths. Though just under 5 feet tall, they’re dense and broad, weighing as much as much taller people. Their skin is earthy brown, sometimes reddish; hair is usually dark or brown and worn long, with pale dwarves sometimes having red hair. Male dwarves highly value their beards.\n\n"
            "Dwarves can live over 400 years, giving them a unique outlook and strong traditions. They are loyal, determined, and slow to forgive, with wrongs against one often becoming clan disputes.\n\n"
            "Dwarven kingdoms stretch deep under mountains, where they mine gems and gold. The clan is central to their society, and losing clan ties is the greatest shame. Many dwarves abroad work as skilled smiths, jewelers, or respected mercenaries.\n\n"
            "Dwarves adventure for treasure, divine guidance, or to restore clan honor. Their devotion to hard work, tradition, and ancestors motivates them throughout their long lives."
        ),
        "features": "some more info",
        "male_names": [
            "Adrik", "Baern", "Barendd", "Brottor", "Dain", "Eberk", "Fargrim", "Harbek", "Orsik"
        ],
        "female_names": [
            "Artin", "Bardryn", "Dagnal", "Eldeth", "Gunnloda", "Hiln", "Kathra", "Kristryd", "Riswynn"
        ],
        "surnames": [
            "Balderk", "Fireforge", "Ironfist", "Loderr", "Rumnaheim", "Strakeln", "Torunn", "Ungart", "Holderheck"
        ],
        "speed": "25 feet",
        "body_size": {
            "small": ["3'9\" (115 cm)", "121 lbs (55 kg)"],
            "medium": ["4'1\" (125 cm)", "148 lbs (67 kg)"],
            "big": ["4'5\" (135 cm)", "176 lbs (80 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": ["under 70 ages", (25, 70)],
            "mature": ["70-200 ages", (70, 200)],
            "old": ["over 350 ages", (350, 500)]
        },
        "language": ["Common", "Dwarvish"],
        "extra_language": 0,   
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
        "description": (
            "Mountain dwarves are hardy and proud, famed for their strength and steadfastness. Dwelling in great halls carved into rugged mountains, they have fair or ruddy skin and thick, well-kept beards.\n\nThey uphold tradition and craftsmanship, value clan honor, and possess unbreakable loyalty and enduring courage.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Dwarvish\n"
            "- *Height range*: 4'0\"-5'0\" (120-150 cm)\n"
            "- *Weight range*: 120-180 lbs (54-82 kg)\n"
            "- *Weapons*: Battleaxe, Handaxe, Light Hammer, Warhammer\n"
            "- *Duration of life*: up to 350 ages\n"
            "- *Recommended classes*: Fighter, Paladin, Barbarian\n"
        ),
        "detailed_description": (
            "Mountain dwarves are hardy and unyielding folk, famed for their unwavering strength and endurance. They dwell in vast stone citadels deep within rugged mountains, where the clang of hammers and the glow of forges fill the halls and the scent of metal and earth lingers in the air. Mountain dwarves prize tradition, skill, and their proud lineage above all.\n\nWith lifespans reaching about 350 years, they approach life with patience and determined resolve. Mountain dwarves are stoic in adversity, fiercely loyal to clan and kin, and slow to trust outsiders, though quick to defend their homeland and honor. Their pride is matched only by their discipline, and they are known to stand firm against any foe or hardship.\n\nMost excel as master smiths, warriors, or protectors, pursuing excellence in craft and combat. Many set out as adventurers to prove their mettle, reclaim lost relics, or achieve legendary feats, carrying the unbreakable spirit and ancient pride of their mountain homes into the wider world."
        ),
        "features": "some more info",
        "male_names": [
            "Adrik", "Baern", "Barendd", "Brottor", "Dain", "Eberk", "Fargrim", "Harbek", "Orsik"
        ],
        "female_names": [
            "Artin", "Bardryn", "Dagnal", "Eldeth", "Gunnloda", "Hiln", "Kathra", "Kristryd", "Riswynn"
        ],
        "surnames": [
            "Balderk", "Fireforge", "Ironfist", "Loderr", "Rumnaheim", "Strakeln", "Torunn", "Ungart",
            "Holderheck"
        ],
        "speed": "25 feet",
        "body_size": {
            "small": ["3'11\" (120 cm)", "132 lbs (60 kg)"],
            "medium": ["4'5\" (135 cm)", "176 lbs (80 kg)"],
            "big": ["4'9\" (145 cm)", "209 lbs (95 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": ["under 70 ages", (25, 70)],
            "mature": ["70-200 ages", (70, 200)],
            "old": ["over 350 ages", (350, 500)]
        },
        "language": ["Common", "Dwarvish"],
        "extra_language": 0,   
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
        "description": (
            "High elves are graceful and intelligent, known for their keen minds and natural talent for magic. Living in elegant, ancient communities, they have slender builds, fair or bronze skin, and striking eyes.\n\nThey value learning, tradition, and beauty, showing both curiosity and pride. Their devotion to study and artistry sets them apart from other races.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Elvish\n"
            "- *Height range*: 5'0\"–6'0\" (150–180 cm)\n"
            "- *Weight range*: 90–145 lbs (41–66 kg)\n"
            "- *Weapons*: Longsword, Shortsword, Shortbow, Longbow\n"
            "- *Duration of life*: up to 750 ages\n"
            "- *Recommended classes*: Wizard, Ranger, Fighter\n"
        ),
        "detailed_description": (
            "Elves are a magical people with otherworldly grace, living in airy places—ancient forests or silver homes crowned with glowing spires. Gentle breezes carry soft melodies and delicate scents. They cherish nature, magic, music, poetry, and all that is beautiful.\n\nLiving over 700 years, elves gain broad perspective. They often find events amusing, driven more by curiosity than greed. Slow to make friends or enemies and even slower to forgive, they respond to minor slights with disdain and serious offenses with vengeance. Flexible like young branches, they prefer diplomacy but fiercely defend their homes with sword, bow, and strategy.\n\nMost live in small forest villages, hunting, gathering, and crafting without harming nature. Some trade metals they don’t mine. Traveling elves become bards, artists, or sages. Passionate about travel, they study, explore, and master magic and combat, preferring a slower pace than humans and sometimes joining rebels or moral causes."
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
        "age": {
            "young": ["under 120 ages", (40, 120)],
            "mature": ["120–250 ages", (120, 250)],
            "old": ["over 750 ages", (750, 1100)]
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
        "description": (
            "Wood elves are swift and perceptive, living in harmony with forests and nature. They are slender, with copper-toned skin and green or hazel eyes, blending easily into woodland surroundings.\n\nThey value freedom, stealth, and close kinship, excelling at archery and survival. Their quiet wisdom and loyalty to their communities define their character.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Elvish\n"
            "- *Height range*: 5'0\"–6'0\" (150–180 cm)\n"
            "- *Weight range*: 90–145 lbs (41–66 kg)\n"
            "- *Weapons*: Longsword, Shortsword, Shortbow, Longbow\n"
            "- *Duration of life*: up to 750 ages\n"
            "- *Recommended classes*: Ranger, Rogue, Druid\n"
        ),
        "detailed_description": (
            "Wood elves are a mystical people with a deep connection to forests, living in hidden villages beneath leafy canopies or within natural halls shaped by ancient magic. Gentle breezes carry soft songs and wild scents through their homes. Wood elves value nature, harmony, freedom, and all forms of natural beauty.\n\nWith lifespans over 700 years, they gain a wide perspective and react to the world with gentle amusement, driven by curiosity more than ambition. They are patient and slow to trust, yet fiercely protective when threatened. Offenses are met with restraint, but grave wrongs spark decisive action. Agile and adaptable like the trees themselves, wood elves prefer diplomacy and camouflage but defend their realms with keen archery and woodland cunning.\n\nMost wood elves hunt, gather, and craft without harming their forests. Skilled in stealth and the arts of survival, some become scouts or guides beyond their lands, valued by those seeking their wisdom and mastery of the wild."
        ),
        "features": "some more info",
        "male_names": [
            "Adran", "Aramil", "Aust", "Carric", "Erevan", "Galinndan", "Himo", "Ivellios", "Laucian"
        ],
        "female_names": [
            "Briana", "Caelynn", "Drusilia", "Felosial", "Keyleth", "Leshanna", "Shanairra", "Thia", "Valanthe"
        ],
        "surnames": [
            "Amakiir", "Galanodel", "Holimion","Liadon", "Meliamne", "Nai'lo", "Siannodel", "Xiloscient", "Ilfelkiir"
        ],
        "speed": "35 feet",
        "body_size": {
            "small": ["4'11\" (150 cm)", "95 lbs (43 kg)"],
            "medium": ["5'3\" (160 cm)", "115 lbs (52 kg)"],
            "big": ["5'9\" (175 cm)", "137 lbs (62 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": ["under 120 ages", (40, 120)],
            "mature": ["120–250 ages", (120, 250)],
            "old": ["over 750 ages", (750, 1100)]
        },
        "language": ["Common", "Elvish"],
        "extra_language": 0,   
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
        "description": (
            "Dark elves are agile and mysterious, renowned for their cunning and magical prowess. Dwelling in vast subterranean cities, they have obsidian skin, white or silver hair, and striking red or purple eyes.\n\nDrow society values secrecy, ambition, and sharp intellect. Though often mistrusted by others, drow are fiercely independent and possess an enigmatic charm.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Elvish, Undercommon\n"
            "- *Height range*: 4'5\"–5'5\" (135–165 cm)\n"
            "- *Weight range*: 75–120 lbs (34–55 kg)\n"
            "- *Weapons*: Rapier, Shortsword, Hand Crossbow\n"
            "- *Duration of life*: up to 750 ages\n"
            "- *Recommended classes*: Rogue, Wizard, Cleric\n"
        ),
        "detailed_description": (
            "Drow are mysterious elves who dwell in vast, shadowy cities deep beneath the earth, living among twisting caverns and halls aglow with eerie magical light. Whispers and subtle magic fill their homes, the air tinged with the scent of rare fungi and minerals. Drow treasure secrecy, ambition, cunning, and the beauty found in darkness and shadow.\n\nWith lifespans over 700 years, drow develop a keen awareness of intrigue and ever-shifting alliances. They're cautious and slow to trust, but respond decisively to betrayal. Minor slights are ignored; true insults spark long-lasting revenge. Flexible and elusive, drow rely on diplomacy or subterfuge, but defend their domains with formidable sorcery and precise tactics.\n\nMost drow master magic and stealth, thriving as spies, assassins, or nobles in a rigid society. Some—driven by curiosity or a desire for redemption—venture beyond the Underdark, becoming adventurers, outcasts, or enigmatic allies valued for their skills and rare insight."
        ),
        "features": "some more info",
        "male_names": [
            "Drizzt", "Jarlaxle", "Pharaun", "Ryld", "Zaknafein", "Gromph", "Malaggar", "Nisstyre", "Solaufein"
        ],
        "female_names": [
            "Vierna", "Briza", "Maya", "Quenthel", "Sos’Umptu", "Zesstra", "Eclavdra", "Shi’nayne", "Xullrae"
        ],
        "surnames": [
            "Do’Urden", "Faen Tlabbar", "Xorlarrin", "Baenre", "Mizzrym", "Ry’Salka", "Hun’ett", "T’sarran", "Barrison Del’Armgo"
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["4'7\" (140 cm)", "84 lbs (38 kg)"],
            "medium": ["4'11\" (150 cm)", "99 lbs (45 kg)"],
            "big": ["5'3\" (160 cm)", "117 lbs (53 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": ["under 120 ages", (40, 120)],
            "mature": ["120–250 ages", (120, 250)],
            "old": ["over 750 ages", (750, 1100)]
        },
        "language": ["Common", "Elvish", "Undercommon"],
        "extra_language": 0,   
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
        "description": (
            "Lightfoot halflings enjoy the comforts of home, the pleasures of food and song, and the thrill of adventure. Whether in bustling city quarters or peaceful farmlands, they blend into societies easily, charming friends and eluding danger through agility and stealth.\n\nThey rarely seek out conflict but will defend their homes with surprising courage and cunning.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Halfling\n"
            "- *Height range*: 2'5\"–3'5\" (75–105 cm)\n"
            "- *Weight range*: 40–66 lbs (18–30 kg)\n"
            "- *Weapons*: None\n"
            "- *Duration of life*: up to 150 ages\n"
            "- *Recommended classes*: Rogue, Bard\n"
        ),
        "detailed_description": (
            "Lightfoot halflings are small, nimble folk known for their cheerful nature and quick wits. They live in cozy, hidden communities nestled in peaceful countryside or gentle hills, where soft breezes carry the scent of fresh earth and blooming flowers. Lightfoots value freedom, friendship, and curiosity.\n\nWith lifespans around 250 years, they see the world with optimism and a playful spirit. They are cautious but warm, quick to trust good company, and gifted with natural stealth and agility. Lightfoot halflings prefer diplomacy and wit over conflict but will stand firm to protect loved ones.\n\nMost lightfoots are skilled in farming, crafting, or trade, blending easily in larger settlements. Many become explorers or adventurers, using their speed and charm to navigate the world beyond their homes."
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
        "age": {
            "young": ["under 35 ages", (20, 35)],
            "mature": ["35–80 ages", (35, 80)],
            "old": ["over 150 ages", (150, 220)]
        },
        "language": ["Common", "Halfling"],
        "extra_language": 0,   
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
        "description": (
            "Stout halflings are known for their uncommon resilience, endurance, and remarkable resistance to poison. Their skin tones are usually darker than those of the Lightfoot halflings, and they appear stockier and sturdier.\n\n"
            "They value the comfort of a safe home, prefer to avoid trouble, but show genuine courage when defending their loved ones.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Halfling\n"
            "- *Height range*: 2'5\"–3'5\" (75–105 cm)\n"
            "- *Weight range*: 40–66 lbs (18–30 kg)\n"
            "- *Weapons*: None\n"
            "- *Duration of life*: up to 150 years\n"
            "- *Recommended classes*: Fighter, Rogue, Ranger\n"
        ),
        "detailed_description": (
            "Stout halflings are hardy and resilient folk, known for their strong builds and steady nerves. They dwell in cozy, close-knit communities hidden in hills, forests, or farms, where fresh earth scents mingle with the warmth of hearth fires. Stouts value loyalty, courage, and perseverance.\n\nWith lifespans around 250 years, they approach life with calm determination and quiet optimism. Stout halflings are tough and resistant to hardship, often showing grit in the face of danger. They are friendly but cautious, preferring to avoid unnecessary conflict while standing firm to protect their own.\n\nMost stouts excel in farming, crafting, or guarding, blending well into larger towns. Many become travelers or adventurers, relying on their endurance and steady focus to overcome challenges."
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
            "young": ["under 35 ages", (20, 35)],
            "mature": ["35–80 ages", (35, 80)],
            "old": ["over 150 ages", (150, 220)]
        },
        "language": ["Common", "Halfling"],
        "extra_language": 0,   
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
        "description": (
            "Humans are the most adaptable and ambitious race in the world. They are widespread and known for their ability to thrive in a variety of environments and pursue diverse goals. Their appearances, habits, and outlooks are extremely varied.\n\n"
            "Often explorers, leaders, and diplomats, humans shape many cultures and traditions.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, one extra language of choice\n"
            "- *Height range*: 5'0\"–6'2\" (150–188 cm)\n"
            "- *Weight range*: 115–240 lbs (52–109 kg)\n"
            "- *Weapons*: None\n"
            "- *Duration of life*: up to 80 years\n"
            "- *Recommended classes*: Any class\n"
        ),
        "detailed_description": (
            "Humans are adaptable and ambitious folk, known for their diverse builds and driven spirits. They thrive in varied environments, from bustling cities to sprawling farmlands, where the scents of smoke, earth, and sea blend with a constant hum of activity. Humans value innovation, resilience, and the pursuit of personal goals.\n\nWith lifespans around 80 to 100 years, they approach life with determination and a willingness to embrace change. Humans are resourceful and versatile, able to face challenges with courage and creativity. They can be both friendly and competitive, often striving to leave a mark on the world.\n\nMost humans excel in a wide range of professions, from artisans to warriors and scholars. Many become explorers or leaders, their ambition and adaptability carrying them far beyond their homelands."
        ),
        "features": "some more info",
        "male_names": [
            "Ander", "Brennen", "Darvin", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn"
        ],
        "female_names": [
            "Arveene", "Esvele", "Jhessail", "Kerri", "Lureene", "Miri", "Rowan", "Shandri", "Tessele"
        ],
        "surnames": [
            "Amblecrown", "Buckman", "Dundragon", "Evenwood", "Greycastle", "Tallstag", "Windrivver", "Marsh", "Hoffman"
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["4'9\" (145 cm)", "99 lbs (45 kg)"],
            "medium": ["5'7\" (170 cm)", "154 lbs (70 kg)"],
            "big": ["6'5\" (195 cm)", "220 lbs (100 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": ["under 20 ages", (16, 20)],
            "mature": ["20–40 ages", (20, 40)],
            "old": ["over 150 ages", (60, 75)]
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
        "description": (
            "Dragonborn are proud and strong warrior nomads, carrying the magical blood, unique appearance, and brave spirit inherited from dragons. Their scaled skin varies in color, reflecting their draconic ancestry.\n\n"
            "They honor tradition, glory, and family bonds, often displaying fortitude and determination.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Draconic\n"
            "- *Height range*: 6'0\"–6'8\" (183–203 cm)\n"
            "- *Weight range*: 220–320 lbs (100–145 kg)\n"
            "- *Weapons*: None\n"
            "- *Duration of life*: up to 80 years\n"
            "- *Recommended classes*: Paladin, Fighter, Sorcerer\n"
        ),
        "detailed_description": (
            "Dragonborn are proud and determined folk, known for their draconic heritage and imposing presence. They make their homes in well-ordered communities, often surrounded by the echoes of ancient legends and the gleam of polished scales. The scent of smoke, metal, and incense lingers in their halls, a reminder of their ancestry and deep traditions. Dragonborn value honor, strength, and personal excellence.\n\nWith lifespans around 80 years, they approach life with bold ambition and unwavering resolve. Dragonborn are resilient in the face of adversity and place great importance on their word and personal reputation. They tend to be confident and direct, striving to rise above challenges and uphold the ideals of their ancestors.\n\nMost dragonborn excel as warriors, leaders, or artisans, their talents shaped by a drive to prove themselves and bring glory to their clan. Many become adventurers, drawn by a desire to leave a lasting legacy and live up to the mighty deeds of dragons past."
        ),
        "features": "some more info",
        "male_names": [
            "Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Raiann", "Shamash"
        ],
        "female_names": [
            "Akra", "Biri", "Daar", "Farideh", "Harann", "Havilar", "Kava", "Korinn", "Mishann", "Sora"
        ],
        "surnames": [
            "Clethtinthiallor", "Daardendrian", "Delmirev", "Drachedandion", "Fenkenkabradon", "Kepeshkmolik", "Kerrhylon", "Norixius", "Turnuroth"
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["5'7\" (170 cm)", "154 lbs (70 kg)"],
            "medium": ["6'1\" (185 cm)", "220 lbs (100 kg)"],
            "big": ["6'7\" (200 cm)", "287 lbs (130 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": ["under 12 ages", (8, 12)],
            "mature": ["12–30 ages", (12, 30)],
            "old": ["over 150 ages", (150, 210)]
        },
        "language": ["Common", "Draconic"],
        "extra_language": 0,   
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
        "description": (
            "Gnomes are a small but exceedingly curious race, valuing invention, magic, and simple joys of life. Forest gnomes are independent and secretive, while rock gnomes are masters of mechanics and craftsmanship.\n\n"
            "Gnomes are characterized by cheerfulness, energy, and boundless optimism.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Gnomish\n"
            "- *Height range*: 3'0\"–4'0\" (90–120 cm)\n"
            "- *Weight range*: 40–45 lbs (18–20 kg)\n"
            "- *Weapons*: None\n"
            "- *Duration of life*: up to 500 years\n"
            "- *Recommended classes*: Wizard, Rogue\n"
        ),
        "detailed_description": (
            "Forest gnomes are secretive and lively folk, known for their deep bond with the natural world and gentle magic. They make their homes in quiet woodland glades, often hidden from view and woven seamlessly into the landscape, where the scents of moss, wildflowers, and rich earth fill the air. Forest gnomes cherish harmony, kindness, and the simple joys found in nature.\n\nWith lifespans of about 350 to 500 years, they view life as an ongoing adventure, greeting each day with bright curiosity and a mischievous smile. Forest gnomes are clever and cautious, excelling at stealth and illusion, yet always ready to lend a helping hand to friends or creatures in need. \n\nMost forest gnomes are talented in stealth, herbalism, and animal friendship, blending seamlessly into the woods. Curiosity often leads them beyond their groves, where they become skilled scouts, storytellers, or traveling companions, always guided by their playful spirit and love of peace."
        ),
        "features": "some more info",
        "male_names": [
            "Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin"
        ],
        "female_names": [
            "Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ellyjobell", "Ellywick", "Loopmottin"
        ],
        "surnames": [
            "Beren", "Daergel", "Folkor", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Timbers"
        ],
        "speed": "25 feet",
        "body_size": {
            "small": ["2'9\" (85 cm)", "40 lbs (18 kg)"],
            "medium": ["3'3\" (100 cm)", "49 lbs (22 kg)"],
            "big": ["3'9\" (115 cm)", "60 lbs (27 kg)"]
        },
        "size": "Small",
        "age": {
            "young": ["under 70 ages", (25, 70)],
            "mature": ["70-200 ages", (70, 200)],
            "old": ["over 350 ages", (350, 500)]
        },
        "language": ["Common", "Gnomish"],
        "extra_language": 0,   
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
       "description": (
            "Gnomes are a small but exceedingly curious race, valuing invention, magic, and simple joys of life. Forest gnomes are independent and secretive, while rock gnomes are masters of mechanics and craftsmanship.\n\n"
            "Gnomes are characterized by cheerfulness, energy, and boundless optimism.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Gnomish\n"
            "- *Height range*: 3'0\"–4'0\" (90–120 cm)\n"
            "- *Weight range*: 40–45 lbs (18–20 kg)\n"
            "- *Weapons*: None\n"
            "- *Duration of life*: up to 500 years\n"
            "- *Recommended classes*: Wizard, Rogue\n"
        ),
        "detailed_description": (
            "Rock gnomes are inventive and cheerful, celebrated for their passion for tinkering and natural curiosity. Living in snug burrows or bustling underground workshops, they surround themselves with sparkling gems, clever contraptions, and the hum of busy activity. The scent of oil, metal, and fresh stone lingers in their realms, reflecting their love for craftsmanship and discovery.\n\nWith life spans reaching 400 to 600 years, rock gnomes approach life as a puzzle to be solved and a story to be told. They are optimistic and persistent, rarely discouraged by setbacks, always eager to test a theory or invent something new. Rock gnomes value ingenuity, humor, and the bonds of friendship above all.\n\nMost excel as artisans, alchemists, or inventors—always ready to tinker or share their clever creations. Many adventure outward, hoping to uncover lost secrets, make new friends, or simply add excitement to their lives, carrying their inventive spirit and bright optimism wherever they go."
        ),
        "features": "some more info",
        "male_names": [
            "Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin"
        ],
        "female_names": [
            "Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ellyjobell", "Ellywick", "Loopmottin"
        ],
        "surnames": [
            "Beren", "Daergel", "Folkor", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Timbers"
        ],
        "speed": "25 feet",
        "body_size": {
            "small": ["2'11\" (90 cm)", "44 lbs (20 kg)"],
            "medium": ["3'5\" (105 cm)", "55 lbs (25 kg)"],
            "big": ["3'11\" (120 cm)", "66 lbs (30 kg)"]
        },
        "size": "Small",
        "age": {
            "young": ["under 70 ages", (25, 70)],
            "mature": ["70-200 ages", (70, 200)],
            "old": ["over 350 ages", (350, 500)]
        },
        "language": ["Common", "Gnomish"],
        "extra_language": 0,   
        "recommended_worldview": "Neutral Good",
        "height_range": "2'11\"–3'11\" (90–120 cm)",
        "weight_range": "44–66 lbs (20–30 kg)",
        "recommended_classes": [
            "Rogue", "Wizard"
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
        "description": (
            "Half-elves combine the charisma of humans with the refined elegance of elves, occupying a unique position between two worlds. Thanks to their adaptable nature and diplomatic talents, they find friends everywhere.\n\n"
            "They inherit timeless beauty but lack strong ties to any one culture, allowing them to adapt easily to any environment.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Elvish\n"
            "- *Height range*: 5'0\"–6'0\" (150–180 cm)\n"
            "- *Weight range*: 100–180 lbs (45–80 kg)\n"
            "- *Weapons*: None\n"
            "- *Duration of life*: up to 180 years\n"
            "- *Recommended classes*: Bard, Sorcerer, Warlock\n"
        ),
        "detailed_description": (
            "Half-elves are adaptable and charismatic, blending the grace of elven heritage with human vigor. They often dwell between worlds, equally at home in bustling cities or tranquil forests, places alive with diversity and possibility. The mingled scents of flower, parchment, and distant hearths mark their communities. Half-elves value freedom, curiosity, and the desire to belong.\n\nWith lifespans averaging around 180 years, half-elves see the world with open eyes, embracing a multitude of experiences. They are resilient in the face of adversity, thriving on versatility and enriched by both cultures. Friendly and diplomatic, they form bonds easily but often struggle to find a place to truly call home.\n\nMost half-elves excel as diplomats, artists, or travelers, drawing upon their diverse heritage. Many pursue adventure out of curiosity or the need to prove themselves, forging unique destinies as bridges between peoples, their lives marked by courage, wonder, and a longing for connection."
        ),
        "features": "some more info",
        "male_names": [
            "Adran", "Aramil", "Carric", "Erevan", "Ivellios", "Laucian", "Quarion", "Soveliss", "Varis"
        ],
        "female_names": [
            "Adrie", "Drusilia", "Felosial", "Keyleth", "Naivara", "Shanairra", "Thia", "Valanthe", "Xanaphia"
        ],
        "surnames": [
            "Amakiir", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Nai'lo", "Siannodel", "Xiloscient", "Moonbrook"
        ],
        "speed": "30 feet",
        "body_size": {
            "small": ["5'1\" (155 cm)", "106 lbs (48 kg)"],
            "medium": ["5'7\" (170 cm)", "143 lbs (65 kg)"],
            "big": ["6'1\" (185 cm)", "187 lbs (85 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": ["under 30 ages", (18, 30)],
            "mature": ["30–70 ages", (30, 70)],
            "old": ["over 180 ages", (180, 300)]
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
        "description": (
            "Half-orcs are known for their powerful build and fierce temperament. Often facing prejudice, few can challenge their bravery and endurance. A half-orc’s life is a constant struggle for respect and a place in the world.\n\n"
            "They draw strength from rage and possess an innate ability to survive even the harshest conditions.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Orc\n"
            "- *Height range*: 5'10\"–6'6\" (178–198 cm)\n"
            "- *Weight range*: 180–250 lbs (82–113 kg)\n"
            "- *Weapons*: None\n"
            "- *Duration of life*: up to 75 years\n"
            "- *Recommended classes*: Barbarian, Fighter\n"
        ),
        "detailed_description": (
            "Half-orcs are tough and tenacious, marked by a blend of human resourcefulness and orcish might. They dwell in the rough edges of societies—fortified villages, frontier lands, and sometimes orc tribes—where the scent of sweat, leather, and iron is common. Half-orcs value strength, survival, and respect, tempered with a drive to overcome prejudice.\n\nWith lifespans of about 75 years, half-orcs navigate life with a sense of urgency and determination. They are quick to act and endure hardships with grit, often channeling pain into focused ambition. Both wary of and drawn to community, half-orcs can be fiercely loyal friends or lone wanderers.\n\nMost find their talents in combat, mercenary work, or hunting, standing out for their courage and endurance. Many take up the adventurer’s path to escape biases, seek personal glory, or discover a place where they are accepted, shaped by the struggle to claim respect and honor."
        ),
        "features": "some more info",
        "male_names": [
            "Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Ront"
        ],
        "female_names": [
            "Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha"
        ],
        "surnames": [],
        "speed": "30 feet",
        "body_size": {
            "small": ["5'1\" (155 cm)", "132 lbs (60 kg)"],
            "medium": ["5'11\" (180 cm)", "198 lbs (90 kg)"],
            "big": ["6'7\" (200 cm)", "265 lbs (120 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": ["under 30 ages", (15, 20)],
            "mature": ["30–70 ages", (20, 40)],
            "old": ["over 180 ages", (75, 90)]
        },
        "language": ["Common", "Orc"],
        "extra_language": 0,   
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
        "description": (
            "Tieflings are mysterious descendants of ancient pacts with denizens of the Lower Planes. They bear distinctive traits such as horns, tails, and unusual skin colors. Tieflings often face distrust, which strengthens their character.\n\n"
            "Nonetheless, they seek independence and welcome new opportunities while never forgetting their heritage.\n\n"
            "*About race*\n\n"
            "- *Available languages*: Common, Infernal\n"
            "- *Height range*: 4'11\"–6'2\" (150–188 cm)\n"
            "- *Weight range*: 110–190 lbs (50–86 kg)\n"
            "- *Weapons*: None\n"
            "- *Duration of life*: up to 100 years\n"
            "- *Recommended classes*: Warlock, Sorcerer, Bard\n"
        ),
        "detailed_description": (
            "Tieflings are enigmatic and resolute, bearing the legacy of infernal ancestry in their striking appearance—horns, tails, and skin in hues of crimson, violet, or dark blue. They make their homes on the fringes of society, whether in shadowed city quarters or distant, windswept lands, where the scent of incense and distant fire lingers. Tieflings value independence, sharp wit, and personal strength.\n\nWith lifespans similar to humans, averaging 80 to 100 years, tieflings persevere through adversity with keen ambition and quiet pride. Tieflings are clever, resourceful, and driven, using their intellect and charisma to overcome prejudice and shape their futures.\n\nMost excel in roles that demand cunning and adaptability—spies, warlocks, or diplomats. Many become adventurers seeking freedom, power, or a sense of belonging, their journeys defined by a determination to rise above their heritage and forge their own identity."
        ),
        "features": "some more info",
        "male_names": [
            "Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Melech"
        ],
        "female_names": [
            "Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria"
        ],
        "surnames": [],
        "speed": "30 feet",
        "body_size": {
            "small": ["4'9\" (145 cm)", "88 lbs (40 kg)"],
            "medium": ["5'5\" (165 cm)", "121 lbs (55 kg)"],
            "big": ["6'1\" (185 cm)", "154 lbs (70 kg)"]
        },
        "size": "Medium",
        "age": {
            "young": ["under 25 ages", (25, 25)],
            "mature": ["25–40 ages", (25, 40)],
            "old": ["over 80 ages", (80, 95)]
        },
        "language": ["Common", "Infernal"],
        "extra_language": 0,   
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