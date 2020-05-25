import config
import telebot

#telebot.apihelper.proxy = {'http':'http://1.0.0.52:80'}
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()