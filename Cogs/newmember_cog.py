
import discord
from discord.ext import commands
from discord import channel
from discord.ext import commands
from discord import member

bot = commands.Bot(command_prefix='$')

class newmember_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     channel = member.guild.system_channel
    #     if channel is not None:
    #         await channel.send('Welcome to the server {0.mention}.'.format(member))
    #         print("THIS COG WORKS!!! NEWMEMBER_COG.PY")

    @commands.Cog.listener()
    async def on_member_join(*member):
        await member.create_dm()
        await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Coders Of Color discord server!')

    @commands.Cog.listener()
    async def on_message(ctx, message):
        channel_id = 766111633243635822
        incoming_messageid = message.id
        incoming_message = message.content
        ROLZ = message.author.roles
        TOPROL = message.author.top_role
        MEMNAME = message.author
        response0 = 'Akwaaba!!!'
        response1 = 'Medaase!'
        response3 = 'You must still tell us about youeself to be given full access to the AB Discord.'
        response4 = 'Congatulations, you have sucessfully posted in the #tell-us-about-yourself channel. You will now be given access to the rest of the Discord'
        # response3 = 'You have achieved TRANSCENDANCE!'
        pre_channels = ["tell-us-about-you"]
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


        role = discord.member
        # print(role)
        # print(role.Role)
        # print(dir(discord.Role))#FIXME:*TEST DIRs
    #print(dir(discord.Member.top_role))

        TOPROL = discord.Member.top_role
        # breakpoint()
        if "New Member" == str(TOPROL):#FIXME: *New Member Cheeck Here!
            # breakpoint()
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
                #FIXME: This is what I think needs work!!!!
                await message.author.send(response4)
                # await message.author.add_roles())
                print(str(discord.Member.top_role(id)))
                if str(discord.Member.top_role) == "New Member":  #TODO: add this member to Members Roles
                    print('Auth:xxx ',message.author.id)
                    await user.add_roles(message.guild.get_role(member_role_id))  #TODO:This is KLUDGY
                    await user.remove_roles(message.guild.get_role(new_member_role_id))  #TODO:This is HACKY Too
                else:
                    print("Already a Member!")
            else:
                await message.author.send(response3)
                await client.delete_message(message) #bot cannot do this ?
                await message.delete()
                await message.author.send(response5)

        # print(f"TOPROL: {TOPROL} for: {MEMNAME}")
        # breakpoint()
        if "New Member" == str(TOPROL):#FIXME: New Member Messages Here!
            print(dir(message.author.role))
            # ROLZ = message.author.roles
            # TOPROL = message.author.top_role
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

    async def info_sessions(message, member):
        response11 = 'If you have any questions about how to use DISCORD please check the #how-to-use-discord channel on the left side of the screen.'
        response12 = 'All New Members must first introduce themselves to the group. Please click on the #tell-us-about you channel on the left of the screen, and introduce yourself.'
        response13 = 'Please make sure to check out the #welcome channel for information on this discord and its ethos.'
        ROLZ = discord.Member.roles
        TOPROL = discord.Member.top_role

        if "New Member" in str(member):  #FIXME: New Member Messages Here!
            time.sleep(1)
            await message.author.send(f"{response11}")
            time.sleep(1)
            await message.author.send(f"{response12}")
            time.sleep(1)
            await message.author.send(f"{response13}")
            time.sleep(1)



def setup(bot):
    bot.add_cog(newmember_cog(bot))
    