from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from .select_age import ask_age
from utils.logger import logger
from ..data import race_info
from .states import SIZE



async def ask_size(update, context):
    logger.info('Size asked')

    query = update.callback_query
    await query.answer()

    # creating and saving character`s gender
    character_gender = query.data.replace("gender_select_", "")
    context.user_data['gender'] = character_gender

    character_race = context.user_data.get('race')
    race_data = race_info.get(character_race, {})

    character_sizes = race_data.get('body_size', "No size available")
    character_size_small = character_sizes['small']
    character_size_medium = character_sizes['medium']
    character_size_big = character_sizes['big']

    keyboard = [
        [InlineKeyboardButton("Small", callback_data='size_select_small'), InlineKeyboardButton("Medium", callback_data='size_select_medium'), InlineKeyboardButton("Big", callback_data='size_select_big')]
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

size_handlers = [
    CallbackQueryHandler(ask_age, pattern='^size_select_(small|medium|big)$')
]