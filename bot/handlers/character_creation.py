from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from telegram import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InputMediaPhoto
from utils.logger import logger

RACE, CLASS, LEVEL, CHARACTERISTICS, NAME, AGE, APPEARANCE, WORLDVIEW, BACKSTORY = range(9)






async def character_race(update, context):
    logger.info('Race asked')

    keyboard = [
        [InlineKeyboardButton(race, callback_data=f'{race}') for race in ["Elf", "Dwarf"]],
        [InlineKeyboardButton(race, callback_data=f'{race}') for race in ["Human", "Half-orc"]],
        [InlineKeyboardButton(race, callback_data=f'{race}') for race in ["Half-elf", "Dragonborn"]],
        [InlineKeyboardButton(race, callback_data=f'{race}') for race in ["Gnome", "Halfling"]],
        [InlineKeyboardButton("Tiefling", callback_data='Tiefling')],
        [InlineKeyboardButton("Race Description", callback_data='character_race_desc')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)


    caption = ( 
        "Step 1: Choose Your Character’s Race\n\nThe world of Dungeons & Dragons is filled with diverse and fascinating races, each with their own unique cultures, abilities, and histories. Will your hero be a wise Elf, a resilient Dwarf, a resourceful Human, or perhaps a mysterious Tiefling?\n\nSelect your character’s race from the keyboard below or type your own choice. Let your imagination guide you!"
    )

    with open('C:\Programming\PetProjects\DnD-character-maker\media\dnd_race.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=reply_markup,
            media=InputMediaPhoto(
                media=photo,
                caption=caption,
            )
    )


    return RACE


async def show_race_description_menu(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton(race, callback_data=f'desc_{race}') for race in ["Elf", "Dwarf"]],
        [InlineKeyboardButton(race, callback_data=f'desc_{race}') for race in ["Human", "Half-orc"]],
        [InlineKeyboardButton(race, callback_data=f'desc_{race}') for race in ["Half-elf", "Dragonborn"]],
        [InlineKeyboardButton(race, callback_data=f'desc_{race}') for race in ["Gnome", "Halfling"]],
        [InlineKeyboardButton("Tiefling", callback_data='desc_Tiefling')],
        [InlineKeyboardButton("Back", callback_data='back_to_race')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_caption(
        caption="Choose a race to learn more about it:",
        reply_markup=reply_markup
    )


RACE_DESCRIPTIONS = {
    "Elf": "Elves are graceful, magical people of otherworldly beauty, living in the world but not entirely part of it.",
    "Dwarf": "Dwarves are known for their skill in warfare, their ability to withstand physical and magical punishment, and their hard work.",
    "Human": "Humans are the most adaptable and ambitious people among the common races.",
    "Half-orc": "Half-orcs are strong and brave, often facing prejudice but proving themselves through their actions.",
    "Half-elf": "Half-elves combine what some say are the best qualities of their elf and human parents.",
    "Dragonborn": "Dragonborn look very much like dragons standing erect in humanoid form, though they lack wings or a tail.",
    "Gnome": "A gnome’s energy and enthusiasm for living shines through every inch of his or her tiny body.",
    "Halfling": "Halflings are an optimistic and cheerful people, known for their resourcefulness.",
    "Tiefling": "Tieflings are known for their cunning and personal allure, but also for their fiendish heritage."
}


async def show_race_description(update, context):
    query = update.callback_query
    await query.answer()
    race = query.data.replace('desc_', '')
    description = RACE_DESCRIPTIONS.get(race, "No description available.")
    keyboard = [
        [InlineKeyboardButton("Back", callback_data='character_race_desc')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_caption(
        caption=f"<b>{race}</b>\n\n{description}",
        reply_markup=reply_markup,
        parse_mode="HTML"
    )












async def character_class(update, context):
    logger.info('Class asked')

    keyboard = [
        [InlineKeyboardButton("Barbarian", callback_data='Barbarian'), InlineKeyboardButton("Bard", callback_data='Bard')],
        [InlineKeyboardButton("Cleric", callback_data='Cleric'), InlineKeyboardButton("Druid", callback_data='Druid')],
        [InlineKeyboardButton("Fighter", callback_data='Fighter'), InlineKeyboardButton("Monk", callback_data='Monk')],
        [InlineKeyboardButton("Paladin", callback_data='Paladin'), InlineKeyboardButton('Rogue', callback_data='Rogue')], 
        [InlineKeyboardButton('Sorcerer', callback_data='Sorcerer'), InlineKeyboardButton('Warlock', callback_data='Wizard')],
        [InlineKeyboardButton('Ranger', callback_data='Ranger')],
        [InlineKeyboardButton('Class Description', callback_data='character_class_description')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    with open('C:\Programming\PetProjects\DnD-character-maker\media\dnd_class.png', 'rb') as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="Step 2: Select Your Character’s Class\n\nA character’s class determines their skills, strengths, and the role they play in the party. Will you wield powerful magic as a Wizard, sneak through the shadows as a Thief, or charge into battle as a Barbarian?\n\nChoose your class from the options below. This is the heart of your hero’s abilities!",
            reply_markup=reply_markup
        )
    
    return CLASS



async def character_level(update, context):

    query = update.callback_query
    await query.answer()
    character_class = query.data

    context.user_data['character_class'] = character_class

    keyboard = [
        [InlineKeyboardButton('level 1', callback_data='character_level_1'), InlineKeyboardButton('level 2', callback_data='character_level_2'), InlineKeyboardButton('level 3', callback_data='character_level_3')],
        [InlineKeyboardButton('level 4', callback_data='character_level_4'), InlineKeyboardButton('level 5', callback_data='character_level_5'), InlineKeyboardButton('level 6', callback_data='character_level_6')],
        [InlineKeyboardButton('level 7', callback_data='character_level_7'), InlineKeyboardButton('level 8', callback_data='character_level_8'), InlineKeyboardButton('level 9', callback_data='character_level_9')],
        [InlineKeyboardButton('level 10', callback_data='character_level_10'), InlineKeyboardButton('level 11', callback_data='character_level_11'), InlineKeyboardButton('level 12', callback_data='character_level_12')],
        [InlineKeyboardButton('level 13', callback_data='character_level_13'), InlineKeyboardButton('level 14', callback_data='character_level_14'), InlineKeyboardButton('level 15', callback_data='character_level_15')],
        [InlineKeyboardButton('level 16', callback_data='character_level_16'), InlineKeyboardButton('level 17', callback_data='character_level_17'), InlineKeyboardButton('level 18', callback_data='character_level_18')],
        [InlineKeyboardButton('level 19', callback_data='character_level_19'), InlineKeyboardButton('level 20', callback_data='character_level_20')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    with open('C:\Programming\PetProjects\DnD-character-maker\media\dnd_level.png', 'rb') as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption='',
            reply_markup=reply_markup
        )

    return LEVEL





async def character_characteristics(update, context):
    logger.info('Characteristics asked')

    query = update.callback_query
    await query.answer()
    character_class = query.data

    keyboard = [
        [InlineKeyboardButton('Characteristics Description', callback_data='character_characteristics_description')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.user_data['character_class'] = character_class

    with open('C:\Programming\PetProjects\DnD-character-maker\media\dnd_characteristics.png', 'rb') as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="Step 3: Define Your Character’s Characteristics\n\nEvery hero has unique traits that set them apart. Think about your character’s strengths, weaknesses, and special talents. Are they incredibly strong, remarkably clever, or perhaps exceptionally charming?\n\nDescribe the main characteristics of your character. This will shape how they interact with the world!",
            reply_markup=reply_markup
    )

    return CHARACTERISTICS





async def character_name(update, context):
    logger.info('Name asked')

    context.user_data['character_characteristics'] = update.message.text

    with open('C:\Programming\PetProjects\DnD-character-maker\media\dnd_name.png', 'rb') as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="Step 4: Name Your Hero\n\nA name gives your character identity and presence in the world. Will it be grand and legendary, or simple and heartfelt? The choice is yours!\n\nPlease enter your character’s name below. Be creative—this is your moment to make your hero truly unique!",
    )
    
    return NAME





async def character_age(update, context):
    logger.info('Age asked')

    context.user_data['character_name'] = update.message.text

    with open('C:\Programming\PetProjects\DnD-character-maker\media\dnd_age.png', 'rb') as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="Step 5: Decide Your Character’s Age\n\nAge can influence your character’s experience, wisdom, and outlook on life. Are they a young adventurer eager for glory, or a seasoned veteran with stories to tell?\n\nEnter your character’s age. Feel free to add a little backstory about their life so far!",
    )
    
    return AGE





async def character_appearance(update, context):
    logger.info('Appearance asked')

    query = update.callback_query
    await query.answer()
    character_body_type = query.data

    context.user_data['character_body_type'] = character_body_type

    with open('C:\Programming\PetProjects\DnD-character-maker\media\dnd_appearance.png', 'rb') as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="Step 7: Describe Your Character’s Appearance\n\nWhat does your character look like? Do they have striking eyes, a memorable scar, or a distinctive style? Their appearance can make them unforgettable in the eyes of friends and foes alike.\n\nDescribe your character’s appearance in a few words or sentences. Paint a vivid picture!",
    )

    return APPEARANCE





async def character_worldview(update, context):
    logger.info('Appearance asked')

    context.user_data['character_appearance'] = update.message.text

    keyboard = [
        [InlineKeyboardButton('Lawful Good', callback_data='Lawful Good'), InlineKeyboardButton('Neutral Good', callback_data='Neutral Good'), InlineKeyboardButton('Chaotic Good', callback_data='Chaotic Good')],
        [InlineKeyboardButton('Lawful Neutral', callback_data='Lawful Neutral'), InlineKeyboardButton('True Neutral', callback_data='True Neutral'), InlineKeyboardButton('Chaotic Neutral', callback_data='Chaotic Neutral')],
        [InlineKeyboardButton('Lawful Evil', callback_data='Lawful Evil'), InlineKeyboardButton('Neutral Evil', callback_data='Neutral Evil'), InlineKeyboardButton('Chaotic Evil', callback_data='Chaotic Evil')],
        [InlineKeyboardButton('Worldview Description', callback_data='character_worldview_description')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    with open('C:\Programming\PetProjects\DnD-character-maker\media\dnd_worldview.png', 'rb') as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="Step 8: Define Your Character’s Worldview\n\nA character’s worldview (alignment) shapes their morals and decisions. Are they guided by honor, driven by chaos, or do they walk the path between good and evil?\n\nChoose an alignment from the keyboard or type your own. This will influence your hero’s actions and choices!",
            reply_markup=reply_markup
    )

    return WORLDVIEW





async def character_backstory(update, context):
    logger.info('Backstory asked')

    query = update.callback_query
    await query.answer()
    character_worldview = query.data

    context.user_data['character_worldview'] = character_worldview

    keyboard = [
        [InlineKeyboardButton('Acolyte', callback_data='Acolyte'), InlineKeyboardButton('Charlatan', callback_data='Charlatan'), InlineKeyboardButton('Criminal', callback_data='Criminal')],
        [InlineKeyboardButton('Entertainer', callback_data='Entertainer'), InlineKeyboardButton('Folk Hero', callback_data='Folk Hero'), InlineKeyboardButton('Guild Artisan', callback_data='Guild Artisan')],
        [InlineKeyboardButton('Noble', callback_data='Noble'), InlineKeyboardButton('Outlander', callback_data='Outlander'), InlineKeyboardButton('Sage', callback_data='Sage')],
        [InlineKeyboardButton('Soldier', callback_data='Soldier'), InlineKeyboardButton('Urchin', callback_data='Urchin')],
        [InlineKeyboardButton('Worldview Description', callback_data='character_backstory_description')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    with open('C:\Programming\PetProjects\DnD-character-maker\media\dnd_backstory.png', 'rb') as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="Step 9: Create Your Character’s Backstory\n\nEvery adventurer has a story. What events shaped your hero before they set out on their journey? Were they a noble, a wanderer, a scholar, or something entirely different?\n\nChoose a background from the keyboard or write your own. The richer the backstory, the more alive your character will become!",
            reply_markup=reply_markup
    )

    return BACKSTORY







async def finish_creation(update, context):

    query = update.callback_query
    await query.answer()
    character_backstory = query.data

    context.user_data['character_backstory'] = character_backstory


    character_name = context.user_data['character_name']
    character_class = context.user_data['character_class']
    character_race = context.user_data['character_race']
    character_characteristics = context.user_data['character_characteristics']
    character_age = context.user_data['character_age']
    character_backstory = context.user_data['character_backstory']
    character_appearance = context.user_data['character_appearance']
    character_worldview = context.user_data['character_worldview']

    await update.effective_message.reply_text(f"Your new character for your lovely boardgame!\n\nName: {character_name}\nClass: {character_class}\nRace: {character_race}\nCharacteristics: {character_characteristics}\nAge: {character_age}\nAppearance: {character_appearance}\nBackstory: {character_backstory}\nWorldview: {character_worldview}")
    logger.info('Character created')
    return ConversationHandler.END




async def cancel(update, context):
    await update.message.reply_text("Creation of character stopped")
    logger.info('Character creation stopped')
    return ConversationHandler.END





character_creation = ConversationHandler(
    entry_points=[CallbackQueryHandler(character_race, pattern='^start_button$')],
    states={
        RACE: [
            CallbackQueryHandler(show_race_description_menu, pattern='^character_race_desc$'),
            CallbackQueryHandler(show_race_description, pattern='^desc_'),
            CallbackQueryHandler(show_race_description_menu, pattern='^back_to_race_desc$'),
            CallbackQueryHandler(character_class, pattern='^(Elf|Dwarf|Human|Half-orc|Half-elf|Dragonborn|Gnome|Halfling|Tiefling)$'),
            CallbackQueryHandler(character_race, pattern='^back_to_race$'),
            # CallbackQueryHandler(character_class)
        ],
        CLASS: [CallbackQueryHandler(character_characteristics)],
        CHARACTERISTICS: [MessageHandler(filters.TEXT & ~filters.COMMAND, character_name)],
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, character_age)],
        AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, character_appearance)],
        APPEARANCE: [MessageHandler(filters.TEXT & ~filters.COMMAND, character_worldview)],
        WORLDVIEW: [CallbackQueryHandler(character_backstory)],
        BACKSTORY: [CallbackQueryHandler(finish_creation)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)
