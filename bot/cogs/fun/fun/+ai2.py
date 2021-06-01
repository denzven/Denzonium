from discord.ext import commands
from prsaw import RandomStuff
import os
from discord.ext.commands import cooldown

api_key = os.environ['prsaw api key']
rs = RandomStuff(api_key = api_key, async_mode=True)

class ai(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    async def ai(self,ctx,*msg):
        first_msg =  await ctx.reply("lemme think...")
        response = await rs.get_ai_response(msg)
        await first_msg.edit(content = response)
        
def setup(bot):
    bot.add_cog(ai(bot))