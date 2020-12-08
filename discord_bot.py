# program version "1.0.0"
# social ovalen id: 671001377899806783


import discord
from discord.ext import commands
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#client
client = commands.Bot(command_prefix = "--")

@client.command(name="version")
async def version(context):
    
    myEmbed = discord.Embed(title = "current version", description = "the bot is in version 1.0", color = 0x00ff00)
    myEmbed.set_author(name = "David aka :3 uwu")
    myEmbed.add_field(name = "code version", value = "v1.0.0", inline = False)
    myEmbed.add_field(name = "Date Released:", value = "8-12-2020", inline = False)

    await context.message.channel.send(embed = myEmbed)

@client.command(name="joke")
async def joke(context):
    
    path = "C:\\Program Files (x86)\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://intellisult.com/#")
    search = driver.find_element_by_css_selector("body > div.main-content > div.body-content.section > div:nth-child(2) > div.insult-form.col-five > input")
    search.send_keys("thomas")
    search.send_keys(Keys.RETURN)
    insult = driver.find_element_by_class_name("printed-insult")
    print(insult)
    general_channel = client.get_channel(671001377899806783)
    await general_channel.send(insult.text)

    
@client.command(name = "clear")
async def clear(context, amount=5):
    await context.channel.purge(limit = 1)

    


@client.event
async def on_ready():
    
    await client.change_presence(status= discord.Status.do_not_disturb, activity = discord.Game("pik"))
    
        

@client.event
async def on_message(message):
    if message.content == "fuck dig thomas":
        general_channel = client.get_channel(671001377899806783)
        await general_channel.send("ja FUCK dig thomas")
    
    await client.process_commands(message)




#run the client on the server
client.run(os.environ["discord_token"])
