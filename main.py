# Discord Imports
import discord
from discord.ext import commands
import discord.utils
# Python Imports
import re
import os
# Other Imports
prefix=commands.when_mentioned_or('!')
bot = commands.Bot(command_prefix=prefix, description='The one, and only: The Bot, created by Pointless#1278.', self_bot=False,)
bot.remove_command('help')

def pointcheck(ctx):
    return ctx.message.author.id == '276043503514025984' #checks if @Pointless#1278 is the author of the command

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='!help | {} servers'.format(len(bot.servers))), status='online')
    print('Online.')
    print('https://discordapp.com/oauth2/authorize?client_id=431951773159129098&scope=bot&permissions=2146958591')
  
@bot.event
async def on_message(message):
    if message.content.startswith(str(prefix) + str('test')):
        bot.say('Hey!')
    else:
        bot.say('Oh boy!')

if not os.environ.get('TOKEN'):
   print("No tokens!")
bot.run(os.environ.get('TOKEN').strip('"'))
