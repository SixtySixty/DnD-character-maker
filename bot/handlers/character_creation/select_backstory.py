from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from .select_traits import ask_traits
from utils.logger import logger
from .utils import build_inline_keyboard
from ..data import backstory_info
from .states import BACKSTORY


async def ask_backstory(update, context):
    logger.info('Backstory asked')

    query = update.callback_query
    await query.answer()

    character_backstories = list(backstory_info.keys())
    character_backstories_titles = [backstory_info[character_backstory]['title'] for character_backstory in character_backstories if character_backstory in backstory_info]

    keyboard = build_inline_keyboard(character_backstories_titles, character_backstories, row_width=3, callback_prefix='backstory_menu_')

    with open('media/stages/dnd_backstory.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    "*Step 10: Choose Your Character’s Backstory*\n\nEvery hero has a tale that shaped who they are—full of challenges, triumphs, and defining moments. What key events set your character on their path? Did they grow up among royalty or in humble beginnings? Were they marked by a great loss, a personal quest, or an unexpected adventure?\n\nShare your character’s backstory below. This is your chance to weave history, purpose, and personality into your hero, making them truly unique for the journeys ahead!"
                )
            )
        ) 

    return BACKSTORY


async def show_backstory_menu(update, context):
    query = update.callback_query
    await query.answer()

    character_backstory = query.data.replace("backstory_menu_", "")
    context.user_data['backstory'] = character_backstory

    backstory_data = backstory_info.get(character_backstory, {})
    backstory_title = backstory_data.get('title', "No title avaliable")
    backstory_description = backstory_data.get('description', "No description avaliable")
    image_path = backstory_data.get('image', None)

    keyboard = [
        [InlineKeyboardButton("Choose this", callback_data=f'backstory_select_{character_backstory}')], 
        [InlineKeyboardButton("Back", callback_data='backstory_back')]
    ]
 
    if image_path:
        with open(image_path, 'rb') as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{backstory_title}*\n\n{backstory_description}",
                    parse_mode='Markdown'
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{backstory_title}*\n\n{backstory_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )

backstory_handlers = [
    CallbackQueryHandler(ask_traits, pattern=r'backstory_select_.+$'),
    CallbackQueryHandler(show_backstory_menu, pattern=r'^backstory_menu_'),
    CallbackQueryHandler(ask_backstory, pattern='^backstory_back$')
]