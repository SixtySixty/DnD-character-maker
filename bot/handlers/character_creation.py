from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from utils.logger import logger

NAME, CLASS = range(2)

async def start_character_creation(update, context):
    await update.effective_message.reply_text("What's the new name of your character? Please enter it below")
    logger.info('Name asked')
    return NAME

async def character_class(update, context):
    context.user_data['character_name'] = update.message.text
    await update.message.reply_text("What's the class of your new character? Please enter it below")
    logger.info('Class asked')
    return CLASS

async def finish_creation(update, context):
    context.user_data['character_class'] = update.message.text
    character_name = context.user_data['character_name']
    character_class = context.user_data['character_class']
    await update.message.reply_text(f"Character {character_name} class {character_class} successfully created!")
    logger.info('Character created')
    return ConversationHandler.END

async def cancel(update, context):
    await update.message.reply_text("Creation of character stopped")
    logger.info('Character creation stopped')
    return ConversationHandler.END

character_creation = ConversationHandler(
    entry_points=[CallbackQueryHandler(start_character_creation, pattern='^start_button$')],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, character_class)],
        CLASS: [MessageHandler(filters.TEXT & ~filters.COMMAND, finish_creation)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)
