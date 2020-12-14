import discord
from discord.ext import commands


class GuildPreamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    for guild in bot.guilds:
            if guild.name == GUILD:
                break
            print(f'{bot.user} is connected to the following guild:\n'
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

async def on_message(message, *member):
    channel_id = 766111633243635822
    member_role_id = 766036644582391868
    new_member_role_id = 766036457118105620
    role = discord.utils.get(member.guild.roles)
    print(role)


class SortingHat(commands.Cog):
    def __init__(self, bot):
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


class MembersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member):
        """Says when a member joined."""
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')

    @commands.command(name='coolbot')
    async def cool_bot(self, ctx):
        """Is the bot cool?"""
        await ctx.send('This bot is cool. :)')

    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member=None):
        """Simple command which shows the members Top Role."""

        if member is None:
            member = ctx.author

        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')
    
    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member=None):
        """A simple command which checks a members Guild Permissions.
        If member is not provided, the author will be checked."""

        if not member:
            member = ctx.author

        # Here we check if the value of each permission is True.
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        # And to make it look nice, we wrap it in an Embed.
        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        # \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
        embed.add_field(name='\uFEFF', value=perms)

        await ctx.send(content=None, embed=embed)
        # Thanks to Gio for the Command.

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(MembersCog(bot))