import sqlite3

connection = sqlite3.connect('Namaz_times.db')
sql = connection.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS my_namaz_times(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                day_number INTEGER NOT NULL,
                month_name TEXT NOT NULL,
                year TEXT NOT NULL,
                day_name TEXT NOT NULL,
                bomdod TEXT NOT NULL,
                sunrise_time TEXT NOT NULL,
                peshin TEXT NOT NULL,
                asr TEXT NOT NULL,
                shom TEXT NOT NULL,
                xufton TEXT NOT NULL)''')

connection.commit()
connection.close()


def add_day(namaz_times_data):
    connection = sqlite3.connect('Namaz_times.db')
    sql = connection.cursor()

    insert_day = sql.execute(
        'INSERT INTO my_namaz_times (user_id, day_number, month_name, year, day_name, bomdod, sunrise_time, peshin, '
        'asr, shom, xufton) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (namaz_times_data['user_id'],
                                                                     namaz_times_data['day_number'],
                                                                     namaz_times_data['month_name'],
                                                                     namaz_times_data['year'],
                                                                     namaz_times_data['day_name'],
                                                                     namaz_times_data['bomdod'],
                                                                     namaz_times_data['sunrise'],
                                                                     namaz_times_data['peshin'],
                                                                     namaz_times_data['asr'],
                                                                     namaz_times_data['shom'],
                                                                     namaz_times_data['xufton']))
    connection.commit()
    connection.close()
    return insert_day


def check_day(namaz_times_data):
    connection = sqlite3.connect('Namaz_times.db')
    sql = connection.cursor()

    check_day_if_it_exists = sql.execute('SELECT day_number, month_name, year from my_namaz_times WHERE user_id = ?',
                                         (namaz_times_data['user_id'],)).fetchone()
    connection.close()
    return check_day_if_it_exists if check_day_if_it_exists else None
