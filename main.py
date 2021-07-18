import discord
from discord.ext import commands
import os
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
    print(text_capit)
    if message.author == client.user:
        return

    if text_capit.startswith('Чепух'):
        await message.reply(random.choice(samrus_chepuh), mention_author=True)
    if text_capit.startswith('Самрус'):
        await message.reply(random.choice(samrus_otvet), mention_author=True)
    if text_capit.startswith('Пизда'):
        await message.reply('https://i.imgur.com/8nLFCVP.png', mention_author=True)


client.run('ODY2MjkwMzE4NTc2MDU4NDA4.YPQZug.hLxsaWB5CrCiqxcswPW1a0BNd18')