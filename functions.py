import discord
import asyncio
import random

def help():
    embed=discord.Embed(title="Hilfe zum Bot: root", description="Dies ist eine Hilfestellung", color=0x9d1092)
    embed.add_field(name=".help", value="Zeigt diese Hilfe an", inline=False)
    embed.add_field(name=".repeat", value="Wiederholt das nach dem Befehl gesagte", inline=False)
    embed.add_field(name=".autorepeat on / off ", value="Wiederholt alle Textnachrichten außer Befehle", inline=False)
    embed.add_field(name=".randint x y", value="Zufallszahl von x bis y", inline=False)
    embed.add_field(name=".randint x", value="Zufallszahl von 1 bis x", inline=False)
    embed.add_field(name=".joke", value="Haut einen Witz raus", inline=False)
    embed.add_field(name=".play", value="Spielt den angegebenen Song von Youtube", inline=False)
    embed.add_field(name=".pause", value="Pausiert den spielenden Titel", inline=False)
    embed.add_field(name=".resume", value="Setzt das Spielen des pausierten Liedes fort", inline=False)
    embed.add_field(name=".stop", value="Stoppt die Musik", inline=False)
    return(embed)

def repeat(message):
    rest = message.content
    if message.content.startswith('.repeat'):
        rest = rest.split()
        rest.remove('.repeat')
        rest = " ".join(rest)

    embed=discord.Embed(title='Repeat', description='{} hat "{}" geschrieben.'.format(message.author.nick ,rest), color=0x9d1092)
    return(embed)

def randint(message):
    rest = message.content
    rest = rest.split()
    if(len(rest) == 3 and rest[1].isnumeric() and rest[2].isnumeric()):
        embed=discord.Embed(title="Randint", description='Zufallszahl von {} bis {}:'.format(int(rest[1]), int(rest[2])), color=0x9d1092)
        embed.add_field(name="Zahl:", value=random.randint(int(rest[1]), int(rest[2])), inline=False)
    elif(len(rest) < 3 and rest[1].isnumeric()):
        embed=discord.Embed(title="Randint", description='Zufallszahl von 1 bis {}:'.format(int(rest[1])), color=0x9d1092)
        embed.add_field(name="Zahl:", value=random.randint(1, int(rest[1])), inline=False)
    else:
        embed=discord.Embed(title="Dumm?", description="Es müssen 2 Zahlen aus dem Zahlenbereich der ganzen Zahlen angegeben werden**!**", color=0x9d1092)
    return(embed)

def joke(message):
    witze = ['Geht ein Pole an die Kasse.',
    '„Wie sehen Sie lesbische Paare?“ – „Full HD.“',
    'Beim Sex ist es ja oft so wie mit dem Lieblingsgürtel. Ein Loch weiter vorne war alles noch entspannter.',
    'Hab neulich ein Kondom der deutschen Bahn genommen. Ich kam später.',
    'Wieso kann eine Frau beim Verkehr besser denken? Sie ist mit dem Zentralrechner verbunden.',
    'Was ist weiß und guckt durchs Schlüsselloch? — Ein Spannbettlaken',
    'Welches Getränk trinken Firmenchefs? — Leitungswasser',
    'Was sagt ein Origami-Lehrer zu seinem Schüler? — „Das kannste knicken.“',
    'Brennholzverleih',
    'Was findet man beim Kannibalen in der Dusche? — Head and Shoulders',
    'Was passiert wenn man Cola und Bier gleichzeitig trinkt? — Man colabiert',
    'Was essen Autos am liebsten? — Parkplätzchen',
    'Was macht eine Bombe im Bordell? — Puff',
    'Wie heißt ein Spanier ohne Auto? — Carlos',
    'Was sitzt auf einem Baum und winkt? — Ein Huhu!',
    "Was ist niedlich und hüpft qualmend über'n Acker? — Ein Kaminchen!",
    'Was sagt ein Gen, wenn es ein anderes trifft? — Halogen',
    'Was ist ein studierter Bauer? — Ein Ackerdemiker',
    'Was ist gelb und schießt? Eine Banone!'
    'Was ist der Unterschied zwischen einem Kindergarten und einem Ausbildungscamp für Terroristen? - Keine Ahnung - Ich fliege nur die Drohne...',
    'Wie nennt man ein Kind aus Tschernobyl mit gebrochenen Beinen? - Knicklicht',
    'Wie heißt ein Hund ohne Beine? - Egal, kommt eh nicht, wenn man ihn ruft',
    'Was haben ein Baby und eine Flasche Sprudelwasser gemeinsam? - Beide werden still, wenn man sie schüttelt',
    'Was haben GTA und das dritte Reich gemeinsam? - Hast du einen Stern, wirst du verfolgt']
    witz = random.choice(witze)
    embed=discord.Embed(title='Witz', description=witz, color=0x9d1092)
    return(embed)
