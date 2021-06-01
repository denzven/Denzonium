from discord.ext import commands
from discord.ext.commands import CommandNotFound

class NSFWChannelRequired(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.errors.NSFWChannelRequired):
            await ctx.reply('NSFWChannelRequired')

def setup(bot):
	bot.add_cog(NSFWChannelRequired(bot))