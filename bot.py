import telebot
from telebot import types
import time
import json
from pyrogram import Client
from pyrogram.errors import FloodWait

bot = telebot.TeleBot('HERE TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    hello = f'Здравствуйте, <b>{message.from_user.first_name} {message.from_user.last_name}, Вас приветствует бот-парсер, чтобы использовать бота, нажмите на /menu</b>'
    bot.send_message(message.chat.id, hello, parse_mode='html')

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup()
    parser_bot_key = types.KeyboardButton('Парсинг беседы/Группы')
    my_id_key = types.KeyboardButton('Мой id')
    markup.add(parser_bot_key, my_id_key)
    bot.send_message(message.chat.id, 'Выберете одну из кнопок', reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    if message.text == "Парсинг беседы/Группы":
        parser_bot = f'\nК сожалению данный функционал еще в разработке. Посмотрите доступные комадлеты:  \n<u>{message}</u>'
        bot.send_message(message.chat.id, parser_bot, parse_mode='html')

    elif message.text == "Мой id":
        bot.send_message(message.chat.id,f'Твой ID в телеграмм: {message.from_user.id} ', parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Пользуйтесь меню! Я вас не понимаю!')

bot.polling(non_stop=True)
