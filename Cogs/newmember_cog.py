
import os
import time
from time import sleep
import discord
from discord.abc import User
from discord.ext import commands
from discord import channel
from discord import member

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
       
     #TODO:See if this works!
    @commands.Cog.listener()
    async def add_rolez3(message_auth_id, server_role):
        
        #trying to import this method to see if it makes the add member function properly.
        for guild in bot.guilds:
            if guild.name == GUILD:
                break
            print(
                f'{bot.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})')
            members = '\n - '.join([member.name for member in guild.members])
            print(f'Guild Members:\n - {members}')
            print(f'{bot.user} is connected to the following guild:\n'
                 f'{guild.name} (id: {guild.id})')
            #TODO: Sorting Hat
            for member in guild.members:
                role_names = [role.name for role in member.roles]
                if "New Member" in role_names:#TODO: Check for posts in tell us about yourself
                    print(f'Member Name: {member.name}, Member Role: {member.roles}')

                role = discord.utils.get(member.guild.roles, name=str(server_role))
                TOTALZ= discord.Member.add_roles(message_auth_id, server_role)
                await discord.Member.add_roles(message_auth_id, server_role)
                await user.add_roles(message.guild.get_role(bot.member_role_id))  #TODO:This is KLUDGY
                await user.remove_roles(message.guild.get_role(bot.new_member_role_id))  #TODO:This is HACKY Too
                # await ctx.discord.Member.remove_roles("New Member") #TODO: Check this for workness
            
        #This is the old one    
        # @bot.event  #This works as expected!
        # async def add_rolex(member, server_role):
        #     '''Adds a role to user profile'''
        #     role = discord.utils.get(member.guild.roles, name=str(server_role))
        #     print(discord.Member.roles)
        #     # await discord.Member.add_roles(role)
        #     await discord.Member.add_roles(member, role)
        #     print(f'Member with id: {member}')
        #     print(member.roles)
        
    async def add_rolez4(message_auth_id, new_server_role,ctx, *message, member):
        for guild in bot.guilds:
            if guild.name == GUILD:
                break
            print(
                f'{bot.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})')
            members = '\n - '.join([member.name for member in guild.members])
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

    @commands.command(name='coolbot', hidden = True)
    @commands.is_owner()
    async def cool_bot(self, ctx):
        """Is the bot cool?"""
        await ctx.send('This bot is cool. :)')

    @commands.command(name='reload', hidden = True)
    @commands.is_owner()
    async def livereload(self, ctx,):
        """REloading extensions NOW!!!"""
        loaded_cogs: list = []
        await ctx.send('Reload hit!')
        for root, dirs, files in os.walk("./Cogs"):
            # print(files)
            for fnamestr in files:
                testcase1 = fnamestr.startswith("_")
                if testcase1 is False and fnamestr.endswith(".py"):
                    cogstr = fnamestr. rstrip(".py")
                    print(cogstr)
                    #reload loaded_cogs method
                    # cogstr = (f"Cogs.{cogstr}")#TODOERROR! ??V???
                    if cogstr not in loaded_cogs:
                        print(f"RELOAD-Appending: {cogstr}")
                        loaded_cogs.append(cogstr)
                    else:
                        pass

 
        for cog2 in loaded_cogs:
            print(type(cog2))
            print(cog2)
            try:
                print("Reloading Cogs")
                self.bot.reload_extension(f"{cog2}")
                print("Done Reloading Cogs")
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                await ctx.send('**`SUCCESS`**')

    # @commands.Cog.listener()
    # async def on_message_delete():
    #         if message.author.top_role.name == "New Member":  #TODO: add this member to Members Roles
    #             print('Auth:xxx ',message.author.id)
    #             await message.author.send("Stay quiet")
    #             await message.delete()
    #             await message.author.send("I said QUIET!")

    @commands.Cog.listener()
    async def on_message(ctx, message, *member):
        # ROLZ = message.author.roles
        message_auth_id = message.author
        channel_id = 766111633243635822
        incoming_message_id = message.id
        incoming_message = message.content
        
        #trying to import this method to see if it makes the add member function properly.
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
        #     for member in guild.members:
        #         role_names = [role.name for role in member.roles]
        #         if len(member.roles) == 1 and "@everyone" in role_names:
        #             print('Candidate for termination!')
        #             #changes @everyone to "New Members"
        #             await add_role(member, "New Member")
        #         else:
        #             pass
        #         role_names = [role.name for role in member.roles]
        #         if "New Member" in role_names:#TODO: Check for posts in tell us about yourself
        #             print(f'Member Name: {member.name}, Member Role: {member.roles}')
        # #trying to import this method to see if it makes the add member function properly.





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

            
                
        isbot = message.author.bot
        if isbot is False and "New Member" == message.author.top_role.name:#FIXME: *New Member Cheeck Here!
            current_channel_id = message.channel.id
            current_message_user_id = message.author.id
            current_user_role_name = message.author.top_role.name
            objective_role_id = guildRolesDict['Member']
            objective_channel_id = guildChannelDict['#tell-us-about-you']
            # breakpoint()
            print("NEW MEMBER HITTT!!!!")
            # await message.author.send(f"Top Role: -{TOPROL}")
            user = message.author
            time.sleep(1)
            await message.author.send(f"{response11}")
            time.sleep(2)
            await message.author.send(f"{response12}")
            time.sleep(2)
            await message.author.send(f"{response13}")
            time.sleep(3)
            if current_channel_id == objective_channel_id :
                #FIXME: This is what I think needs work!!!!
                await message.author.send(response4)
                # await message.author.add_roles())

                if str(message.author.top_role) == "New Member":  #TODO: add this member to Members Roles
                    print('Auth:xxx ',message.author.id)
                    await user.add_roles(message.guild.get_role(bot.member_role_id))  #TODO:This is KLUDGY
                    await user.remove_roles(message.guild.get_role(bot.new_member_role_id))  #TODO:This is HACKY Too
                else:
                    print("Already a Member!")
            else:
                await message.author.send(response3)
                # newmember_cog.on_message_delete(message)
                await message.delete()
                await message.author.send(response3)

        else:
            return 

 #This is a repeat of what s already heppening               
 
        # isbot = message.author.bot
        # # if isbot is False and "New Member" == str(message.author.top_role.name):#FIXME: New Member Messages Here!
        # if isbot is False: #FIXME: test to see if thsi works
        #     print("This bot is on fireee!!!")
        #     # await message.author.send(f"{response4}: Role: -{ctx.guild_role1.name}-")#Here?
        #     # await message.author.send(f"Top Role {str(guild_role1.name)}")
        #     # thang = guildChannelDict['tell-us-about-you']
        #     if  766111633243635822 == int(message.channel.id):
        #         await message.author.send(response4)
        #         # await newmember_cog.add_role(message.author.id, "Member")
        #     try:
        #         print("Adding new roles")
        #         message_auth_id = message.author.id
        #         role_assignment = "Member"
        #         await newmember_cog.add_rolez3(message_auth_id,  role_assignment)
        #         # await newmember_cog.add_rolex(member,"New Member")
        #         # await discord.Member.add_roles("Member") #TODO: Check this for workness
        #         print("Done Adding Roles")
        #     except Exception as e:
        #         await message.author.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        #         print(f'**`ERROR:`** {type(e).__name__} - {e}')
        #     else:
        #         await message.author.send(f"**`SUCCESS`**' {response4}")
        #         print(f"**`SUCCESS`**' {response4}")


def setup(bot):
    bot.add_cog(newmember_cog(bot))
    