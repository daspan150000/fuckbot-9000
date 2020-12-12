# program version "1.0.0"
# social ovalen id: 671001377899806783



import discord
from discord.ext import commands
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import asyncio
import time



#client
client = commands.Bot(command_prefix = "--")

@client.command(name="version")
async def version(context):
    
    myEmbed = discord.Embed(title = "current version", description = "the bot is in version 1.0", color = 0x00ff00)
    myEmbed.set_author(name = "fuckbot-9000")
    myEmbed.add_field(name = "code version", value = "v1.0.0", inline = False)
    myEmbed.add_field(name = "Date Released:", value = "8-12-2020", inline = False)
    await context.message.channel.send(embed = myEmbed)


@client.command(name = "hjælp")
async def hjælp(context):
    if not context.author.client:
        com_embed = discord.Embed(title = "kommandoer", description = "disse er kommandoerne du kan bruge med fuckbot-9000", color = 0xFF0000)
        com_embed.set_author(name = "fuckbot-9000")
        com_embed.add_field(name = "--version", value = "viser hvilken version botten er i" , inline = False)
        com_embed.add_field(name = "--slet_besked", value = "sletter bottens sidste 100 beskeder. virker godt mod spam" , inline = False)
        com_embed.add_field(name = "botten vil også reagere på visse ord og sætninger.", value = "'gamer' er en af ordene botten reagere på \n'fuck dig thomas' er en sætning botten vil reagere på" , inline = False)
        com_embed.add_field(name = "det er ikke vigtigt om du skriver disse sætniger med stort eller småt", value = "så slå dig løs. og fuck thomas." , inline = False)
    await context.message.channel.send(embed = com_embed)


def is_me(m):
    return m.author == client.user

@client.command(name="slet_besked", aliases =["slet", "slet_beskeder"])
@commands.has_permissions(manage_messages = True)
async def slet_besked(ctx, arg1:int):
    print(arg1)
    await ctx.channel.purge(limit = arg1, check = is_me)


@client.event
async def on_command_error(context, error):
    print(context.command.name + " was invoked incorrectly")
    print(error)


@client.event
async def on_ready():
    print("fuckbot-9000 is logged in")
    await client.change_presence(status= discord.Status.do_not_disturb, activity = discord.Game(name = "kiks med thomas' far"))

#seconds = time.time()
#local_time = time.localtime(seconds)
#current_time = str(local_time.tm_hour + 1) + ":" + str(local_time.tm_min - 2) + ":" + str(local_time.tm_sec - 10)
#print(current_time)
#if current_time == "15:00:00":
#    await client.change_presence(status= discord.Status.do_not_disturb, activity = discord.Game(name = "kiks med thomas' far"))
#if current_time == 




@client.event
async def on_message(message):
    File = open("fuck.txt", "r")
    read = File.read()
    File.close()
    if message.content.lower() in read:
        answer = "ja FUCK dig thomas"
        general_channel = client.get_channel(671001377899806783)
        await general_channel.send(answer)
    await client.process_commands(message)

    if message.content.lower() == "gamer":
        åh_gamer = "århh GAMER!"
        general_channel = client.get_channel(671001377899806783)
        await general_channel.send(åh_gamer)
    await client.process_commands(message)

    
    fil = open("leg_dig.txt", "r")
    læs = fil.open()
    fil.close()
    if message.content.lower() in læs:
        læg_dig = "Ja læg dig HELT ned og sig undskyld Thomas"
        general_channel = client.get_channel(671001377899806783)
        await general_channel.send(læg_dig)
    await client.process_commands(message)



#671001377899806783 fuck dig thomas


#run the client on the server
client.run(os.environ["discord_token"])

