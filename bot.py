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
msg_count = 0

#comment to get push
@client.event
async def on_ready():
    print("Bot is Ready")
    drinkwater.start()


@client.event
async def on_message_delete(message):
    if str(message.author.id) == "773081074418712576":
        return 
    embed=discord.Embed(title="{} deleted a message".format(message.author.name), description=message.content, color=0x968cec)
    embed.add_field(name= "Discord ID" ,value=message.author.id)
    embed.add_field(name= "Channel" ,value=message.channel)
    guild = client.get_guild(744817281871249428)
    channel = guild.get_channel(800965152132431892)
    await channel.send(embed=embed)


@client.event
async def on_message_edit(message_before, message_after):
    if str(message_before.author.id) == "773081074418712576":
        return

    elif len(list(message_before.content)) + len(list(message_after.content)) < 3500:
        embed_description = "**Old Message** \n" + message_before.content + "\n\n**New Message**\n" + message_after.content
        embed=discord.Embed(title="{} Edited A Message".format(message_before.author.name), description=embed_description, color=0x968cec)
        embed.add_field(name= "Discord ID" ,value=message_before.author.id)
        embed.add_field(name= "Channel" ,value=message_before.channel)
        guild = client.get_guild(744817281871249428)
        channel = guild.get_channel(800965152132431892)
        await channel.send(embed=embed)
    else:
        embed=discord.Embed(title="{} Edited A Message".format(message_before.author.name), description=message_before.content, color=0x968cec)
        embed.add_field(name= "Discord ID" ,value=message_before.author.id)
        embed.add_field(name= "Channel" ,value=message_before.channel)
        guild = client.get_guild(744817281871249428)
        channel = guild.get_channel(800965152132431892)
        await channel.send(embed=embed)

        embed=discord.Embed(title="{} New Message".format(message_after.author.name), description=message_after.content, color=0x968cec)
        embed.add_field(name= "Discord ID" ,value=message_after.author.id)
        embed.add_field(name= "Channel" ,value=message_after.channel)
        guild = client.get_guild(744817281871249428)
        channel = guild.get_channel(800965152132431892)
        await channel.send(embed=embed)



    


@tasks.loop(minutes=90)
async def drinkwater():
    messages = ["Water Time!", "It is water o'clock! Go drink some water!", "It is hydration time!",
                "Drink Water, or else. "]
    guild = client.get_guild(744817281871249428)
    channel = guild.get_channel(801326450396758076)
    timenow = str(datetime.datetime.now().time())
    timenow = timenow.split(':')
    print(int(timenow[0]))
    if ( 7 <= (int(timenow[0])) <= 12):
        await channel.send(f"Remember to sleep my fleurs")
    if ((int(timenow[0]) >= 17) or (int(timenow[0]) <= 8)):
        m = random.randint(0, 3)
        await channel.send(f"{messages[m]}")
    

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



# @client.command()
# async def addsongs(ctx, url):
#     try:
#         song = requests.get(f'{url}', timeout=5)
#     except:
#         await ctx.send("Could not establish a connection to the url, or url is invald")
#     db = mysql.connector.connect(
#         host=os.environ['HOST'],
#         user=os.environ['USER'],
#         password=os.environ['PASSWORD'],
#         database=os.environ['DATABASE']
#     )
#     c = db.cursor()
#     print(url)
#     c.execute(f"""INSERT INTO Songs
#                   VALUES ('{url}', 0)

#     """)
#     db.commit()
#     await ctx.send("Added")
#     c.close()
#     db.close()


@client.event
async def on_message(message):
    global msg_count
    msg_count += 1
    guild = client.get_guild(744817281871249428)
    channel = guild.get_channel(801326450396758076)
    if msg_count % 200 == 0:
        messages = ["HONK", "Duck Duck Duck GOOSE", "BRRRRZK", "Give me a - wait one sec phone call"]
        m = random.randint(0, 3)
        await channel.send(f"{messages[m]}")



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

    elif reaction == "🌱":
        role = discord.utils.get(guild.roles, name="she/her")
        await member.add_roles(role)

    elif reaction == "🌲":
        role = discord.utils.get(guild.roles, name="he/him")
        await member.add_roles(role)

    elif reaction == "🌴":
        role = discord.utils.get(guild.roles, name="they/them")
        await member.add_roles(role)

    elif reaction == "🌵":
        role = discord.utils.get(guild.roles, name="fae/faer")
        await member.add_roles(role)

    elif reaction == "🌿":
        role = discord.utils.get(guild.roles, name="ze/zir")
        await member.add_roles(role)

    elif reaction == "☘":
        role = discord.utils.get(guild.roles, name="xe/xem")
        await member.add_roles(role)

    elif reaction == "🌳":
        role = discord.utils.get(guild.roles, name="ze/hir")
        await member.add_roles(role)

    elif reaction == "🍃":
        role = discord.utils.get(guild.roles, name="any")
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

    elif reaction == "🌱":
        role = discord.utils.get(guild.roles, name="she/her")
        await member.remove_roles(role)

    elif reaction == "🌲":
        role = discord.utils.get(guild.roles, name="he/him")
        await member.remove_roles(role)

    elif reaction == "🌴":
        role = discord.utils.get(guild.roles, name="they/them")
        await member.remove_roles(role)

    elif reaction == "🌵":
        role = discord.utils.get(guild.roles, name="fae/faer")
        await member.remove_roles(role)

    elif reaction == "🌿":
        role = discord.utils.get(guild.roles, name="ze/zir")
        await member.remove_roles(role)

    elif reaction == "☘":
        role = discord.utils.get(guild.roles, name="xe/xem")
        await member.remove_roles(role)

    elif reaction == "🌳":
        role = discord.utils.get(guild.roles, name="ze/hir")
        await member.remove_roles(role)

    elif reaction == "🍃":
        role = discord.utils.get(guild.roles, name="any")
        await member.remove_roles(role)

    else:
        print("UHHHHHH")


# Blackbox
client.run(os.environ['TOKEN'])
