from discord.ext import commands
import discord
import os

class ping(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot
    @commands.command() 
    async def ping(self,ctx):
        await ctx.reply(f'ping of discord.py module----> {round(self.bot.latency*1000)}ms', mention_author=False)
def setup(bot):
    bot.add_cog(ping(bot))