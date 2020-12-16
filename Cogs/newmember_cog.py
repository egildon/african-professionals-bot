
from discord.ext import commands


class newmember_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome to the server {0.mention}.'.format(member))
            print("THIS COG WORKS!!! NEWMEMBER_COG.PY")


def setup(bot):
    bot.add_cog(newmember_cog(bot))
