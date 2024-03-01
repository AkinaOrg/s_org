# main.py

import telebot
from answers import *
import random

TOKEN = '6770825707:AAEvVyG90EJwlsS1i7uLndysh09wQBPGyl0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Используй /role чтобы получить роль и /catastrophe чтобы узнать о катастрофе.")

@bot.message_handler(commands=['role'])
def role(message):
    role_info = f"""Профессия: {random.choice(roles)}
Пол: {random.choice(genders)}
Возраст: {random.choice(ages)}
Плодовитость: {random.choice(fertility)}
Здоровье: {random.choice(health)}
Черта характера: {random.choice(character_traits)}
Фобия: {random.choice(phobias)}
Хобби: {random.choice(hobbies)}
Доп.информация: {random.choice(additional_info)}
Багаж: {random.choice(baggage)}
Карта действия №1: {random.choice(action_cards)}
Карта действия №2: {random.choice(action_cards)}"""
    bot.reply_to(message, role_info)

@bot.message_handler(commands=['catastrophe'])
def catastrophe(message):
    catastrophe_info = f"""Катастрофа: {random.choice(catastrophes)}
Убежище: {random.choice(shelter)}
Запасы: {random.choice(supplies)}
Сколько нужно выгнать людей: {random.choice(people_to_kick)}"""
    bot.reply_to(message, catastrophe_info)

bot.polling()
