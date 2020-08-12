import discord
import asyncio
import random
from functions import *

#Umfragen hinzufügen
#Neuer Mensch auf Server -> Infomessage
#Randint wenn nur eine Zahl angegeben wurde
#Weitere Pornoseiten Liste mit random

client = discord.Client()

autorepeat_status = False
pornoseiten = ['Pornhub', 'Youporn', 'Hamster Porn', 'xHamster', 'xnxx', 'xvideos']

@client.event
async def on_ready():
    print("Eingeloggt als User {}".format(client.user.name))
    client.loop.create_task(status_task())

@client.event
async def on_message(message):
    if message.author.bot:  
        return
    if message.content.startswith('.'):
        if(message.content == '.help'):
            await message.channel.send(help())
        elif message.content.startswith('.repeat'):
            await message.channel.send(repeat(message))

        elif message.content.startswith('.autorepeat'):
            await message.channel.send(autorepeat(message))
        
        elif message.content.startswith('.randint'):
            await message.channel.send(randint(message))
        else:
            await message.channel.send("**Dumm?**\r\nSiehe *.help* für mehr Informationen**!**")
    elif message.content.startswith('!'): 
        return 
    elif message.content.startswith('gs.'):
        return
    elif message.content.startswith('b.'):
        return
    elif(autorepeat_status):
        await message.channel.send(repeat(message))
    else:
        return

async def status_task():
    while True:
        global pornoseiten
        await client.change_presence(activity=discord.Game(random.choice(pornoseiten)), status=discord.Status.online)
        await asyncio.sleep(3)
def token():
    token = open('token.txt', 'r')
    return token.read()

client.run(token())
