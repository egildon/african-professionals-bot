"""This as a Command and Control cog for my bots"""
import asyncio
import os
import discord
from discord.ext import commands
# from discord import command

from .ap_discord_bot_rewrite.py import cogs 




class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commmands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n~~~")

    @commands.command(name='reload', description="Reload all one of the cogs")
    @commands.is_owner()
    async def reload(self, ctx):
        async with ctx.typing():
            embed = discord.Embed(
                title="Reloading cogs!",
                color=0x0008080,
                timestamp=ctx.message.created_at)
            for ext in os.listdir("./Cogs"):
                if ext.endswith("_cog.py") and not ext.startsswith("_"):
                    try:
                        self.bot.unload.extensions(f"cogs.{ext[:-3]}")
                        self.bot.load.extensions(f"cogs.{ext[:-3]}")
                        embed.add_field(
                            name=f"Reloaded: '{ext}'",
                            value='\uFEFF',
                            inline=False)

                    except Exception as e:
                        embed.add_field(
                            name=f"Failed to Reload:'{ext}'",
                            value=e,
                            inline=False)
                    await asyncio.sleep(0.5)

    @commands.command(name='reload', description="Reload all one of the cogs")
    @commands.is_owner()
    async def reloadCogsDir(self, ctx, cogs):
        for extension in self.extensions:
            try:
                self.unload_extension(extension)
            except:
                pass

        #deleting the contents of the cogs list
        del cogs
           #Reload the cogs directory 
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
                        print(f"Appending: {cogstr} to cogs list.")
                        cogs.append(cogstr)
                    else:
                        pass

        for item in cogs:
            print(f"COgs List items: {item}")
            for cog in cogs:
                try:
                    print(f"Re-Loading cog {cog}")
                    self.bot.unload_extension(cog)
                    self.bot.reload_extension(cog) # I dont know if this will work or not does it load if not already loaded?
                    self.bot.load_extension(cog)
                    print(f"Done Loading {cog}")
                except Exception as err:
                    exec = (type(err).__name__)
                    print(f"Failed to Re-load cog: {exec}")
        await asyncio.sleep(0.5)
        # breakpoint()


        


def setup(bot):
    bot.add_cog(Admin(bot))
