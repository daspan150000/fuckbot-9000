# program version "1.0.0"
# general channel id: 785663356689448962

#import discord package
import discord
from discord.ext import commands
#import datetime
#import asyncio
#from openpyxl import Workbook
#from openpyxl import load_workbook
#import schedule

#current_message = 7

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
    print("bot is ready")
    
        

@client.event
async def on_message(message):
    if message.content == "fuck dig thomas":
        general_channel = client.get_channel(785663356689448962)
        await general_channel.send("ja FUCK dig thomas")
    
    await client.process_commands(message)

#@client.event
#async def send_message():
#    while(True):
#        await client.wait_until_ready()
#        general_channel = client.get_channel(785663356689448962)
#        current_hour = int(datetime.datetime.now().strftime("%I"))
#        current_minute = int(datetime.datetime.now().strftime("%M"))
#        current_second = int(datetime.datetime.now().strftime("%S"))
#        current_time = str(current_hour) + ":" + str(current_minute) + ":" + str(current_second)
#        print(current_time)
#        #load workbook
#        wb = load_workbook(filename = "fornærmelser.xlsx")
#        ws = wb.active
#        #hent fornærmelser
#        collumn_b = ws['B']
#        #vælg dagens fornærmelse
#        if current_hour == int("8") and current_minute == int("53") and current_second == int("00"):
#            global current_message
#            current = collumn_b[current_message]
#            current_message = current_message + 1
#            print("dag nummer:" + str(current_message) + str(current.value))
#            #send fornærmelse til kanalen
#            await general_channel.send(current.value)
#    await asyncio.sleep(10)
#       
#client.loop.create_task(send_message())



#run the client on the server
client.run("Nzg1NjQ2NzIwMjA5NTE4NjUz.X864hg.a-Qzo8vDN8VuwgqQnIKRUf6Ew-c")
