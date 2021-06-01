from discord.ext import commands
from discord.ext.commands import CommandNotFound

class CommandNotFoundclass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.reply("command not found!")

def setup(bot):
	bot.add_cog(CommandNotFoundclass(bot))