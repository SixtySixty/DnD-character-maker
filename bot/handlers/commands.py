from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.logger import logger

async def start_command(update, context):
    logger.info('Start command used by user')

    keyboard = [[InlineKeyboardButton("Continue", callback_data='start_button')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    with open('/project/workspace/media/dnd_white_logo.png', 'rb') as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="Greetings, adventurer!\n\nWelcome to the character creation bot for the Dungeons & Dragons tabletop game! Here, you can create a unique hero step by step, choose their race,     class, abilities, and even come up with an exciting backstory.\n\nReady to embark on a journey into a world of magic, mysteries, and great deeds? Just follow my prompts, and your character will be ready for any challenge!\n\nShall we begin? Click the button “Continue” to start",
            reply_markup=reply_markup
    )