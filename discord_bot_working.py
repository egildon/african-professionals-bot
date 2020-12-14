'''This is a discord bot initiall designed for African Professionals Discord'''
#discord_bot.py
from collections import Counter
import os
import re
import discord
from discord import channel
from discord import member
#from envmaster import envmastediscord bot python
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

#client = discord.Client()
bot = commands.Bot(command_prefix='$')
CHANNEL_ID = 766111633243635822 
client = commands.Bot(command_prefix='!')
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
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})')
        members = '\n - '.join([member.name for member in guild.members])
        # members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')
        print(f'{bot.user} is connected to the following guild:\n'
             f'{guild.name} (id: {guild.id})')
        #TODO: Sorting Hat
        for member in guild.members:
            role_names = [role.name for role in member.roles]
            if len(member.roles) == 1 and "@everyone" in role_names:
                print('Candidate for termination!')
                #changes @everyone to "New Members"
                await add_role(member, "New Member")
            else:
                pass
            role_names = [role.name for role in member.roles]
            if "New Member" in role_names:#TODO: Check for posts in tell us about yourself
                print(f'Member Name: {member.name}, Member Role: {member.roles}')

        ch = bot.get_channel(766111633243635822)
        print(ch)
    for channelz in guild.text_channels:
        print(channelz)
        
@bot.command
async def dm(ctx):
    await ctx.author.send('DM Message!!!!')

@bot.event #TODO:See if this works!
async def add_role(member, server_role):
        role = discord.utils.get(member.guild.roles, name=str(server_role))
        await discord.Member.add_roles(member, role)
        print(f'Member with id: {member}')
        print(member.roles)
        mrolls = member.roles
        print(len(mrolls))
        print('Candidate Exterminated!!!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
    f'Hi {member.name}, welcome to the Coders Of Color discord server!')

@bot.event
async def on_message(message, *member):
    channel_id = 766111633243635822
    incoming_message = message.content.lower()


    response0 = 'Akwaaba!!!'
    response1 = 'Medaase!'
    response3 = 'You must still tell us about youeself to be given full access to the AB Discord.'
    response4 = 'Congatulations, you have sucessfully posted in the #tell-us-about-yourself channel. You will now be given access to the rest of the Discord'

    # response3 = 'You have achieved TRANSCENDANCE!'

    pre_channels = ["tell-us-about-you"]

    if message.author == bot.user:
        return

    if incoming_message.lower() == 'hello':
        await message.channel.send(response0)

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
        await message.author.send(response3)#This sends to DM Channel

    incoming_message = message.content.lower()

    if message.author == bot.user:
        return

    if "New Member" in str(message.author.top_role):#FIXME: New Member Messages Here!
        ROLZ = message.author.roles
        TOPROL = message.author.top_role
        await message.author.send(f"{response4}: Roles {ROLZ}")
        await message.author.send(f"Top Role {TOPROL}")

        if str(message.channel) in pre_channels:
            await message.author.send(response4)
            if str(member) == "New Member":#TODO: add this member to Members Roles
                await add_role(member.roles, "Member")       
                await message.auhor.add_roles("Member") #TODO: Check this for workness      
                await message.auhor.remove_roles("New Member") #TODO: Check this for workness      
            else:
                print("Already a Member!")
        else:
            await message.author.send(response3)

async def info_sessions(message, *member):

    response11 = 'If you have any questions about how to use DISCORD please check the #how-to-use-discord channel on the left side of the screen.'
    response12 = 'All New Members must first introduce themselves to the group. Please click on the #tell-us-about you channel on the left of the screen, and introduce yourself.'
    response13 = 'Please make sure to check out the #welcome channel for information on this discord and its ethos.'
    if "New Member" in str(message.author.top_role):#FIXME: New Member Messages Here!
        ROLZ = message.author.roles
        TOPROL = message.author.top_role
        time.sleep(1)
        await message.author.send(f"{response11}")
        time.sleep(1)
        await message.author.send(f"{response12}")
        time.sleep(1)
        await message.author.send(f"{response13}")
        time.sleep(1)

@in_channel(766111633243635822)
@bot.event
async def get_channel_messages():
    async for message in channel.history():
        counter = 0
        if message.author == bot.user:
            counter +=1
        print(f'Message: {message} No: {Counter}')

@client.command(pass_context = True)
async def delete_messag(ctx, number):
    number = int(number)
    counter = 0
    async for x in discord.Client.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await discord.Client.delete_message(x)
            counter += 1
            await asyncio.sleep(1.2)


# @client.command()
# async def test(ctx):
#     guild = ctx.guild
#     for channel in guild.text_channels:
#         for message in channel:
#             await message.delete()
# bot.run(str_conditioning(TOKEN))