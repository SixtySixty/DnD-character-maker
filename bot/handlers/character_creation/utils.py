from telegram import InlineKeyboardButton
import re
import random



# creating inline keyboard

def build_inline_keyboard(items, values, row_width=2, callback_prefix=''):
    keyboard = []
    for i in range(0, len(items), row_width):
        row_items = items[i:i+row_width]
        row_values = values[i:i+row_width]
        row = [
            InlineKeyboardButton(
                text=text,
                callback_data=f'{callback_prefix}{value}'
            ) for text, value in zip(row_items, row_values)
        ]
        keyboard.append(row)
    return keyboard


#parser for callback_data

def escape_markdown(text):
    return re.sub(r'([*_`\[\]])', r'\\\1', str(text))


# giving a random number between two numbers

def random_number(min_value: int, max_value: int) -> int:
    return random.randint(min_value, max_value)