from discord.ext import commands
from discord.ext.commands import cooldown
import discord
import json
import os
from discord import Embed
import random

class economy(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()

    async def bal(self,ctx):
        await self.open_acc(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
        em = discord.Embed(title = f"{ctx.author.name}'s balance", color = discord.Color.red())
        em.add_field(name = "Wallet balance",value= wallet_amt)
        em.add_field(name = "Bank balance",value= bank_amt)
        await ctx.send(embed = em)

    @commands.command()
    @cooldown(1,60)
    async def beg(self,ctx):
        await self.open_acc(ctx.author)
        users = await self.get_bank_data()
        user = ctx.author
        earnings = random.randrange(101)
        await ctx.send(f"Someone gave you {earnings} coins ! !")
        users[str(user.id)]["wallet"] += earnings
        with open("bot/json/mainbank.json","w") as f:
            json.dump(users,f)

    async def open_acc(self,user):
        users = await self.get_bank_data()
        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}    
            users[str(user.id)]["wallet"] = 0
            users[str(user.id)]["bank"] = 0

        with open("bot/json/mainbank.json","w") as f:
            json.dump(users,f)
        return True
    async def get_bank_data(self):
        with open("bot/json/mainbank.json","r") as f:
            users = json.load(f)
        return users

def setup(bot):
    bot.add_cog(economy(bot))