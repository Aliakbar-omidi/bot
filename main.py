
import telebot
import re

bot = telebot.TeleBot('7392506579:AAGNVj-Qfw-by0_uM3sz4SOiCJ3GpBHEfRo')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, " سلام به ربات دانلودر فیلم خوش اومدی ")


# Handles all sent documents, audio files, and voice messages
@bot.message_handler(content_types=['audio','document','voice'])
def message_for_file(message):
    if message.audio:
        bot.reply_to(message, 'This is an audio file')
    elif message.document:
        bot.reply_to(message, 'This is a document file')
    elif message.voice:
        bot.reply_to(message, 'This is voice')


# Handles all text message that match the regular expression
@bot.message_handler(func=lambda message: True)
def message_all(message):
    if re.match(r"^[A-Za-z]+$", message.text):
        bot.reply_to(message, 'لطفاً فقط فارسی تایپ کنید.')


# Handles all message for wich the lambda returns True

bot.polling()