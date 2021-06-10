import discord
import bs4
import random
import json
import requests
import numpy
import base64
import os 
import colorama
import aiohttp
import datetime
import time
import re
import io
import asyncio

# Separated (imports and froms)

from discord.ext import commands
from colorama import *
from requests import get
from bs4 import BeautifulSoup as bs4


colorama.init()


#####################
# Loads json config #
#####################

with open('config1.json') as f:
    config1 = json.load(f)
    
token = config1.get('token')
password = config1.get('password')
prefix = config1.get('prefix')
nitro_sniper = config1.get('nitro_sniper')
stream_url = config1.get('stream_url')
instagram = config1.get('instagram')
afk_message = config1.get('afk_message')






##########
# Colors #
##########

LIGHTRED = Fore.LIGHTRED_EX
LIGHTWHITE = Fore.LIGHTWHITE_EX
LIGHTYELLOW = Fore.LIGHTYELLOW_EX
LIGHTCYAN = Fore.LIGHTCYAN_EX
LIGHTGREEN = Fore.LIGHTGREEN_EX
LIGHTMAGENTA = Fore.LIGHTMAGENTA_EX
RESET = Fore.RESET



# Define Client
Poison = commands.Bot(command_prefix=prefix, self_bot=True)



# DEFS

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def Clear():
	os.system('cls')



start_time = datetime.datetime.utcnow()

###############
Poison.antiraid = False
Poison.msgsniper = True
Poison.slotbot_sniper = True
Poison.giveaway_sniper = True
Poison.mee6 = False
Poison.mee6_channel = None
Poison.yui_kiss_user = None
Poison.yui_kiss_channel = None
Poison.yui_hug_user = None
Poison.yui_hug_channel = None
Poison.sniped_message_dict = {}
Poison.sniped_edited_message_dict = {}
Poison.whitelisted_users = {}
Poison.copycat = None
Poison.remove_command('help') # removes Preset Help Command
################








@Poison.event
async def on_connect():
	if nitro_sniper:
		nitro = "Active"
	else:
		nitro = "Disabled"

	print(f'''
  {LIGHTGREEN}
 
				 ____  _____  ____  ___  _____  _  _ 
				(  _ \(  _  )(_  _)/ __)(  _  )( \( )
				 )___/ )(_)(  _)(_ \__ \ )(_)(  )  ( 
				(__)  (_____)(____)(___/(_____)(_)\_)

				{LIGHTMAGENTA}Logged in as: {LIGHTGREEN}{Poison.user.name}#{Poison.user.discriminator}{RESET}
				{LIGHTMAGENTA}Nitro Sniper: {LIGHTGREEN}{nitro}{RESET}
				{LIGHTMAGENTA}Prefix: {LIGHTGREEN}{prefix}{RESET} 

  
  
  ''')

Clear()






# On Message Command (Nitro, Givaway, Slotbot)
@Poison.event
async def on_message(message):
    if Poison.copycat is not None and Poison.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def GiveawayData():
        print(
            f"{LIGHTWHITE} - CHANNEL: {LIGHTGREEN}[{message.channel}]"
            f"\n{LIGHTWHITE} - SERVER: {LIGHTGREEN}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{LIGHTWHITE} - CHANNEL: {LIGHTGREEN}[{message.channel}]"
            f"\n{LIGHTWHITE} - SERVER: {LIGHTGREEN}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"{LIGHTWHITE} - CHANNEL: {LIGHTGREEN}[{message.channel}]"
            f"\n{LIGHTWHITE} - SERVER: {LIGHTGREEN}[{message.guild}]"
            f"\n{LIGHTWHITE} - AUTHOR: {LIGHTGREEN}[{message.author}]"
            f"\n{LIGHTWHITE} - ELAPSED: {LIGHTGREEN}[{elapsed}]"
            f"\n{LIGHTWHITE} - CODE: {LIGHTGREEN}{code}"
            + Fore.RESET)

    def Pick():
        print(
            f"{LIGHTWHITE} - CHANNEL: {LIGHTGREEN}[{message.channel}]"
            f"\n{LIGHTWHITE} - SERVER: {LIGHTGREEN}[{message.guild}]"
            + Fore.RESET)
            
    time = datetime.datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config1.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n{LIGHTMAGENTA}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{LIGHTMAGENTA}[{time} - Nitro Success]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{LIGHTMAGENTA}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if Poison.slotbot_sniper:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{LIGHTMAGENTA}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{LIGHTMAGENTA}[{time} - Slotbot Grabbed]" + Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if Poison.giveaway_sniper:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{LIGHTMAGENTA}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{LIGHTMAGENTA}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Poison.user.id}>' in message.content:
        if Poison.giveaway_sniper:
            if message.author.id == 294882584201003009:
                print(""
                      f"\n{LIGHTMAGENTA}[{time} - Giveaway Won]" + Fore.RESET)
                GiveawayData()
        else:
            return
    if 'Hey, Im pretty sure you want to see this Lootbox here.You all have **20 Seconds** to dispute it! Type ``pick`` for a chance to claim it!' in message.content:
        if Candy.slotbot_sniper:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('Pick')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{LIGHTMAGENTA}[{time} - Lootbox Invalid" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{LIGHTMAGENTA}[{time} - Lootbox Rolled]" + Fore.RESET)
                SlotBotData()
        else:
            return

    

    await Poison.process_commands(message)



# Edit Logger
@Poison.event
async def on_message_edit(before, after):
    if before.author.id == Poison.user.id:
        return
    if Poison.msgsniper:
        if before.content is after.content:
            return
        if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**_BEFORE_**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**_AFTER_**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(Poison.sniped_edited_message_dict) > 1000:
        Poison.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**_BEFORE_**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**_AFTER_**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Poison.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        Poison.sniped_edited_message_dict.update({channel_id: message_content})








@Poison.command()
async def help(ctx):
	await ctx.message.delete()
	embed = discord.Embed(title="**𝓟𝓸𝓲𝓼𝓸𝓷 𝓢𝓮𝓵𝓯𝓫𝓸𝓽**", description="``| ACCOUNT``\n``| TEXT``\n``| TOOLS``\n``| FUN``",color=discord.Color(random.randint(0, 0xffffff)))
	embed.set_image(url='https://images-ext-1.discordapp.net/external/uJrwjeaYPBe4H_c5y6SRH63ZCX3JNrBPPDStZUjcZ7g/http/cleanoffers.isis.careers/uploads/8ef1e546-dc33-4f76-a1b3-56b1d16196d4/dUKUtq4I.png')
	await ctx.send(embed=embed)


##################
#  Account Embed #
##################
  
@Poison.command()
async def account(ctx):
	await ctx.message.delete()
	embed = discord.Embed(title="**Account Commands**", description="``Stream [Status]``  >  Sets Streaming Status\n`Playing [Status]`  >  Sets Playing Status\n`Listening [Status]`  >  Sets Listening Status\n`Watching [Status]`  >  Sets Watching Status\n`Read`  >  Marks All Messages As Read\n`Adminservers`  >  Shows All Servers You Are Admin In\n", color=discord.Color(random.randint(0, 0xffffff)))
	embed.set_image(url='https://images-ext-1.discordapp.net/external/uJrwjeaYPBe4H_c5y6SRH63ZCX3JNrBPPDStZUjcZ7g/http/cleanoffers.isis.careers/uploads/8ef1e546-dc33-4f76-a1b3-56b1d16196d4/dUKUtq4I.png')
	await ctx.send(embed=embed)


#### Account Commands




# Stream Command

@Poison.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await Poison.change_presence(activity=stream)



# Playing Command

@Poison.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Poison.change_presence(activity=game)


# Listening Command

@Poison.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await Poison.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))


# Watching Command

@Poison.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Poison.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))



# Stop All Activity Command

@Poison.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await Poison.change_presence(activity=None, status=discord.Status.dnd)


# Read Command
@Poison.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    for guild in Poison.guilds:
        await guild.ack()


# Admin Servers

@Poison.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in Poison.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    embed = discord.Embed(title="*Servers Admin In*", description=f"{adminPermServers}\n{botPermServers}\n{banPermServers}\n{kickPermServers}", color=discord.Color(random.randint(0, 0xffffff)))
    await ctx.send(embed=embed)





###############
# Tools Embed #
###############

@Poison.command()
async def tools(ctx):
	await ctx.message.delete()
	embed = discord.Embed(title="**Tools Commands**", description="`Pscan [IP]` > Port Scans IP\n`Geoip [IP]` > Looks Up IP\n`Editsnipe` > Shows Last Edited Message\n`Snipe` > Shows Last Deleted Message\n`Purge [Amount]` > Purges An Amount Of Messages\n`Toxic` > Sends A Huge Blank Message\n`Snapcheck [Username]` > Checks Availability Of Snapchat Username\n`Bump [Channel ID]` > Sends Disboard Bump Every 2 Hours\n`Pfp` > Sends Av Of Yourself Or Someone Else", color=discord.Color(random.randint(0, 0xffffff)))
	embed.set_image(url='https://images-ext-1.discordapp.net/external/uJrwjeaYPBe4H_c5y6SRH63ZCX3JNrBPPDStZUjcZ7g/http/cleanoffers.isis.careers/uploads/8ef1e546-dc33-4f76-a1b3-56b1d16196d4/dUKUtq4I.png')
	await ctx.send(embed=embed)

# PFP

@Poison.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))


# Disboard Auto Bump

@Poison.command(aliases=['bump'])
async def _auto_bump(ctx, channelid): 
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            channel = Poison.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f" {LIGHTCYAN}Poison {LIGHTWHITE}> {LIGHTGREEN}Sent Bump Number: {count}\n")
            await asyncio.sleep(7200)
        except Exception as e:
        	pass


@Poison.command()
async def snapcheck(ctx):
  await ctx.message.delete()
  msg = ctx.message.content.split("snapcheck", 1)
  username = msg[1]
  headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://accounts.snapchat.com/",
        "Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
	}

  url = "https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={}&xsrf_token=PlEcin8s5H600toD4Swngg".format(username)
  r = requests.post(url, headers=headers)
  data = r.json()
  status = data.get("reference").get("status_code")

  if status == "OK":
    await ctx.send(f"Username {username} Is Available")
    
  
  elif status == "TAKEN":
    await ctx.send(f"Username {username} Is Taken")
  


# Blank Chat
@Poison.command(pass_context=True)
async def toxic(ctx): #this bitch is toxic -Poison
 await ctx.message.delete()
 await ctx.send('ﾠﾠ'+'\n' * 1000 + 'ﾠﾠ')



#Purge
@Poison.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Poison.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass


# Deleted Snipe 
@Poison.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Poison.sniped_message_dict:
        await ctx.send(Poison.sniped_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!")



# Edit Sniper
@Poison.command(aliases=["esnipe"])
async def editsnipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Poison.sniped_edited_message_dict:
        await ctx.send(Poison.sniped_edited_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!")




# Ip Lookup
@Poison.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed(color=discord.Color(random.randint(0, 0xffffff)))
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)


# Port Scanner
@Poison.command()
async def pscan(ctx, arg1):
    print(f" {LIGHTCYAN}poison {LIGHTWHITE}> {LIGHTGREEN}Send IP INFO\n") 
    await ctx.message.delete()
    scanyuh = get("https://api.hackertarget.com/nmap/?q=%s" % arg1)
    result = scanyuh.text.strip("   ")
    embed = discord.Embed(title="**Port Scan Results**", description=f"{result}", color=discord.Color(random.randint(0, 0xffffff)))
    await ctx.send(embed=embed)







##############
# TEXT EMBED #
##############


@Poison.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)


@Poison.command()
async def text(ctx):
	await ctx.message.delete()
	embed = discord.Embed(title="**Text Commands**", description="`Msgniper [ON/OFF]`  >  Turns On and Off Message Sniper\n`Reverse [Text]` > Reverse Text\n`Shrug` > Sends Shrug\n`Lenny` > Sends Lenny Face\n`Tableflip` > Flips Table\n`Unflip` > Unflips Table\n`Bold [Text]` > Makes Bold Text\n`Censor [Text]` > Censors Text\n`Underline [Text]` > Underline Text\n`Italicize [Text]` > Italicize Text\n`Strike [Text]` > Strikethrough Text\n`Quote [Text]` > Quote Text\n`Code [Text]` > Makes Code Text\n", color=discord.Color(random.randint(0, 0xffffff)))
	embed.set_image(url='https://images-ext-1.discordapp.net/external/uJrwjeaYPBe4H_c5y6SRH63ZCX3JNrBPPDStZUjcZ7g/http/cleanoffers.isis.careers/uploads/8ef1e546-dc33-4f76-a1b3-56b1d16196d4/dUKUtq4I.png')
	await ctx.send(embed=embed)


@Poison.command()
async def strike(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('~~' + message + '~~')


@Poison.command()
async def quote(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('> ' + message)


@Poison.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('`' + message + "`")



@Poison.command()
async def censor(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')


@Poison.command()
async def underline(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('__' + message + '__')


@Poison.command()
async def italicize(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')



@Poison.command(aliases=["fliptable"])
async def tableflip(ctx):
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@Poison.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)


@Poison.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')



# Lenny 
@Poison.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)



# Shrug
@Poison.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)


# Reverse Text
@Poison.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)



# Message Logger

@Poison.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        Poison.msgsniper = True
        await ctx.send('Poison Message-Sniper is now **enabled**')
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        Poison.msgsniper = False
        await ctx.send('Poison Message-Sniper is now **disabled**')



# FUN EMBED
@Poison.command()
async def fun(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Fun Commands**", description="`Cum` > Emoji Man Cumming :D\n`Copycat [User]` > Copys Users Messages In Chat\n`Stopcopycat` > Stops Copying User\n`Wyr` > Sends A Would You Rather Question\n`911` > Bombs The Twin Towers :D\n`Dick` > Sends Dick Size", color=discord.Color(random.randint(0, 0xffffff)))
    embed.set_image(url='https://images-ext-1.discordapp.net/external/uJrwjeaYPBe4H_c5y6SRH63ZCX3JNrBPPDStZUjcZ7g/http/cleanoffers.isis.careers/uploads/8ef1e546-dc33-4f76-a1b3-56b1d16196d4/dUKUtq4I.png')
    await ctx.send(embed=embed)


@Poison.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): 
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D")
    await ctx.send(embed=em)


#911
@Poison.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')


# Would You Rather
@Poison.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):  
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    message = await ctx.send(f"{qa}\nor\n{qb}")
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")

# Stop Copycat
@Poison.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if Poison.user is None:
        await ctx.send("You weren't copying anyone to begin with")
        return
    await ctx.send("Stopped copying " + str(Poison.copycat))
    Poison.copycat = None

# Copycat
@Poison.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User):
    await ctx.message.delete()
    Poison.copycat = user
    await ctx.send("Now copying " + str(Poison.copycat))


#CUM
@Poison.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')



















# For Message Logger ##################
@Poison.event
async def on_message_delete(message):
    if message.author.id == Poison.user.id:
        return
    if Poison.msgsniper:
        if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(Poison.sniped_message_dict) > 1000:
        Poison.sniped_message_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
            message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Poison.sniped_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
            message.content) + "\n\n**Attachments:**\n" + links
        Poison.sniped_message_dict.update({channel_id: message_content})
#############################################################

Poison.run(token, bot=False)
