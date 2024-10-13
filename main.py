
import telebot

bot = telebot.TeleBot('7392506579:AAGNVj-Qfw-by0_uM3sz4SOiCJ3GpBHEfRo')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, " سلام به ربات دانلودر فیلم خوش اومدی ")

# send message for text
@bot.message_handler(func=lambda message: True)
def handle_text_message(message):
    bot.reply_to(message, "لطفا از دستورات داخل منو استفاده کنید")


# Handles all sent documents and audio files
@bot.message_handler(content_types=['audio','document'])
def message_for_file(message):
    if message.audio:
        bot.reply_to(message, 'This is an audio file')
    elif message.document:
        bot.reply_to(message, 'This is a document file')

bot.polling()