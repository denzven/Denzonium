from discord.ext import commands
from discord.ext.commands import cooldown
import asyncio
import discord
from discord import Embed as e
from typing import Optional, Union

class timer(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    @cooldown(1,10,commands.BucketType.user) 
    async def timer(self,ctx,time_input): #done

        t=int(time_input)
        sleep = 1
        if t > 3600:
            await ctx.reply("thats over an hour.. sry", mention_author=False)
        if t < 0:
            negative_embed = e(title='i aint dr.strange.. time doesnt go negative irl lol', color=discord.Color.random())
            await ctx.reply(embed=negative_embed, mention_author=False)
        if t <= 3600 and t > 0 :
            mins = t // 60
            secs = t % 60
            first_embed = e(title='Timer',description=f'```{mins}:{secs}```', color=discord.Color.random())#first sent embed
            msg = await ctx.reply(embed=first_embed, mention_author=False)
            while t:
                t -= 1
                mins = t // 60
                secs = t % 60      
                await asyncio.sleep(sleep)
                editembed = e(title="Timer",description=f'```{mins}:{secs}```', color=discord.Color.random())#editing embed
                timesup_embed = e(title='Times up!',description=f'```{mins}:{secs}```', color=discord.Color.random()) #timesup embed
                await msg.edit ( embed=editembed ) 
            else:
                await msg.edit ( content = " ", embed=timesup_embed)

def setup(bot):
    bot.add_cog(timer(bot))