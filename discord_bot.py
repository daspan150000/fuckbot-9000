# program version "1.0.1"
# social ovalen id: 671001377899806783


# ideer til botten eller andre bots:
#
#
# første prioritet, mange af de andre ideer fungerer ikke uden.
# change over to nextcord
# refacturer alt koden så det også virker med slash-commands istedet for kun on_message
#
# en "UWU" counter.
#
# en "fuck dig thomas" counter og en "roast thomas" counter.
#
# 
#
# en chat med spil i. så kan en (eller flere) personer vælge et spil at spille selv eller imod hinanden.
#       potentielle spil:
#                        fantasy rpg (discord dungeons).
#                        ping pong.
#                        AK47.
#                        kryds og bolle.
#                        hangman.
#                        
#                        
# udførsel af denne ide:
# 
# jeg kan lave en bot for hver text chat. botterne hedder gamer + et tal.
# hver bot er programeret med alle de spil jeg kan få programeret ind i botten. 

#husk at skrive på requirements
import discord 
from discord.ext import commands
import os
import asyncio
import random
import praw
import sqlite3
 
#skal fjernes når commands er implementeret.
client = discord.Client()

#brug commands i stedet for on_message
intents = discord.Intents.default()
intents.members = True
new_client = commands.Bot(intents = intents, command_prefix = "--")


def create_and_populate_db():
    with sqlite3.connect("counts.db") as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS uwu_counts(user_id INT, amount INT DEFAULT 1 NOT NULL, server TEXT")
            cur.execute("CREATE TABLE IF NOT EXISTS fuckdig_counts(user_id INT, amount INT DEFAULT 1 NOT NULL, server TEXT")
            

#når botten er klar
@client.event
async def on_ready():
    print("fuckbot-9000 is logged in")
    create_and_populate_db()


#når botten får en besked
@client.event
async def on_message(message):
    
    #"uwu" counter.
    #hvis beskeden indeholder "uwu" skal der enten tilskrives en counter til brugeren der sendte beskeden. ellers så skal værdien af beskedens senders counter øges.
    message_lower = message.content.lower()
    uwu_amount = message_lower.count("uwu")
    user = message.author.id
    server = message.server
    if uwu_amount >= 1:
        with sqlite3.connect("counts.db") as conn:
            cur = conn.cursor()
            cur.execute("IF EXISTS SELECT amount FROM uwu_counts WHERE user_id = (?) AND server = (?)", user, server )
            stored_uwu = cur.fetchall()
            stored_uwu += uwu_amount
            cur.execute("INSERT OR UPDATE counts VALUES uwu_amount = (?)", stored_uwu)
            conn.commit()
            print("uwu")


    fuck = ["fuck dig thomas","fuck dig thomas!","fuck dig thomas!!"]
    #hvis den besked er "fuck dig thomas", så skal botten svarer "ja FUCK dig thomas"
    if message.content.lower() in fuck:
        with sqlite3.conn.cursor() as conn:
            cur = conn.cursor()
            cur.execute("IF EXISTS SELECT amount FROM fuckdig_counts WHERE user_id = (?) AND server = (?)", user, server )
            stored_fuck = cur.fetchall()
            stored_fuck += 1
            cur.execute("INSERT OR UPDATE counts VALUES fuckdig_amount = (?)", stored_fuck)
            conn.commit()
        print(message.content)
        thomas_id = '<@173149463886561280>'
        await message.channel.send('%s ja FUCK dig thomas ' % thomas_id)
        
    

    #hvis beskeden er "gamer", så skal botten svarer "århh GAMER!"
    if message.content.lower() == "gamer":
        print(message.content)
        åh_gamer = "århh GAMER!"
        context_channel = client.get_channel(message.channel.id)
        await context_channel.send(åh_gamer)
    
    
    
    

    


    ned = ["læg dig thomas","læg dig ned thomas","ned thomas"]
    #hvis beskeden er "læg dig ned thomas", så skal botten svarer "Ja læg dig HELT ned og sig undskyld Thomas"
    if message.content.lower() in ned:
        print(message.content)
        thomas_id = '<@173149463886561280>'
        await message.channel.send('%s Ja læg dig HELT ned og sig undskyld Thomas' % thomas_id)
    

    if message.content.lower().startswith("--roast"):
        insults = open("insults.txt", "r")
        lines = insults.readlines()
        print(len(lines))
        insults.close()
        person = message.content.split()
        rand = random.randint(0, len(lines))
        print(rand)
        final_roast = str(person[1]) + ", " + lines[rand]
        context_channel = client.get_channel(message.channel.id)
        await context_channel.send(final_roast)


    if message.content.lower() == "--ping":
        context_channel = client.get_channel(message.channel.id)
        await context_channel.send("pong")


    if message.content.lower() == "--version":
        myEmbed = discord.Embed(title = "current version", description = "the bot is in version 1.0", color = 0x00ff00)
        myEmbed.set_author(name = "fuckbot-9000")
        myEmbed.add_field(name = "code version", value = "v1.0.1", inline = False)
        myEmbed.add_field(name = "Date Released:", value = "8-12-2020", inline = False)
        context_channel = client.get_channel(message.channel.id)
        await context_channel.send(embed = myEmbed)


    if message.content.lower() == "--hjælp":
        com_embed = discord.Embed(title = "kommandoer", description = "disse er kommandoerne du kan bruge med fuckbot-9000", color = 0xFF0000)
        com_embed.set_author(name = "fuckbot-9000")
        com_embed.add_field(name = "--version", value = "viser hvilken version botten er i" , inline = False)
        com_embed.add_field(name = "--roast", value = "denne kommando efterfølges af et navn. den person du nævner vil blive ristet hårdt \neks: --roast thomas" , inline = False)
        com_embed.add_field(name = "botten vil også reagere på visse ord og sætninger.", value = "'gamer' er en af ordene botten reagere på \n'fuck dig thomas' er en sætning botten vil reagere på \n'læg dig thomas' kan også bruges for virkelig at vise thomas hvor han høre til." , inline = False)
        com_embed.add_field(name = "det er ikke vigtigt om du skriver disse sætniger med stort eller småt", value = "så slå dig løs. og fuck thomas." , inline = False)
        context_chat = client.get_channel(message.channel.id)
        await context_chat.send(embed = com_embed)

    
    if message.content.lower() == "--meme":
        reddit = praw.Reddit(client_id = os.environ["reddit_client_id"],
        client_secret = os.environ["reddit_client_secret"],
        username = "daspan15000",
        password = os.environ["pass"],
        user_agent = "fuckbot-9000")

        subreddit = reddit.subreddit("memes")
        all_meme_subs = []
        top_memes = subreddit.top(limit = 50)
        for meme_submission in top_memes:
            all_meme_subs.append(meme_submission)

        random_meme_sub = random.choice(all_meme_subs)
        meme_name = random_meme_sub.title
        meme_url = random_meme_sub.url
        meme_em = discord.Embed(title = meme_name)
        meme_em.set_image(url = meme_url)
        context_channel = client.get_channel(message.channel.id)
        await context_channel.send(embed = meme_em)



    if message.content.lower() == "--cat":
        reddit = praw.Reddit(client_id = os.environ["reddit_client_id"],
        client_secret = os.environ["reddit_client_secret"],
        username = "daspan15000",
        password = os.environ["pass"],
        user_agent = "fuckbot-9000")

        subreddit = reddit.subreddit("cursedcats")
        all_cat_subs = []
        top_cats = subreddit.top(limit = 50)
        for cat_submission in top_cats:
            all_cat_subs.append(cat_submission)

        random_cat_sub = random.choice(all_cat_subs)
        cat_name = random_cat_sub.title
        cat_url = random_cat_sub.url
        cat_em = discord.Embed(title = cat_name)
        cat_em.set_image(url = cat_url)
        context_channel = client.get_channel(message.channel.id)
        await context_channel.send(embed = cat_em)


    #async def find_insult():
        


#skift aktivitet en gang hver halve time
async def ch_pr():
    await client.wait_until_ready()

    #aktiviteter der starter med "spiller"
    activities = ["kiks på thomas", "pik", "baseball med thomas løg", "'mob thomas', med thomas´ mor", "banjo på thomas´ røvskæg", '"spike" thomas` drink']

    while not client.is_closed():
        #vælg en tilfældig aktivitet
        status = random.choice(activities)
        #skift aktivitet
        await client.change_presence(status= discord.Status.do_not_disturb, activity = discord.Game(name = status))
        #vent en halv time og gentag
        await asyncio.sleep(1800)

client.loop.create_task(ch_pr())


#671001377899806783 fuck dig thomas

#run the client on the server
client.run(os.environ["discord_token"])


##hjælper funktion
#def is_me(m):
#    return m.author == client.user
#
##slet beskeder
#@client.command(name="slet_besked", aliases =["slet", "slet_beskeder"])
#@commands.has_permissions(manage_messages = True)
#async def slet_besked(ctx):
#    await ctx.channel.purge(limit = 10, check = is_me)
