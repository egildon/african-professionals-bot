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
import sys


bot = commands.Bot(command_prefix='$')

client = commands.Bot(command_prefix='!')
client.load_extension('apdb_cogs')


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')



def test_func():
    print("test, test, test")

def in_channel(channel_id):
    '''Decorator to lock channel to supplied chennel_id'''
    def predicate(ctx):
        ctx.message.channel.id = channel_id
        return ctx.message.channel.id
    return  commands.check(predicate)

def channel_zero(message):
    '''Decorator to lock channel to supplied chennel_id 0'''
    def predicate(ctx):
        channel_id = 766111633243635822
        ctx.message.channel.id = channel_id
        # return ctx.message.channel.id
    return  commands.check(predicate)
 
def str_conditioning(dirtystr):
    regex = r"{([^}]*)}"
    new = re.findall(regex, dirtystr, re.MULTILINE)
    goodstr = new[0]
    return goodstr

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('We have logged in as {0.user}'.format(bot))
    print(dir(bot))  

    
      

@bot.command
async def dm(ctx):
    await ctx.author.send('DM Message!!!!')

@bot.event #This works as expected!
async def add_role(member, server_role):
        role = discord.utils.get(member.guild.roles, name=str(server_role))
        print(member.roles)
        await discord.Member.add_roles(member, role)
        print(f'Member with id: {member}')
        print(member.roles)
        mrolls = member.roles
        print(len(mrolls))


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, Welcome to the African Profesionals discord server!')
    # print(dir(member))
    print('Top Role 1:', member.top_role)
    print(member.roles)
    # await member.add_roles("New Member")
    await add_role(member, "New Member") # add this back if on guild join doesnt work
    print('Top Role 2:', member.top_role)
    print(member.roles)
    
    if str(member.top_role) == "@everyone":
        await add_role(member, 'New Member')
        print(f"New Member: {member.name} added with {member.roles} Roles")
    else:
        return

    if str(member.top_role) == "New Member":
        info_sessions(member)
    else:

        return
async def info_sessions(message, *member, ctx):
    response11 = 'If you have any questions about how to use DISCORD please check the #how-to-use-discord channel on the left side of the screen.'
    response12 = 'All New Members must first introduce themselves to the group. Please click on the #tell-us-about you channel on the left of the screen, and introduce yourself.'
    response13 = 'Please make sure to check out the #welcome channel for information on this discord and its ethos.'

    if "New Member" in str(ctx.message.author.top_role):#FIXME: New Member Messages Here!
        ROLZ = message.author.roles
        TOPROL = message.author.top_role
        time.sleep(1)
        await message.author.send(f"{response11}")
        time.sleep(1)
        await message.author.send(f"{response12}")
        time.sleep(1)
        await message.author.send(f"{response13}")
        time.sleep(1)


@bot.event
# @bot.command
async def on_message(message):
    channel_id = 766111633243635822
    member_role_id = 766036644582391868
    new_member_role_id = 766036457118105620

    incoming_message = message.content.lower()
    response11 = 'If you have any questions about how to use DISCORD please check the #how-to-use-discord channel on the left side of the screen.'
    response12 = 'All New Members must first introduce themselves to the group. Please click on the #tell-us-about you channel on the left of the screen, and introduce yourself.'
    response13 = 'Please make sure to check out the #welcome channel for information on this discord and its ethos.'

    response0 = 'Akwaaba!!!'
    response1 = 'Medaase!'
    response3 = 'You must still tell us about youeself to be given full access to the African Professionals Discord.'
    response4 = 'Congatulations, you have sucessfully posted in the #tell-us-about-yourself channel. You will now be given access to the rest of the Discord'
    response5 = 'Your first post must be in the: #tell-us-about-yourself channel. Your message has been deleted.'


    pre_channels = ["tell-us-about-you"]

    if message.author == bot.user:
        return

    if incoming_message.lower() == 'hello':
        await message.channel.send(response0)

    #FIXME: Make the Regular ex    await on_message2(message)pression work here!
    # pattern1 = re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
    if 'happy birthday' in message.content.lower():
        await message.channel.send(response1)
    incoming_message = message.content.lower()
    if message.author == bot.user:
        return
    if incoming_message.lower() == 'listen':
        curious = message.channel
        message.channel.id = channel_id
        # await message.channel.send(response3)#This sends to the channel it was recieved on
        await message.author.send(response0)#This sends to DM Channel

    incoming_message = message.content.lower()

    if message.author == bot.user:
        return

bot.run(str_conditioning(TOKEN))






