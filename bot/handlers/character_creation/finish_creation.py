from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ConversationHandler
from telegram.constants import ParseMode
from utils.logger import logger
from .utils import escape_markdown
from ..data import race_info, class_info, backstory_info, worldview_info




async def finish_character_creation(update, context):
    logger.info('Character created')

    query = update.callback_query
    await query.answer()
    character_backstory = query.data

    character_race = context.user_data['race']
    character_race_title = race_info[character_race]['title']

    character_class = context.user_data['class']
    character_class_title = class_info[character_class]['title']

    character_name = context.user_data['name']
    if 'surname' in context.user_data:
        character_surname = context.user_data['surname']
    else:
        character_surname = ''

    character_size = context.user_data['size']

    character_age = context.user_data['age']
    character_age_title = race_info[character_race]['age'][character_age]

    character_appearance = context.user_data['appearance']

    character_backstory = context.user_data['backstory']
    character_backstory_title = backstory_info[character_backstory]['title']

    character_worldview = context.user_data['worldview']
    character_worldview_title = worldview_info[character_worldview]['title']

    character_languages = context.user_data['languages']

    keyboard = [[InlineKeyboardButton("Restart", callback_data='start_button')]]

    with open('media/stages/dnd_start.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption = (
                    f"Your new character for your lovely boardgame!\n\n"
                    f"Name: {escape_markdown(character_name)} {escape_markdown(character_surname)}\n"
                    f"Class: {escape_markdown(character_class_title)}\n"
                    f"Race: {escape_markdown(character_race_title)}\n"
                    f"Age: {escape_markdown(character_age_title)}\n"
                    f"Size: {escape_markdown(character_size)}\n"
                    f"Appearance: {escape_markdown(character_appearance)}\n"
                    f"Backstory: {escape_markdown(character_backstory_title)}\n"
                    f"Worldview: {escape_markdown(character_worldview_title)}\n"
                    f"Counter extra language: {escape_markdown(character_languages)}"
                )
            )
        ) 

    return ConversationHandler.END