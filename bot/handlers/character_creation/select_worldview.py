from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from .select_backstory import character_backstory
from utils.logger import logger
from .utils import build_inline_keyboard
from ..data import worldview_info
from .states import WORLDVIEW

async def character_worldview(update, context):
    logger.info('Worldview asked')

    character_worldviews = list(worldview_info.keys())
    character_worldview_titles = [worldview_info[character_worldview]['title'] for character_worldview in character_worldviews if character_worldview in worldview_info]

    keyboard = build_inline_keyboard(character_worldview_titles, character_worldviews, row_width=3, callback_prefix='worldview_menu_')

    if update.callback_query:
        query = update.callback_query
        await query.answer()
        character_appearance = query.data
        context.user_data['appearance'] = character_appearance

        with open('media/stages/dnd_worldview.png', 'rb') as photo:
            await context.bot.edit_message_media(
                chat_id=query.message.chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    parse_mode=ParseMode.MARKDOWN,
                    caption=(
                        "*Step 9: Select Your Character’s Worldview*\n\nEvery hero sees the world through their own lens—shaped by their beliefs, values, and sense of right and wrong. Is your character guided by honor and justice, or do they follow their own code? Are they a force for good, a champion of order, or a free spirit who values independence above all?\n\nChoose your character’s worldview below. This step helps shape their motivations and the choices they’ll make on their journey!"
                    )
                )
            ) 
    elif update.message:
        character_appearance = update.message.text
        context.user_data['appearance'] = character_appearance

        with open('media/stages/dnd_worldview.png', 'rb') as photo:
            await context.bot.send_photo(
                chat_id=update.message.chat.id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                photo=photo,
                caption=(
                    "*Step 9: Select Your Character’s Worldview*\n\nEvery hero sees the world through their own lens—shaped by their beliefs, values, and sense of right and wrong. Is your character guided by honor and justice, or do they follow their own code? Are they a force for good, a champion of order, or a free spirit who values independence above all?\n\nChoose your character’s worldview below. This step helps shape their motivations and the choices they’ll make on their journey!"
                ),
                parse_mode=ParseMode.MARKDOWN
            )

    return WORLDVIEW    


async def show_worldview_menu(update, context):
    query = update.callback_query
    await query.answer()

    character_worldview = query.data.replace("worldview_menu_", "")
    context.user_data['worldview'] = character_worldview

    worldview_data = worldview_info.get(character_worldview, {})
    worldview_title = worldview_data.get('title', "No title avaliable")
    worldview_description = worldview_data.get('description', "No description avaliable")

    keyboard = [
        [InlineKeyboardButton("Choose this", callback_data=f'worldview_select_{character_worldview}')], 
        [InlineKeyboardButton("Back", callback_data='worldview_back')]
    ]

    await update.callback_query.edit_message_caption(
            caption=f"*{worldview_title}*\n\n{worldview_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
    )

worldview_handlers = [
    CallbackQueryHandler(character_backstory, pattern=r'^worldview_select_.+$'),
    CallbackQueryHandler(show_worldview_menu, pattern=r'^worldview_menu_'),
    CallbackQueryHandler(character_worldview, pattern='^worldview_back$')
]