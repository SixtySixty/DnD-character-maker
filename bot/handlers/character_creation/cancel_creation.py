from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ConversationHandler
from utils.logger import logger

async def cancel_character_creation(update, context):
    logger.info('Character creation stopped')

    context.user_data.clear()

    keyboard = [[InlineKeyboardButton("Restart", callback_data='start_button')]]
    
    with open('media/stages/dnd_cancel.png', 'rb') as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="*Adventure paused!*\n\nYour character creation has been cancelled. Sometimes even the bravest heroes need a break or a fresh start. When you’re ready to return, simply begin again and craft a new legend for the world of *Dungeons & Dragons*.\n\nFeel free to explore, rest, or gather inspiration. When the call to adventure returns, I’ll be here to guide you every step of the way!\n\nWant to try again? Click the *“Restart”* button to begin anew.",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
    )

    return ConversationHandler.END
