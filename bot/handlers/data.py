# races, their descriptions, bonuses and pictures


race_info = {
    "hill_dwarf": {
        "title": "Hill Dwarf",
        "description": "Hill dwarves are tough, wise, and deeply connected to their clans. They are known for their resilience and sense of tradition.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Adrik", "Baern", "Barendd", "Brottor", "Dain", "Eberk", "Fargrim", "Harbek", "Orsik"],
        "female_names": ["Artin", "Bardryn", "Dagnal", "Eldeth", "Gunnloda", "Hiln", "Kathra", "Kristryd", "Riswynn"],
        "size_small": ["3'9\" (115 cm)", "121 lbs (55 kg)"],
        "size_medium": ["4'1\" (125 cm)", "148 lbs (67 kg)"],
        "size_big": ["4'5\" (135 cm)", "176 lbs (80 kg)"],
        "age": ["under 70 ages", "70–200 ages", "over 350 ages"],
        "ability_bonuses": {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 2,
            "Intelligence": 0,
            "Wisdom": 1,
            "Charisma": 0
        },
        "image": "media/races/dnd_hill_dwarf.png"
    },
    "mountain_dwarf": {
        "title": "Mountain Dwarf",
        "description": "Mountain dwarves are strong and hardy, living in high mountain fortresses and renowned for their martial prowess.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Adrik", "Baern", "Barendd", "Brottor", "Dain", "Eberk", "Fargrim", "Harbek", "Orsik"],
        "female_names": ["Artin", "Bardryn", "Dagnal", "Eldeth", "Gunnloda", "Hiln", "Kathra", "Kristryd", "Riswynn"],
        "size_small": ["3'11\" (120 cm)", "132 lbs (60 kg)"],
        "size_medium": ["4'5\" (135 cm)", "176 lbs (80 kg)"],
        "size_big": ["4'9\" (145 cm)", "209 lbs (95 kg)"],
        "age": ["under 70 ages", "70–200 ages", "over 350 ages"],
        "ability_bonuses": {
            "Strength": 2,
            "Dexterity": 0,
            "Constitution": 2,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        },
        "image": "media/races/dnd_mountain_dwarf.png"
    },
    "high_elf": {
        "title": "High Elf",
        "description": "High elves are a refined and proud race, known for their keen intellect, mastery of magic, and artistic flair. They live longer than other elves, have refined manners, and are often considered arrogant, but they also strive for harmony and perfection. High elves value knowledge, independence, and have an innate talent for the study of magic.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Adran", "Aramil", "Arannis", "Aust", "Enialis", "Heian", "Paelias", "Quarion", "Soveliss"],
        "female_names": ["Adrie", "Drusilia", "Felosial", "Ielenia", "Lia", "Mialee", "Naivara", "Quelenna", "Thia"],
        "size_small": ["5'1\" (155 cm)", "99 lbs (45 kg)"],
        "size_medium": ["5'5\" (165 cm)", "119 lbs (54 kg)"],
        "size_big": ["5'11\" (180 cm)", "143 lbs (65 kg)"],
        "age": ["under 100 ages", "100–250 ages", "over 750 ages"],
        "ability_bonuses": {
            "Strength": 0,
            "Dexterity": 2,
            "Constitution": 0,
            "Intelligence": 1,
            "Wisdom": 0,
            "Charisma": 0
        },
        "image": "media/races/dnd_high_elf.png"
    },
    "wood_elf": {
        "title": "Wood Elf",
        "description": "Wood elves are children of nature, living in harmony with forests and their inhabitants. They are agile, quick to react, and naturally cautious. Wood elves are excellent hunters and masters of disguise, preferring light armor and often becoming rangers or scouts. Their culture is closely tied to nature and the protection of their native lands.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Adran", "Aramil", "Arannis", "Aust", "Enialis", "Heian", "Paelias", "Quarion", "Soveliss"],
        "female_names": ["Adrie", "Drusilia", "Felosial", "Ielenia", "Lia", "Mialee", "Naivara", "Quelenna", "Thia"],
        "size_small": ["4'11\" (150 cm)", "95 lbs (43 kg)"],
        "size_medium": ["5'3\" (160 cm)", "115 lbs (52 kg)"],
        "size_big": ["5'9\" (175 cm)", "137 lbs (62 kg)"],
        "age": ["under 100 ages", "100–250 ages", "over 750 ages"],
        "ability_bonuses": {
            "Strength": 0,
            "Dexterity": 2,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 1,
            "Charisma": 0
        },
        "image": "media/races/dnd_wood_elf.png"
    },
    "dark_elf": {
        "title": "Dark Elf (Drow)",
        "description": "Drow are a mysterious and dangerous race of elves that live in the Underdark. Their skin is dark, their hair is white, and their eyes glow in the dark. Drow are known for their cruelty, cunning, and natural affinity for magic. They are skilled in ambush, wield poisonous weapons, and often use magic to create illusions and darkness. Drow society is brutal and hierarchical.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Drizzt", "Jarlaxle", "Pharaun", "Ryld", "Zaknafein", "Gromph", "Malaggar", "Nisstyre", "Solaufein"],
        "female_names": ["Vierna", "Briza", "Maya", "Quenthel", "Sos’Umptu", "Zesstra", "Eclavdra", "Shi’nayne", "Xullrae"],
        "size_small": ["4'7\" (140 cm)", "84 lbs (38 kg)"],
        "size_medium": ["4'11\" (150 cm)", "99 lbs (45 kg)"],
        "size_big": ["5'3\" (160 cm)", "117 lbs (53 kg)"],
        "age": ["under 100 ages", "100–250 ages", "over 750 ages"],
        "ability_bonuses": {
            "Strength": 0,
            "Dexterity": 2,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 1
        },
        "image": "media/races/dnd_drow.png"
    },
    "lightfoot_halfling": {
        "title": "Lightfoot Halfling",
        "description": "Lightfoot halflings are cheerful, nimble, and lucky, blending easily into crowds and always finding a way out of trouble.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Garret", "Lyle", "Milo", "Wellby"],
        "female_names": ["Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Seraphina"],
        "size_small": ["2'5\" (75 cm)", "40 lbs (18 kg)"],
        "size_medium": ["2'11\" (90 cm)", "53 lbs (24 kg)"],
        "size_big": ["3'5\" (105 cm)", "66 lbs (30 kg)"],
        "age": ["under 35 ages", "35–80 ages", "over 150 ages"],
        "ability_bonuses": {
            "Strength": 0,
            "Dexterity": 2,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 1
        },
        "image": "media/races/dnd_lightfoot_halfling.png"
    },
    "stout_halfling": {
        "title": "Stout Halfling",
        "description": "Stout halflings are hearty and brave, with a natural resistance to poison and a love for home and hearth.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Garret", "Lyle", "Milo", "Wellby"],
        "female_names": ["Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Seraphina"],
        "size_small": ["2'7\" (80 cm)", "44 lbs (20 kg)"],
        "size_medium": ["3'1\" (95 cm)", "57 lbs (26 kg)"],
        "size_big": ["3'7\" (110 cm)", "71 lbs (32 kg)"],
        "age": ["under 35 ages", "35–80 ages", "over 150 ages"],
        "ability_bonuses": {
            "Strength": 0,
            "Dexterity": 2,
            "Constitution": 1,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        },
        "image": "media/races/dnd_stout_halfling.png"
    },
    "human": {
        "title": "Human",
        "description": "Humans are the most adaptable and ambitious people among the common races, excelling in a wide variety of roles.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal"],
        "female_names": ["Arveene", "Esvele", "Jhessail", "Kerri", "Miri", "Rowan", "Shandri", "Tessele", "Zane"],
        "size_small": ["4'9\" (145 cm)", "99 lbs (45 kg)"],
        "size_medium": ["5'7\" (170 cm)", "154 lbs (70 kg)"],
        "size_big": ["6'5\" (195 cm)", "220 lbs (100 kg)"],
        "age": ["under 25 ages", "25–50 ages", "over 65 ages"],
        "ability_bonuses": {
            "Strength": 1,
            "Dexterity": 1,
            "Constitution": 1,
            "Intelligence": 1,
            "Wisdom": 1,
            "Charisma": 1
        },
        "image": "media/races/dnd_human.png"
    },
    "dragonborn": {
        "title": "Dragonborn",
        "description": "Dragonborn are proud, honorable, and powerful, possessing draconic ancestry and the ability to breathe elemental energy.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Rhogar"],
        "female_names": ["Akra", "Biri", "Daar", "Farideh", "Harann", "Havilar", "Jheri", "Kava", "Sora"],
        "size_small": ["5'7\" (170 cm)", "154 lbs / 70 kg)"],
        "size_medium": ["6'1\" (185 cm)", "220 lbs / 100 kg)"],
        "size_big": ["6'7\" (200 cm)", "287 lbs / 130 kg)"],
        "age": ["under 15 ages", "15–30 ages", "over 50 ages"],
        "ability_bonuses": {
            "Strength": 2,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 1
        },
        "image": "media/races/dnd_dragonborn.png"
    },
    "forest_gnome": {
        "title": "Forest Gnome",
        "description": "Forest gnomes are shy, quick, and clever, with a deep connection to nature and innate magical abilities.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Alston", "Alvyn", "Boddynock", "Dimble", "Fonkin", "Gimble", "Namfoodle", "Orryn", "Wrenn"],
        "female_names": ["Breena", "Caramip", "Duvamil", "Ellyjobell", "Ellywick", "Loopmottin", "Mardnab", "Roywyn"],
        "size_small": ["2'9\" (85 cm)", "40 lbs (18 kg)"],
        "size_medium": ["3'3\" (100 cm)", "49 lbs (22 kg)"],
        "size_big": ["3'9\" (115 cm)", "60 lbs (27 kg)"],
        "age": ["under 60 ages", "60–120 ages", "over 350 ages"],
        "ability_bonuses": {
            "Strength": 0,
            "Dexterity": 1,
            "Constitution": 0,
            "Intelligence": 2,
            "Wisdom": 0,
            "Charisma": 0
        },
        "image": "media/races/dnd_forest_gnome.png"
    },
    "rock_gnome": {
        "title": "Rock Gnome",
        "description": "Rock gnomes are curious inventors and tinkerers, known for their resilience and love of discovery.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Alston", "Alvyn", "Boddynock", "Dimble", "Fonkin", "Gimble", "Namfoodle", "Orryn", "Wrenn"],
        "female_names": ["Breena", "Caramip", "Duvamil", "Ellyjobell", "Ellywick", "Loopmottin", "Mardnab", "Roywyn"],
        "size_small": ["2'11\" (90 cm)", "44 lbs (20 kg)"],
        "size_medium": ["3'5\" (105 cm)", "55 lbs (25 kg)"],
        "size_big": ["3'11\" (120 cm)", "66 lbs (30 kg)"],
        "age": ["under 60 ages", "60–120 ages", "over 350 ages"],
        "ability_bonuses": {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 1,
            "Intelligence": 2,
            "Wisdom": 0,
            "Charisma": 0
        },
        "image": "media/races/dnd_rock_gnome.png"
    },
    "half_elf": {
        "title": "Half-Elf",
        "description": "Half-elves combine the best traits of elves and humans, being versatile, charismatic, and adaptable.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Berrian", "Carric", "Enialis", "Lucan", "Peren", "Soveliss", "Thamior", "Varis", "Rolen"],
        "female_names": ["Althaea", "Anastrianna", "Drusilia", "Keyleth", "Lia", "Mialee", "Naivara", "Shava", "Thia"],
        "size_small": ["5'1\" (155 cm)", "106 lbs (48 kg)"],
        "size_medium": ["5'7\" (170 cm)", "143 lbs (65 kg)"],
        "size_big": ["6'1\" (185 cm)", "187 lbs (85 kg)"],
        "age": ["under 25 ages", "25–70 ages", "over 180 ages"],
        "ability_bonuses": {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 2
            # + 1 to any characteristic
        },
        "image": "media/races/dnd_half_elf.png"
    },
    "half_orc": {
        "title": "Half-Orc",
        "description": "Half-orcs are strong and brave, often facing prejudice but proving themselves through their actions and endurance.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Ront"],
        "female_names": ["Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Shautha", "Sutha"],
        "size_small": ["5'1\" (155 cm)", "132 lbs (60 kg)"],
        "size_medium": ["5'11\" (180 cm)", "198 lbs (90 kg)"],
        "size_big": ["6'7\" (200 cm)", "265 lbs (120 kg)"],
        "age": ["under 20 ages", "20–40 ages", "over 75 ages"],
        "ability_bonuses": {
            "Strength": 2,
            "Dexterity": 0,
            "Constitution": 1,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        },
        "image": "media/races/dnd_half_orc.png"
    },
    "tiefling": {
        "title": "Tiefling",
        "description": "Tieflings are known for their cunning, personal allure, and fiendish heritage, often facing suspicion but possessing innate magical talent.",
        "detailed_description": "some more info",
        "features": "some more info",
        "male_names": ["Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Mordai"],
        "female_names": ["Akta", "Bryseis", "Criella", "Damaia", "Kallista", "Lerissa", "Makaria", "Nemeia", "Orianna"],
        "size_small": ["4'9\" (145 cm)", "88 lbs (40 kg)"],
        "size_medium": ["5'5\" (165 cm)", "121 lbs (55 kg)"],
        "size_big": ["6'1\" (185 cm)", "154 lbs (70 kg)"],
        "age": ["under 25 ages", "25–40 ages", "over 70 ages"],
        "ability_bonuses": {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 1,
            "Wisdom": 0,
            "Charisma": 2
        },
        "image": "media/races/dnd_tiefling.png"
    }
}




# classes, their descriptions, characteristics and pictures

class_info = {
    "barbarian": {
        "title": "Barbarian",
        "description": "Barbarians are mighty warriors powered by primal forces. Their Rage is a force of nature that fuels battle prowess, reflexes, and senses. Barbarians often serve as protectors and leaders, charging into danger to shield others.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d12",
        "primary_ability": "Strength",
        "saving_throws": ["Strength", "Constitution"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields"],
        "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
        "ability_scores": {
            "Strength": 15,
            "Dexterity": 13,
            "Constitution": 14,
            "Intelligence": 10,
            "Wisdom": 12,
            "Charisma": 8
        },
        "image": "media/classes/dnd_barbarian.png"
    },
    "bard": {
        "title": "Bard",
        "description": "Bards invoke magic through music and words, inspiring allies, creating illusions, and gathering lore. They are masters of many things, traveling, telling stories, and living on the gratitude of audiences.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d8",
        "primary_ability": "Charisma",
        "saving_throws": ["Dexterity", "Charisma"],
        "armor_proficiencies": ["Light armor"],
        "weapon_proficiencies": ["Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"],
        "ability_scores": {
            "Strength": 8,
            "Dexterity": 14,
            "Constitution": 12,
            "Intelligence": 13,
            "Wisdom": 10,
            "Charisma": 15
        },
        "image": "media/classes/dnd_bard.png"
    },
    "cleric": {
        "title": "Cleric",
        "description": "Clerics draw power from the gods to heal, protect, and smite foes. Blessed by a deity or pantheon, they channel divine magic and often serve temples or shrines, performing miracles and rituals.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d8",
        "primary_ability": "Wisdom",
        "saving_throws": ["Wisdom", "Charisma"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields"],
        "weapon_proficiencies": ["Simple weapons"],
        "ability_scores": {
            "Strength": 14,
            "Dexterity": 8,
            "Constitution": 13,
            "Intelligence": 10,
            "Wisdom": 15,
            "Charisma": 12
        },
        "image": "media/classes/dnd_cleric.png"
    },
    "druid": {
        "title": "Druid",
        "description": "Druids call on the forces of nature, healing, transforming, and wielding elemental power. They gain magic from nature or a deity, often guarding sacred sites and maintaining the balance of the wild.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d8",
        "primary_ability": "Wisdom",
        "saving_throws": ["Intelligence", "Wisdom"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields (non-metal)"],
        "weapon_proficiencies": ["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"],
        "ability_scores": {
            "Strength": 8,
            "Dexterity": 12,
            "Constitution": 14,
            "Intelligence": 13,
            "Wisdom": 15,
            "Charisma": 10
        },
        "image": "media/classes/dnd_druid.png"
    },
    "fighter": {
        "title": "Fighter",
        "description": "Fighters are masters of weapons and armor, skilled in various combat styles. They adapt to any battlefield, specializing in techniques like archery, two-weapon fighting, or combining martial skill with magic.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d10",
        "primary_ability": "Strength or Dexterity",
        "saving_throws": ["Strength", "Constitution"],
        "armor_proficiencies": ["All armor", "Shields"],
        "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
        "ability_scores": {
            "Strength": 15,
            "Dexterity": 14,
            "Constitution": 13,
            "Intelligence": 8,
            "Wisdom": 10,
            "Charisma": 12
        },
        "image": "media/classes/dnd_fighter.png"
    },
    "monk": {
        "title": "Monk",
        "description": "Monks use combat training and discipline to focus internal power. They channel speed and strength into attacks, often living ascetic lives or seeking growth through adventure.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d8",
        "primary_ability": "Dexterity",
        "saving_throws": ["Strength", "Dexterity"],
        "armor_proficiencies": [],
        "weapon_proficiencies": ["Simple weapons", "Shortswords"],
        "ability_scores": {
            "Strength": 12,
            "Dexterity": 15,
            "Constitution": 13,
            "Intelligence": 10,
            "Wisdom": 14,
            "Charisma": 8
        },
        "image": "media/classes/dnd_monk.png"
    },
    "paladin": {
        "title": "Paladin",
        "description": "Paladins swear oaths to fight evil and corruption, combining martial skill with divine magic to heal, smite foes, and protect allies. Their oath is a powerful bond and source of strength.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d10",
        "primary_ability": "Strength",
        "saving_throws": ["Wisdom", "Charisma"],
        "armor_proficiencies": ["All armor", "Shields"],
        "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
        "ability_scores": {
            "Strength": 15,
            "Dexterity": 10,
            "Constitution": 13,
            "Intelligence": 8,
            "Wisdom": 12,
            "Charisma": 14
        },
        "image": "media/classes/dnd_paladin.png"
    },
    "ranger": {
        "title": "Ranger",
        "description": "Rangers are hunters and trackers, skilled in wilderness survival and deadly with weapons. They use magic tied to nature and focus their talents to protect the world from threats.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d10",
        "primary_ability": "Dexterity",
        "saving_throws": ["Strength", "Dexterity"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields"],
        "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
        "ability_scores": {
            "Strength": 12,
            "Dexterity": 15,
            "Constitution": 13,
            "Intelligence": 8,
            "Wisdom": 14,
            "Charisma": 10
        },
        "image": "media/classes/dnd_ranger.png"
    },
    "rogue": {
        "title": "Rogue",
        "description": "Rogues excel at cunning, stealth, and exploiting vulnerabilities. They solve problems creatively and may learn magical tricks. In combat, they strike precisely rather than with brute force.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d8",
        "primary_ability": "Dexterity",
        "saving_throws": ["Dexterity", "Intelligence"],
        "armor_proficiencies": ["Light armor"],
        "weapon_proficiencies": ["Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"],
        "ability_scores": {
            "Strength": 12,
            "Dexterity": 15,
            "Constitution": 13,
            "Intelligence": 14,
            "Wisdom": 10,
            "Charisma": 8
        },
        "image": "media/classes/dnd_rogue.png"
    },
    "sorcerer": {
        "title": "Sorcerer",
        "description": "Sorcerers wield innate magic, often from mysterious origins. Their power is part of them, and they learn to harness and channel it in unique ways, developing distinct magical abilities.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d6",
        "primary_ability": "Charisma",
        "saving_throws": ["Constitution", "Charisma"],
        "armor_proficiencies": [],
        "weapon_proficiencies": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"],
        "ability_scores": {
            "Strength": 10,
            "Dexterity": 13,
            "Constitution": 14,
            "Intelligence": 8,
            "Wisdom": 12,
            "Charisma": 15
        },
        "image": "media/classes/dnd_sorcerer.png"
    },
    "warlock": {
        "title": "Warlock",
        "description": "Warlocks seek hidden knowledge and power, forming pacts with powerful patrons. They gain eldritch abilities and arcane secrets, often pursuing greater power and deeper understanding.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d8",
        "primary_ability": "Charisma",
        "saving_throws": ["Wisdom", "Charisma"],
        "armor_proficiencies": ["Light armor"],
        "weapon_proficiencies": ["Simple weapons"],
        "ability_scores": {
            "Strength": 8,
            "Dexterity": 14,
            "Constitution": 13,
            "Intelligence": 12,
            "Wisdom": 10,
            "Charisma": 15
        },
        "image": "media/classes/dnd_warlock.png"
    },
    "wizard": {
        "title": "Wizard",
        "description": "Wizards are scholars of magic, casting powerful spells and studying arcane secrets. Their knowledge allows them to shape reality, summon creatures, and master a variety of magical effects.",
        "detailed_description": "some more info",
        "features": "some more info",
        "hit_die": "d6",
        "primary_ability": "Intelligence",
        "saving_throws": ["Intelligence", "Wisdom"],
        "armor_proficiencies": [],
        "weapon_proficiencies": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"],
        "ability_scores": {
            "Strength": 8,
            "Dexterity": 12,
            "Constitution": 13,
            "Intelligence": 15,
            "Wisdom": 14,
            "Charisma": 10
        },
        "image": "media/classes/dnd_wizard.png"
    }
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
