from discord.ext import commands
from discord.ext.commands import CommandNotFound

class MissingRequiredArgument(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.reply('MissingRequiredArgument')

def setup(bot):
	bot.add_cog(MissingRequiredArgument(bot))