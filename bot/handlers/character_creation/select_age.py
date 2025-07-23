from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from .select_name_surname import character_name
from utils.logger import logger
from ..data import race_info
from .states import AGE


async def character_age(update, context):
    logger.info('Age asked')

    query = update.callback_query
    await query.answer()

    # creating and saving character`s size
    character_size = query.data.replace("size_select_", "")
    context.user_data["size"] = character_size

    keyboard = [
        [InlineKeyboardButton("Young", callback_data='age_select_young'), InlineKeyboardButton("Mature", callback_data='age_select_mature'), InlineKeyboardButton("Old", callback_data='age_select_old')]
    ]

    character_race = context.user_data.get('race', "")
    race_data = race_info.get(character_race, {})

    character_ages = race_data.get('age', "No age avaliable")

    with open('media/stages/dnd_age.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    f"*Step 5: Choose Your Character’s Age*\n\nEvery adventurer has a story shaped by the years they’ve lived. Is your hero young and eager, wise and experienced, or somewhere in between? The age you choose can add depth to your character’s background and personality.\n\n*Young:* {character_ages['young']}\n*Mature:* {character_ages['mature']}\n*Old:* {character_ages['old']}\n\nChoose your character’s age from the options below."
                )
            )
        )
    
    return AGE

age_handlers = [
    CallbackQueryHandler(character_name, pattern='^age_select_(young|mature|old)$')
]