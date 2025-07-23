from telegram import InputMediaPhoto
from telegram.ext import MessageHandler, filters
from telegram.constants import ParseMode
from .select_worldview import ask_worldview
from utils.logger import logger
from .states import APPEARANCE

async def ask_appearance(update, context):
    logger.info('Appearance asked')

    if update.callback_query:
        query = update.callback_query
        await query.answer()

        if 'name' in context.user_data:
            if query.data == 'surname_skip':
                context.user_data['surname'] = "" 
            else:
                character_surname = query.data.replace("surname_select_", "")
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
            if query.data == 'surname_skip':
                context.user_data['surname'] = "" 
            else:
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


appearance_handlers = [
    MessageHandler(filters.TEXT & ~filters.COMMAND, ask_worldview)
]