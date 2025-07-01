from utils.logger import logger

async def start_command(update, context):
    logger.info('Start command used by user')
    await update.message.reply_text("Hello new user!")