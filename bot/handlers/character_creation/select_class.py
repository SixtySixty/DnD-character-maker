from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from utils.logger import logger
from .utils import build_inline_keyboard
from ..data import class_info
from .states import CLASS

async def character_class(update, context):
    logger.info('Class asked')

    query = update.callback_query
    await query.answer()

    logger.info(f"Callback data received: {query.data}")

    character_classes = list(class_info.keys())
    character_classes_titles = [class_info[character_class]['title'] for character_class in character_classes if character_class in class_info]

    logger.info(character_classes_titles)
    logger.info(character_classes)

    keyboard = build_inline_keyboard(character_classes_titles, character_classes, row_width=3, callback_prefix='class_menu_')

    with open('media/stages/dnd_class.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    "*Step 2: Select Your Character’s Class*\n\n"
                    "A character’s class determines their skills, strengths, and the role they play in the party. "
                    "Will you wield powerful magic as a Wizard, sneak through the shadows as a Thief, or charge into battle as a Barbarian?\n\n"
                    "Choose your class from the options below. This is the heart of your hero’s abilities!"
                )
            )
        )
        
    return CLASS


async def show_class_menu(update, context):
    query = update.callback_query
    await query.answer()

    logger.info(f"Callback data received: {query.data}")

    if query.data.startswith("class_menu_back"):
        character_class = context.user_data.get('class', "")
    elif query.data.startswith("class_menu"):
        character_class = query.data.replace("class_menu_", "")
        context.user_data['class'] = character_class

    logger.info(f'{character_class}')

    class_data = class_info.get(character_class, {})
    class_title = class_data.get('title', "No title available.")
    class_description = class_data.get('description', "No description available.")
    image_path = class_data.get('image', None)
    
    keyboard = [
        [InlineKeyboardButton("More info", callback_data='class_info'),
         InlineKeyboardButton("Features", callback_data='class_features')],
        [InlineKeyboardButton("Choose this", callback_data='class_select')],
        [InlineKeyboardButton("Back", callback_data='class_back')]
    ]

    if image_path:
        with open(image_path, "rb") as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{class_title}*\n\n{class_description}",
                    parse_mode='Markdown'
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{character_class}*\n\n{class_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    return CLASS
        

async def show_class_more_info(update, context):
    query = update.callback_query
    await query.answer()

    logger.info(f"Callback data received: {query.data}")

    character_class = context.user_data.get('class', "")

    class_data = class_info.get(character_class, {})

    if query.data.startswith("class_info"):
        title = "More info"
        text = class_data.get('detailed_description', "No description available.")
    elif query.data.startswith("class_features"):
        title = "Features"
        text = class_data.get('features', "No features available.")
    else:
        character_class = None
        title = "Info"
        text = "No info available."

    class_title = class_data.get('title', character_class)

    keyboard = [[InlineKeyboardButton('Back', callback_data='class_menu_back')]]

    await query.edit_message_caption(
        caption=f"*{class_title} — {title}*\n\n{text}",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

    return CLASS

from .select_gender import character_gender

class_handlers = [
    CallbackQueryHandler(show_class_menu, pattern=r'^class_menu_.+$'),
    CallbackQueryHandler(character_class, pattern='^class_back$'),
    CallbackQueryHandler(show_class_more_info, pattern='^class_(info|features)$'),
    CallbackQueryHandler(show_class_menu, pattern='^class_menu_back$'),
    CallbackQueryHandler(character_gender, pattern='^class_select$')
]
