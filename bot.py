import discord
import asyncio
import datetime 
import os
import random
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '-')

intents = discord.Intents.default()
intents.members = True


@client.event
async def on_ready():
    print("Bot is Ready")
    drinkwater.start()

@tasks.loop(minutes=90)
async def drinkwater():
    messages = ["Make sure to drink water Dodos!", "Love you dodos! Make sure to stay hydrated", "Guess what time it is: ||Drinking water time||. Love you Dodos!"]
    guild = client.get_guild(744817281871249428)
    channel = guild.get_channel(801326450396758076)
    timenow = str(datetime.datetime.now().time())
    timenow = timenow.split(':')
    print(int(timenow[0]))
    if ((int(timenow[0]) >= 17) or (int(timenow[0]) <= 8)):
        m = random.randint(0,2)
        await channel.send(messages[m])

@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(744817281871249428)

    reaction = payload.emoji
    reaction = str(reaction)
    member = payload.user_id
    print(member)
    member = guild.get_member(int(member))

    if str(payload.channel_id) != '744818329427902504':
        print("Wrong channel mate")
        return
    
    elif reaction == "🔔":
        print("DODO PROPER")
        role = discord.utils.get(guild.roles, name="Dodo Proper")
        await member.add_roles(role)

    elif reaction == "🎵":
        role = discord.utils.get(guild.roles, name="DJ")
        print("DJ")
        await member.add_roles(role)
    
    elif reaction == "🔣":
        print("MISC")
        role = discord.utils.get(guild.roles, name="--------------- Misc ---------------")
        await member.add_roles(role)

    elif reaction == "🖌":
        print("COLOURS")
        role = discord.utils.get(guild.roles, name="--------------- Colours---------------")
        await member.add_roles(role)


    elif reaction == "♈":
        print("ARIES")
        role = discord.utils.get(guild.roles, name = "Aries")
        await member.add_roles(role)
    
    elif reaction == "♉":
        print("T")
        role = discord.utils.get(guild.roles, name = "Taurus")
        await member.add_roles(role)

    elif reaction == "♊":
        print("G")
        role = discord.utils.get(guild.roles, name = "Gemini")
        await member.add_roles(role)

    elif reaction == "♋":
        print("C")
        role = discord.utils.get(guild.roles, name = "Cancer")
        await member.add_roles(role)

    elif reaction == "♌":
        print("L")
        role = discord.utils.get(guild.roles, name = "Leo")
        await member.add_roles(role)

    elif reaction == "♍":
        print("V")
        role = discord.utils.get(guild.roles, name = "Virgo")
        await member.add_roles(role)

    elif reaction == "♎":
        print("LI")
        role = discord.utils.get(guild.roles, name = "Libra")
        await member.add_roles(role)

    elif reaction == "♏":
        print("SC")
        role = discord.utils.get(guild.roles, name = "Scorpio")
        await member.add_roles(role)

    elif reaction == "♐":
        print("SA")
        role = discord.utils.get(guild.roles, name = "Sagittarius")
        await member.add_roles(role)

    elif reaction == "♑":
        print("CA")
        role = discord.utils.get(guild.roles, name = "Capricorn")
        await member.add_roles(role)

    elif reaction == "♒":
        print("AQ")
        role = discord.utils.get(guild.roles, name = "Aquarius")
        await member.add_roles(role)
        
    elif reaction == "♓":
        print("PI")
        role = discord.utils.get(guild.roles, name = "Pisces")
        await member.add_roles(role)
    else:
        print("UHHHHHH")



@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(744817281871249428)

    reaction = payload.emoji
    reaction = str(reaction)
    member = payload.user_id
    
    member = guild.get_member(member)

    if str(payload.channel_id) != '744818329427902504':
        print("Wrong channel mate")
        return
    
    elif reaction == "🔔":
        print("DODO PROPER")
        role = discord.utils.get(guild.roles, name="Dodo Proper")
        await member.remove_roles(role)

    elif reaction == "🎵":
        role = discord.utils.get(guild.roles, name="DJ")
        print("DJ")
        await member.remove_roles(role)
    
    elif reaction == "🔣":
        print("MISC")
        role = discord.utils.get(guild.roles, name="--------------- Misc ---------------")
        await member.remove_roles(role)

    elif reaction == "🖌":
        print("COLOURS")
        role = discord.utils.get(guild.roles, name="--------------- Colours---------------")
        await member.remove_roles(role)


    elif reaction == "♈":
        print("ARIES")
        role = discord.utils.get(guild.roles, name = "Aries")
        await member.remove_roles(role)
    
    elif reaction == "♉":
        print("T")
        role = discord.utils.get(guild.roles, name = "Taurus")
        await member.remove_roles(role)

    elif reaction == "♊":
        print("G")
        role = discord.utils.get(guild.roles, name = "Gemini")
        await member.remove_roles(role)

    elif reaction == "♋":
        print("C")
        role = discord.utils.get(guild.roles, name = "Cancer")
        await member.remove_roles(role)

    elif reaction == "♌":
        print("L")
        role = discord.utils.get(guild.roles, name = "Leo")
        await member.remove_roles(role)

    elif reaction == "♍":
        print("V")
        role = discord.utils.get(guild.roles, name = "Virgo")
        await member.remove_roles(role)

    elif reaction == "♎":
        print("LI")
        role = discord.utils.get(guild.roles, name = "Libra")
        await member.remove_roles(role)

    elif reaction == "♏":
        print("SC")
        role = discord.utils.get(guild.roles, name = "Scorpio")
        await member.remove_roles(role)

    elif reaction == "♐":
        print("SA")
        role = discord.utils.get(guild.roles, name = "Sagittarius")
        await member.remove_roles(role)

    elif reaction == "♑":
        print("CA")
        role = discord.utils.get(guild.roles, name = "Capricorn")
        await member.remove_roles(role)

    elif reaction == "♒":
        print("AQ")
        role = discord.utils.get(guild.roles, name = "Aquarius")
        await member.remove_roles(role)
        
    elif reaction == "♓":
        print("PI")
        role = discord.utils.get(guild.roles, name = "Pisces")
        await member.remove_roles(role)
    else:
        print("UHHHHHH")
        
    

#Blackbox
client.run(os.environ['TOKEN'])
