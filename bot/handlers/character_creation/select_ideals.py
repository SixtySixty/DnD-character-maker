from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from .select_attachments import character_attachments
from utils.logger import logger
from .utils import build_inline_keyboard
from ..data import backstory_info
from .states import IDEALS

async def character_ideals(update, context):
    logger.info('Ideals asked')

    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get('backstory', "")
    character_ideals_names = [ideal['name'] for ideal in backstory_info[character_backstory ]['ideals']]

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

    character_backstory = context.user_data.get('backstory')
    backstory_data = backstory_info.get(character_backstory, {})
    character_ideal = query.data.replace('ideals_menu_', "")
    image_path = backstory_data.get('image', None)
    
    character_ideal_description = next(
        ideal['description'] for ideal in backstory_info[character_backstory]['ideals']
        if ideal['name'] == character_ideal
    )

    keyboard = [
        [InlineKeyboardButton("Choose this", callback_data=f'ideal_select_{character_ideal}')],
        [InlineKeyboardButton("Back", callback_data='ideals_back')]
    ]

    if image_path:
        with open(image_path, 'rb') as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{character_ideal}*\n\n{character_ideal_description}",
                    parse_mode='Markdown'
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{character_ideal}*\n\n{character_ideal_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )

ideals_handlers = [
    CallbackQueryHandler(character_attachments, pattern=r'ideal_select_.+$'),
    CallbackQueryHandler(show_ideal_menu, pattern=r'^ideals_menu_'),
    CallbackQueryHandler(character_ideals, pattern='^ideals_back$')
]