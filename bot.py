import discord
import asyncio
import datetime 
import os
import random
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '-')


@client.event
async def on_ready():
    print("Bot is Ready")
    drinkwater.start()

@tasks.loop(minutes=90)
async def drinkwater():
    guild = client.get_guild(744817281871249428)
    channel = guild.get_channel(801326450396758076)
    timenow = str(datetime.datetime.now().time())
    timenow = timenow.split(':')
    print(int(timenow[0]))
    if ((int(timenow[0]) >= 17) or (int(timenow[0]) <= 8)):
        await channel.send("Make sure to drink water Dodos!")

# @tasks.loop(minutes = 90)
# async def goodmorning():
#     guild = client.get_guild(744817281871249428)
#     channel = guild.get_channel(801326450396758076)
#     timenow = str(datetime.datetime.now().time())
#     timenow = timenow.split(':')
#     print(int(timenow[0]))
#     if ((int(timenow[0]) == 9)):
#         await channel.send("Good Night Dodos!")
#     elif ((int(timenow[0]) == 17)):
#         await channel.send("Good Morning Dodos!")
    

#Blackbox
client.run(os.environ['TOKEN'])
