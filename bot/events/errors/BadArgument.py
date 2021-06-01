from discord.ext import commands
from discord.ext.commands import CommandNotFound

class BadArgument(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error,commands.BadArgument):
            await ctx.send('BadArgument') 

def setup(bot):
	bot.add_cog(BadArgument(bot))