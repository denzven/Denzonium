from discord.ext import commands
import random
import requests
import discord
from discord.ext.commands import cooldown
import traceback

class cogclass(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot    
    
    @commands.command()
    @commands.is_nsfw()
    @cooldown(1,10,commands.BucketType.user) 
    async def henisfun(self,ctx):
        inputreq = ['Random_hentai_gif', 'meow', 'erok', 'lizard', 'feetg', 'baka', 'v3', 'bj', 'erokemo', 'tickle', 'feed', 'neko', 'kuni', 'femdom', 'futanari', 'smallboobs', 'goose', 'nekoapi_v3.1', 'poke', 'les', 'trap', 'pat', 'boobs', 'blowjob', 'hentai', 'hololewd', 'ngif', 'fox_girl', 'wallpaper', 'lewdk', 'solog', 'pussy', 'yuri', 'lewdkemo', 'lewd', 'anal', 'pwankg', 'nsfw_avatar', 'eron', 'kiss', 'pussy_jpg', 'woof', 'hug', 'keta', 'cuddle', 'eroyuri', 'slap', 'cum_jpg', 'waifu', 'gecg', 'tits', 'avatar', 'holoero', 'classic', 'kemonomimi', 'feet', 'gasm', 'spank', 'erofeet', 'ero', 'solo', 'cum', 'smug', 'holo', 'nsfw_neko_gif']
        ran_req = random.choice(inputreq)
        try:
            r = requests.get(f'https://nekos.life/api/v2/img/{ran_req}')
            res = r.json()
            embed=discord.Embed(title=f'{res["url"]} from {ran_req}', color=discord.Color.random())
            embed.set_image(url=res["url"])

            await ctx.send(embed=embed)

        except Exception as e:
            traceback.print_exc()

    @commands.command()
    @cooldown(1,10,commands.BucketType.user) 
    async def hug(self,ctx, user:discord.Member):
        if len(ctx.message.mentions) != 1:
            await ctx.send("you must mention a user!")
            return
        try:
            r = requests.get(f'https://nekos.life/api/v2/img/hug')
            res = r.json()
            embed = discord.Embed(title=f"{ctx.author.display_name} hugs {user.display_name}",color=discord.Color.random(), description="aww...")
            embed.set_image(url=res["url"])

            await ctx.send(embed=embed)

        except Exception as e:
            traceback.print_exc()

    @commands.command()
    @commands.is_nsfw()
    @cooldown(1,10,commands.BucketType.user) 
    async def kiss(self,ctx, user:discord.Member):
        if len(ctx.message.mentions) != 1:
            await ctx.send("you must mention a user!")
            return
        try:
            r = requests.get(f'https://nekos.life/api/v2/img/kiss')
            res = r.json()
            embed = discord.Embed(title=f"{ctx.author.display_name} kisses {user.display_name}",color=discord.Color.random(), description="aww...")
            embed.set_image(url=res["url"])

            await ctx.send(embed=embed)

        except Exception as e:
            traceback.print_exc()

    @commands.command()
    @cooldown(1,10,commands.BucketType.user) 
    async def pat(self,ctx, user:discord.Member):
        if len(ctx.message.mentions) != 1:
            await ctx.send("you must mention a user!")
            return
        try:
            r = requests.get(f'https://nekos.life/api/v2/img/pat')
            res = r.json()
            embed = discord.Embed(title=f"{ctx.author.display_name} pats {user.display_name}",color=discord.Color.random(), description="aww...")
            embed.set_image(url=res["url"])

            await ctx.send(embed=embed)

        except Exception as e:
            traceback.print_exc()

    
    @commands.command()
    @commands.is_nsfw()
    @cooldown(1,10,commands.BucketType.user) 
    async def slap(self,ctx, user:discord.Member):
        if len(ctx.message.mentions) != 1:
            await ctx.send("you must mention a user!")
            return
        try:
            r = requests.get(f'https://nekos.life/api/v2/img/slap')
            res = r.json()
            embed = discord.Embed(title=f"{ctx.author.display_name} slapped {user.display_name}",color=discord.Color.random())
            embed.set_image(url=res["url"])

            await ctx.send(embed=embed)

        except Exception as e:
            traceback.print_exc()

def setup(bot):
    bot.add_cog(cogclass(bot))