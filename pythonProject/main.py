import telebot
from telebot import types
TOKEN = '5393037685:AAHrkARJZsRCsIz1imiSD-tRCTjQo-5W3pE'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    iteam1 = types.KeyboardButton('Город проживания')
    markup.add(iteam1)
    bot.send_message(message.chat.id, 'Привет!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Город проживания':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            iteam1 = types.KeyboardButton('Новосибирск')
            iteam2 = types.KeyboardButton('Томск')
            iteam3 = types.KeyboardButton('Пермь')
            iteam4 = types.KeyboardButton('Красноярск')
            back = types.KeyboardButton('Назад')
            markup.add(iteam1, iteam2, iteam3, iteam4, back)
            bot.send_message(message.chat.id, 'Город проживания', reply_markup = markup)
    if message.text == 'Новосибирск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        iteam1 = types.KeyboardButton('Качество жизни в городе Новосибирск')
        iteam2 = types.KeyboardButton('Преступность в городе Новосибирск')
        iteam3 = types.KeyboardButton('Здравоохранение в городе Новосибирск')
        iteam4 = types.KeyboardButton('Аренда в городе Новосибирск')
        back = types.KeyboardButton('Назад')
        markup.add(iteam1, iteam2, iteam3, iteam4, back)
        bot.send_message(message.chat.id, 'Новосибирск', reply_markup=markup)
    if message.text == 'Качество жизни в городе Новосибирск':
        bot.send_message(message.chat.id, 'Индекс качества жизни: 77.94 из 240 - Очень низкий')
    if message.text == 'Преступность в городе Новосибирск':
        bot.send_message(message.chat.id, 'Уровень преступности в Новосибирске: 47.55 из 120 - Умеренная')
    if message.text == 'Здравоохранение в городе Новосибирск':
        bot.send_message(message.chat.id, 'Уровень здравоохранение в Новосибирске: 56.1 из 100 - Умеренная')
    if message.text == 'Аренда в городе Новосибирск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        iteam1 = types.KeyboardButton('1 спальная в городе Новосибирск')
        iteam2 = types.KeyboardButton('3 спальная в городе Новосибирск')
        back = types.KeyboardButton('Назад')
        markup.add(iteam1, iteam2, back)
        bot.send_message(message.chat.id, 'Аренда в городе Новосибирск', reply_markup=markup)
    if message.text == '1 спальная в городе Новосибирск':
        bot.send_message(message.chat.id, 'Стоимость 1 спальной квартиры в Новосибирске состовляет 20000 рублей ')
    if message.text == '3 спальная в городе Новосибирск':
        bot.send_message(message.chat.id, 'Стоимость 3 спальной квартиры в Новосибирске состовляет 50000 рублей ')




    if message.text == 'Томск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        iteam1 = types.KeyboardButton('Качество жизни в городе Томск')
        iteam2 = types.KeyboardButton('Преступность в городе Томск')
        iteam3 = types.KeyboardButton('Здравоохранение в городе Томск')
        iteam4 = types.KeyboardButton('Аренда в городе Томск')
        back = types.KeyboardButton('Назад')
        markup.add(iteam1, iteam2, iteam3, iteam4, back)
        bot.send_message(message.chat.id, 'Томск', reply_markup=markup)
    if message.text == 'Качество жизни в городе Томск':
        bot.send_message(message.chat.id, 'Индекс качества жизни: 106.15 из 240 - Умеренный')
    if message.text == 'Преступность в городе Томск':
        bot.send_message(message.chat.id, 'Уровень преступности в Томске: 41.86 из 120 - Умеренная')
    if message.text == 'Здравоохранение в городе Томск':
        bot.send_message(message.chat.id, 'Уровень здравоохранение в Томске: 62.19 из 100 - Умеренная')
    if message.text == 'Аренда в городе Томск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        iteam1 = types.KeyboardButton('1 спальная в городе Томск')
        iteam2 = types.KeyboardButton('3 спальная в городе Томск')
        back = types.KeyboardButton('Назад')
        markup.add(iteam1, iteam2, back)
        bot.send_message(message.chat.id, 'Аренда в городе Томск', reply_markup=markup)
    if message.text == '1 спальная в городе Томск':
        bot.send_message(message.chat.id, 'Стоимость 1 спальной квартиры в Томске состовляет 20000 рублей ')
    if message.text == '3 спальная в городе Томск':
        bot.send_message(message.chat.id, 'Стоимость 3 спальной квартиры в Томске состовляет 37500 рублей ')



    if message.text == 'Пермь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        iteam1 = types.KeyboardButton('Качество жизни в городе Пермь')
        iteam2 = types.KeyboardButton('Преступность в городе Пермь')
        iteam3 = types.KeyboardButton('Здравоохранение в городе Пермь')
        iteam4 = types.KeyboardButton('Аренда в городе Пермь')
        back = types.KeyboardButton('Назад')
        markup.add(iteam1, iteam2, iteam3, iteam4, back)
        bot.send_message(message.chat.id, 'Пермь', reply_markup=markup)
    if message.text == 'Качество жизни в городе Пермь':
        bot.send_message(message.chat.id, 'Индекс качества жизни: 85.29 из 240 - Умеренный')
    if message.text == 'Преступность в городе Пермь':
        bot.send_message(message.chat.id, 'Уровень преступности в Перми: 28.95 из 120 - Умеренная')
    if message.text == 'Здравоохранение в городе Пермь':
        bot.send_message(message.chat.id, 'Уровень здравоохранение в Перми: 43.48 из 100 - Умеренная')
    if message.text == 'Аренда в городе Пермь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        iteam1 = types.KeyboardButton('1 спальная в городе Пермь')
        iteam2 = types.KeyboardButton('3 спальная в городе Пермь')
        back = types.KeyboardButton('Назад')
        markup.add(iteam1, iteam2, back)
        bot.send_message(message.chat.id, 'Аренда в городе Пермь', reply_markup=markup)
    if message.text == '1 спальная в городе Пермь':
        bot.send_message(message.chat.id, 'Стоимость 1 спальной квартиры в Перми состовляет 19000 рублей ')
    if message.text == '3 спальная в городе Пермь':
        bot.send_message(message.chat.id, 'Стоимость 3 спальной квартиры в Перми состовляет 35500 рублей ')





    if message.text == 'Красноярск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        iteam1 = types.KeyboardButton('Качество жизни в городе Красноярск')
        iteam2 = types.KeyboardButton('Преступность в городе Красноярск')
        iteam3 = types.KeyboardButton('Здравоохранение в городе Красноярск')
        iteam4 = types.KeyboardButton('Аренда в городе Красноярск')
        back = types.KeyboardButton('Назад')
        markup.add(iteam1, iteam2, iteam3, iteam4, back)
        bot.send_message(message.chat.id, 'Красноярск', reply_markup=markup)
    if message.text == 'Качество жизни в городе Красноярск':
        bot.send_message(message.chat.id, 'Индекс качества жизни: 80.01 из 240 - Умеренный')
    if message.text == 'Преступность в городе Красноярск':
        bot.send_message(message.chat.id, 'Уровень преступности в Красноярск: 29.12 из 120 - Умеренная')
    if message.text == 'Здравоохранение в городе Красноярск':
        bot.send_message(message.chat.id, 'Уровень здравоохранение в Красноярск: 40.05 из 100 - Умеренная')
    if message.text == 'Аренда в городе Красноярск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        iteam1 = types.KeyboardButton('1 спальная в городе Красноярск')
        iteam2 = types.KeyboardButton('3 спальная в городе Красноярск')
        back = types.KeyboardButton('Назад')
        markup.add(iteam1, iteam2, back)
        bot.send_message(message.chat.id, 'Аренда в городе Красноярск', reply_markup=markup)
    if message.text == '1 спальная в городе Красноярск':
        bot.send_message(message.chat.id, 'Стоимость 1 спальной квартиры в Красноярске состовляет 18500 рублей ')
    if message.text == '3 спальная в городе Красноярск':
        bot.send_message(message.chat.id, 'Стоимость 3 спальной квартиры в Красноярске состовляет ??? рублей ')





    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        iteam1 = types.KeyboardButton('Город проживания')
        markup.add(iteam1)
        bot.send_message(message.chat.id,'Назад', reply_markup = markup)






bot.polling(none_stop=True)