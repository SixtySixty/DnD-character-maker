from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from telegram import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InputMediaPhoto
from telegram.constants import ParseMode
from utils.logger import logger
from .data import class_features, race_info

RACE, CLASS, LEVEL, CHARACTERISTICS, NAME, AGE, APPEARANCE, WORLDVIEW, BACKSTORY = range(9)


# function that generates the inline_keyboard

def build_inline_keyboard(
    items: list[str],
    row_width: int = 2,
    callback_prefix: str = '',
    add_desc_button: bool = False,
    desc_callback_data: str = '',
    add_back_button: bool = False,
    back_callback_data: str = ''
) -> InlineKeyboardMarkup:
    keyboard = []
    for i in range(0, len(items), row_width):
        row = items[i:i+row_width]
        keyboard.append([InlineKeyboardButton(text=item, callback_data=f'{callback_prefix}{item}') for item in row])
    if add_desc_button and desc_callback_data:
        keyboard.append([InlineKeyboardButton('Description', callback_data=desc_callback_data)])
    if add_back_button and back_callback_data:
        keyboard.append([InlineKeyboardButton('Back', callback_data=back_callback_data)])
    return InlineKeyboardMarkup(keyboard)





# choosing a race + descriptions

async def character_race(update, context):
    logger.info('Race asked')

    keyboard = build_inline_keyboard(
        items=list(race_info.keys()),
        row_width=3,
        callback_prefix='desc_'
    )

    with open('media/dnd_race.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=keyboard,
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption="*Step 1: Choose Your Character’s Race*\n\nThe world of *Dungeons & Dragons* is filled with diverse and fascinating races, each with their own unique cultures, abilities, and histories. Will your hero be a wise Elf, a resilient Dwarf, a resourceful Human, or perhaps a mysterious Tiefling?\n\nSelect your character’s race from the keyboard below and read a short description. Let your imagination guide you!",
            )
        )


    return RACE


async def show_race_desc(update, context):
    query = update.callback_query
    await query.answer()
    race = query.data.replace('desc_', '')

    race_data = race_info.get(race, {})
    description = race_data.get("description", "No description available.")
    image_path = race_data.get("image", None)

    keyboard = [[InlineKeyboardButton("Choose this", callback_data=race)], [InlineKeyboardButton("Back", callback_data='back_to_race')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if image_path:
        with open(image_path, "rb") as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=reply_markup,
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{race}*\n\n{description}",
                    parse_mode="Markdown"
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{race}*\n\n{description}",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )










# choosing character class + descriptions


async def character_class(update, context):
    logger.info('Class asked')

    keyboard = build_inline_keyboard(
        items=list(class_features.keys()),
        row_width=3,
        callback_prefix='desc_'
    )

    with open('C:\Programming\PetProjects\DnD-character-maker\media\dnd_class.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=keyboard,
            media=InputMediaPhoto(
                media=photo,
                caption="Step 2: Select Your Character’s Class\n\nA character’s class determines their skills, strengths, and the role they play in the party. Will you wield powerful magic as a Wizard, sneak through the shadows as a Thief, or charge into battle as a Barbarian?\n\nChoose your class from the options below. This is the heart of your hero’s abilities!",
            )
        )

    return CLASS





async def show_class_desc(update, context):
    query = update.callback_query
    await query.answer()

    character_class = query.data.replace('desc_', '')

    class_info = class_features.get(character_class, {})
    description = class_info.get("description", "No description available.")
    image_path = class_info.get("image", None)  # путь к картинке

    keyboard = [[InlineKeyboardButton("Choose this", callback_data=character_class)], [InlineKeyboardButton("Back", callback_data='back_to_class')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if image_path:
        with open(image_path, "rb") as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=reply_markup,
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{character_class}*\n\n{description}",
                    parse_mode="Markdown"
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{character_class}*\n\n{description}",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )


# characteristics


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
            CallbackQueryHandler(character_class, pattern='^(Hill Dwarf|Mountain Dwarf|High Elf|Wood Elf|Dark Elf (Drow)|Lightfoot Halfling|Stout Halfling|Human|Dragonborn|Forest Gnome|Rock Gnome|Half-Elf|Half-Orc|Tiefling)$'),
            CallbackQueryHandler(show_race_desc, pattern='^desc_'),
            CallbackQueryHandler(character_race, pattern='^back_to_race$'),
        ],
        CLASS: [
            CallbackQueryHandler(character_characteristics, pattern='^(Barbarian|Cleric|Fighter|Paladin|Sorcerer|Ranger|Bard|Druid|Monk|Rogue|Warlock|Wizard)$'),
            CallbackQueryHandler(show_class_desc, pattern='^desc_'),
            CallbackQueryHandler(character_class, pattern='^back_to_class$')
        ],
        CHARACTERISTICS: [MessageHandler(filters.TEXT & ~filters.COMMAND, character_name)],
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, character_age)],
        AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, character_appearance)],
        APPEARANCE: [MessageHandler(filters.TEXT & ~filters.COMMAND, character_worldview)],
        WORLDVIEW: [CallbackQueryHandler(character_backstory)],
        BACKSTORY: [CallbackQueryHandler(finish_creation)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)
