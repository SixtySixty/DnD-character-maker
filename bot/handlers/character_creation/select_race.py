from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from utils.logger import logger
from .utils import build_inline_keyboard
from ..data import race_info
from .states import RACE

async def character_race(update, context):
    logger.info('Race asked')

    # getting data to create buttons in inline keyboard
    races = list(race_info.keys())
    races_titles = [race_info[race]['title'] for race in races if race in race_info] 

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
        character_race = context.user_data.get('race', "")
        languages = context.user_data.get('languages', [])
    elif query.data.startswith("race_menu_"):
        character_race = query.data.replace("race_menu_", "")
        context.user_data['race'] = character_race

        languages = race_info[character_race]['language']
        context.user_data['languages'] = languages

        if 'extra_language' in race_info[character_race]:
            counter_extra_language = race_info[character_race]['extra_language']
            context.user_data['counter_extra_language'] = counter_extra_language

            logger.info(f'{counter_extra_language}')


    logger.info(f'{character_race}')

    logger.info(f'{languages}')

    # getting data to show race info
    race_data = race_info.get(character_race, {})
    race_title = race_data.get('title', "No title available.")
    race_description = race_data.get('description', "No description available.")
    image_path = race_data.get('image', None)

    # creating inlinekeyboard
    keyboard = [
        [InlineKeyboardButton("More info", callback_data='race_info'),
         InlineKeyboardButton("Features", callback_data='race_features')],
        [InlineKeyboardButton("Choose", callback_data='race_select')],
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
                    parse_mode='Markdown'
                )
            )
    else:
        await update.callback_query.edit_message_caption(
            caption=f"*{race_title}*\n\n{race_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )

    return RACE



async def show_race_more_info(update, context):
    query = update.callback_query
    await query.answer()    

    character_race = context.user_data.get('race', '')

    race_data = race_info.get(character_race, {})

    if query.data.startswith("race_info"):
        title = "More info"
        text = race_data.get('detailed_description', "No description available.")
    elif query.data.startswith("race_features"):
        title = "Features"
        text = race_data.get('features', "No features available.")
    else:
        character_race = None
        title = "Info"
        text = "No info available."

    race_title = race_data.get('title', "No title available.")

    keyboard = [[InlineKeyboardButton("Back", callback_data=f'race_menu_back')]]

    await query.edit_message_caption(
        caption=f"*{race_title} — {title}*\n\n{text}",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

    return RACE

from .select_class import character_class

race_handlers = [
    CallbackQueryHandler(show_race_menu, pattern=r'race_menu_.+$'),
    CallbackQueryHandler(character_race, pattern='^race_back$'),
    CallbackQueryHandler(show_race_more_info, pattern='^race_(info|features)$'),
    CallbackQueryHandler(show_race_menu, pattern='^race_menu_back$'),
    CallbackQueryHandler(character_class, pattern='^race_select$'),
] 