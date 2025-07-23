from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler, MessageHandler, filters
from telegram.constants import ParseMode
from .select_appearance import ask_appearance
from utils.logger import logger
from .utils import build_inline_keyboard
from ..data import race_info
from .states import NAME, SURNAME

# choosing / enter name 

async def ask_name(update, context):
    logger.info('Name asked')

    query = update.callback_query
    await query.answer()

    character_age = query.data.replace("age_select_", "")
    context.user_data['age'] = character_age

    character_race = context.user_data.get('race')
    character_gender = context.user_data.get('gender') + "_names" # male_names / female_names
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


async def ask_surname(update, context):
    logger.info('Surname asked')

    character_race = context.user_data.get('race', "")

    if character_race in ["tiefling", "half_orc"]:
        if update.callback_query:
            query = update.callback_query
            await query.answer()
            character_name = query.data.replace("name_select_", "")
            context.user_data['name'] = character_name
        elif update.message:
            context.user_data['name'] = update.message.text.strip()
        return await ask_appearance(update, context)
    
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        character_name = query.data.replace("name_select_", "")
        context.user_data['name'] = character_name
    elif update.message:
        context.user_data['name'] = update.message.text.strip()
    
    character_surnames = race_info[character_race]['surnames']
    keyboard = build_inline_keyboard(character_surnames, character_surnames, row_width=3, callback_prefix='surname_select_')

    keyboard.append([InlineKeyboardButton("Skip", callback_data='surname_skip')])
    # keyboard.append([InlineKeyboardButton("Back", callback_data='')])
    
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_caption(
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown',
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
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='Markdown',
                caption="*Step 7: Select Or Enter Your Character's Surname.*\n\n"
                "This is your chance to give your character an identity that will echo through legends and tales. "
                "Will it be a surname of ancient power, a clever alias, or something entirely unique?\n\n"
                "Choose your character’s surname from below. With this, your hero’s story truly begins!",
            )

    return SURNAME


name_handlers = [
    CallbackQueryHandler(ask_surname, pattern=r'name_select_'),
    MessageHandler(filters.TEXT & ~filters.COMMAND, ask_surname),
]


surname_handlers = [
    CallbackQueryHandler(ask_appearance, pattern=r'surname_select'),
    CallbackQueryHandler(ask_appearance, pattern='^surname_skip$'),
    MessageHandler(filters.TEXT & ~filters.COMMAND, ask_appearance),
]

