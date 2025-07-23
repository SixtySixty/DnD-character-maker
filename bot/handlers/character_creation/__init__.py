from .character_creation import character_creation_handler

from .utils import build_inline_keyboard, escape_markdown

from .select_race import race_handlers, character_race
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
from .finish_creation import finish_character_creation
from .cancel_creation import cancel_character_creation

RACE, CLASS, GENDER, SIZE, AGE, NAME, SURNAME, APPEARANCE, WORLDVIEW, TRAITS, IDEALS, ATTACHMENTS, WEAKNESSES, BACKSTORY, LANGUAGE = range(15)

__all__ = [
    'character_creation_handler',
    'build_inline_keyboard',
    'escape_markdown',
    'race_handlers', 'character_race',
    'class_handlers', 'gender_handlers', 'size_handlers', 'age_handlers',
    'name_handlers', 'surname_handlers', 'appearance_handlers',
    'worldview_handlers', 'backstory_handlers', 'traits_handlers',
    'ideals_handlers', 'attachments_handlers', 'weaknesses_handlers',
    'language_handlers', 'finish_character_creation', 'cancel_character_creation',
    'RACE', 'CLASS', 'GENDER', 'SIZE', 'AGE', 'NAME', 'SURNAME', 'APPEARANCE',
    'WORLDVIEW', 'TRAITS', 'IDEALS', 'ATTACHMENTS', 'WEAKNESSES', 'BACKSTORY', 'LANGUAGE'
]
