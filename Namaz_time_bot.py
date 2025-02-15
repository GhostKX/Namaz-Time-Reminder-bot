# Namaz Time Reminder bot


import telebot
import buttons
from datetime import datetime
import random
import requests
from bs4 import BeautifulSoup
import schedule
import database
import threading
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()
API_KEY = str(os.getenv('API_KEY'))
bot = telebot.TeleBot(API_KEY)

namaz_times_data = {}


# Message handler to start the bot
@bot.message_handler(commands=['start'])
def start_bot(message):
    user_id = message.from_user.id
    bot.send_message(user_id, '✨ Welcome to the Namaz time reminder bot ✨',
                     reply_markup=buttons.start_bot_buttons())
    bot.register_next_step_handler(message, tashkent_city)


def tashkent_city(message):
    user_id = message.from_user.id
    if message.text == '🏙️ Tashkent':
        bot.send_message(user_id, 'Loading the data 🔎 ...', reply_markup=buttons.remove_button())
        show_all_namaz_times(message)
    else:
        bot.send_message(user_id, '❌ Error. Invalid symbols ❌'
                                  '\n\n⬇️ Please use buttons below ⬇️', reply_markup=buttons.start_bot_buttons())
        bot.register_next_step_handler(message, tashkent_city)


def show_all_namaz_times(message):
    user_id = message.from_user.id
    today_date = datetime.today()
    day_number = today_date.day
    month_name = today_date.strftime('%B')
    year = today_date.strftime('%Y')
    formatted_day = datetime.strftime(today_date, '%d of %B, %Y')
    day_name = today_date.strftime('%A')

    namaz_times_data = {'user_id': int(user_id), 'day_number': day_number, 'month_name': month_name, 'day_name': day_name,
                        'year': year}
    print(namaz_times_data)

    url = 'https://islom.uz/vaqtlar/27/11'

    user_agents = [
        # Chrome on Windows
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 '
        'Safari/537.36',

        # Firefox on Windows
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',

        # Safari on macOS
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 '
        'Safari/605.1.15',

        # Edge on Windows
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 '
        'Safari/537.36 Edg/90.0.818.49',

        # Chrome on Android
        'Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 '
        'Mobile Safari/537.36',

        # Safari on iPhone
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
        'Version/14.1.1 Mobile/15E148 Safari/604.1',

        # Firefox on macOS
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0',

        # Opera on Windows
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 '
        'Safari/537.36 OPR/62.0.3331.72',

        # Chrome on Linux
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36',

        # Edge on macOS
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 '
        'Safari/537.36 Edg/91.0.864.37'
    ]

    headers = {'User-Agent': random.choice(user_agents)}
    namaz_data = requests.get(url, headers=headers)

    if namaz_data.status_code == 200:
        soup = BeautifulSoup(namaz_data.text, 'html.parser')
        table = soup.find('table', {'class': 'table table-bordered prayer_table'})
        tbody = table.find('tbody')
        namaz_time = tbody.find_all('tr')
        namaz_time_today_date = namaz_time[day_number - 1]
        namaz_time_today_date = namaz_time_today_date.find_all('td')
        bomdod_vaxti = namaz_time_today_date[3].text.strip()
        quyosh_chiqish = namaz_time_today_date[4].text.strip()
        peshin_vaxti = namaz_time_today_date[5].text.strip()
        asr_vaxti = namaz_time_today_date[6].text.strip()
        shom_vaxti = namaz_time_today_date[7].text.strip()
        xufton_vaxti = namaz_time_today_date[8].text.strip()

        namaz_times_data['bomdod'] = bomdod_vaxti
        namaz_times_data['sunrise'] = quyosh_chiqish
        namaz_times_data['peshin'] = peshin_vaxti
        namaz_times_data['asr'] = asr_vaxti
        namaz_times_data['shom'] = shom_vaxti
        namaz_times_data['xufton'] = xufton_vaxti
        print(namaz_times_data)

        bot.send_message(user_id, f'\n\n{'*' * 29}'
                                  f'\n\n         {formatted_day}'
                                  f'\n\n{'*' * 29}'
                                  f'\n\n                 {day_name}'
                                  f'\n{'_' * 25}'
                                  f'\n\n⏰ Bomdod: {bomdod_vaxti}'
                                  f'\n\n☀️ Sunrise: {quyosh_chiqish}'
                                  f'\n\n🕰️ Peshin: {peshin_vaxti}'
                                  f'\n\n⌚️ Asr: {asr_vaxti}'
                                  f'\n\n🕰️ Shom: {shom_vaxti}'
                                  f'\n\n⌚️ Xufton: {xufton_vaxti}'
                                  f'\n{'_' * 25}', reply_markup=buttons.set_reminder())
        if database.check_day(namaz_times_data) is None:
            database.add_day(namaz_times_data)
        else:
            pass
        bot.register_next_step_handler(message, set_reminder)

    else:
        bot.send_message(user_id, '❌ Error.  Could not retrieve data❌'
                                  '\n\nPlease try again later 💬', reply_markup=buttons.start_bot_buttons())
        bot.register_next_step_handler(message, tashkent_city)


sent_reminders = set()


def set_reminder(message):
    user_id = message.from_user.id
    if message.text == '✅ Yes':
        now = datetime.today().strftime('%H:%M')
        for prayer_name, reminder_time in namaz_times_data.items():
            if now == reminder_time and reminder_time not in sent_reminders:
                schedule.every().day.at(reminder_time).do(send_reminder, user_id, prayer_name, reminder_time)
        bot.send_message(user_id, '✅ Reminder is set successfully! ✅',
                         reply_markup=buttons.start_bot_buttons())
        bot.register_next_step_handler(message, tashkent_city)
    elif message.text == '❌ No':
        bot.send_message(user_id, '❗️ Reminder is not set ❗️', reply_markup=buttons.start_bot_buttons())
        bot.register_next_step_handler(message, start_bot)
    else:
        bot.send_message(user_id, '❌ Error. Invalid symbols ❌'
                                  '\n\n⬇️ Please use buttons below ⬇️', reply_markup=buttons.set_reminder())
        bot.register_next_step_handler(message, set_reminder)


def send_reminder(user_id, prayer_name, reminder_time):
    bot.send_message(user_id, f'🤲🏻 It is prayer time brother 🤲🏻'
                              f'\n\nIt is {prayer_name} Namaz time ({reminder_time})',
                     reply_markup=buttons.start_bot_buttons())
    sent_reminders.add(reminder_time)


# Running the bot infinitely
bot.polling(non_stop=True)
