# program version "1.0.1"
# social ovalen id: 671001377899806783


#husk at skrive på requirements
import discord
from discord.ext import commands, tasks
import os
import asyncio
import time
import random
import requests





#client med "--" som prefix
client = commands.Bot(command_prefix = "--")


#hvis nogen skriver "version" i (social-ovalen)
@client.command(name="version")
async def version(context):
    
    myEmbed = discord.Embed(title = "current version", description = "the bot is in version 1.0", color = 0x00ff00)
    myEmbed.set_author(name = "fuckbot-9000")
    myEmbed.add_field(name = "code version", value = "v1.0.1", inline = False)
    myEmbed.add_field(name = "Date Released:", value = "8-12-2020", inline = False)
    await context.message.channel.send(embed = myEmbed)

#hvis nogen skriver "hjælp" i (social-ovalen)
@client.command(name = "hjælp")
async def hjælp(context):
    if not context.author.client:
        com_embed = discord.Embed(title = "kommandoer", description = "disse er kommandoerne du kan bruge med fuckbot-9000", color = 0xFF0000)
        com_embed.set_author(name = "fuckbot-9000")
        com_embed.add_field(name = "--version", value = "viser hvilken version botten er i" , inline = False)
        com_embed.add_field(name = "--slet_besked", value = "sletter bottens sidste 100 beskeder. virker godt mod spam" , inline = False)
        com_embed.add_field(name = "botten vil også reagere på visse ord og sætninger.", value = "'gamer' er en af ordene botten reagere på \n'fuck dig thomas' er en sætning botten vil reagere på \n'læg dig thomas' kan også bruges for virkelig at vise thomas hvor han høre til." , inline = False)
        com_embed.add_field(name = "det er ikke vigtigt om du skriver disse sætniger med stort eller småt", value = "så slå dig løs. og fuck thomas." , inline = False)
    await context.message.channel.send(embed = com_embed)






#hjælper funktion
def is_me(m):
    return m.author == client.user

#slet beskeder
@client.command(name="slet_besked", aliases =["slet", "slet_beskeder"])
@commands.has_permissions(manage_messages = True)
async def slet_besked(ctx, arg1:int):
    print(arg1)
    await ctx.channel.purge(limit = arg1, check = is_me)

#når der sker en fejl
@client.event
async def on_command_error(context, error):
    print(context.command.name + " was invoked incorrectly")
    print(error)


#når robotten er klar
@client.event
async def on_ready():
    print("fuckbot-9000 is logged in")
    

    
    
    
    


#når (social-ovalen) får en besked
@client.event
async def on_message(message):
    fuck = ["fuck dig thomas","fuck dig thomas!","fuck dig thomas!!"]
    #hvis den besked er "fuck dig thomas", så skal botten svarer "ja FUCK dig thomas"
    if message.content.lower() in fuck:
        print(message.content)
        answer = "ja FUCK dig thomas"
        general_channel = client.get_channel(671001377899806783)
        await general_channel.send(answer)
    await client.process_commands(message)

    #hvis beskeden er "gamer", så skal botten svarer "århh GAMER!"
    if message.content.lower() == "gamer":
        print(message.content)
        åh_gamer = "århh GAMER!"
        general_channel = client.get_channel(671001377899806783)
        await general_channel.send(åh_gamer)
    await client.process_commands(message)
    
   
    ned = ["læg dig thomas","læg dig ned thomas","ned thomas"]
    #hvis beskeden er "læg dig ned thomas", så skal botten svarer "Ja læg dig HELT ned og sig undskyld Thomas"
    if message.content.lower() in ned:
        print(message.content)
        læg_dig = "Ja læg dig HELT ned og sig undskyld Thomas"
        general_channel = client.get_channel(671001377899806783)
        await general_channel.send(læg_dig)
    await client.process_commands(message)



@client.command(name = "roast")
async def roast(context, person, times):
    gange = 0
    while gange <= times:
        gange += 1
        insults = open("insults.txt", "r")
        lines = insults.readlines()
        print(len(lines))
        insults.close()
        rand = random.randint(0, len(lines))
        final_roast = str(person) + ", " + str(lines[rand])
        print(final_roast)
        general_channel = client.get_channel(671001377899806783)
        await general_channel.send(final_roast)
    
 
        

    
    

    #async def find_insult():
    #    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    #    response_json = response.json()
    #    insult = response_json["insult"]
    #    insults = open("insults.txt", "a")
    #    insults.write(insult)
    #    insults.close()
  


#skift aktivitet en gang hver halve time
async def ch_pr():
    await client.wait_until_ready()

    #aktiviteter der starter med "spiller"
    activities = ["kiks med thomas", "pik", "baseball med thomas løg"]

    while not client.is_closed():
        #vælg en tilfældig aktivitet
        status = random.choice(activities)
        #skft aktivitet
        await client.change_presence(status= discord.Status.do_not_disturb, activity = discord.Game(name = status))
        #vent en halv time
        await asyncio.sleep(1800)

client.loop.create_task(ch_pr())


#671001377899806783 fuck dig thomas

#run the client on the server
client.run(os.environ["discord_token"])

