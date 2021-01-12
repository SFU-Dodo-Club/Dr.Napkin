import discord
import asyncio
import os
import random
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = ',')
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is Ready")
    drinkwater.start()

@tasks.loop(minutes=60)
async def drinkwater():
    channel = client.get_channel(744817323973804093)
    await channel.send("Make sure to drink water Dodos!")


#Blackbox
f = open("specialCode.txt", "r")
Token = str(f.readline()).strip('\n')
client.run(Token)
