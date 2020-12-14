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

@bot.event #This works as expected!
async def add_role(member, server_role):
        role = discord.utils.get(member.guild.roles, name=str(server_role))
        print(member.roles)
        await discord.Member.add_roles(member, role)
        print(f'Member with id: {member}')
        print(member.roles)
        mrolls = member.roles
        print(len(mrolls))

# @bot.event
# async def on_guild_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#     f'Hi {member.name}, welcome to the Coders Of Color discord server!')
#     # print(dir(member))
#     print('Top Role:', member.top_role)
#     await add_role(member, "New Member")
#     print('Top Role:', member.top_role)

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
@bot.event
# @bot.command
async def on_message(message, *member):
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

    # response = 'Akwaaba!!!'
    # response2 = 'Medaase!'

    # response0 = 'Congatulations, you have sucessfully posted in the #tell-us-about-yourself channel. You will now be given access to the rest of the Discord'
    # response1 = 'You must still tell us about youeself to be given full access to the AB Discord.'
    # response3 = 'You have achieved TRANSCENDANCE!'

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

    role = discord.member
    print(role)
    print(discord.Role)
    print(dir(discord.Role))#FIXME:*TEST DIRs
   #print(dir(discord.Member.top_role))

    TOPROL = discord.Member.top_role
    if "New Member" == str(discord.Member.top_role):#FIXME: *New Member Cheeck Here!
        print("NEW MEMBER HITTT!!!!")
        ROLZ = discord.Member.roles
        info_sessions()
        # await message.author.send(f"Top Role: -{TOPROL}")
        user = message.author
        time.sleep(1)
        await message.author.send(f"{response11}")
        time.sleep(2)
        await message.author.send(f"{response12}")
        time.sleep(2)
        await message.author.send(f"{response13}")
        time.sleep(3)
        if str(message.channel) in pre_channels:
            await message.author.send(response4)
            #print(dir(message.author.add_roles))
            print(str(discord.Member.top_role(id)))
            if str(discord.Member.top_role) == "New Member":#TODO: add this member to Members Roles
                print('Auth: ',message.author.id)
                await user.add_roles(message.guild.get_role(member_role_id))#TODO:This is KLUDGY       
                await user.remove_roles(message.guild.get_role(new_member_role_id))#TODO:This is HACKY Too       
            else:
                print("Already a Member!")
        else:
            await message.author.send(response3)
            # await client.delete_message(message) #bot cannot do this ?
            await message.delete()
            await message.author.send(response5)

async def info_sessions(message, *member, ctx):
    response11 = 'If you have any questions about how to use DISCORD please check the #how-to-use-discord channel on the left side of the screen.'
    response12 = 'All New Members must first introduce themselves to the group. Please click on the #tell-us-about you channel on the left of the screen, and introduce yourself.'
    response13 = 'Please make sure to check out the #welcome channel for information on this discord and its ethos.'
    
    if "New Member" in str(discord.Member.top_role):#FIXME: New Member Messages Here!
        ROLZ = discord.Member.roles
        TOPROL = discord.Member.top_role
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
            
@bot.command
async def getmsg(ctx, msg_id: int):
    msg = await ctx.fetch_message(msg_id)

async def delete_and_move(): # FIXME: MAke this work  new project
    '''This is a function to move people to the proper channels and to delete ALL messages from my server'''
    channel = discord.utils.find(lambda x: x.name == 'afk', message.server.channels)
    await client.move_member(message.author, channel)


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))
            print("COG is hit!!!!!!")
        #TODO: MAke this work to find messages
    async def on_member_join(self, member):
        
        # if "New Member" == str(ctx.message.author.top_role):#FIXME: New Member Cheeck Here!
        #     ROLZ = message.author.roles
        #     TOPROL = message.author.top_role
        #     # await message.author.send(f"Top Role: -{TOPROL}")
        #     user = message.author
        #     time.sleep(1)
        #     await message.author.send(f"{response11}")
        #     time.sleep(2)
        #     await message.author.send(f"{response12}")
        #     time.sleep(2)
        #     await message.author.send(f"{response13}")
        #     time.sleep(3)
        #     if str(message.channel) in pre_channels:
        #         await message.author.send(response4)
        #         #print(dir(message.author.add_roles))
        #         if str(ctx.message.author.top_role) == "New Member":#TODO: add this member to Members Roles
        #             print('Auth: ',message.author.id)
        #             await user.add_roles(message.guild.get_role(member_role_id))#TODO:This is KLUDGY       
        #             await user.remove_roles(message.guild.get_role(new_member_role_id))#TODO:This is HACKY Too       
        #         else:
        #             print("Already a Member!")
        #     else:
        #         await message.author.send(response3)
        #         # await client.delete_message(message) #bot cannot do this ?
        #         await message.delete()
        #         await message.author.send(response5)

        @commands.command()
        async def hello(self, ctx,*,member:discord.Member = None):
            """Says Hello"""
            member = member or ctx.author
            if self._last_member is None or self._last_member.id != member.id:
                await ctx.send('Hello {0.name}~'.format(member))
            else:
                await ctx.send('Hello {0.name}... This feels familliar.'.format(member))
            self._last_member = member

bot.run(str_conditioning(TOKEN))