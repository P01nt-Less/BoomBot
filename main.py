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
async def help(ctx,c):
    if c == None:
        embed=discord.Embed(title='Help', description='Find all commands here!', color=0x2874A6)
        embed.add_field(name='General',value='`ping` | `prefixes`')
        embed.add_field(name='Informational',value='`urban`| `cryptocurrency`')
        embed.add_field(name='Fun',value='Nothing')
        embed.add_field(name='BoomBot',value='`info`')
        embed.add_field(name='Moderation',value='`kick` | `ban` | `unmute` | `softban` |')
        embed.add_field(name='Managing',value='`giverole` | `takerole`')
        embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=embed)
    else:
        return bot.say('Checking help for each command is not done yet. Check later.')
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
        async with aiohttp.ClientSession() as api:
            async with api.get('https://api.coinmarketcap.com/v2/ticker/') as r:
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


'''
'########:::'#######:::'#######::'##::::'##:'########:::'#######::'########:                                                    
 ##.... ##:'##.... ##:'##.... ##: ###::'###: ##.... ##:'##.... ##:... ##..::                                                    
 ##:::: ##: ##:::: ##: ##:::: ##: ####'####: ##:::: ##: ##:::: ##:::: ##::::                                                    
 ########:: ##:::: ##: ##:::: ##: ## ### ##: ########:: ##:::: ##:::: ##::::                                                    
 ##.... ##: ##:::: ##: ##:::: ##: ##. #: ##: ##.... ##: ##:::: ##:::: ##::::                                                    
 ##:::: ##: ##:::: ##: ##:::: ##: ##:.:: ##: ##:::: ##: ##:::: ##:::: ##::::                                                    
 ########::. #######::. #######:: ##:::: ##: ########::. #######::::: ##::::                                                    
........::::.......::::.......:::..:::::..::........::::.......::::::..:::::    '''
'''
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
async def kick(ctx, member : discord.Member=None,*, reason=None):
    if not ctx.message.author.server_permissions.kick_members:
        pkick=discord.Embed(title='Error',description='You don\'t have permission to kick members!',color=0xFF0000)
        pkick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pkick)
    if not member:
        mkick=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        mkick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mkick)
    if not reason:
        rkick=discord.Embed(title='Error',description='You must specify a reason!',color=0xFF0000)
        rkick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rkick)
    try:
        await bot.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            ekick=discord.Embed(title='Error',description='The person you are trying to kick has high permissions.',color=0xFF0000)
            ekick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=ekick)
        else:
            pass
    skick=discord.Embed(title='Kick',description=f'{ctx.message.author.mention} has kicked {member.name}, because: {reason}!',color=0x00FF00)
    skick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=skick)
    return await bot.send_message(member, f'You have been kicked from {discord.Server.name} by {ctx.message.author.mention}, because {reason}!', tts=True) 

@bot.command(pass_context = True)
async def ban(ctx, member : discord.Member=None,*, reason=None):
    if not ctx.message.author.server_permissions.kick_members:
        pban=discord.Embed(title='Error',description='You don\'t have permission to ban members!',color=0xFF0000)
        pban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pban)
    if not member:
        mban=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        mban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mban)
    if not reason:
        rban=discord.Embed(title='Error',description='You must specify a reason!',color=0xFF0000)
        rban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rban)
    try:
        await bot.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            eban=discord.Embed(title='Error',description='The person you are trying to ban has high permissions.',color=0xFF0000)
            eban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=eban)
        else:
            pass
    sban=discord.Embed(title='Ban',description=f'{ctx.message.author.mention} has banned {member.name}, because: {reason}!',color=0x00FF00)
    sban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=sban)
    return await bot.send_message(member, f'You have been banned from {discord.Server.name} by {ctx.message.author.mention}, because {reason}!', tts=True) 

@bot.command(pass_context = True)
async def unban(ctx, member : discord.Member=None,*, reason=None):
    if not ctx.message.author.server_permissions.kick_members:
        punban=discord.Embed(title='Error',description='You don\'t have permission to unban members!',color=0xFF0000)
        punban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=punban)
    if not member:
        munban=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        munban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=munban)
    if not reason:
        runban=discord.Embed(title='Error',description='You must specify a reason!',color=0xFF0000)
        runban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=runban)
    try:
        await bot.unban(discord.Server,member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            eunban=discord.Embed(title='Error',description='The person you are trying to unban has high permissions.',color=0xFF0000)
            eunban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=eunban)
        else:
            pass
    sunban=discord.Embed(title='Unban',description=f'{ctx.message.author.mention} has unbanned {member.name}, because: {reason}!',color=0x00FF00)
    sunban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=unban)
    return await bot.send_message(member, f'You have been unbanned from {discord.Server.name} by {ctx.message.author.mention}, because {reason}!', tts=True) 

@bot.command(pass_context = True)
async def softban(ctx, member : discord.Member=None,*, reason=None):
    if not ctx.message.author.server_permissions.kick_members:
        psoftban=discord.Embed(title='Error',description='You don\'t have permission to softban members!',color=0xFF0000)
        psoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=psoftban)
    if not member:
        msoftban=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        msoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=msoftban)
    if not reason:
        rsoftban=discord.Embed(title='Error',description='You must specify a reason!',color=0xFF0000)
        rsoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rsoftban)
    try:
        await bot.ban(member, delete_message_days=7)
        await bot.unban(discord.Server,member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            esoftban=discord.Embed(title='Error',description='The person you are trying to softban has high permissions.',color=0xFF0000)
            esoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=esoftban)
        else:
            pass
    ssoftban=discord.Embed(title='Softban',description=f'{ctx.message.author.mention} has softbanned {member.name}, because: {reason}!',color=0x00FF00)
    ssoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=ssoftban)
    return await bot.send_message(member, f'You have been softbanned from {discord.Server.name} by {ctx.message.author.mention}, because {reason}!', tts=True) 
'''
@bot.command(pass_context=True, aliases=['purge','prune'])  
async def clear(ctx, amount:int):
    if not ctx.message.author.server_permissions.manage_messages:
        pclear=discord.Embed(title='Error',description='You don\'t have the manage_messages permission.', color=0xFF0000)
        pclear.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=pclear)
        return
    if amount < 1:
        aclear=discord.Embed(title='Error',description='Please put in a number more than 1.',color=0xFF0000)
        return await bot.say(embed=aclear)
    deleted = await bot.purge_from(ctx.message.channel, limit=amount)
    await asyncio.sleep(3)
    try:
        sclear=discord.Embed(title='Clear',description='I have cleared {} messages.'.format(len(deleted)),color=0x00FF00)
        sclear.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        delete = await bot.say(embed=embed1)
        asyncio.sleep(3)
        bot.delete_message(delete)
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
'''
'##::::'##::::'###::::'##::: ##::::'###:::::'######:::'####:'##::: ##::'######:::                                               
 ###::'###:::'## ##::: ###:: ##:::'## ##:::'##... ##::. ##:: ###:: ##:'##... ##::                                               
 ####'####::'##:. ##:: ####: ##::'##:. ##:: ##:::..:::: ##:: ####: ##: ##:::..:::                                               
 ## ### ##:'##:::. ##: ## ## ##:'##:::. ##: ##::'####:: ##:: ## ## ##: ##::'####:                                               
 ##. #: ##: #########: ##. ####: #########: ##::: ##::: ##:: ##. ####: ##::: ##::                                               
 ##:.:: ##: ##.... ##: ##:. ###: ##.... ##: ##::: ##::: ##:: ##:. ###: ##::: ##::                                               
 ##:::: ##: ##:::: ##: ##::. ##: ##:::: ##:. ######:::'####: ##::. ##:. ######:::                                               
..:::::..::..:::::..::..::::..::..:::::..:::......::::....::..::::..:::......::::    '''
'''
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
'''
if not os.environ.get('TOKEN'):
   print("No tokens!")
bot.run(os.environ.get('TOKEN').strip('"'))
