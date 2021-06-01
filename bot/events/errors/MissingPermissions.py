from discord.ext import commands
from discord.ext.commands import CommandNotFound

class MissingPermissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.reply("You don't have permission.")
            return

def setup(bot):
	bot.add_cog(MissingPermissions(bot))