from discord.ext import commands
from discord.ext.commands import CommandNotFound
import discord

class CommandOnCooldown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error,commands.errors.CommandOnCooldown):
            em = discord.Embed(title="Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.")
            await ctx.reply(embed=em)

def setup(bot):
	bot.add_cog(CommandOnCooldown(bot))