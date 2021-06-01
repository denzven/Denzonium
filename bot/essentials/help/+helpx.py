from discord.ext import commands
import asyncio
import requests
import json
from discord.ext.commands import cooldown
import discord
from discord import Embed

class help(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    @cooldown(1,10,commands.BucketType.user) 
    async def helpx(self,ctx):

        embed=discord.Embed(title="help", description="help has arrived!", color=discord.Color.random())
        embed.add_field  ( name = "✨command name"                  , value = "```description of command```                                  " , inline = True)
        embed.add_field  ( name = "✨+8ball <question>"             , value = "```ask the magic 8ball```                                     " , inline = True)
        embed.add_field  ( name = "✨+base64 <tag(-e/-d)> <message>", value = "```encode and decode with base 64 cipher!```                  " , inline = True)
        embed.add_field  ( name = "✨+rot <tag(-e/-d)> <message>"   , value = "```encode and decode your message with the rot cipher!```     " , inline = True)
        embed.add_field  ( name = "✨+iptrack <ip>"                 , value = "```track and get info on ip```                                " , inline = True)
        embed.add_field  ( name = "✨+wiki <query>"                 , value = "```gets info from wiki```                                     " , inline = True)
        embed.add_field  ( name = "✨+timer <time in sec>"          , value = "```creates a timer for you```                                 " , inline = True)
        embed.add_field  ( name = "✨+youtube <query>"              , value = "```description of command```                                  " , inline = True)
        embed.add_field  ( name = "✨+ping"                         , value = "```gives ping of the bot```                                   " , inline = True)
        embed.add_field  ( name = "✨+wanted <member>"              , value = "```sends a wanted person photo```                             " , inline = True)
        embed.add_field  ( name = "✨+cat"                          , value = "```sends a cute cats pic```                                   " , inline = True)
        embed.add_field  ( name = "✨+sadcat"                       , value = "```sends a cute sadcats pic```                                " , inline = True)
        embed.add_field  ( name = "✨+dog"                          , value = "```sends a cute dogs pic```                                   " , inline = True)
        embed.set_footer(text=f'requested by {ctx.author}',icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(help(bot))