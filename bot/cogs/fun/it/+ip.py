from discord.ext import commands
import asyncio
import requests
import json
from discord.ext.commands import cooldown
import discord
from discord import Embed

class iptrack(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(aliases = ["ip"])
    @cooldown(1,10,commands.BucketType.user) 
    async def iptrack(self,ctx,inputip):
        """tracks ip."""
        r = requests.get(f"http://ip-api.com/json/{inputip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
        res = r.json()
        countrycode = res["countryCode"]
        country = res["country"]
        region = res["region"]
        regionName = res["regionName"]
        city = res["city"]
        lat = res["lat"]
        lon = res["lon"]
        time_zone = res["timezone"]
        isp = res["isp"]
        query = res["query"]
        continent = res["continent"]
        continentcode = res["continentCode"]
        name = res["asname"]

        #await ctx.send(f"countrycode - {countrycode} \ncountry - {country} \nregion - {region} \nregionName - {regionName} \ncity - {city} \nlat - {lat} \nlon - {lon} \ntime_zone - {time_zone} \nisp - {isp} \nquery- {query} \ncontinent - {continent} \ncontinentcode - {continentcode} \nname - {name}")

        embed=discord.Embed(title=f"{name} = {query}", description="tracks and gives info abt the given ip", color=discord.Color.random())
        embed.add_field  ( name = "continent"      , value = f"{continent}"     , inline = False )
        embed.add_field  ( name = "continent code" , value = f"{continentcode}" , inline = False )
        embed.add_field  ( name = "country"        , value = f"{country}"       , inline = False )
        embed.add_field  ( name = "country code"   , value = f"{countrycode}"   , inline = False )
        embed.add_field  ( name = "region name"    , value = f"{regionName}"    , inline = False )
        embed.add_field  ( name = "region"         , value = f"{region}"        , inline = False )
        embed.add_field  ( name = "city"           , value = f"{city}"          , inline = False )
        embed.add_field  ( name = "timezone"       , value = f"{time_zone}"     , inline = False )
        embed.add_field  ( name = "isp"            , value = f"{isp}"           , inline = False )
        embed.add_field  ( name = "latitude"       , value = f"{lat}"           , inline = False )
        embed.add_field  ( name = "longitude"      , value = f"{lon}"           , inline = False )
        embed.set_footer(text=f'requested by {ctx.author}',icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(iptrack(bot))