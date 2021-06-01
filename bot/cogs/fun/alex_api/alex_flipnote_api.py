from discord.ext import commands
import os
import alexflipnote
import discord 
alex_api = alexflipnote.Client(os.getenv("apitoken"))

class alexflipnote_api(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

##################################
    @commands.command()
    async def birb(self,ctx):
        birbimg = await alex_api.birb()
        await ctx.reply(birbimg, mention_author=False)

    @commands.command()
    async def cat(self,ctx):
        catimg = await alex_api.cats()
        await ctx.reply(catimg, mention_author=False)

    @commands.command()
    async def dog(self,ctx):
        dogimg = await alex_api.dogs()
        await ctx.reply(dogimg, mention_author=False)

    @commands.command()
    async def sadcat(self,ctx):
        sadcatimg = await alex_api.sadcat()
        await ctx.reply(sadcatimg, mention_author=False)

  
    @commands.command()
    async def fml(self,ctx):
        fmlimg = await alex_api.fml()
        await ctx.reply(fmlimg, mention_author=False)


    @commands.command()
    async def captcha(self,ctx, text: str):
        image = await alex_api.captcha(text=text)
        image_bytes = await image.read()
        file = discord.File(image_bytes, "captcha.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)

    @commands.command()
    async def supreme(self,ctx, text: str):
        image = await alex_api.supreme(text = text)
        image_bytes = await image.read() 
        file = discord.File(image_bytes, "supreme.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)

    @commands.command()
    async def amiajoke(self,ctx,  user: discord.Member = None):
        if user == None:
            user = ctx.author
        image = user.avatar_url
        image = await alex_api.amiajoke(image)
        image_bytes = await image.read() 
        file = discord.File(image_bytes, "amiajoke.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)

    @commands.command()
    async def woosh(self,ctx,  user: discord.Member = None):
        if user == None:
            user = ctx.author
        image = user.avatar_url
        image = await alex_api.joke_overhead(image)
        image_bytes = await image.read() 
        file = discord.File(image_bytes, "woosh.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)

    @commands.command()
    async def bad(self,ctx,  user: discord.Member = None):
        if user == None:
            user = ctx.author
        image = user.avatar_url
        image = await alex_api.bad(image)
        image_bytes = await image.read() 
        file = discord.File(image_bytes, "bad.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)

    @commands.command()
    async def drake(self,ctx,top :str,bottom :str):
        image = await alex_api.drake(top, bottom)
        image_bytes = await image.read() 
        file = discord.File(image_bytes, "drake.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)

    @commands.command()
    async def pornhub(self,ctx,text :str,text2:str):
        image = await alex_api.pornhub(text, text2)
        image_bytes = await image.read() 
        file = discord.File(image_bytes, "pornhub.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)

    @commands.command()
    async def didyoumean(self,ctx,top :str,bottom :str):
        image = await alex_api.did_you_mean(top, bottom)
        image_bytes = await image.read() 
        file = discord.File(image_bytes, "didyoumean.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)

    @commands.command()
    async def facts(self,ctx, text: str):
        image = await alex_api.facts(text)
        image_bytes = await image.read() 
        file = discord.File(image_bytes, "facts.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)

    @commands.command()
    async def floor(self,ctx, text: str):
        image = await alex_api.floor(text, image = None)
        image_bytes = await image.read() 
        file = discord.File(image_bytes, "floor.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)

    @commands.command()
    async def call(self,ctx, text: str):
        image = await alex_api.calling(text = text)
        image_bytes = await image.read() 
        file = discord.File(image_bytes, "calling.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)

    @commands.command()
    async def achievement(self,ctx, text: str, icon = None): 
        image = await alex_api.achievement(text=text, icon=icon)
        image_bytes = await image.read()
        file = discord.File(image_bytes, "achievement.png")
        await ctx.reply(f"Rendered by {ctx.author}", file=file, mention_author=False)


def setup(bot):
    bot.add_cog(alexflipnote_api(bot))    
