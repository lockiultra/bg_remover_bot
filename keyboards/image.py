from aiogram import types


def get_mode_choose_keyboard():
    kb = [
        [types.KeyboardButton(text='Однотонный фон')],
        [types.KeyboardButton(text='Своя картинка')]
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)

    return keyboard
