"""This as a Command and Control cog for my bots"""
import asyncio
import os
import discord
from discord.ext import commands
from discord import Command

print(dir(Command))

print(dir(commands))





class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commmands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n~~~")

    @commands.command(
        name='reload', description="Reload all one of the cogs"
    )
    @commands.is_owner()
    async def reload(self, ctx):
        async with ctx.typing():
            embed = discord.Embed(
                title="Reloading cogs!",
                color=0x0008080,
                timestamp=ctx.message.created_at
            )
            for ext in os.listdir("./Cogs"):
                if ext.endswith("_cog.py") and not ext.startsswith("_"):
                    try:
                        self.bot.unload.extensions(f"cogs.{ext[:-3]}")
                        self.bot.load.extensions(f"cogs.{ext[:-3]}")
                        embed.add_field(
                            name=f"Reloaded: '{ext}'",
                            value='\uFEFF',
                            inline=False

                        )
                    except Exception as e:
                        embed.add_field(
                            name=f"Failed to Reload:'{ext}'",
                            value=e,
                            inline=False
                        )
                    await asyncio.sleep(0.5)


def setup(bot):
    bot.add_cog(Admin(bot))
