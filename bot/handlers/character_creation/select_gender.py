from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from .select_size import character_size
from utils.logger import logger
from .states import GENDER

async def character_gender(update, context):
    logger.info('Gender asked')

    query = update.callback_query
    await query.answer()

    keyboard = [[InlineKeyboardButton("Female", callback_data='gender_select_female'), InlineKeyboardButton("Male", callback_data='gender_select_male')]]
    

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

gender_handlers = [
    CallbackQueryHandler(character_size, pattern='^gender_select_(male|female)$')
]