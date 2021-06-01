
import asyncio
from discord.ext import commands
import discord
import random
import datetime


class giveaway(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def giveaway(self,ctx, duration: int, *, prize: str):
        embed = discord.Embed(title=prize,
                              description=f"Hosted by - {ctx.author.mention}\nReact with :tada: to enter!\nTime Remaining: **{duration}** seconds",
                              color=ctx.guild.me.top_role.color, )

        msg = await ctx.channel.send(content=":tada: **GIVEAWAY** :tada:", embed=embed)
        await msg.add_reaction("🎉")
        await asyncio.sleep(duration)
        new_msg = await ctx.channel.fetch_message(msg.id)

        user_list = [u for u in await new_msg.reactions[0].users().flatten() if u != self.bot.user] # Check the reactions/don't count the bot reaction
        if len(user_list) == 0:
            await ctx.send("No one reacted.") 
        else:
            winner = random.choice(user_list)
            e = discord.Embed()
            e.title = "Giveaway ended!"
            e.description = f"{winner.mention} won: {prize}"
            e.timestamp = datetime.datetime.utcnow()
            await ctx.send(f"{winner.mention}", embed=e)

def setup(bot):
    bot.add_cog(giveaway(bot))