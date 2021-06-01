from discord.ext import commands
import discord
import datetime

class serverinfo(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    async def memberinfo(self,ctx):
        embed = discord.Embed(title=f"serverinfo", description="shows guild info", timestamp=datetime.datetime.utcnow(), color=discord.Color.random())
        embed.add_field( name = "Server name"                     , value = f"```{ctx.guild.name}```"                      , inline = False )
        embed.add_field( name = "Server created at"               , value = f"```{ctx.guild.created_at}```"                , inline = False )
        embed.add_field( name = "Server Owner"                    , value = f"```{ctx.guild.owner}```"                     , inline = False )
        embed.add_field( name = "Server Region"                   , value = f"```{ctx.guild.region}```"                    , inline = False )
        embed.add_field( name = "Server ID"                       , value = f"```{ctx.guild.id}```"                        , inline = False )
        embed.add_field( name = "Server member count"             , value = f"```{ctx.guild.member_count}```"              , inline = False )
        embed.add_field( name = "Server emoji limit"              , value = f"```{ctx.guild.emoji_limit}```"               , inline = False )
        embed.add_field( name = "Server afk channel"              , value = f"```{ctx.guild.afk_channel}```"               , inline = False )
        embed.add_field( name = "Server afk timeout"              , value = f"```{ctx.guild.afk_timeout}s```"              , inline = False )
        embed.add_field( name = "Server rules channel"            , value = f"```#{ctx.guild.rules_channel}```"            , inline = False )
        embed.add_field( name = "Server public updates channel"   , value = f"```#{ctx.guild.public_updates_channel}```"   , inline = False )
        embed.add_field( name = "Server system channel"           , value = f"```#{ctx.guild.system_channel}```"           , inline = False )
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        embed.set_footer(text=f'{ctx.author}',icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(serverinfo(bot))
    

