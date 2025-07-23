from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler

# Импорт всех хендлеров этапов из файлов этого пакета
from .select_race import race_handlers, ask_race
from .select_class import class_handlers
from .select_gender import gender_handlers
from .select_size import size_handlers
from .select_age import age_handlers
from .select_name_surname import name_handlers, surname_handlers
from .select_appearance import appearance_handlers
from .select_worldview import worldview_handlers
from .select_backstory import backstory_handlers
from .select_traits import traits_handlers
from .select_ideals import ideals_handlers
from .select_attachments import attachments_handlers
from .select_weaknesses import weaknesses_handlers
from .select_language import language_handlers
from .cancel_creation import cancel_character_creation

from .states import RACE, CLASS, GENDER, SIZE, AGE, NAME, SURNAME, APPEARANCE, WORLDVIEW, BACKSTORY, TRAITS, IDEALS, ATTACHMENTS, WEAKNESSES, LANGUAGE

# RACE, CLASS, GENDER, SIZE, AGE, NAME, SURNAME, APPEARANCE, WORLDVIEW, TRAITS, IDEALS, ATTACHMENTS, WEAKNESSES, BACKSTORY, LANGUAGE = range(15)

handle_character_creation = ConversationHandler(
    entry_points=[CallbackQueryHandler(ask_race, pattern='^start_button$')],
    states={
        RACE: race_handlers,
        CLASS: class_handlers,
        GENDER: gender_handlers,
        SIZE: size_handlers,
        AGE: age_handlers,
        NAME: name_handlers,
        SURNAME: surname_handlers,
        APPEARANCE: appearance_handlers,
        WORLDVIEW: worldview_handlers,
        BACKSTORY: backstory_handlers,
        TRAITS: traits_handlers,
        IDEALS: ideals_handlers,
        ATTACHMENTS: attachments_handlers,
        WEAKNESSES: weaknesses_handlers,
        LANGUAGE: language_handlers,
    },
    fallbacks=[CommandHandler('cancel', cancel_character_creation)]
)
