import discord
import random
import json
import requests

client = discord.Client()
samrus_chepuh = ["Да,да", "Ты не ахуел?", "НЕПОНЯЛ", "А вот чичас не понял"]
samrus_otvet = ["Да,да", "что", "я тут", "да"]
samrus_pizda = ["сука...","Твоя?"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    random.shuffle(samrus_otvet)
    random.shuffle(samrus_chepuh)
    random.shuffle(samrus_pizda)

@client.event
async def on_message(message):
    text_capit = message.content.capitalize()
    text_author = message.author
    text_channel = message.channel
    print("| Пользователь: {0} | Канал: {1}".format(text_author, text_channel))
    print(text_capit)
    print("-----------")

    if message.author == client.user:
        return
        
    if message.content.startswith('<@!424982736902684673>') or message.content.startswith('<@424982736902684673>'):
        await message.channel.send('', file=discord.File('dima.png'))
        
    if message.content.startswith('<@!451080245576073217>') or message.content.startswith('<@451080245576073217>'):
        await message.channel.send('', file=discord.File('tost.png'))
        
    if message.content.startswith('<@!280028432501309440>') or message.content.startswith('@280028432501309440>'):
        await message.channel.send('Кубаноид!!!')
        
    if text_capit == "Хохлы" and (message.author.name == '!Gramlin!' or message.author.name == 'FNG' or message.author.name == 'stnlm' or message.author.name == 'princess_8564'):
        await text_channel.send('',file=discord.File('hohli.png'))

    if text_capit == 'Чепух':
        await message.reply(random.choice(samrus_chepuh), mention_author=True)

    if text_capit == 'Самрус':
        await message.reply(random.choice(samrus_otvet), mention_author=True)

    if text_capit == 'Пизда':
        await message.reply('сука...', mention_author=True, file=discord.File('cat.jpg'))
        
    if text_capit == 'Да' or text_capit == "Да.":
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
    
    if text_capit == "Шлюхи аргумент":
        await message.reply("Аргумент не нужен, пидор обнаружен")
        
    if text_capit == "Пошёл нахуй":
        await message.reply("Ладно, простите пожалуйста...")

client.run('Token')
