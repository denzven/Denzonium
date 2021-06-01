
import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://denzven:1234@cluster0.vaa3d.mongodb.net/test")

db = cluster["Denzonium_db"]

collection = db["Denzonium_db"]

from discord.ext import commands

class cogclass(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    async def dbtest(self,ctx):
        post = {"_id": ctx.author.id, "score": 1}
        collection.insert_one(post)
        await ctx.channel.send('accepted!')

def setup(bot):
    bot.add_cog(cogclass(bot))

