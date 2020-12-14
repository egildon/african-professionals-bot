import discord
from discord.ext import commands

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
    async def on_member_join2(self, member):
        if "New Member" == str(ctx.message.author.top_role):#FIXME: New Member Cheeck Here!
            ROLZ = message.author.roles
            TOPROL = message.author.top_role
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
                if str(ctx.message.author.top_role) == "New Member":#TODO: add this member to Members Roles
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

    @commands.command()
    async def hello(self, ctx,*,member:discord.Member = None):
        """Says Hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familliar.'.format(member))
        self._last_member = member