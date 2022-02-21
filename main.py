import discord
import asyncio
import random
from functions import *
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
import time

#Umfragen
client = discord.Client()

autorepeat_status = False
pornoseiten = ['Pornhub', 'Youporn', 'Hamster Porn', 'xHamster', 'xnxx', 'xvideos']
playlist = []
voice_is_stopped = False

@client.event
async def on_ready():
    print("Login as user {}".format(client.user.name))
    print("Bot ready!")
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
        elif message.content.startswith('.skip'):
            await skip(message)
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

async def play_from_playlist(message):
    global playlist
    channel = message.author.voice.channel
    voice = get(client.voice_clients, guild=message.guild)
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    url = message.content[len(".play "):]

    while(len(playlist) > 0):
        if not voice.is_playing():
            voice.play(FFmpegPCMAudio(playlist[0], **FFMPEG_OPTIONS))
            await message.channel.send('Bot spielt: ' + url)
            time.sleep(1)
            try:
                playlist.pop()
            except IndexError:
                pass
        else:
            time.sleep(5)

async def play(message):
    global playlist
    message = message
    channel = message.author.voice.channel
    voice = get(client.voice_clients, guild=message.guild)
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
#Bot connectet
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        try:
            voice = await channel.connect()
        except:
            pass

    url = message.content[len(".play "):]
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
    URL = info['url']
    playlist.append(URL)

    if voice.is_playing():
        await message.channel.send("Titel zur Warteschlange hinzugefügt")
    elif not voice.is_playing():
        await play_from_playlist(message)

async def pause(message):
    global voice_is_stopped
    voice = get(client.voice_clients, guild=message.guild)

    if voice.is_playing():
        voice.pause()
        await message.channel.send('Bot pausiert')
        voice_is_stopped = True

async def resume(message):
    voice = get(client.voice_clients, guild=message.guild)

    if not voice.is_playing():
        voice.resume()
        await message.channel.send('Bot fährt fort')

async def skip(message):
    print("Not implemented yet")

async def stop(message):
    global playlist
    playlist = []
    voice = get(client.voice_clients, guild=message.guild)
    channel = message.author.voice.channel
    try:
        if voice.is_playing():
            voice.stop()
            await message.channel.send('Stoppt...')
    except AttributeError:
        pass

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

client.run(token())
