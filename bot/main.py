from telegram.ext import ApplicationBuilder, CommandHandler

from .handlers import start_command
from config import TOKEN
from utils.logger import logger

if __name__ == '__main__':
    logger.info('Starting bot...')

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler(('start'), start_command))

    logger.info('Poiling')
    app.run_polling(poll_interval=3)
