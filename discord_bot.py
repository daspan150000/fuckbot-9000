# program version "1.0.0"
# social ovalen id: 671001377899806783


import discord
from discord.ext import commands
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import asyncio

all_ways_to_say_it = ["fuck dig thomas", "Fuck dig Thomas", "Fuck Dig Thomas", "FUCK DIG THOMAS", "Fuck dig Thomas!", "FUCK DIG THOMAS!"]

#client
client = commands.Bot(command_prefix = "--")

@client.command(name="version")
async def version(context):
    
    myEmbed = discord.Embed(title = "current version", description = "the bot is in version 1.0", color = 0x00ff00)
    myEmbed.set_author(name = "fuckbot-9000")
    myEmbed.add_field(name = "code version", value = "v1.0.0", inline = False)
    myEmbed.add_field(name = "Date Released:", value = "8-12-2020", inline = False)

    await context.message.channel.send(embed = myEmbed)

def is_me(m):
    return m.author == client.user

@client.command(name="slet_besked")
async def slet_besked(context, arg:int):
    amount = arg
    print(amount)
    await context.channel.purge(limit = amount, check = is_me)

    





@client.event
async def on_ready():
    
    await client.change_presence(status= discord.Status.do_not_disturb, activity = discord.Game("pik"))
    
        

@client.event
async def on_message(message):
    if message == "fuck dig thomas":
        answer = "ja FUCK dig thomas"
        general_channel = client.get_channel(785663356689448962)
        await general_channel.send(answer)
    await client.process_commands(message)


#671001377899806783


#run the client on the server
client.run(os.environ["discord_token"])

