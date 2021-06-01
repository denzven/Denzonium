from discord.ext import commands
import discord
from PIL import Image
from io import BytesIO
from discord.ext.commands import cooldown
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

class rip(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    @cooldown(1,10,commands.BucketType.user) 
    async def rip(self,ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        wanted = Image.open("bot/cogs/fun/img/input_img/" + "rip.png")
        asset = user.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((237,237))
        wanted.paste(pfp,(118,276))
        wanted.save("bot/cogs/fun/img/output_img/" + "rip_final.png")
        await ctx.send(file = discord.File("bot/cogs/fun/img/output_img/" + "rip_final.png"))

    

def setup(bot):
    bot.add_cog(rip(bot))