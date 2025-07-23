from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from .select_weaknesses import ask_weaknesses
from utils.logger import logger
from .utils import build_inline_keyboard
from ..data import backstory_info
from .states import ATTACHMENTS

async def ask_attachments(update, context):
    logger.info('Attachments asked')

    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get('backstory', "")
    character_attachments_names = [attachment['name'] for attachment in backstory_info[character_backstory]['attachments']]

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

    character_backstory = context.user_data.get('backstory')
    backstory_data = backstory_info.get(character_backstory, {})
    character_attachment = query.data.replace('attachments_menu_', "")
    image_path = backstory_data.get('image', None)
    
    character_attachment_description = next(
        attachment['description'] for attachment in backstory_info[character_backstory]['attachments']
        if attachment['name'] == character_attachment
    )

    keyboard = [
        [InlineKeyboardButton("Choose this", callback_data=f'attachment_select_{character_attachment}')],
        [InlineKeyboardButton("Back", callback_data='attachment_back')]
    ]

    if image_path:
        with open(image_path, 'rb') as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{character_attachment}*\n\n{character_attachment_description}",
                    parse_mode='Markdown'
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{character_attachment}*\n\n{character_attachment_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )

attachments_handlers = [
    CallbackQueryHandler(ask_weaknesses, pattern=r'attachment_select_.+$'),
    CallbackQueryHandler(show_attachment_menu, pattern=r'^attachments_menu_'),
    CallbackQueryHandler(ask_attachments, pattern='^attachments_back$')
]