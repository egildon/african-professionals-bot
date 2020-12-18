'''This is a discord bot designed for the African Professionals Discord'''
from collections import Counter
# import sys
import pdb
import os
from pathlib import Path
import re
# import time
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import channel

#global variables because... fuckit!!!

bot = commands.Bot(command_prefix='$')
client = commands.Bot(command_prefix='!')
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

guildRoles = {"Member": 766036644582391868, "New Member": 766036457118105620, "@everyone": 760873008738074704}
guildChannel = {"#tell-us-about-you": 766111633243635822, "#read-first": 788606582761717761}

# cogs: list = ['Cogs.newmember_cog']


@bot.event
async def on_ready():
    # cogs: list = ['Cogs.newmember_cog']
    cogs: list = []
    print("ON READY: READY!!!")
    print(f'{bot.user} has connected to Discord!')
    print('We have logged in as {0.user}'.format(bot))
    print("program ap_discord_bot_rewrite.py")
    for root, dirs, files in os.walk("./Cogs"):
        # print(files)
        for fnamestr in files:
            testcase1 = fnamestr.startswith("_")
            if testcase1 is False and fnamestr.endswith(".py"):
                cogstr = fnamestr. rstrip(".py")
                print(cogstr)

                #reload cogs method
                cogstr = (f"Cogs.{cogstr}")
                if cogstr not in cogs:
                    print(f"Appending: {cogstr}")
                    cogs.append(cogstr)
                else:
                    pass

    for item in cogs:
        print(f"List item: {item}")

    for cog in cogs:
        try:
            print(f"Loading cog {cog}")
            bot.load_extension(cog)
            print(f"Done Loading {cog}")
        except Exception as err:
            exec = (type(err).__name__)
            print(f"Failed to load cog: {exec}")
    # breakpoint()

@bot.event
async def on_message(message):
    # ignores bot messages##
    if message.author.bot:
        return

    await bot.process_commands(message)


def str_conditioning(dirtystr):
    """This is a function helper to help in parsing .env file information"""
    regex = r"{([^}]*)}"
    new = re.findall(regex, dirtystr, re.MULTILINE)
    goodstr = new[0]
    return goodstr


if __name__ == "__main__":
    ##FIXME:Loading the directory only doesnt work, fix it or not!!!
    # @bot.event
    # async def on_ready():
    #     # run cogs in Cogs dir
    #     for root, dirs, files in os.walk(cwd + "/Cogs"):
    #         for fnamestr in files:
    #             # fnamestr = name(fnamestr)
    #             # print(fnamestr)
    #             # print(type(fnamestr))
    #             # print(dir(fnamestr))
    #             test1 = fnamestr.endswith("_cog.py")
    #             test2 = fnamestr.startswith("_")
    #             if test1 and not test2:
    #                 # print(dir(bot.load_<F2>extension))
    #                 bot.load_extension(f".Cogs{fnamestr[:-3]}")
    bot.run(str_conditioning(TOKEN))
    # breakpoint()
