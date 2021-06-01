import wikipedia
from discord.ext import commands
import discord
from discord.ext.commands import cooldown


class wiki(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot
    @commands.command("wiki", help="Fetch the summary from wikipedia page")
    @cooldown(1,10,commands.BucketType.user) 
    async def wiki(self,ctx, *query):
      search = ''.join(query)
      search = search.strip()
      try :
        results = wikipedia.summary(search, sentences=2)
        await ctx.reply(f"Results for {search}!")
        await ctx.reply(results)
        await ctx.reply(f"Wikipedia page url {wikipedia.page(search).url}")
      except Exception as e:
        await ctx.reply("Specify please!")
      pass

def setup(bot):
    bot.add_cog(wiki(bot))
