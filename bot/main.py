from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from .handlers import start_command, character_creation
from config import TOKEN
from utils.logger import logger

async def handle_button(update, context):
        query = update.callback_query
        await query.answer()

if __name__ == '__main__':
    logger.info('Starting bot...')

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    
    app.add_handler(character_creation)

    logger.info('Poiling')
    app.run_polling(poll_interval=3)