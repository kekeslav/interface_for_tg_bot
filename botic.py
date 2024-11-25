# Подключаем модуль случайных чисел
import random
import sqlite3
import telebot
import requests
from telebot import types

# подключение к бд
conn = sqlite3.connect("D:/bazz.db", check_same_thread=False)
cur = conn.cursor()
# Подключаем модуль для Телеграма

# Импортируем типы из модуля, чтобы создавать кнопки


# Указываем токен
bot = telebot.TeleBot('6760726195:AAGp7yOvkUmAJHPaMPNqzoRKYS_xSbI-k2U')


@bot.message_handler(commands=['start', 'help'])
def commands(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Gosling? Для продолжения напиши 'Привет'.")

    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Пока я понимаю только 'Привет' и тык по экрану.")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
   keyboard = types.InlineKeyboardMarkup(row_width=2)
   # Если написали «Привет»
   # По очереди готовим текст и обработчик
   key_who = types.InlineKeyboardButton(text='Хто такой етот Гослинг?', callback_data='who_gosling_butt')
   key_where = types.InlineKeyboardButton(text='А где этот Гослинг?', callback_data="how_films_gosling_butt")
   key_how_films = types.InlineKeyboardButton(text='Что посмотрим с ним?', callback_data="films_gosling_butt")
   keyboard.add(key_where, key_who, key_how_films)
   if message.text == 'Привет':
      # Показываем все кнопки сразу и пишем сообщение о выборе
      bot.send_message(message.from_user.id, text='Поговорим о Гослинге?', reply_markup=keyboard)
   else:
      bot.reply_to(message, text='Ето ты зачем написал? Гляшь шо я понимаю с помощью /help')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "who_gosling_butt":
        msg = 'Канадский киноактер и певец'
        link = 'https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%81%D0%BB%D0%B8%D0%BD%D0%B3,' \
               '_%D0%A0%D0%B0%D0%B9%D0%B0%D0%BD '
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, f"<a href=\"{link}\">{msg}</a>", parse_mode='HTML')
    elif call.data == "how_films_gosling_butt":
        msg = 'Он снялся в 122 фильмах.'
        link = "https://kino.mail.ru/person/454079_ryan_gosling/movies/"
        bot.send_message(call.message.chat.id, f"<a href=\"{link}\">{msg}</a>", parse_mode='HTML')
    elif call.data == "films_gosling_butt":
        cur.execute('Select Name from Films')
        films = list()
        while True:
            next_row =cur.fetchmany()
            if next_row:
                films.append(next_row)
            else:break
        bot.send_message(call.message.chat.id, random.choice(films))

        # крч надо подумать, что  еще можно сделать с этой апи и запихнуть в отедльную функцию
        # мб сделать вводе актера и как тут, инфа про него, рандомный фильм с ним мб еще
        # мб упороться и сделать интелектуального бота который будет подбирать фильм по определеным парамерам которые сам вычислит из беседы
        # прям как Лиманова показывала с винами только с фильмами
        # также с фактами можно найти через api и выдавать рандомные

        #headers = {
        #    'accept': 'application/json',
        #    'X-API-KEY': '52HVSKP-XH44BNQ-QETHPER-67W3NZV'
        #           }
        #url ='https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&selectFields=alternativeName&type=&persons.id=10143&persons.enProfession=actor'
        #r = requests.get(url, headers=headers)
        #print(r.json())
        #data = r.json()
        #alternative_names = [doc['alternativeName'] for doc in data['docs']]

        #for name in alternative_names:
        #    cur.execute('INSERT INTO Films (Name) VALUES (?)', (name,))

        # Сохраняем изменения
        #conn.commit()

        # Закрываем соединение
        #conn.close()



# Запускаем постоянный опрос бота в Телеграме
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)

