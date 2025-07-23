from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from .select_language import handle_language_selection
from utils.logger import logger
from .utils import build_inline_keyboard
from ..data import backstory_info
from .states import WEAKNESSES

async def ask_weaknesses(update, context):
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
        [InlineKeyboardButton("Back", callback_data='weaknesses_back')]
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

weaknesses_handlers = [
    CallbackQueryHandler(handle_language_selection, pattern=r'weakness_select_.+$'),
    CallbackQueryHandler(show_weakness_menu, pattern=r'^weaknesses_menu_'),
    CallbackQueryHandler(ask_weaknesses, pattern='^weaknesses_back$')
]
