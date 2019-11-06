import telebot
import wget
bot = telebot.TeleBot('1025293224:AAGuTf6dK_F0hfY06j6p4ilntUT7ilbD_9s')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока',)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'debug':
	    keyboard2 = telebot.types.ReplyKeyboardMarkup()
	    keyboard2.row('Chat_ID', 'stop', 'Site_vps')
	    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard2)
    elif message.text.lower() == 'stop':
        bot.send_message(message.chat.id, 'Стооооой! моя остоновка')
        print(fdf)
    site = message.text
    filename = wget.download(site)
    bot.send_document(message.chat.id, filename)
bot.polling()
print ('hellp')

