#!/usr/bin/env python
#UTF-8
import json
import requests
import telebot

TOKEN = '6106215509:AAHeZyeDPU9uBucTEH6I1OfFG8ymAuuR4QE'
bot = telebot.TeleBot(TOKEN)
with open("out.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, text="Привет, {0.first_name}\nДавай сыграем в города\n Вводите название города англ.буквами".format(message.from_user))



@bot.message_handler(content_types=['text'])
def echo_message(message):
    if message.text in data:
        data.remove(message.text)

        for i in data:
            if str(message.text[-1]).upper() == str(i[0]).upper():
                bot.send_message(message.chat.id,i)
                print(i)
                data.remove(i)
                break
    else:
        bot.send_message(message.chat.id, "Это слово уже было или не правильный ввод данных")

bot.infinity_polling()