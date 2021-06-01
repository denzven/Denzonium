#########################################
from discord.ext import commands
from bot.cogs.fun.web.youtube import GetYoutubeVideo
from discord.ext.commands import cooldown

class yt(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot
    @commands.command(aliases=["yt"])
    @cooldown(1,10,commands.BucketType.user) 
    async def youtube(self,ctx, *query):
      result = GetYoutubeVideo(' '.join(query))
      await ctx.reply(f"Link https://www.youtube.com/watch\?v={result}")
      pass

def setup(bot):
    bot.add_cog(yt(bot))    
