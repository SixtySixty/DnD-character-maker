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