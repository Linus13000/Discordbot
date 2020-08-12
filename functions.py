import discord
import asyncio
import random

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