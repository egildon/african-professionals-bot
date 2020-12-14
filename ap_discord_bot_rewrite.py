import discord
from discord.ext import commands

import sys, traceback

'''This is a discord bot designed for the African Professionals Discord'''
#discord_bot.py
from collections import Counter
import os
import re
import discord
from discord import channel
#from envmaster import envmastediscord bot python
from dotenv import load_dotenv
from discord.ext import commands
import time




bot = commands.Bot(command_prefix='$')
client = commands.Bot(command_prefix='!')
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


cogs: list = ['apdb_cogs1']



@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('We have logged in as {0.user}'.format(bot))
    for cog in cogs:
        try:
            print(f"Loading cog {cog}")
            client.load_extension(cog)
            print(f"Done Loading {cog}")
        except Exception as err:
            exec = "{}: {}".format(type(err).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))

   
    
        
def str_conditioning(dirtystr):
    regex = r"{([^}]*)}"
    new = re.findall(regex, dirtystr, re.MULTILINE)
    goodstr = new[0]
    return goodstr

bot.run(str_conditioning(TOKEN))