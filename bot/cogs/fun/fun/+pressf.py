from discord.ext import commands
import discord
import random

f = [
    "https://tenor.com/view/team-fortress2-pay-respects-press-f-gif-14764178",
    "https://tenor.com/view/press-f-pay-respect-keyboard-gif-12855017",
    "https://tenor.com/view/f-respect-coffin-respect-video-game-gif-17724130",
    "https://tenor.com/view/press-f-pay-respect-gif-12855019",
    "https://tenor.com/view/karol-paciorek-lekko-stronniczy-ls-bezbek-gif-19272367",
    "https://tenor.com/view/press-f-gif-18676734"
    ]
class pressf(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    async def pressf(self,ctx):
        embed=discord.Embed(title='', color=discord.Color.random())
        embed.set_image(url=random.choice(f))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(pressf(bot))