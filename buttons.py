from telebot import types


def start_bot_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Tashkent_Namaz_time = types.KeyboardButton('🏙️ Tashkent')
    markup.add(Tashkent_Namaz_time)
    return markup


def remove_button():
    return types.ReplyKeyboardRemove()


def set_reminder():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes_button = types.KeyboardButton('✅ Yes')
    no_button = types.KeyboardButton('❌ No')
    markup.row(yes_button, no_button)
    return markup
