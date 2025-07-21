from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.constants import ParseMode
from utils.logger import logger
from .data_race import race_info
from .data_class import class_info
from .data_worldview import worldview_info
from .data_backstory  import backstory_info

RACE, CLASS, GENDER, SIZE, AGE, NAME, SURNAME, APPEARANCE, WORLDVIEW, TRAITS, IDEALS, ATTACHMENTS, WEAKNESSES, CHARACTERISTICS, LEVEL, BACKSTORY = range(16)


# function that generates the inlineKeyboard

def build_inline_keyboard(items, values, row_width=2, callback_prefix=''):
    keyboard = []
    for i in range(0, len(items), row_width):
        row_items = items[i:i+row_width]
        row_values = values[i:i+row_width]
        row = [
            InlineKeyboardButton(
                text=text,
                callback_data=f'{callback_prefix}{value}'
            ) for text, value in zip(row_items, row_values)
        ]
        keyboard.append(row)
    return keyboard




# choosing a race + descriptions

async def character_race(update, context):
    logger.info('Race asked')

    # getting data to create buttons in inline keyboard
    races = list(race_info.keys())
    races_titles = [race_info[race]["title"] for race in races if race in race_info] 

    # creating inlinekeyboard
    keyboard = build_inline_keyboard(races_titles, races, row_width=3, callback_prefix='race_menu_')

    # creating the message to user
    with open('media/stages/dnd_race.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    "*Step 1: Choose Your Character’s Race*\n\n"
                    "The world of *Dungeons & Dragons* is filled with diverse and fascinating races, each with their own unique cultures, abilities, and histories. "
                    "Will your hero be a wise Elf, a resilient Dwarf, a resourceful Human, or perhaps a mysterious Tiefling?\n\n"
                    "Select your character’s race from the keyboard below and read a short description. Let your imagination guide you!"
                )
            )
        )

    return RACE




async def show_race_menu(update, context):
    query = update.callback_query
    await query.answer()

    # editing and saving data
    if query.data.startswith("race_menu_back"):
        character_race = context.user_data.get('race')
    elif query.data.startswith("race_menu_"):
        character_race = query.data.replace("race_menu_", "")
        context.user_data['race'] = character_race

    logger.info(f'{character_race}')

    # getting data to show race info
    race_data = race_info.get(character_race, {})
    race_title = race_data.get("title", "No title available.")
    race_description = race_data.get("description", "No description available.")
    image_path = race_data.get("image", None)

    # creating inlinekeyboard
    keyboard = [
        [InlineKeyboardButton("More info", callback_data=f'race_info'),
         InlineKeyboardButton("Features", callback_data=f'race_features')],
        [InlineKeyboardButton("Choose", callback_data=f'race_select')],
        [InlineKeyboardButton("Back", callback_data='race_back')]
    ]

    # creating the message to user
    if image_path:
        with open(image_path, "rb") as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=update.callback_query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{race_title}*\n\n{race_description}",
                    parse_mode="Markdown"
                )
            )
    else:
        await update.callback_query.edit_message_caption(
            caption=f"*{race_title}*\n\n{race_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    return RACE



async def show_race_more_info(update, context):
    query = update.callback_query
    await query.answer()    

    character_race = context.user_data.get('race')

    if query.data.startswith("race_info"):
        title = "More info"
        text = race_info[character_race].get("detailed_description", "No description available.")
    elif query.data.startswith("race_features"):
        title = "Features"
        text = race_info[character_race].get("features", "No features available.")
    else:
        character_race = None
        title = "Info"
        text = "No info available."

    race_title = race_info.get(character_race, {}).get('title', character_race)

    keyboard = [[InlineKeyboardButton('Back', callback_data=f'race_menu_back')]]

    await query.edit_message_caption(
        caption=f"*{race_title} — {title}*\n\n{text}",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

    return RACE


# choosing a class + descriptions


async def character_class(update, context):
    logger.info('Class asked')

    query = update.callback_query
    await query.answer()

    character_classes = list(class_info.keys())
    character_classes_titles = [class_info[character_class]["title"] for character_class in character_classes if character_class in class_info]

    keyboard = build_inline_keyboard(character_classes_titles, character_classes, row_width=3, callback_prefix='class_menu_')

    with open('media/stages/dnd_class.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    "*Step 2: Select Your Character’s Class*\n\n"
                    "A character’s class determines their skills, strengths, and the role they play in the party. "
                    "Will you wield powerful magic as a Wizard, sneak through the shadows as a Thief, or charge into battle as a Barbarian?\n\n"
                    "Choose your class from the options below. This is the heart of your hero’s abilities!"
                )
            )
        )
        
    return CLASS


async def show_class_menu(update, context):
    query = update.callback_query
    await query.answer()

    if query.data.startswith("class_menu_back"):
        character_class = context.user_data.get('class')
    elif query.data.startswith("class_menu"):
        character_class = query.data.replace("class_menu_", "")
        context.user_data['class'] = character_class

    logger.info(f'{character_class}')

    class_data = class_info.get(character_class, {})
    class_title = class_data.get("title", "No title available.")
    class_description = class_data.get("description", "No description available.")
    image_path = class_data.get("image", None)
    
    keyboard = [
        [InlineKeyboardButton("More info", callback_data=f'class_info'),
         InlineKeyboardButton("Features", callback_data=f'class_features')],
        [InlineKeyboardButton("Choose this", callback_data=f'class_select')],
        [InlineKeyboardButton("Back", callback_data='class_back')]
    ]

    if image_path:
        with open(image_path, "rb") as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{class_title}*\n\n{class_description}",
                    parse_mode="Markdown"
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{character_class}*\n\n{class_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )
    
    return CLASS
        

async def show_class_more_info(update, context):
    query = update.callback_query
    await query.answer()

    character_class = context.user_data.get('class')

    if query.data.startswith("class_info"):
        title = "More info"
        text = class_info[character_class].get("detailed_description", "No description available.")
    elif query.data.startswith("class_features"):
        title = "Features"
        text = class_info[character_class].get("features", "No features available.")
    else:
        character_class = None
        title = "Info"
        text = "No info available."

    class_title = class_info.get(character_race, {}.get('title', character_class))

    keyboard = [[InlineKeyboardButton('Back', callback_data='class_menu_back')]]

    await query.edit_message_caption(
        caption=f"*{class_title} — {title}*\n\n{text}",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

    return CLASS





# choosing gender 

async def character_gender(update, context):
    logger.info('Gender asked')

    query = update.callback_query
    await query.answer()

    keyboard = [[InlineKeyboardButton('Female', callback_data='gender_select_female'), InlineKeyboardButton('Male', callback_data='gender_select_male')]]
    

    with open('media/stages/dnd_gender.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    "*Step 3: Select Your Character’s Gender*\n\n"
                    "Every hero’s story is unique, and so is their identity. Will your character be a fearless woman, a bold man, or perhaps someone who walks a different path? The choice is yours to shape their journey and personality.\n\nSelect your character’s gender from the options below. This is another step in bringing your adventurer to life!"
                )
            )
        )

    return GENDER



# choosing character size (small / mid / big)

async def character_size(update, context):
    logger.info('Size asked')

    query = update.callback_query
    await query.answer()

    # creating and saving character`s gender
    character_gender = query.data.replace('gender_select_', '')
    context.user_data['gender'] = character_gender

    character_race = context.user_data.get('race')
    race_data = race_info.get(character_race, {})

    character_sizes = race_data.get("body_size", "No size available")
    character_size_small = character_sizes["small"]
    character_size_medium = character_sizes["medium"]
    character_size_big = character_sizes["big"]

    keyboard = [
        [InlineKeyboardButton('Small', callback_data='size_select_small'), InlineKeyboardButton('Medium', callback_data='size_select_medium'), InlineKeyboardButton('Big', callback_data='size_select_big')]
    ]

    with open('media/stages/dnd_size.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    f"*Step 4: Choose Your Character’s Size*\n\nThe size you select helps define your character’s presence and how they interact with the world—will they move with the grace of the small or the strength of the mighty?\n\n*Small size:* {character_size_small[0]}, {character_size_small[1]}\n*Medium size:* {character_size_medium[0]}, {character_size_medium[1]}\n*Big size:* {character_size_big[0]}, {character_size_big[1]}\n\nChoose your character’s size from the options below."
                )
            )
        )


    return SIZE



# choosing age

async def character_age(update, context):
    logger.info('Age asked')

    query = update.callback_query
    await query.answer()

    # creating and saving character`s size
    character_size = query.data.replace('size_select_', '')
    context.user_data["size"] = character_size

    keyboard = [
        [InlineKeyboardButton('Young', callback_data='age_select_young'), InlineKeyboardButton('Mature', callback_data='age_select_mature'), InlineKeyboardButton('Old', callback_data='age_select_old')]
    ]

    character_race = context.user_data.get('race')
    race_data = race_info.get(character_race, {})

    character_ages = race_data.get("age", "No age avaliable")

    with open('media/stages/dnd_age.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    f"*Step 5: Choose Your Character’s Age*\n\nEvery adventurer has a story shaped by the years they’ve lived. Is your hero young and eager, wise and experienced, or somewhere in between? The age you choose can add depth to your character’s background and personality.\n\n*Young:* {character_ages[0]}\n*Mature:* {character_ages[1]}\n*Old:* {character_ages[2]}\n\nChoose your character’s age from the options below."
                )
            )
        )
    
    return AGE




# choosing / enter name 

async def character_name(update, context):
    logger.info('Name asked')

    query = update.callback_query
    await query.answer()

    character_age = query.data.replace('age_select_', '')
    context.user_data['age'] = character_age

    character_race = context.user_data.get("race")
    character_gender = context.user_data.get("gender") + '_names' # male_names / female_names
    character_names = race_info[character_race][character_gender]
    
    keyboard = build_inline_keyboard(character_names, character_names, row_width=3, callback_prefix='name_select_')

    with open('media/stages/dnd_name.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    "*Step 6: Select Or Enter Your Character`s Name.*\n\nThis is your chance to give your character an identity that will echo through legends and tales. Will it be a name of ancient power, a clever alias, or something entirely unique?\n\nChoose your character’s name below or enter the new that you prefer more. With this, your hero’s story truly begins!"
                )
            )
        )

    return NAME


async def character_surname(update, context):
    character_race = context.user_data.get("race")

    if character_race in ["tiefling", "half_orc"]:
        if update.callback_query:
            query = update.callback_query
            await query.answer()
            character_name = query.data.replace('name_select_', '')
            context.user_data['name'] = character_name
        elif update.message:
            context.user_data['name'] = update.message.text.strip()
        return await character_appearance(update, context)
    
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        character_name = query.data.replace('name_select_', '')
        context.user_data['name'] = character_name
    elif update.message:
        context.user_data['name'] = update.message.text.strip()
    
    character_surnames = race_info[character_race]["surnames"]
    keyboard = build_inline_keyboard(character_surnames, character_surnames, row_width=3, callback_prefix='surname_select_')
    
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_caption(
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown",
            caption=(
                "*Step 7: Select Or Enter Your Character's Surname.*\n\n"
                "This is your chance to give your character an identity that will echo through legends and tales. "
                "Will it be a surname of ancient power, a clever alias, or something entirely unique?\n\n"
                "Choose your character’s surname from below. With this, your hero’s story truly begins!"
            )
    )
    elif update.message:
        with open('media/stages/dnd_name.png', 'rb') as photo:
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=photo,
                caption="*Step 7: Select Or Enter Your Character's Surname.*\n\n"
                "This is your chance to give your character an identity that will echo through legends and tales. "
                "Will it be a surname of ancient power, a clever alias, or something entirely unique?\n\n"
                "Choose your character’s surname from below. With this, your hero’s story truly begins!",
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode="Markdown"
            )

    return SURNAME

# choosing character appearance

async def character_appearance(update, context):
    logger.info('Appearance asked')

    if update.callback_query:
        query = update.callback_query
        await query.answer()

        if 'name' in context.user_data:
            character_surname = query.data.replace('surname_select_', '')
            context.user_data['surname'] = character_surname
        else:
            character_name = query.data.replace('name_select_', '')
            context.user_data['name'] = character_name

        with open('media/stages/dnd_appearance.png', 'rb') as photo:
            await context.bot.edit_message_media(
                chat_id=query.message.chat.id,
                message_id=query.message.message_id,
                media=InputMediaPhoto(
                    media=photo,
                    parse_mode=ParseMode.MARKDOWN,
                    caption=(
                        "*Step 8: Describe Your Character’s Appearance*\n\nEvery hero stands out in their own way—through striking features, unique style, or the subtle marks of their adventures. Is your character tall and imposing, graceful and mysterious, or perhaps marked by an unusual scar or vibrant eyes?\n\nShare details about your character’s appearance below. This is your chance to paint a vivid picture and make your hero truly memorable!"
                    )
                )
            )
    elif update.message:

        if 'name' in context.user_data:
            character_surname = update.message.text.strip()
            context.user_data['surname'] = character_surname
        else:
            character_name = update.message.text.strip()
            context.user_data['name'] = character_name

        with open('media/stages/dnd_appearance.png', 'rb') as photo:
            await context.bot.send_photo(
                chat_id=update.message.chat.id,
                photo=photo,
                caption=(
                    "*Step 8: Describe Your Character’s Appearance*\n\nEvery hero stands out in their own way—through striking features, unique style, or the subtle marks of their adventures. Is your character tall and imposing, graceful and mysterious, or perhaps marked by an unusual scar or vibrant eyes?\n\nShare details about your character’s appearance below. This is your chance to paint a vivid picture and make your hero truly memorable!"
                ),
                parse_mode=ParseMode.MARKDOWN
            )

    return APPEARANCE


# choosing character worldview

async def character_worldview(update, context):
    logger.info('Worldview asked')

    character_worldviews = list(worldview_info.keys())
    character_worldview_titles = [worldview_info[character_worldview]["title"] for character_worldview in character_worldviews if character_worldview in worldview_info]

    keyboard = build_inline_keyboard(character_worldview_titles, character_worldviews, row_width=3, callback_prefix='worldview_menu_')

    if update.callback_query:
        query = update.callback_query
        await query.answer()
        character_appearance = query.data
        context.user_data['appearance'] = character_appearance

        with open('media/stages/dnd_worldview.png', 'rb') as photo:
            await context.bot.edit_message_media(
                chat_id=query.message.chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    parse_mode=ParseMode.MARKDOWN,
                    caption=(
                        "*Step 9: Select Your Character’s Worldview*\n\nEvery hero sees the world through their own lens—shaped by their beliefs, values, and sense of right and wrong. Is your character guided by honor and justice, or do they follow their own code? Are they a force for good, a champion of order, or a free spirit who values independence above all?\n\nChoose your character’s worldview below. This step helps shape their motivations and the choices they’ll make on their journey!"
                    )
                )
            ) 
    elif update.message:
        character_appearance = update.message.text
        context.user_data['appearance'] = character_appearance

        with open('media/stages/dnd_worldview.png', 'rb') as photo:
            await context.bot.send_photo(
                chat_id=update.message.chat.id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                photo=photo,
                caption=(
                    "*Step 9: Select Your Character’s Worldview*\n\nEvery hero sees the world through their own lens—shaped by their beliefs, values, and sense of right and wrong. Is your character guided by honor and justice, or do they follow their own code? Are they a force for good, a champion of order, or a free spirit who values independence above all?\n\nChoose your character’s worldview below. This step helps shape their motivations and the choices they’ll make on their journey!"
                ),
                parse_mode=ParseMode.MARKDOWN
            )

    return WORLDVIEW    


async def show_worldview_menu(update, context):
    query = update.callback_query
    await query.answer()

    character_worldview = query.data.replace('worldview_menu_', '')
    context.user_data["worldview"] = character_worldview

    worldview_data = worldview_info.get(character_worldview, {})
    worldview_title = worldview_data.get("title", "No title avaliable")
    worldview_description = worldview_data.get("description", "No description avaliable")

    keyboard = [
        [InlineKeyboardButton("Choose this", callback_data=f'worldview_select_{character_worldview}')], 
        [InlineKeyboardButton("Back", callback_data='worldview_back')]
    ]

    await update.callback_query.edit_message_caption(
            caption=f"*{worldview_title}*\n\n{worldview_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
    )


# character backstory 

async def character_backstory(update, context):
    logger.info('Backstory asked')

    query = update.callback_query
    await query.answer()

    character_backstories = list(backstory_info.keys())
    character_backstories_titles = [backstory_info[character_backstory]["title"] for character_backstory in character_backstories if character_backstory in backstory_info]

    keyboard = build_inline_keyboard(character_backstories_titles, character_backstories, row_width=3, callback_prefix='backstory_menu_')

    with open('media/stages/dnd_backstory.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    "*Step 10: Choose Your Character’s Backstory*\n\nEvery hero has a tale that shaped who they are—full of challenges, triumphs, and defining moments. What key events set your character on their path? Did they grow up among royalty or in humble beginnings? Were they marked by a great loss, a personal quest, or an unexpected adventure?\n\nShare your character’s backstory below. This is your chance to weave history, purpose, and personality into your hero, making them truly unique for the journeys ahead!"
                )
            )
        ) 

    return BACKSTORY


async def show_backstory_menu(update, context):
    query = update.callback_query
    await query.answer()

    character_backstory = query.data.replace('backstory_menu_', '')
    context.user_data["backstory"] = character_backstory

    backstory_data = backstory_info.get(character_backstory, {})
    backstory_title = backstory_data.get("title", "No title avaliable")
    backstory_description = backstory_data.get("description", "No description avaliable")
    image_path = backstory_data.get("image", None)

    keyboard = [
        [InlineKeyboardButton("Choose this", callback_data=f'backstory_select_{character_backstory}')], 
        [InlineKeyboardButton("Back", callback_data='backstory_back')]
    ]

    if image_path:
        with open(image_path, "rb") as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{backstory_title}*\n\n{backstory_description}",
                    parse_mode="Markdown"
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{character_class}*\n\n{backstory_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )



# character traits 

async def character_traits(update, context):
    logger.info('Traits asked')

    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get("backstory")
    character_trait_names = [trait["name"] for trait in backstory_info[character_backstory]["personality_traits"]]

    keyboard = build_inline_keyboard(character_trait_names, character_trait_names, row_width=3, callback_prefix='traits_menu_')

    with open('media/stages/dnd_traits.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    f"*Step 11: Select Your Character’s Traits*\n\nTraits give your hero personality and individuality, reflecting habits, quirks, or ideals that set them apart from others. Is your character brave or cautious, honest or cunning, cheerful or reserved? These small details can influence choices, friendships, and how your hero responds to the world.\n\nChoose or describe your character’s key traits below. This final touch adds depth and brings your hero’s story to life!"
                )
            )
        ) 

    return TRAITS

async def show_trait_menu(update, context):
    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get("backstory")
    backstory_data = backstory_info.get(character_backstory, {})
    character_trait = query.data.replace('traits_menu_', '')
    image_path = backstory_data.get("image", None)
    
    character_trait_description = next(
        trait["description"] for trait in backstory_info[character_backstory]["personality_traits"]
        if trait["name"] == character_trait
    )

    keyboard = [
        [InlineKeyboardButton("Choose this", callback_data=f'trait_select_{character_trait}')],
        [InlineKeyboardButton("back", callback_data='traits_back')]
    ]

    if image_path:
        with open(image_path, "rb") as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{character_trait}*\n\n{character_trait_description}",
                    parse_mode="Markdown"
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{character_trait}*\n\n{character_trait_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

# character ideals

async def character_ideals(update, context):
    logger.info('Ideals asked')

    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get("backstory")
    character_ideals_names = [ideal["name"] for ideal in backstory_info[character_backstory ]["ideals"]]

    keyboard = build_inline_keyboard(character_ideals_names, character_ideals_names, row_width=3, callback_prefix='ideals_menu_')

    with open('media/stages/dnd_ideals.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    f"*Step 12: Define Your Character’s Ideals*\n\nIdeals are the beliefs and guiding principles that shape your hero’s actions and decisions. Is your character driven by the pursuit of justice, loyalty to friends, a thirst for freedom, or the quest for knowledge? Their ideals reveal what truly matters most to them on their journey.\n\nDescribe your character’s core ideals below. These values will inspire your hero and guide them through every adventure!"
                )
            )
        ) 

    return IDEALS

async def show_ideal_menu(update, context):
    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get("backstory")
    backstory_data = backstory_info.get(character_backstory, {})
    character_ideal = query.data.replace('ideals_menu_', '')
    image_path = backstory_data.get("image", None)
    
    character_ideal_description = next(
        ideal["description"] for ideal in backstory_info[character_backstory]["ideals"]
        if ideal["name"] == character_ideal
    )

    keyboard = [
        [InlineKeyboardButton("Choose this", callback_data=f'ideal_select_{character_ideal}')],
        [InlineKeyboardButton("back", callback_data='ideals_back')]
    ]

    if image_path:
        with open(image_path, "rb") as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{character_ideal}*\n\n{character_ideal_description}",
                    parse_mode="Markdown"
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{character_ideal}*\n\n{character_ideal_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )





# character attachments

async def character_attachments(update, context):
    logger.info('Attachments asked')

    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get("backstory")
    character_attachments_names = [attachment["name"] for attachment in backstory_info[character_backstory]["attachments"]]

    keyboard = build_inline_keyboard(character_attachments_names, character_attachments_names, row_width=3, callback_prefix='attachments_menu_')

    with open('media/stages/dnd_attachments.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    f"*Step 13: Define Your Character’s Attachments*\n\nAdd depth to your hero by including meaningful attachments, such as personal items, heirlooms, or symbols of their journey. These objects can reflect your character’s history, beliefs, and values—perhaps a cherished locket, a battle-worn weapon, or a mysterious artifact.\n\nDescribe your character’s important attachments below. Each item helps build your hero’s story and connects them to the world in unique ways!"
                )
            )
        ) 

    return ATTACHMENTS

async def show_attachment_menu(update, context):
    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get("backstory")
    backstory_data = backstory_info.get(character_backstory, {})
    character_attachment = query.data.replace('attachments_menu_', '')
    image_path = backstory_data.get("image", None)
    
    character_attachment_description = next(
        attachment["description"] for attachment in backstory_info[character_backstory]["attachments"]
        if attachment["name"] == character_attachment
    )

    keyboard = [
        [InlineKeyboardButton("Choose this", callback_data=f'attachment_select_{character_attachment}')],
        [InlineKeyboardButton("back", callback_data='attachment_back')]
    ]

    if image_path:
        with open(image_path, "rb") as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{character_attachment}*\n\n{character_attachment_description}",
                    parse_mode="Markdown"
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{character_attachment}*\n\n{character_attachment_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )






# character weraknesses

async def character_weaknesses(update, context):
    logger.info('Weaknesses asked')

    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get("backstory")
    character_weaknesses_names = [weakness["name"] for weakness in backstory_info[character_backstory ]["weaknesses"]]

    keyboard = build_inline_keyboard(character_weaknesses_names, character_weaknesses_names, row_width=3, callback_prefix='weaknesses_menu_')

    with open('media/stages/dnd_weaknesses.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    f"*Step 14: Define Your Character’s Weaknesses*\n\nWeaknesses add depth and personality, making your character more relatable and their story more compelling. Are they impulsive or overly cautious? Do they struggle to trust, act on anger, or carry a hidden fear?\n\nDescribe your character’s weaknesses below. Embracing these imperfections will help bring your hero to life and open the door for personal growth and unforgettable adventures!"
                )
            )
        ) 

    return WEAKNESSES



async def show_weakness_menu(update, context):
    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get("backstory")
    backstory_data = backstory_info.get(character_backstory, {})
    character_weakness = query.data.replace('weaknesses_menu_', '')
    image_path = backstory_data.get("image", None)
    
    character_weakness_description = next(
        weakness["description"] for weakness in backstory_info[character_backstory]["weaknesses"]
        if weakness["name"] == character_weakness
    )

    keyboard = [
        [InlineKeyboardButton("Choose this", callback_data=f'weakness_select_{character_weakness}')],
        [InlineKeyboardButton("back", callback_data='weaknesses_back')]
    ]

    if image_path:
        with open(image_path, "rb") as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{character_weakness}*\n\n{character_weakness_description}",
                    parse_mode="Markdown"
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{character_weakness}*\n\n{character_weakness_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )





async def finish_creation(update, context):
    logger.info('Character created')

    query = update.callback_query
    await query.answer()
    character_backstory = query.data

    character_name = context.user_data['name'].replace('_', ' ')
    character_class = context.user_data['class'].replace('_', ' ')
    character_race = context.user_data['race'].replace('_', ' ')
    character_age = context.user_data['age'].replace('_', ' ')
    character_backstory = context.user_data['backstory'].replace('_', ' ')
    character_appearance = context.user_data['appearance'].replace('_', ' ')
    character_worldview = context.user_data['worldview'].replace('_', ' ')

    keyboard = [[InlineKeyboardButton("Restart", callback_data='start_button')]]

    with open('media/stages/dnd_start.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    f"Your new character for your lovely boardgame!\n\nName: {character_name}\nClass: {character_class}\nRace: {character_race}\nAge: {character_age}\nAppearance: {character_appearance}\nBackstory: {character_backstory}\nWorldview: {character_worldview}"
                )
            )
        ) 

    return ConversationHandler.END



async def cancel(update, context):
    logger.info('Character creation stopped')

    context.user_data.clear()

    keyboard = [[InlineKeyboardButton("Restart", callback_data='start_button')]]
    
    with open('media/stages/dnd_cancel.png', 'rb') as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="*Adventure paused!*\n\nYour character creation has been cancelled. Sometimes even the bravest heroes need a break or a fresh start. When you’re ready to return, simply begin again and craft a new legend for the world of *Dungeons & Dragons*.\n\nFeel free to explore, rest, or gather inspiration. When the call to adventure returns, I’ll be here to guide you every step of the way!\n\nWant to try again? Click the *“Restart”* button to begin anew.",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
    )

    return ConversationHandler.END





character_creation = ConversationHandler(
    entry_points=[CallbackQueryHandler(character_race, pattern='^start_button$')],
    states={
        RACE: [
            CallbackQueryHandler(show_race_menu, pattern=r'race_menu_.+$'),
            CallbackQueryHandler(character_race, pattern='^race_back$'),
            CallbackQueryHandler(show_race_more_info, pattern='^race_(info|features)$'),
            CallbackQueryHandler(show_race_menu, pattern='^race_menu_back$'),
            CallbackQueryHandler(character_class, pattern='^race_select$'),
        ],
        CLASS: [
            CallbackQueryHandler(show_class_menu, pattern=r'class_menu_.+$'),
            CallbackQueryHandler(character_class, pattern='^class_back$'),
            CallbackQueryHandler(show_class_more_info, pattern='^class_(info|features)$'),
            CallbackQueryHandler(show_race_menu, pattern='^class_menu_back$'),
            CallbackQueryHandler(character_gender, pattern='^class_select$')
        ],
        GENDER: [
            CallbackQueryHandler(character_size, pattern='^gender_select_(male|female)$')
        ],
        SIZE: [
            CallbackQueryHandler(character_age, pattern='^size_select_(small|medium|big)$')
        ],
        AGE: [
            CallbackQueryHandler(character_name, pattern='^age_select_(young|mature|old)$')
        ],
        NAME: [
            CallbackQueryHandler(character_surname, pattern=r'name_select_'), #handler works when it sees a part of callback
            MessageHandler(filters.TEXT & ~filters.COMMAND, character_surname),
        ],
        SURNAME: [
            CallbackQueryHandler(character_appearance, pattern=r'surname_select'),
            MessageHandler(filters.TEXT & ~filters.COMMAND, character_appearance),
        ],
        APPEARANCE: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, character_worldview)
        ],
        WORLDVIEW: [
            CallbackQueryHandler(character_backstory, pattern=r'^worldview_select_.+$'),
            CallbackQueryHandler(show_worldview_menu, pattern=r'^worldview_menu_'),
            CallbackQueryHandler(character_worldview, pattern='^worldview_back$')
        ],
        BACKSTORY: [
            CallbackQueryHandler(character_traits, pattern=r'backstory_select_.+$'),
            CallbackQueryHandler(show_backstory_menu, pattern=r'^backstory_menu_'),
            CallbackQueryHandler(character_backstory, pattern='^backstory_back$')
        ],
        TRAITS: [
            CallbackQueryHandler(character_ideals, pattern=r'trait_select_.+$'),
            CallbackQueryHandler(show_trait_menu, pattern=r'^traits_menu_'),
            CallbackQueryHandler(character_traits, pattern='^traits_back$')
        ],
        IDEALS: [
            CallbackQueryHandler(character_attachments, pattern=r'ideal_select_.+$'),
            CallbackQueryHandler(show_ideal_menu, pattern=r'^ideals_menu_'),
            CallbackQueryHandler(character_ideals, pattern='^ideals_back$')
        ],
        ATTACHMENTS: [
            CallbackQueryHandler(character_weaknesses, pattern=r'attachment_select_.+$'),
            CallbackQueryHandler(show_attachment_menu, pattern=r'^attachments_menu_'),
            CallbackQueryHandler(character_attachments, pattern='^attachments_back$')
        ],
        WEAKNESSES: [
            CallbackQueryHandler(finish_creation, pattern=r'weakness_select_.+$'),
            CallbackQueryHandler(show_weakness_menu, pattern=r'^weaknesses_menu_'),
            CallbackQueryHandler(character_weaknesses, pattern='^weaknesses_back$')
        ]
    }, 
    fallbacks=[CommandHandler('cancel', cancel)]
)


# async def character_level(update, context):

#     query = update.callback_query
#     await query.answer()
#     character_class = query.data

#     context.user_data['character_class'] = character_class

#     keyboard = [
#         [InlineKeyboardButton('level 1', callback_data='character_level_1'), InlineKeyboardButton('level 2', callback_data='character_level_2'), InlineKeyboardButton('level 3', callback_data='character_level_3')],
#         [InlineKeyboardButton('level 4', callback_data='character_level_4'), InlineKeyboardButton('level 5', callback_data='character_level_5'), InlineKeyboardButton('level 6', callback_data='character_level_6')],
#         [InlineKeyboardButton('level 7', callback_data='character_level_7'), InlineKeyboardButton('level 8', callback_data='character_level_8'), InlineKeyboardButton('level 9', callback_data='character_level_9')],
#         [InlineKeyboardButton('level 10', callback_data='character_level_10'), InlineKeyboardButton('level 11', callback_data='character_level_11'), InlineKeyboardButton('level 12', callback_data='character_level_12')],
#         [InlineKeyboardButton('level 13', callback_data='character_level_13'), InlineKeyboardButton('level 14', callback_data='character_level_14'), InlineKeyboardButton('level 15', callback_data='character_level_15')],
#         [InlineKeyboardButton('level 16', callback_data='character_level_16'), InlineKeyboardButton('level 17', callback_data='character_level_17'), InlineKeyboardButton('level 18', callback_data='character_level_18')],
#         [InlineKeyboardButton('level 19', callback_data='character_level_19'), InlineKeyboardButton('level 20', callback_data='character_level_20')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     with open('C:\Programming\PetProjects\DnD-character-maker\media\dnd_level.png', 'rb') as photo:
#         await context.bot.send_photo(
#             chat_id=update.effective_chat.id,
#             photo=photo,
#             caption='',
#             reply_markup=reply_markup
#         )

#     return LEVEL
