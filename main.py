import discord
import asyncio
import random

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

    elif(autorepeat_status == True):
        await message.channel.send(repeat(message))

    else:
        return

def help():
    helplist = open('help.txt', 'r')
    return(helplist.read())

def repeat(message):
    rest = message.content
    if message.content.startswith('.repeat'):
        rest = rest.split()
        rest.remove('.repeat')
        rest = " ".join(rest)
    return('{} hat "{}" geschrieben.'.format(message.author.nick ,rest))


def autorepeat(message):
    global autorepeat_status
    if(message.content == '.autorepeat on' or message.content == '.autorepeat On'):
        autorepeat_status = True
        return("**Autorepeat is on**")
    elif(message.content == '.autorepeat off' or message.content == '.autorepeat Off'):
        autorepeat_status = False
        return("**Autorepeat is off**")
    else:
        return('**Dumm?**\r\n*on* oder *off* als Option für diesen Befehl**!**')

def randint(message): 
    rest = message.content
    rest = rest.split()
    if(rest[1].isnumeric() and rest[2].isnumeric()):
        return('Zufallszahl von {} bis {}:\r\n**{}**').format(int(rest[1]), int(rest[2]), random.randint(int(rest[1]), int(rest[2])))
    else:
        return('**Dumm?**\r\nEs müssen 2 Zahlen aus dem Zahlenbereich der ganzen Zahlen angegeben werden**!**')

async def status_task():
    while True:
        global pornoseiten
        await client.change_presence(activity=discord.Game(random.choice(pornoseiten)), status=discord.Status.online)
        await asyncio.sleep(3)
        #await client.change_presence(activity=discord.Game('PornHub'), status=discord.Status.online)
        #await asyncio.sleep(3)
        #await client.change_presence(activity=discord.Game('Hamster Porn'), status=discord.Status.online)
        #await asyncio.sleep(3)

def token():
    token = open('token.txt', 'r')
    return token.read()

client.run(token())
