from discord.ext import commands
from discord.ext.commands import cooldown
from prsaw import RandomStuff
import os

api_key = os.environ['prsaw api key']
rs = RandomStuff(api_key = api_key, async_mode=True)

class ai(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.Cog.listener()
    @cooldown(20,10,commands.BucketType.user) 
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.channel.id == 831365004984975391:
            response = await rs.get_ai_response(message.content)
            await message.reply(response)
        
def setup(bot):
    bot.add_cog(ai(bot))