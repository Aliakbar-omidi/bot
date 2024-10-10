
import telebot

bot = telebot.TeleBot('7392506579:AAGNVj-Qfw-by0_uM3sz4SOiCJ3GpBHEfRo')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "به ربات دانلودر فیلم خوش اومدی")


bot.polling()