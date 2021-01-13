import discord
import asyncio
import datetime 
import os
import random
from google_trans_new import google_translator  
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '-')

translator = google_translator()  
@client.event
async def on_ready():
    print("Bot is Ready")
    drinkwater.start()

@tasks.loop(minutes=90)
async def drinkwater():
    timenow = str(datetime.datetime.now().time())
    timenow = timenow.split(':')
    if (int(timenow[0]) >= 9 and int(timenow[0]) <= 22):
        channel = client.get_channel(744817323973804093)
        await channel.send("Make sure to drink water Dodos!")
    else:
        pass

@client.command()
async def translate(ctx,*,sentence):
    translate_text = translator.translate(sentence,lang_tgt='en')  
    await ctx.send(translate_text)


#Blackbox
f = open("specialCode.txt", "r")
Token = str(f.readline()).strip('\n')
client.run(Token)
