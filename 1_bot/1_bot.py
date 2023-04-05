# # Обучаюсь делать бота # изучить библиотеку аиоган # для установки pip3 install ...
#
import random
import telebot
import time
import json
from os import link
import requests
from bs4 import BeautifulSoup
import re
from horos import pars
from money import currency




token = ''

bot = telebot.TeleBot(token)

number = 0

# with open('horoscope.txt', 'r', encoding='utf-8') as here: # Создание txt
#      text = 'text'
#      here.write('text')

# with open('horoscope.json', 'r', encoding='utf-8') as horo:
    # some_dict = json.load(horo)
    # print(some_dict)




@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('рандомное число')
    item2 = telebot.types.KeyboardButton('кинуть кость')
    item3 = telebot.types.KeyboardButton('как дела?')
    item4 = telebot.types.KeyboardButton('курсы валют')
    item5 = telebot.types.KeyboardButton('загадай число')
    item6 = telebot.types.KeyboardButton('знак зодиака')
    item7 = telebot.types.KeyboardButton('покажи id стикера')

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(
        message.chat.id, 'Добро пожаловать! Выберите нужный Вам пункт меню:', reply_markup=markup)


# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, как дела?')

@bot.message_handler(content_types=['text'])
def answer(message):

    if message.text.lower() == 'рандомное число':
        bot.send_message(message.chat.id, str(random.randint(1, 100)))

    elif message.text.lower() == 'кинуть кость':
        bot.send_message(message.chat.id, str(random.randint(1, 7)))

    elif message.text.lower() == 'загадай число':
         global number
         number = random.randint(1, 10)
         bot.send_message(message.chat.id, 'ОК, загадал')
         bot.register_next_step_handler(message, think_of)
    elif message.text.lower() == 'курсы валют':
        bot.send_message(message.chat.id, 'Введите название валюты')
        bot.register_next_step_handler(message, kak_nibud)

    elif message.text.lower() == 'знак зодиака':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item11 = telebot.types.KeyboardButton('Водолей')
        item22 = telebot.types.KeyboardButton('Овен')
        item33 = telebot.types.KeyboardButton('Телец')
        item44 = telebot.types.KeyboardButton('Близнецы')
        item55 = telebot.types.KeyboardButton('Рак')
        item66 = telebot.types.KeyboardButton('Лев')
        item77 = telebot.types.KeyboardButton('Дева')
        item88 = telebot.types.KeyboardButton('Весы')
        item99 = telebot.types.KeyboardButton('Скорпион')
        item1010 = telebot.types.KeyboardButton('Стрелец')
        item1111 = telebot.types.KeyboardButton('Козерог')
        item1212 = telebot.types.KeyboardButton('Рыбы')
        markup.add(item11, item22, item33, item44, item55, item66, item77, item88, item99, item1010, item1111, item1212)
        bot.send_message(message.chat.id, 'Выберите нужный Вам знак Зодиака:', reply_markup=markup)
        bot.register_next_step_handler(message, horoscope)

    elif message.text.lower() == 'как дела?':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item111 = telebot.types.KeyboardButton('хорошо')
        item222 = telebot.types.KeyboardButton('плохо')
        markup.add(item111, item222)
        bot.send_message(
            message.chat.id, 'Пока не родила, как у тебя?)', reply_markup=markup)

    elif message.text.lower() == 'хорошо':
            bot.send_message(message.chat.id, 'Я рад за тебя')
    elif message.text.lower() == 'плохо':
            bot.send_message(message.chat.id, 'Не переживай, все образуется)')

    elif message.text.lower() == 'напоминалка':
        bot.send_message(message.chat.id, 'Введите время для будильника!')
        bot.register_next_step_handler(message, alarm)
    else:
        bot.send_message(
            message.chat.id, 'Я пока не умею отвечать на данное сообщение!')


@bot.message_handler(content_types=['text'])
def think_of(message):
    print(number)
    if message.text.lower() != f'{number}':
        bot.send_message(message.chat.id, 'Нет')
        bot.register_next_step_handler(message, think_of)
    else:
         bot.send_message(message.chat.id, 'Да')

@bot.message_handler(content_types=['text'])
def horoscope(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item11 = telebot.types.KeyboardButton('Водолей')
    item22 = telebot.types.KeyboardButton('Овен')
    item33 = telebot.types.KeyboardButton('Телец')
    item44 = telebot.types.KeyboardButton('Близнецы')
    item55 = telebot.types.KeyboardButton('Рак')
    item66 = telebot.types.KeyboardButton('Лев')
    item77 = telebot.types.KeyboardButton('Дева')
    item88 = telebot.types.KeyboardButton('Весы')
    item99 = telebot.types.KeyboardButton('Скорпион')
    item1010 = telebot.types.KeyboardButton('Стрелец')
    item1111 = telebot.types.KeyboardButton('Козерог')
    item1212 = telebot.types.KeyboardButton('Рыбы')
    item1313 = telebot.types.KeyboardButton('Назад')
    markup.add(item11, item22, item33, item44, item55, item66, item77, item88, item99, item1010, item1111, item1212, item1313)

    if message.text != 'Назад':
         bot.send_message(message.chat.id, pars(message.text), reply_markup=markup)    # до парсинга  bot.send_message(message.chat.id, some_dict[message.text], reply_markup=markup)
         bot.register_next_step_handler(message, horoscope)


@bot.message_handler(content_types=['text'])
def kak_nibud(message):
    bot.send_message(message.chat.id, currency(message.text))



# @bot.message_handler(content_types=['text'])
 #def alarm(message):
   # bot.send_message(message.chat.id, 'Включи напоминалку')
  # global ti    time = messag    global chat_id
   # chat_id = message


bot.polling(none_stop=True)
