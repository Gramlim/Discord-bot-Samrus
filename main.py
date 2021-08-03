import discord
import random
import json
import requests

client = discord.Client()
samrus_chepuh = ["Да,да", "Ты не ахуел?", "НЕПОНЯЛ", "А вот чичас не понял"]
samrus_otvet = ["Да,да", "что", "я тут", "да"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    random.shuffle(samrus_otvet)

@client.event
async def on_message(message):
    text_capit = message.content.capitalize()
    print(message.author)
    print(text_capit)
    print("-----------")

    if message.author == client.user:
        return

    if text_capit.startswith('Чепух'):
        await message.reply(random.choice(samrus_chepuh), mention_author=True)
    if text_capit.startswith('Самрус'):
        await message.reply(random.choice(samrus_otvet), mention_author=True)
    if text_capit.startswith('Пизда'):
        await message.reply('https://i.imgur.com/8nLFCVP.png', mention_author=True)
    if text_capit.startswith('Да'):
        await message.reply("Пизда", mention_author=True)
    if text_capit.startswith('Нет'):
        await message.reply("Пидора ответ", mention_author=True)
    if text_capit.startswith('Тёма'):
        await message.reply("Что? Что?", mention_author=True)
    if text_capit.startswith('Анекдот'):
        response = requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=11")
        anekdot = response.text
        await message.reply(anekdot[12:-2], mention_author=True)


client.run('ODY2MjkwMzE4NTc2MDU4NDA4.YPQZug.iKsMeLuaX-UltSpWIBBqgDEGzi0')