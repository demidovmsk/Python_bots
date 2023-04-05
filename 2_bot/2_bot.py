import random
import telebot
import time
import json
from os import link
import requests
from bs4 import BeautifulSoup
import re
from aquarium import currency


token = ''

bot = telebot.TeleBot(token)

# number = 0


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('ввести название продукта:')
    markup.add(item1)
    reply_markup = markup
    bot.send_message(message.chat.id, 'Добро пожаловать! Этот бот поможет вам узнать калорийность продукта.', reply_markup=markup)

@bot.message_handler(commands=['text'])
def answer(message):
    if message.text.lower() == 'ввести название продукта:':
        bot.send_message(message.chat.id, 'введите название продукта')
        bot.register_next_step_handler(message, kak_nibud)
    else:
        bot.send_message(message.chat.id, 'Я пока не умею отвечать на данное сообщение!')

@bot.message_handler(content_types=['text'])
def kak_nibud(message):
    bot.send_message(message.chat.id, currency(message.text))


bot.polling(none_stop=True)
