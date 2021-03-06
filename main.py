#Discord Imports
import discord
from discord.ext import commands
import discord.utils
#Other Imports
import traceback #to see the error while in Discord
import random # for randomizing things
from random import randint # randints
import requests # for APIs
import aiohttp # for APIs 2
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
    embed.add_field(name='Informational',value='')
    embed.add_field(name='Fun',value='')
    embed.add_field(name='BoomBot',value='')
    embed.add_field(name='Moderation',value='`kick` | `ban` | `unmute` | `softban`')
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
'##::::'##::::'###::::'##::: ##::::'###:::::'######:::'####:'##::: ##::'######:::                                               
 ###::'###:::'## ##::: ###:: ##:::'## ##:::'##... ##::. ##:: ###:: ##:'##... ##::                                               
 ####'####::'##:. ##:: ####: ##::'##:. ##:: ##:::..:::: ##:: ####: ##: ##:::..:::                                               
 ## ### ##:'##:::. ##: ## ## ##:'##:::. ##: ##::'####:: ##:: ## ## ##: ##::'####:                                               
 ##. #: ##: #########: ##. ####: #########: ##::: ##::: ##:: ##. ####: ##::: ##::                                               
 ##:.:: ##: ##.... ##: ##:. ###: ##.... ##: ##::: ##::: ##:: ##:. ###: ##::: ##::                                               
 ##:::: ##: ##:::: ##: ##::. ##: ##:::: ##:. ######:::'####: ##::. ##:. ######:::                                               
..:::::..::..:::::..::..::::..::..:::::..:::......::::....::..::::..:::......::::    '''

@bot.command(pass_context=True,aliases=['gr'])
async def giverole(ctx, member: discord.Member, *, role: discord.Role = None):
    if not ctx.message.author.server_permissions.manage_roles:
        pgiverole=discord.Embed(title='Error',description='You don\'t have permission to give roles to members!',color=0xFF0000)
        pgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pgiverole)
    if not member:
        mgiverole=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        mgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mgiverole)
    if not role:
        rgiverole=discord.Embed(title='Error',description='You must specify a role!',color=0xFF0000)
        rgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rgiverole)
    if role not in ctx.message.server.roles:
        ngiverole=discord.Embed(title='Error',description='That isn\'t a role!',color=0xFF0000)
        ngiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ngiverole)
    try:
        rolegive = discord.utils.get(ctx.message.server.roles, name=role)
        bot.add_roles(member, role)
        sgiverole=discord.Embed(title='Giverole',description=f'{ctx.message.author.mention} has given the role, {role}, to {member.name}!',color=0x00FF00)
        sgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=sgiverole)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            egiverole=discord.Embed(title='Error',description='The person you are trying to give a role to has high permissions.',color=0xFF0000)
            egiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=egiverole)
        else:
            pass
@bot.command(pass_context=True,aliases=['tr'])
async def takerole(ctx, member: discord.Member, *, role: discord.Role = None):
    if not ctx.message.author.server_permissions.manage_roles:
        ptakerole=discord.Embed(title='Error',description='You don\'t have permission to give roles to members!',color=0xFF0000)
        ptakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ptakerole)
    if not member:
        mtakerole=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        mtakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mtakerole)
    if not role:
        rtakerole=discord.Embed(title='Error',description='You must specify a role!',color=0xFF0000)
        rtakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rtakerole)
    if role not in ctx.message.server.roles:
        ntakerole=discord.Embed(title='Error',description='That isn\'t a role!',color=0xFF0000)
        ntakeerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ntakerole)
    try:
        bot.remove_roles(member, role)
        stakerole=discord.Embed(title='Takerole',description=f'{ctx.message.author.mention} has taken the role, {role}, from {member.name}!',color=0x00FF00)
        stakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=stakerole)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            egiverole=discord.Embed(title='Error',description=f'The person you are trying to take a role from has high permissions.',color=0xFF0000)
            egiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=etakerole)
        else:
            pass

        
  
  
if not os.environ.get('TOKEN'):
   print("No tokens!")
bot.run(os.environ.get('TOKEN').strip('"'))
