
import discord
from discord.ext import commands
from discord import channel
from discord.ext import commands
from discord import member
import time
from time import sleep
import os
bot = commands.Bot(command_prefix='$')

GUILD = os.getenv('DISCORD_GUILD')
# ROLZ = message.author.roles
# TOPROL = message.author.top_role

guildRolesDict = {"Member": 766036644582391868, "New Member": 766036457118105620, "@everyone": 760873008738074704}
guildChannelDict = {"#tell-us-about-you": 766111633243635822, "#read-first": 788606582761717761}

class newmember_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @bot.event  #This works as expected!
    async def add_role(member, server_role):
        '''Adds a role to user profile'''
        role = discord.utils.get(member, name=str(server_role))
        print(member.roles)
        await discord.Member.add_roles(member, role)
        print(f'Member with id: {member}')
        print(member.roles)

    @commands.Cog.listener()
    async def on_member_join(*member):
        await member.create_dm()
        await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Coders Of Color discord server!(newmwmber_cog)')

    @commands.Cog.listener()
    async def info_sessions(message, member):
        response11 = 'If you have any questions about how to use DISCORD please check the #how-to-use-discord channel on the left side of the screen.'
        response12 = 'All New Members must first introduce themselves to the group. Please click on the #tell-us-about you channel on the left of the screen, and introduce yourself.'
        response13 = 'Please make sure to check out the #welcome channel for information on this discord and its ethos.'
        if "New Member" in str(member):  #FIXME: New Member Messages Here!
            time.sleep(1)
            await message.author.send(f"{response11}")
            time.sleep(1)
            await message.author.send(f"{response12}")
            time.sleep(1)
            await message.author.send(f"{response13}")
            time.sleep(1)
                
    # @bot.command(pass_context=True)  #This works as expected!
    # async def add_role(member, server_role):
    #     role = discord.utils.get(member.guild.roles, name=str(server_role))
    #     print(member.roles)
    #     await discord.Member.add_roles(member, role)
    #     print(f'Member with id: {member}')
    #     print(member.roles)
    #     print(len(mrolls))

    @commands.Cog.listener()
    async def on_message(ctx, message):
        # ROLZ = message.author.roles
        message_auth_id = message.author
        channel_id = 766111633243635822
        incoming_message_id = message.id
        incoming_message = message.content
        guild_role = discord.Member.top_role #FIXME: guild_role is not returning a useable variable
        # guild_role1 = message.author.top_role #FIXME: guild_role is not returning a useable variable
        guild_role2 = member #FIXME: guild_role is not returning a useable variable
        response0 = 'Akwaaba!!!'
        response1 = 'Medaase!'
        response3 = 'You must still tell us about youeself to be given full access to the AB Discord.'
        response4 = 'Congatulations, you have sucessfully posted in the #tell-us-about-yourself channel. You will now be given access to the rest of the Discord'
        response11 = 'If you have any questions about how to use DISCORD please check the #how-to-use-discord channel on the left side of the screen.'
        response12 = 'All New Members must first introduce themselves to the group. Please click on the #tell-us-about you channel on the left of the screen, and introduce yourself.'
        response13 = 'Please make sure to check out the #welcome channel for information on this discord and its ethos.'
        if "New Member" in str(guild_role):#FIXME: New Member Messages Here!
            time.sleep(1)
            await message.author.send(f"{response11}")
            time.sleep(1)
            await message.author.send(f"{response12}")
            time.sleep(1)
            await message.author.send(f"{response13}")
            time.sleep(1)
        pre_channels = ["tell-us-about-you"]
        if incoming_message.lower() == 'hello':
            await message.channel.send(response0)

        await newmember_cog.info_sessions(message, member)

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

        role = discord.member
        # breakpoint()

        if "New Member" == str(guild_role):#FIXME: *New Member Cheeck Here!
            # breakpoint()
            print("NEW MEMBER HITTT!!!!")
            ROLZ = discord.Member.roles
            # await message.author.send(f"Top Role: -{TOPROL}")
            user = message.author
            time.sleep(1)
            await message.author.send(f"{response11}")
            time.sleep(2)
            await message.author.send(f"{response12}")
            time.sleep(2)
            await message.author.send(f"{response13}")
            time.sleep(3)

            if str(message.channel.id) ==  guildChannelDict['tell_us-about-you']:
                #FIXME: This is what I think needs work!!!!
                await message.author.send(response4)
                # await message.author.add_roles())
                print(str(discord.Member.top_role(id)))

                if str(message.author.top_role) == "New Member":  #TODO: add this member to Members Roles
                    print('Auth:xxx ',message.author.id)
                    await user.add_roles(message.guild.get_role(bot.member_role_id))  #TODO:This is KLUDGY
                    await user.remove_roles(message.guild.get_role(bot.new_member_role_id))  #TODO:This is HACKY Too
                else:
                    print("Already a Member!")
            else:
                await message.author.send(response3)
                await ctx.client.delete_message(message) #bot cannot do this ?
                await message.delete()
                await message.author.send(response3)
        isbot = message.author.bot
        if isbot is False and "New Member" == str(message.author.top_role.name):#FIXME: New Member Messages Here!
            # await message.author.send(f"{response4}: Role: -{ctx.guild_role1.name}-")#Here?
            # await message.author.send(f"Top Role {str(guild_role1.name)}")
            # thang = guildChannelDict['tell-us-about-you']
            if  766111633243635822 == int(message.channel.id):
                await message.author.send(response4)
                # await newmember_cog.add_role(message.author.id, "Member")
                await discord.Member.add_roles(discord.Role("Member")) #TODO: Check this for workness
                # await ctx.discord.Member.remove_roles("New Member") #TODO: Check this for workness
            else:
                await message.author.send(response3)



def setup(bot):
    bot.add_cog(newmember_cog(bot))
    