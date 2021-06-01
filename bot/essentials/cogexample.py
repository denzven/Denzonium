from discord.ext import commands

class cogclass(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    async def cogcommand(self,ctx):
        print("stuff")

def setup(bot):
    bot.add_cog(cogclass(bot))