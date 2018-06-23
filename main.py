#Discord Imports
import discord
from discord.ext import commands
import discord.utils
#Other Imports
import traceback #to see the error while in Discord
import random # for randomizing things
from random import randint # randints
import requests # for APIs
import aiohttp # fetching client sessions or stuff
import sys #for system-specific parameters and functions
import re # for regular expression operations
import json # self-explanatory kek
import time # also self-explanatory le
import asyncio #tasks and such
import os # operating system stuff and heroku
import datetime # self-explanatory too lol

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='The one, and only: The Bot, created by Pointless#1278.', self_bot=False,)
bot.remove_command('help')

start_time = time.time()
starttime2 = time.ctime(int(time.time()))

def pointcheck(ctx):
    return ctx.message.author.id == '276043503514025984' #checks if @Pointless#1278 is the author of the command

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='!help | {} servers'.format(len(bot.servers))), status='online')
    print('Online.')
    print('https://discordapp.com/oauth2/authorize?client_id=431951773159129098&scope=bot&permissions=2146958591')


'''
:'#######::'##:::::'##:'##::: ##:'########:'########::                                                                          
'##.... ##: ##:'##: ##: ###:: ##: ##.....:: ##.... ##:                                                                          
 ##:::: ##: ##: ##: ##: ####: ##: ##::::::: ##:::: ##:                                                                          
 ##:::: ##: ##: ##: ##: ## ## ##: ######::: ########::                                                                          
 ##:::: ##: ##: ##: ##: ##. ####: ##...:::: ##.. ##:::                                                                          
 ##:::: ##: ##: ##: ##: ##:. ###: ##::::::: ##::. ##::                                                                          
. #######::. ###. ###:: ##::. ##: ########: ##:::. ##:                                                                          
:.......::::...::...:::..::::..::........::..:::::..::  '''
@bot.command(pass_context=True)
@commands.check(pointcheck)
async def say(ctx, *, text: str = None):
    await bot.delete_message(ctx.message)
    await bot.say(text)

@bot.command(pass_context=True)
@commands.check(pointcheck)
async def restart(ctx):
    await bot.delete_message(ctx.message)
    embed = discord.Embed(title='Restart',description=f'Sorry, but {ctx.message.author.mention} has forced me to restart. It\'ll only take a moment!',color=0xFF0000)
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=embed)
    await bot.logout()

'''
'##::::'##:'########:'##:::::::'########::                                                                                      
 ##:::: ##: ##.....:: ##::::::: ##.... ##:                                                                                      
 ##:::: ##: ##::::::: ##::::::: ##:::: ##:                                                                                      
 #########: ######::: ##::::::: ########::                                                                                      
 ##.... ##: ##...:::: ##::::::: ##.....:::                                                                                      
 ##:::: ##: ##::::::: ##::::::: ##::::::::                                                                                      
 ##:::: ##: ########: ########: ##::::::::                                                                                      
..:::::..::........::........::..:::::::::     '''
@bot.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title='Help', description='Find all commands here!', color=0x2874A6)
    embed.add_field(name='General',value='`ping` | `prefixes`')
    embed.add_field(name='Informational',value='`urban`| `cryptocurrency`')
    embed.add_field(name='Fun',value='`comic` | `cat` | `dog` | `coinflip` | `8ball` | `chucknorris` | `roll` | `joke`')
    embed.add_field(name='BoomBot',value='`info`')
    embed.add_field(name='Moderation',value='`kick` | `ban` | `unban` | `mute` | `unmute` | `softban` | `hackban` | `purge`')
    embed.add_field(name='Managing',value='`giverole` | `takerole`')
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=embed)

'''
:'######:::'########:'##::: ##:'########:'########:::::'###::::'##:::::::                                                       
'##... ##:: ##.....:: ###:: ##: ##.....:: ##.... ##:::'## ##::: ##:::::::                                                       
 ##:::..::: ##::::::: ####: ##: ##::::::: ##:::: ##::'##:. ##:: ##:::::::                                                       
 ##::'####: ######::: ## ## ##: ######::: ########::'##:::. ##: ##:::::::                                                       
 ##::: ##:: ##...:::: ##. ####: ##...:::: ##.. ##::: #########: ##:::::::                                                       
 ##::: ##:: ##::::::: ##:. ###: ##::::::: ##::. ##:: ##.... ##: ##:::::::                                                       
. ######::: ########: ##::. ##: ########: ##:::. ##: ##:::: ##: ########:                                                       
:......::::........::..::::..::........::..:::::..::..:::::..::........::        '''
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.delete_message(ctx.message)
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await bot.send_typing(channel)
    t2 = time.perf_counter()
    embed=discord.Embed(title='Ping',description='Pong! {} milliseconds.'.format(round((t2-t1)*1000)), color=0x00FF00)
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def prefixes(ctx):
    await bot.delete_message(ctx.message)
    embed=discord.Embed(title='Prefixes',description='You can mention me, as a prefix, or use \'!\'.',color=0x00FF00)
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=embed)

'''
'####:'##::: ##:'########::'#######::'########::'##::::'##::::'###::::'########:'####::'#######::'##::: ##::::'###::::'##:::::::
. ##:: ###:: ##: ##.....::'##.... ##: ##.... ##: ###::'###:::'## ##:::... ##..::. ##::'##.... ##: ###:: ##:::'## ##::: ##:::::::
: ##:: ####: ##: ##::::::: ##:::: ##: ##:::: ##: ####'####::'##:. ##::::: ##::::: ##:: ##:::: ##: ####: ##::'##:. ##:: ##:::::::
: ##:: ## ## ##: ######::: ##:::: ##: ########:: ## ### ##:'##:::. ##:::: ##::::: ##:: ##:::: ##: ## ## ##:'##:::. ##: ##:::::::
: ##:: ##. ####: ##...:::: ##:::: ##: ##.. ##::: ##. #: ##: #########:::: ##::::: ##:: ##:::: ##: ##. ####: #########: ##:::::::
: ##:: ##:. ###: ##::::::: ##:::: ##: ##::. ##:: ##:.:: ##: ##.... ##:::: ##::::: ##:: ##:::: ##: ##:. ###: ##.... ##: ##:::::::
'####: ##::. ##: ##:::::::. #######:: ##:::. ##: ##:::: ##: ##:::: ##:::: ##::::'####:. #######:: ##::. ##: ##:::: ##: ########:
....::..::::..::..:::::::::.......:::..:::::..::..:::::..::..:::::..:::::..:::::....:::.......:::..::::..::..:::::..::........::'''

@bot.command(pass_context=True, aliases=['urbandictionary','urbandict','udict','udictionary','udefine','urbandefine'])
async def urban(ctx,*msg):
    await bot.delete_message(ctx.message)
    word = ' '.join(msg)
    api = "http://api.urbandictionary.com/v0/define"
    response = requests.get(api, params=[("term", word)]).json()
    if len(response["list"]) == 0: return await bot.say("Could not find that word!")
    embed = discord.Embed(title=":mag: Search Word", description=word,color=0x00FF00)
    embed.add_field(name= "Top definition",value=response['list'][0]['definition'])
    embed.add_field(name= "Examples",value=response['list'][0]["example"])
    embed.add_field(name= 'Author',value=response['list'][0]['author'])
    embed.add_field(name= 'Thumbs Up',value=response['list'][0]['thumbs_up'])
    embed.add_field(name= 'Thumbs Down',value=response['list'][0]['thumbs_down'])
    embed.set_footer(text = "Tags: " + ', '.join(response['tags']))
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed = embed)

@bot.command(pass_context=True, aliases=['cc'])
async def cryptocurrency(ctx):
    if ctx.invoked_subcommand is None:
        await bot.delete_message(ctx.message)
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.coinmarketcap.com/v2/ticker/') as r:
                data = await r.json()
                embed=discord.Embed(title='Cryptocurrency', description='Here is the top three calculated by CoinMarketCap:\n\n{}. {} ({}): ${}\n{}. {} ({}): ${}\n{}. {} ({}): ${}'.format(data['data']['1']['rank'],data['data']['1']['name'],data['data']['1']['symbol'],data['data']['1']['quotes']['USD']['price'],data['data']['1027']['rank'],data['data']['1027']['name'],data['data']['1027']['symbol'],data['data']['1027']['quotes']['USD']['price'],data['data']['52']['rank'],data['data']['52']['name'],data['data']['52']['symbol'],data['data']['52']['quotes']['USD']['price']), color=0x00FF00)
                embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
                await bot.say(embed=embed)
    else:
        pass


'''
'########:'##::::'##:'##::: ##:                                                                                                 
 ##.....:: ##:::: ##: ###:: ##:                                                                                                 
 ##::::::: ##:::: ##: ####: ##:                                                                                                 
 ######::: ##:::: ##: ## ## ##:                                                                                                 
 ##...:::: ##:::: ##: ##. ####:                                                                                                 
 ##::::::: ##:::: ##: ##:. ###:                                                                                                 
 ##:::::::. #######:: ##::. ##:                                                                                                 
..:::::::::.......:::..::::..:: '''
@bot.command(pass_context=True, no_pm=True)
async def comic(ctx):
    await bot.delete_message(ctx.message)
    api = "https://xkcd.com/{}/info.0.json".format(random.randint(1, 1800))
    async with aiohttp.ClientSession() as session:
        async with session.get(api) as r:
            response = await r.json()
            embed = discord.Embed(title="Comic", description=response["title"], color=0x00FF00)
            embed.set_image(url=response["img"])
            embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            await bot.say(embed=embed)

@bot.command(pass_context=True)
async def cat(ctx):
    api = 'https://aws.random.cat/meow'
    async with aiohttp.ClientSession() as session:
        async with session.get(api) as r:
            if r.status == 200:
                response = await r.json()
                embed = discord.Embed(title="Cat", description="Here's your random cat image", color=0x00FF00)
                embed.set_author(name=f"{ctx.message.author.display_name}", icon_url=f"{ctx.message.author.avatar_url}")
                embed.set_image(url=response['file'])
                await bot.say(embed=embed)
            else:
                embed1 = discord.Embed(title='Error',description='I could not access the random.cat API!',color=0xFF0000)
                embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
                bot.say(embed=embed1)
                

@bot.command(pass_context=True)
async def dog(ctx):
    await bot.delete_message(ctx.message)
    api = "https://api.thedogapi.co.uk/v2/dog.php"
    async with aiohttp.ClientSession() as session:
        async with session.get(api) as r:
            if r.status == 200:
                response = await r.json()
                embed = discord.Embed(title="Dog", description="Here's your random Dog", color=0xFF0000)
                embed.set_author(name=f"{ctx.message.author.display_name}", icon_url=f"{ctx.message.author.avatar_url}")
                embed.set_image(url=response['data'][0]["url"])
                await bot.say(embed=embed)
            else:
                embed1 = discord.Embed(title='Error', description='I could not access thedogapi.co.uk!',color=0xFF0000)
                embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
                bot.say(embed=embed1)

@bot.command(pass_context=True)
async def coinflip(ctx):
    await bot.delete_message(ctx.message)
    choice = random.choice(['Heads!','Tails!'])
    embed = discord.Embed(title='Coinflip',description=choice,color=0x00FF00)
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=embed)

@bot.command(name="8ball", pass_context=True, aliases=['eightball'])
async def _8ball(ctx, question : str= None):
    await bot.delete_message(ctx.message)
    responses = [["Signs point to yes.", "Yes.", "Without a doubt.", "As I see it, yes.", "You may rely on it.", "It is decidedly so.", "Yes - definitely.", "It is certain.", "Most likely.", "Outlook good."],
    ["Reply hazy, try again.", "Concentrate and ask again.", "Better not tell you now.", "Cannot predict now.", "Ask again later."],
    ["My sources say no.", "Outlook not so good.", "Very doubtful.", "My reply is no.", "Don't count on it."]]
    embed = discord.Embed(title='8Ball',description=':8ball:' + random.choice(random.choice(responses)),color=0x00FF00)
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed1 = discord.Embed(title='8Ball',description='Make sure to put a question mark and add quotation marks on both sides of the question.',color=0xFF0000)
    embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    if "?" in question:
        await bot.say(embed=embed)
    else:
        await bot.say(embed=embed1)

@bot.command(pass_context=True)
async def chucknorris(ctx):
    await bot.delete_message(ctx.message)
    r = requests.get('https://api.chucknorris.io/jokes/random')
    embed = discord.Embed(title='Chuck Norris Facts', description=r.json()['value'], color=0x00FF00)
    embed.set_image(url='https://assets.chucknorris.host/img/avatar/chuck-norris.png')
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=embed)

@bot.command(pass_context=True, aliases=['rolls','dice','gamedie','die'])
async def roll(ctx, number: int=6):
    await bot.delete_message(ctx.message)
    if number > 1:
        embed = discord.Embed(title='Roll',description=f':game_die: {randint(1,number)}',color=0x00FF00)
        embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=embed)
    else:
        embed1 = discord.Embed(title='Error',description=f'Please insert a number higher than one.',color=0xFF0000)
        embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=embed1)

@bot.command(pass_context=True)
async def joke(ctx):
    await bot.delete_message(ctx.message)
    r = requests.get('https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke')
    embed = discord.Embed(title=r.json()['setup'], description=r.json()['punchline'], color=0x00FF00)
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=embed)

'''
'########:::'#######:::'#######::'##::::'##:'########:::'#######::'########:                                                    
 ##.... ##:'##.... ##:'##.... ##: ###::'###: ##.... ##:'##.... ##:... ##..::                                                    
 ##:::: ##: ##:::: ##: ##:::: ##: ####'####: ##:::: ##: ##:::: ##:::: ##::::                                                    
 ########:: ##:::: ##: ##:::: ##: ## ### ##: ########:: ##:::: ##:::: ##::::                                                    
 ##.... ##: ##:::: ##: ##:::: ##: ##. #: ##: ##.... ##: ##:::: ##:::: ##::::                                                    
 ##:::: ##: ##:::: ##: ##:::: ##: ##:.:: ##: ##:::: ##: ##:::: ##:::: ##::::                                                    
 ########::. #######::. #######:: ##:::: ##: ########::. #######::::: ##::::                                                    
........::::.......::::.......:::..:::::..::........::::.......::::::..:::::    '''

@bot.command(pass_context=True, aliases=['botinfo','information','botinformation','binfo','boti','binformation','about'])
async def info(ctx):
    await bot.delete_message(ctx.message)
    second = time.time() - start_time
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)
    embed = discord.Embed(description= '',title = 'Information', colour = 0x00FF00)
    embed.add_field(name = '__Information__', value = f"The Bot is just an ordinary, multi-purpose bot that is really fun, made with Python (aka the best programming language ever made) for Discord. This bot used to be called CommuniBot, and before that: PointBot. CommuniBot was archived because I really didn't care enough anymore about it and it died, so I decided - for no reason - to make a new one! Perhaps because I was really bored... :P", inline=True)
    embed.add_field(name = '__Status__', value = f"Uptime: I've been online for %d week(s), %d day(s), %d hour(s), %d minute(s), %d second(s)!" % (week, day, hour, minute, second) + "\nTotal Servers: {} servers.".format(len(bot.servers)), inline=True)
    embed.add_field(name = '__Links__', value = f"[Invite](https://discordapp.com/oauth2/authorize?client_id=431951773159129098&scope=bot&permissions=2146958591)\n[Support Server](https://discord.gg/6Z6Xx)", inline=True)
    embed.add_field(name = '__Credit__', value = f"<@276043503514025984> - Created the the bot.", inline=True)
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed = embed)

'''
'##::::'##::'#######::'########::'########:'########:::::'###::::'########:'####::'#######::'##::: ##:                          
 ###::'###:'##.... ##: ##.... ##: ##.....:: ##.... ##:::'## ##:::... ##..::. ##::'##.... ##: ###:: ##:                          
 ####'####: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##::'##:. ##::::: ##::::: ##:: ##:::: ##: ####: ##:                          
 ## ### ##: ##:::: ##: ##:::: ##: ######::: ########::'##:::. ##:::: ##::::: ##:: ##:::: ##: ## ## ##:                          
 ##. #: ##: ##:::: ##: ##:::: ##: ##...:::: ##.. ##::: #########:::: ##::::: ##:: ##:::: ##: ##. ####:                          
 ##:.:: ##: ##:::: ##: ##:::: ##: ##::::::: ##::. ##:: ##.... ##:::: ##::::: ##:: ##:::: ##: ##:. ###:                          
 ##:::: ##:. #######:: ########:: ########: ##:::. ##: ##:::: ##:::: ##::::'####:. #######:: ##::. ##:                          
..:::::..:::.......:::........:::........::..:::::..::..:::::..:::::..:::::....:::.......:::..::::..::   '''
@bot.command(pass_context = True)
async def kick(ctx, *, member : discord.Member=None):
    await bot.delete_message(ctx.message)
    if not ctx.message.author.server_permissions.kick_members:
        embed=discord.Embed(title='Error',description='You don\'t have the kick_members permission.', color=0xFF0000)
        embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=embed)
        return
    if not member:
        embed1=discord.Embed(title='Error',description='You have to specify a user to kick.', color=0xFF0000)
        embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=embed1)
    try:
        await bot.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            embed2=discord.Embed(title='Error',description='The person you are trying to kick has high permissions.', color=0xFF0000)
            embed2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=embed2)
    embed3 = discord.Embed(title='Kick',description =f"**%s** has been kicked!"%member.name, color = 0x00FF00)
    embed3.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed = embed3)

@bot.command(pass_context = True)
async def ban(ctx, *,member : discord.Member=None):
    await bot.delete_message(ctx.message)
    if not ctx.message.author.server_permissions.ban_members:
        embed=discord.Embed(title='Error',description='You don\'t have the ban_members permission.', color=0xFF0000)
        embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=embed)
        return
    if not member:
        embed1=discord.Embed(title='Error',description='You have to specify a user to ban.', color=0xFF0000)
        embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=embed1)
    try:
        await bot.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            embed2=discord.Embed(title='Error',description='The person you are trying to ban has high permissions.', color=0xFF0000)
            embed2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=embed2)
        else:
            pass
    embed3 = discord.Embed(title='Ban',description =f"**%s** has been banned!"%member.name, color = 0x00FF00)
    embed3.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed = embed3)

@bot.command(pass_context = True)
async def unban(ctx, *, member : discord.Member=None):
    await bot.delete_message(ctx.message)
    if not ctx.message.author.server_permissions.ban_members:
        embed=discord.Embed(title='Error',description='You don\'t have the ban_members permission.', color=0xFF0000)
        embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=embed)
        return
    if not member:
        embed1=discord.Embed(title='Error',description='You have to specify a user to unban.', color=0xFF0000)
        embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=embed1)
    try:
        await bot.unban(member.server,member)
    except:
        return
    embed3=discord.Embed(title='Unban',description=f"**%s** has been unbanned!"%member.name, color=0x00FF00)
    embed3.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed = embed3)

@bot.command(pass_context = True)
async def softban(ctx, *,member : discord.Member=None):
    await bot.delete_message(ctx.message)
    if not ctx.message.author.server_permissions.ban_members:
        embed=discord.Embed(title='Error',description='You don\'t have the ban_members permission.', color=0xFF0000)
        embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=embed)
        return
    if not member:
        embed1=discord.Embed(title='Error',description='You have to specify a user to soft-ban.', color=0xFF0000)
        embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=embed1)
    try:
        await bot.ban(member)
        await bot.unban(member.server,member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            embed2=discord.Embed(title='Error',description='The person you are trying to soft-ban has high permissions.', color=0xFF0000)
            embed2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=embed2)
        else:
            pass
    
    embed3 = discord.Embed(title='Ban',description =f"**%s** has been soft-banned!"%member.name, color = 0x00FF00)
    embed3.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed = embed3)

@bot.command(pass_context=True, aliases=['purge','prune'])  
async def clear(ctx, amount:int):
    await bot.delete_message(ctx.message)
    if not ctx.message.author.server_permissions.manage_messages:
        embed=discord.Embed(title='Error',description='You don\'t have the manage_messages permission.', color=0xFF0000)
        embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=embed)
        return
    if amount < 1:
        embed2=discord.Embed(title='Error',description='Please put in a number more than 1.',color=0xFF0000)
        await bot.say(embed=embed2)
    deleted = await bot.purge_from(ctx.message.channel, limit=amount)
    await asyncio.sleep(3)
    try:
        embed1=discord.Embed(title='Clear',description='I have cleared {} messages.'.format(len(deleted)),color=0x00FF00)
        embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=embed1)
    except:
        pass

@bot.command(pass_context=True, no_pm=True)
async def mute(ctx, *, member : discord.Member):
    await bot.delete_message(ctx.message)
    if not ctx.message.author.server_permissions.manage_messages:
        embed1 = discord.Embed(title='Error',description ='You don\'t have the manage_messages permission.', color = 0xFF0000)
        embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=embed1)
    else:  
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
        await bot.delete_message(ctx.message)
    embed = discord.Embed(title='Mute',description = "**%s** has been muted!"%member.name, color = 0x00FF00)
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=embed)

@bot.command(pass_context=True, no_pm=True)
async def unmute(ctx, *, member : discord.Member):
    await bot.delete_message(ctx.message)
    if not ctx.message.author.server_permissions.manage_messages:
        embed1 = discord.Embed(title='Error',description ='You don\'t have the manage_messages permission.', color = 0xFF0000)
        embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=embed1)
    else:  
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
        await bot.delete_message(ctx.message)
    embed = discord.Embed(title='Unmute',description = "**%s** has been unmuted!"%member.name, color = 0x00FF00)
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=embed)

'''
'##::::'##::::'###::::'##::: ##::::'###:::::'######:::'####:'##::: ##::'######:::                                               
 ###::'###:::'## ##::: ###:: ##:::'## ##:::'##... ##::. ##:: ###:: ##:'##... ##::                                               
 ####'####::'##:. ##:: ####: ##::'##:. ##:: ##:::..:::: ##:: ####: ##: ##:::..:::                                               
 ## ### ##:'##:::. ##: ## ## ##:'##:::. ##: ##::'####:: ##:: ## ## ##: ##::'####:                                               
 ##. #: ##: #########: ##. ####: #########: ##::: ##::: ##:: ##. ####: ##::: ##::                                               
 ##:.:: ##: ##.... ##: ##:. ###: ##.... ##: ##::: ##::: ##:: ##:. ###: ##::: ##::                                               
 ##:::: ##: ##:::: ##: ##::. ##: ##:::: ##:. ######:::'####: ##::. ##:. ######:::                                               
..:::::..::..:::::..::..::::..::..:::::..:::......::::....::..::::..:::......::::    '''

@bot.command(pass_context=True, no_pm=True)
async def giverole(ctx, user: discord.Member, *, role:str=None):
    await bot.delete_message(ctx.message)
    if ctx.message.author.server_permissions.manage_roles:
        await bot.add_roles(user, discord.utils.get(ctx.message.server.roles, name=role))
        embed1 = discord.Embed(title='Add role',description = 'I added the role ' + str(role) + ' to ' + str(user) + '.', color = 0x00FF00)
        embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed = embed1)
    else:
        embed2 = discord.Embed(title='Error',description = 'You don\'t have the manage_roles permission.', color = 0xFF0000)
        embed2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed = embed2)

@bot.command(pass_context=True, no_pm=True,aliases=[])
async def takerole(ctx, user: discord.Member, *, role:str=None):
    await bot.delete_message(ctx.message)
    if ctx.message.author.server_permissions.manage_roles:
        await bot.remove_roles(user, discord.utils.get(ctx.message.server.roles, name=role))
        embed1 = discord.Embed(title='Add role',description = 'I removed the role ' + str(role) + ' from ' + str(user) + '.', color = 0x00FF00)
        embed1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed = embed1)
    else:
        embed2 = discord.Embed(title='Error',description = 'You don\'t have the manage_roles permission.', color = 0xFF0000)
        embed2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed = embed2)

if not os.environ.get('TOKEN'):
   print("No tokens!")
bot.run(os.environ.get('TOKEN').strip('"'))
