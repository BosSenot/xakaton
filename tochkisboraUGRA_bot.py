import telebot
import requests
import random
from bs4 import BeautifulSoup
#Получаем токен у бота BotFather
token = '6396720277:AAH_D6N3RsFSGsq9AV-BxECzm9cskwqC6w0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message, res=False):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEKzDJlXeaFBxIgaPbhFLoa-yNjvNkotQAC8zMAAjE98Upj_2I0m8NOzzME")
    welcome_text = 'Приветствую, друзья! Я рад приветствовать вас в нашем чате, посвященном точкам сбора мусора в Югре. Мы собрались здесь с целью сделать наш регион более чистым и здоровым, и каждый из нас играет важную роль в этом процессе.'
    #Создаем меню для пользователя, чтобы он мог использовать заложенные функции бота
    #В скобках указываем(1 кол-во столбцев, 2 изменение размера под экран, 3 запрещаем закрываться после нажатия)
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard = False)
    button1 = telebot.types.KeyboardButton("Пунткы приема")
    button2 = telebot.types.KeyboardButton("Обучающие материалы")
    button3 = telebot.types.KeyboardButton("Полезные ссылки")
    button4 = telebot.types.KeyboardButton("Виды сырья")
    button5 = telebot.types.KeyboardButton("Эко копилка")
    button6 = telebot.types.KeyboardButton("Эко урок")
    #Не забываем добавить созданные кнопки в пустой шаблон
    keyboard.add(button1,button2,button3,button4,button5,button6)
    bot.send_message(message.chat.id,  welcome_text, reply_markup=keyboard)

@bot.message_handler(commands=['typesofrawmaterials'])
def send_fact(message):
    poem_text = "Сырье "
    bot.send_message(message.chat.id, poem_text)
    #Создаем кнопку, которая появится только после сообщения и будет хранить ссылку на сайт
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    button_url = telebot.types.InlineKeyboardButton("Перейти", url='https://sobiraet.yugra-ecology.ru/form')
    keyboard.add(button_url)
    bot.send_message(message.chat.id,  'Обучающие материалы', reply_markup=keyboard)

@bot.message_handler(commands=['Onlinetests'])
def send_lesson(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEKzDtlXfITDNwU31L_WqzsE4-N2c6UoAACnj0AAvuS8EqCz2sleJcFojME")
    poem_text2 = "Записаться на посещение эклогического урока "
    bot.send_message(message.chat.id, poem_text2)
    #Создаем кнопку, которая появится только после сообщения и будет хранить ссылку на сайт
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url = telebot.types.InlineKeyboardButton("Перейти", url='https://sobiraet.yugra-ecology.ru/form')
    keyboard.add(button_url)
    bot.send_message(message.chat.id,  'Обучающие материалы', reply_markup=keyboard)

@bot.message_handler(commands=['Onlinetests'])
def send_punkt(message):
    poem_text2 = "bbbbb "
    bot.send_message(message.chat.id, poem_text2)
    #Создаем кнопку, которая появится только после сообщения и будет хранить ссылку на сайт
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url = telebot.types.InlineKeyboardButton("Перейти", url='https://sobiraet.yugra-ecology.ru/training')
    keyboard.add(button_url)
    bot.send_message(message.chat.id,  'Обучающие материалы', reply_markup=keyboard)

@bot.message_handler(commands=['Onlinetests'])
def send_poem(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEKzGtlXfSb3WOZksJsUafjISklB5SGfAAC3jsAAlto8Er9y4es_b7emjME")
    poem_text2 = "Экоцентр «Югра Собирает» не только пункт приема вторсырья - это еще и образовательная площадка, на которой проходят лекции. "
    bot.send_message(message.chat.id, poem_text2)
    #Создаем кнопку, которая появится только после сообщения и будет хранить ссылку на сайт
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url = telebot.types.InlineKeyboardButton("Перейти", url='https://sobiraet.yugra-ecology.ru/training')
    keyboard.add(button_url)
    bot.send_message(message.chat.id,  'Обучающие материалы', reply_markup=keyboard)

@bot.message_handler(commands=['usefullinks'])
def send_links(message):
    poem_text = "Полезные ссылки"
    bot.send_message(message.chat.id, poem_text)
    #Создаем кнопку, которая появится только после сообщения и будет хранить ссылку на сайт
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button1_url = telebot.types.InlineKeyboardButton("Одноклассники", url='https://ok.ru/group/55933980573950')
    button2_url = telebot.types.InlineKeyboardButton("VK1", url='https://vk.com/yugraecology')
    button3_url = telebot.types.InlineKeyboardButton("VK2", url='https://vk.com/eco4u2')
    button4_url = telebot.types.InlineKeyboardButton("Телеграмм", url='https://t.me/yugraecology')
    keyboard.add(button1_url,button2_url,button3_url,button4_url)
    bot.send_message(message.chat.id,  'Нажми, если хочешь знать больше', reply_markup=keyboard)

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    #Обращаемся к стикеру по токену, который можно получить у бота Get Stiker ID
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGyAFjlcn6NwXCN0gfFcJfQ-iv-usiUAAC1CIAAvhtsEgTy0IAAWSuHYgrBA")


@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text.strip() == 'Виды сырья':
        send_fact(message)#Скобки не должны быть пустыми, тут ставится аргумент нашей функции
    elif message.text.strip() == 'Пунткы приема':
        send_punkt(message)
    elif message.text.strip() == 'Обучающие материалы':
        send_poem(message)
    elif message.text.strip() == 'Эко копилка':
        send_sticker(message)
    elif message.text.strip() == 'Эко урок':
        send_lesson(message)
    elif message.text.strip() == 'Полезные ссылки':
        send_links(message)
    else:
        bot.send_message(message.chat.id, 'Я не могу прочитать, что вы написали! введите новый запрос корректно, пожалуйста)')
#Чтобы программа работы все время
bot.polling()