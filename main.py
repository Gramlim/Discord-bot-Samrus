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
    random.shuffle(samrus_chepuh)

@client.event
async def on_message(message):
    text_capit = message.content.capitalize()
    print(message.author)
    print(text_capit)
    print("-----------")

    if message.author == client.user:
        return

    if text_capit == 'Чепух':
        await message.reply(random.choice(samrus_chepuh), mention_author=True)

    if text_capit == 'Самрус':
        await message.reply(random.choice(samrus_otvet), mention_author=True)

    if text_capit == 'Пизда':
        await message.reply('сука...', mention_author=True, file=discord.File('cat.jpg'))

    if text_capit == 'Да':
        await message.reply("Пизда", mention_author=True)

    if text_capit == 'Нет':
        await message.reply("Пидора ответ", mention_author=True)

    if text_capit == 'Тёма':
        await message.reply("Что? Что?", mention_author=True)
    
    if text_capit == 'Шлёпа' or text_capit == 'Флопа' or text_capit == 'Шлепа' :
        await message.reply("Колчак, разлогинься", mention_author=True)

    if text_capit == 'Анекдот':
        response = requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=11")
        anekdot = response.text
        await message.reply(anekdot[12:-2], mention_author=True)

    if text_capit == 'Joke':
        response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
        anekdot = response.text
        await message.reply(anekdot[10:-3], mention_author=True)

    if text_capit == "Алё" or text_capit == "Алло" or text_capit == "Ало":
        await message.reply("Хуем по лбу не дало?")

    if text_capit == "Чё":
        await message.reply("Хуй через плечо")

client.run('ODY2MjkwMzE4NTc2MDU4NDA4.YPQZug.Srku815gc3rcUqfUpsR-VeiL4ZU')