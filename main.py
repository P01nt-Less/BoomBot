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
  
if not os.environ.get('TOKEN'):
   print("No tokens!")
bot.run(os.environ.get('TOKEN')