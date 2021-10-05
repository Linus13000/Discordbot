import discord
import asyncio
import random
from functions import *
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL

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
        elif message.content.startswith('.play'):
            await play(message)
        elif message.content.startswith('.stop'):
            await stop(message)
        elif message.content.startswith('.pause'):
            await pause(message)
        elif message.content.startswith('.resume'):
            await resume(message)
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

async def play(message):
    channel = message.author.voice.channel
    voice = get(client.voice_clients, guild=message.guild)
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    if not voice.is_playing():
        url = message.content[len(".play "):]
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await message.channel.send('Bot spielt: ' + url)

# check if the bot is already playing
    else:
        await message.channel.send("Bot spielt bereits Musik")
        return

async def pause(message):
    voice = get(client.voice_clients, guild=message.guild)

    if voice.is_playing():
        voice.pause()
        await message.channel.send('Bot pausiert')

async def resume(message):
    voice = get(client.voice_clients, guild=message.guild)

    if not voice.is_playing():
        voice.resume()
        await message.channel.send('Bot fährt fort')

async def stop(message):
    voice = get(client.voice_clients, guild=message.guild)
    channel = message.author.voice.channel

    try:
        if voice.is_playing():
            voice.stop()
            await message.channel.send('Stoppt...')
    except AttributeError:
        channel.disconnect()
        voice.disconnect()
        channel.cleanup()
        voice.cleanup()

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

def token():
    token = open('token.txt', 'r')
    return token.read()

#Neu
#async def playown(message):
#    channel = message.author.voice.channel
#    global player
#    try:
#        await connect(reconnect(True))
#        play()
#    except:
#        pass
#
#async def stop():
#    player.disconnect()

client.run(token())
