import telebot
import re
from config import *
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telebot import types


bot = telebot.TeleBot(API_token)



# start command
User_id = []
reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
reply_keyboard.add("btn1", "btn2", "close")

@bot.message_handler(func=lambda message: True)
def process_command(message):
    if message.text == '/start':
        if message.chat.id not in User_id:
            User_id.append(message.chat.id)

        bot.send_message(message.chat.id, "سلام، لطفاً اسم خودت رو بهم بگو ")
        bot.register_next_step_handler(message, process_name)
    elif message.text == '/criticism':
        bot.reply_to(message, "کیبورد زیر رو چک کن  و")
        bot.send_message(message.chat.id, "بازخورد خودت رو بنویس", reply_markup=reply_keyboard)
    else:
        if message.text == "btn1":
            bot.reply_to(message, "دکمه شماره 1 رو فشردید")
        elif message.text == "btn2":
            bot.reply_to(message, "دکمه شماره 2 رو فشردید")
        elif message.text == "close":
            bot.send_message(message.chat.id, "دستور بسته شد.", reply_markup=types.ReplyKeyboardRemove())
        elif re.match(r"^[A-Za-zآ-ی0-9]+$", message.text):
            bot.reply_to(message, f"پیام شما: {message.text}")

def process_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"خب {name} حالا به من بگو چند سالته؟")
    bot.register_next_step_handler(message, process_age)

def process_age(message):
    age = message.text
    bot.send_message(message.chat.id, f"پس {age} سالته. خیلی عالی!")


# Handles all sent documents, audio files, and voice messages
@bot.message_handler(content_types=['audio', 'document', 'voice'])
def message_for_file(message):
    if message.audio:
        bot.reply_to(message, 'This is an audio file')
    elif message.document:
        bot.reply_to(message, 'This is a document file')
    elif message.voice:
        bot.reply_to(message, 'This is voice')


# adding button for inlinekeyboard (call command)
button2 = InlineKeyboardButton(text="تماس با مدیر", callback_data="btn1")
button3 = InlineKeyboardButton(text="تماس با پشتیبانی", callback_data="btn2")
inline_keyboard = InlineKeyboardMarkup(row_width=1)
inline_keyboard.add(button2, button3)


@bot.callback_query_handler(func=lambda call: True)
def check_button(call):
    if call.data == "btn1":
        bot.answer_callback_query(call.id, "09121212", show_alert=True)
    elif call.data == "btn2":
        bot.answer_callback_query(call.id, "09193232", show_alert=True)


@bot.message_handler(commands=['call'])
def message_help(message):
    bot.send_message(message.chat.id, "برای برقراری ارتباط دکمه های زیر رو بزن", reply_markup=inline_keyboard)

#################### End of command #############################


# send message for update products
@bot.message_handler(commands=['SUP2024'])
def send_update(message):
    for id in User_id:
        bot.send_message(id, "محصول مورد نظر موجود شد")

#################### End of command #############################


try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"An error occurred: {e}")

