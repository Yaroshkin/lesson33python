#!/usr/bin/env python
import telebot

TOKEN = "6063076548:AAGtPJyUd8pH7kCg75lxJ4OrhZ9XzJLwONY"
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "beep!")


@bot.message_handler(func=lambda message: message.text=="keyboard")
def echo_message(message):
    # bot.reply_to(message, message.text)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('a')
    itembtn2 = telebot.types.KeyboardButton('v')
    itembtn3 = telebot.types.KeyboardButton('d')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()