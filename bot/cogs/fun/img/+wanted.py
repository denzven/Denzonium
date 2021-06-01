from discord.ext import commands
import discord
from PIL import Image
from io import BytesIO
from discord.ext.commands import cooldown

class wanted(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    @cooldown(1,10,commands.BucketType.user) 
    async def wanted(self,ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        wanted = Image.open("bot/cogs/fun/img/input_img/" + "wanted.jpg")
        asset = user.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((291,291))
        wanted.paste(pfp,(87,224))
        wanted.save("bot/cogs/fun/img/output_img/" + "wanted_final.jpg")
        await ctx.send(file = discord.File("bot/cogs/fun/img/output_img/" + "wanted_final.jpg"))

    

def setup(bot):
    bot.add_cog(wanted(bot))