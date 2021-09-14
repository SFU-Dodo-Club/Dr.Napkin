import discord
import asyncio
import datetime
import os
import random
import mysql.connector
import requests
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='-', intents=intents)

#comment to get push
@client.event
async def on_ready():
    print("Bot is Ready")
    drinkwater.start()
    songOTD.start()
    


@tasks.loop(minutes=120)
async def drinkwater():
    messages = ["Time to grab a drink!", "It is water o'clock! Go drink water!", "It is water time!",
                "Drink Water or Else"]
    guild = client.get_guild(744817281871249428)
    channel = guild.get_channel(801326450396758076)
    timenow = str(datetime.datetime.now().time())
    timenow = timenow.split(':')
    print(int(timenow[0]))
    if ((int(timenow[0]) >= 17) or (int(timenow[0]) <= 8)):
        m = random.randint(0, 2)
        await channel.send(f"{messages[m]}")
    
    too = guild.get_member(183227077942706176)
    #ader = guild.get_member(632326508949798925)
    try:   
        await too.send("TOOOO")
    catch: #Debunking stackoverflow
        await too.send("TOOOOOOOO")
    #await ader.send("ADERRRRCHIII")


@tasks.loop(minutes=1440)
async def songOTD():
    db = mysql.connector.connect(
        host=os.environ['HOST'],
        user=os.environ['USER'],
        password=os.environ['PASSWORD'],
        database=os.environ['DATABASE']
    )
    c = db.cursor()
    c.execute(f"""SELECT datetimeyear FROM Songs

    """)
    datestored = ''.join(map(str, c.fetchall()[0]))
    datestored = int(datestored)
    c.close()
    db.close()
    todayDateD = datetime.datetime.today().strftime('%d')
    todayDateD = int(todayDateD)
    if datestored == todayDateD:
        pass
    else:
        db = mysql.connector.connect(
            host=os.environ['HOST'],
            user=os.environ['USER'],
            password=os.environ['PASSWORD'],
            database=os.environ['DATABASE']
        )
        c = db.cursor()
        c.execute(f"""SELECT songs_list FROM Songs
                    ORDER BY RAND()
                    LIMIT 3
    
        """)
        todaysSong = ''.join(map(str, c.fetchall()[1]))
        guild = client.get_guild(744817281871249428)
        channel = guild.get_channel(832025867471421480)
        todayDate = datetime.datetime.today().strftime('%Y-%m-%d')
        todayDate = str(todayDate)
        c.execute(f"""UPDATE Songs
                    SET datetimeyear = {todayDateD}

                """)
        db.commit()
        await channel.send(f"**{todayDate}: Song of the day**: {todaysSong} ")
        c.close()
        db.close()


@client.command()
async def addsongs(ctx, url):
    try:
        song = requests.get(f'{url}', timeout=5)
    except:
        await ctx.send("Could not establish a connection to the url, or url is invald")
    db = mysql.connector.connect(
        host=os.environ['HOST'],
        user=os.environ['USER'],
        password=os.environ['PASSWORD'],
        database=os.environ['DATABASE']
    )
    c = db.cursor()
    print(url)
    c.execute(f"""INSERT INTO Songs
                  VALUES ('{url}', 0)

    """)
    db.commit()
    await ctx.send("Added")
    c.close()
    db.close()


@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(744817281871249428)
    reaction = payload.emoji
    reaction = str(reaction)
    member = payload.user_id
    print(member)
    member = guild.get_member(member)

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
        role = discord.utils.get(guild.roles, name="Aries")
        await member.add_roles(role)

    elif reaction == "♉":
        print("T")
        role = discord.utils.get(guild.roles, name="Taurus")
        await member.add_roles(role)

    elif reaction == "♊":
        print("G")
        role = discord.utils.get(guild.roles, name="Gemini")
        await member.add_roles(role)

    elif reaction == "♋":
        print("C")
        role = discord.utils.get(guild.roles, name="Cancer")
        await member.add_roles(role)

    elif reaction == "♌":
        print("L")
        role = discord.utils.get(guild.roles, name="Leo")
        await member.add_roles(role)

    elif reaction == "♍":
        print("V")
        role = discord.utils.get(guild.roles, name="Virgo")
        await member.add_roles(role)

    elif reaction == "♎":
        print("LI")
        role = discord.utils.get(guild.roles, name="Libra")
        await member.add_roles(role)

    elif reaction == "♏":
        print("SC")
        role = discord.utils.get(guild.roles, name="Scorpio")
        await member.add_roles(role)

    elif reaction == "♐":
        print("SA")
        role = discord.utils.get(guild.roles, name="Sagittarius")
        await member.add_roles(role)

    elif reaction == "♑":
        print("CA")
        role = discord.utils.get(guild.roles, name="Capricorn")
        await member.add_roles(role)

    elif reaction == "♒":
        print("AQ")
        role = discord.utils.get(guild.roles, name="Aquarius")
        await member.add_roles(role)

    elif reaction == "♓":
        print("PI")
        role = discord.utils.get(guild.roles, name="Pisces")
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
        role = discord.utils.get(guild.roles, name="Aries")
        await member.remove_roles(role)

    elif reaction == "♉":
        print("T")
        role = discord.utils.get(guild.roles, name="Taurus")
        await member.remove_roles(role)

    elif reaction == "♊":
        print("G")
        role = discord.utils.get(guild.roles, name="Gemini")
        await member.remove_roles(role)

    elif reaction == "♋":
        print("C")
        role = discord.utils.get(guild.roles, name="Cancer")
        await member.remove_roles(role)

    elif reaction == "♌":
        print("L")
        role = discord.utils.get(guild.roles, name="Leo")
        await member.remove_roles(role)

    elif reaction == "♍":
        print("V")
        role = discord.utils.get(guild.roles, name="Virgo")
        await member.remove_roles(role)

    elif reaction == "♎":
        print("LI")
        role = discord.utils.get(guild.roles, name="Libra")
        await member.remove_roles(role)

    elif reaction == "♏":
        print("SC")
        role = discord.utils.get(guild.roles, name="Scorpio")
        await member.remove_roles(role)

    elif reaction == "♐":
        print("SA")
        role = discord.utils.get(guild.roles, name="Sagittarius")
        await member.remove_roles(role)

    elif reaction == "♑":
        print("CA")
        role = discord.utils.get(guild.roles, name="Capricorn")
        await member.remove_roles(role)

    elif reaction == "♒":
        print("AQ")
        role = discord.utils.get(guild.roles, name="Aquarius")
        await member.remove_roles(role)

    elif reaction == "♓":
        print("PI")
        role = discord.utils.get(guild.roles, name="Pisces")
        await member.remove_roles(role)
    else:
        print("UHHHHHH")


# Blackbox
client.run(os.environ['TOKEN'])
