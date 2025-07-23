from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import CallbackQueryHandler
from telegram.constants import ParseMode
from .finish_creation import finish_character_creation
from utils.logger import logger
from .utils import build_inline_keyboard
from .states import LANGUAGE

async def character_languages(update, context):
    logger.info('Asked language')

    query = update.callback_query
    await query.answer()

    dnd_languages = ["Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon"]

    counter_extra_languages = context.user_data.get('counter_extra_language', 0)
    character_languages = context.user_data.get('languages', [])

    current_character_languages = ""

    for i in range (0, len(character_languages)):
        current_character_languages += f"{i+1}) " + character_languages[i] + "\n" 
    
    keyboard = build_inline_keyboard(dnd_languages, dnd_languages, row_width=3, callback_prefix='language_select_')

    with open('media/stages/dnd_language.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    "*Step 15: Select Additional Language*\n\nA true adventurer often learns more than just the language of their homeland. Does your character speak the tongue of ancient dragons, trade in mysterious dialects, or share secret words with hidden allies? Additional languages can open new doors, forge alliances, and reveal secrets on your hero’s path.\n\n"
                    f"How many languages can you choose: {counter_extra_languages}\n\n"
                    f"Languages you already know:\n{current_character_languages}\n\n"
                    "Pick an extra language from the list below, or enter your own if you prefer. Each language you choose adds depth to your character’s story and connects them to the wider world of adventure!"
                )
            )
        )


    return LANGUAGE


async def checking_languages_selected(update, context):
    query = update.callback_query
    await query.answer()

    counter_extra_languages = context.user_data.get('counter_extra_language', 0)
    languages = context.user_data.get('languages', [])

    if query.data.startswith("language_select_"):
        character_selected_language = query.data.replace("language_select_", "")

        if character_selected_language not in languages:
            context.user_data['languages'].append(character_selected_language)
            counter_extra_languages -=1
            context.user_data['counter_extra_language'] = counter_extra_languages

            if counter_extra_languages == 0:
                return await finish_character_creation(update, context)

        else:
            return await character_language_error(update, context)

    return await character_languages(update, context)




async def character_language_error(update, context):
    logger.info('Error')

    query = update.callback_query
    await query.answer()

    keyboard = [[InlineKeyboardButton("Back", callback_data='languages_back')]]

    with open('media/stages/dnd_error.png', 'rb') as photo:
        await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
            media=InputMediaPhoto(
                media=photo,
                parse_mode=ParseMode.MARKDOWN,
                caption=(
                    "*Error: character`s language*\n\n"
                    "The error occurred because it seems you have selected a language for your character that has already been chosen.\n\n"
                    "Please return to the language selection step and pick a different language to continue creating your hero."
                )
            )
        )

    return LANGUAGE

language_handlers = [
    CallbackQueryHandler(checking_languages_selected, pattern=r'language_select_.+$'),
    CallbackQueryHandler(character_languages, pattern='^languages_back$')
]