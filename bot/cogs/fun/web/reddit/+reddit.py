import discord
from discord.ext import commands
import random
import traceback
import requests
from discord.ext.commands import cooldown

class reddit(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    async def meme(self,ctx):
        try:
            r = requests.get('https://memes.blademaker.tv/api?lang=en')
            res = r.json()
            title = res["title"]
            ups = res["ups"]
            sub = res["subreddit"]
            isNSFW = res["nsfw"]
            embed=discord.Embed(title=f'{title}\nsubreddit:{sub}', color=discord.Color.random())
            embed.set_image(url=res["image"])
            embed.set_footer(text=f" 👍  : {ups}\n {ctx.author}")
            if isNSFW == False:
                print("nope nsfw")
                await ctx.reply(embed=embed,mention_author=False)
            if isNSFW == True:
                print("nsfw")
                pass

        except Exception as e:
            print(e)

    @commands.command()
    @cooldown(1,10,commands.BucketType.user) 
    async def reddit(self,ctx,input = None):
        try:
            r = requests.get(f'https://memes.blademaker.tv/api/{input}')
            res = r.json()
            title = res["title"]
            ups = res["ups"]
            downs = res["downs"]
            sub = res["subreddit"]
            isNSFW = res["nsfw"]
            embed=discord.Embed(title=f'{title} \n subreddit: r/{sub}', color=discord.Color.random())
            embed.set_image(url=res["image"])
            embed.set_footer(text=f" 👍  : {ups}\n {ctx.author}")
            if input == None:
                await ctx.reply(f"{ctx.author.display_name},you cant leave your input empty",mention_author=False)
            if isNSFW == False and input != None:
                print("nope nsfw")
                await ctx.reply(embed=embed,mention_author=False)
            if isNSFW == True:
                print("nsfw")
                await ctx.reply(f"post from `{input}` was nsfw, try another",mention_author=False)
                pass
        except Exception as e:
            print(e)
            await ctx.reply("no response from api, try another",mention_author=False)

    @commands.command()
    @commands.is_nsfw()
    @cooldown(1,10,commands.BucketType.user) 
    async def nsfw(self,ctx,input):
        try:
            r = requests.get(f'https://memes.blademaker.tv/api/{input}')
            res = r.json()
            title = res["title"]
            ups = res["ups"]
            sub = res["subreddit"]
            isNSFW = res["nsfw"]
            embed=discord.Embed(title=f'{title}\nsubreddit: r/{sub}', color=discord.Color.random())
            embed.set_image(url=res["image"])
            embed.set_footer(text=f"👍:{ups}")
            if isNSFW == False:
                pass
            if isNSFW == True:
                await ctx.send(embed=embed)

        except Exception as e:
            traceback.print_exc()

def setup(bot):
    bot.add_cog(reddit(bot))