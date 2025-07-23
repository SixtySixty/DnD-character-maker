from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from .select_ideals import ask_ideals
from utils.logger import logger
from .utils import build_inline_keyboard
from ..data import backstory_info
from .states import TRAITS


async def ask_traits(update, context):
    logger.info('Traits asked')

    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get('backstory', "")
    character_trait_names = [trait['name'] for trait in backstory_info[character_backstory]['personality_traits']]

    if 'extra_language' in backstory_info[character_backstory]:
        counter_extra_language = backstory_info[character_backstory]['extra_language']

        if 'counter_extra_language' in context.user_data:
            context.user_data['counter_extra_language'] += counter_extra_language
            logger.info(f'{counter_extra_language}')
        else:
            context.user_data['counter_extra_language'] = counter_extra_language
            logger.info(f'{counter_extra_language}')

    logger.info(f"Full counter: {context.user_data['counter_extra_language']}")

    keyboard = build_inline_keyboard(character_trait_names, character_trait_names, row_width=3, callback_prefix='traits_menu_')

    with open('media/stages/dnd_traits.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    f"*Step 11: Select Your Character’s Traits*\n\nTraits give your hero personality and individuality, reflecting habits, quirks, or ideals that set them apart from others. Is your character brave or cautious, honest or cunning, cheerful or reserved? These small details can influence choices, friendships, and how your hero responds to the world.\n\nChoose or describe your character’s key traits below. This final touch adds depth and brings your hero’s story to life!"
                )
            )
        ) 

    return TRAITS

async def show_trait_menu(update, context):
    query = update.callback_query
    await query.answer()

    character_backstory = context.user_data.get('backstory', "")
    backstory_data = backstory_info.get(character_backstory, {})
    character_trait = query.data.replace("traits_menu_", "")
    image_path = backstory_data.get('image', None)
    
    character_trait_description = next(
        trait['description'] for trait in backstory_info[character_backstory]['personality_traits']
        if trait['name'] == character_trait
    )

    keyboard = [
        [InlineKeyboardButton("Choose this", callback_data=f'trait_select_{character_trait}')],
        [InlineKeyboardButton("Back", callback_data='traits_back')]
    ]

    if image_path:
        with open(image_path, 'rb') as photo:
            await context.bot.edit_message_media(
                chat_id=update.effective_chat.id,
                message_id=query.message.message_id,
                reply_markup=InlineKeyboardMarkup(keyboard),
                media=InputMediaPhoto(
                    media=photo,
                    caption=f"*{character_trait}*\n\n{character_trait_description}",
                    parse_mode='Markdown'
                )
            )
    else:
        await query.edit_message_caption(
            caption=f"*{character_trait}*\n\n{character_trait_description}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )

traits_handlers = [
    CallbackQueryHandler(ask_ideals, pattern=r'trait_select_.+$'),
    CallbackQueryHandler(show_trait_menu, pattern=r'^traits_menu_'),
    CallbackQueryHandler(ask_traits, pattern='^traits_back$')
]