# program version "1.0.0"
# social ovalen id: 671001377899806783


import discord
from discord.ext import commands
import os


#client
client = commands.Bot(command_prefix = "--")

@client.command(name="version")
async def version(context):
    
    myEmbed = discord.Embed(title = "current version", description = "the bot is in version 1.0", color = 0x00ff00)
    myEmbed.set_author(name = "David aka :3 uwu")
    myEmbed.add_field(name = "code version", value = "v1.0.0", inline = False)
    myEmbed.add_field(name = "Date Released:", value = "8-12-2020", inline = False)

    await context.message.channel.send(embed = myEmbed)

@client.event
async def on_ready():
    general_channel = client.get_channel(671001377899806783)
    await general_channel.send("ja FUCK dig thomas")
    
        

@client.event
async def on_message(message):
    if message.content == "fuck dig thomas":
        general_channel = client.get_channel(671001377899806783)
        await general_channel.send("ja FUCK dig thomas")
    
    await client.process_commands(message)




#run the client on the server
client.run(os.environ["discord_token"])
