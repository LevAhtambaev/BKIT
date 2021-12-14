import telebot

token = '5084230485:AAEGuKxkf_ZZmsgRGBG1udLJ9o9o7V0pLuo'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Первая кнопка', 'Это вторая')
    bot.send_message(message.chat.id, 'Выберите одну из предложенных кнопок', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'первая кнопка':
        bot.send_message(message.chat.id, 'Выбрана первая кнопка')
    elif message.text.lower() == 'это вторая':
        bot.send_message(message.chat.id, 'Выбрана вторая')


bot.polling()