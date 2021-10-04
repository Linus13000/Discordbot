import discord
import asyncio
import random
from functions import *

#Umfragen
client = discord.Client()

autorepeat_status = False
pornoseiten = ['Pornhub', 'Youporn', 'Hamster Porn', 'xHamster', 'xnxx', 'xvideos']


@client.event
async def on_ready():
    print("Eingeloggt als User {}".format(client.user.name))
    print("Bot Ready!")
    client.loop.create_task(status_task())


@client.event
async def on_message(message):
    if message.author.bot:  
        return
    if message.content.startswith('!' or 'gs.' or 'b.' or '!!'): 
        return 
    elif message.content.startswith('.'):
        if(message.content == '.help'):
            await message.channel.send(embed=help())
        elif message.content.startswith('.repeat'):
            await message.channel.send(embed=repeat(message))
        elif message.content.startswith('.autorepeat'):
            await message.channel.send(embed=autorepeat(message))     
        elif message.content.startswith('.randint'):
            await message.channel.send(embed=randint(message))
        elif message.content.startswith('.joke'):
            await message.channel.send(embed=joke(message))
#        elif message.content.startswith('.play'):
#            await play(message)
#        elif message.content.startswith('.stop'):
#            await stop()
        else:
            await message.channel.send("**Dumm?**\r\nSiehe *.help* für mehr Informationen**!**")
    elif(autorepeat_status):
        await message.channel.send(embed=repeat(message))
    else:
        return

async def status_task():
    global pornoseiten
    while True:
        await client.change_presence(activity=discord.Game(random.choice(pornoseiten)), status=discord.Status.online)
        await asyncio.sleep(3)
def token():
    token = open('token.txt', 'r')
    return token.read()

def autorepeat(message):
    global autorepeat_status
    if(message.content == '.autorepeat on' or message.content == '.autorepeat On'):
        autorepeat_status = True
        embed=discord.Embed(title="Autorepeat", description="Autorepeat ist an", color=0x9d1092)
    elif(message.content == '.autorepeat off' or message.content == '.autorepeat Off'):
        autorepeat_status = False
        embed=discord.Embed(title="Autorepeat", description="Autorepeat ist aus", color=0x9d1092)
    else:
        embed=discord.Embed(title="Dumm?", description="*on* oder *off* als Option für diesen Befehl**!**", color=0x9d1092)
    return(embed)


#Neu
#async def play(message):
#    channel = message.author.voice.channel
#    global player
#    try:
#        player = await channel.connect()
#    except:
#        pass
#
#async def stop():
#    player.stop()

client.run(token())
