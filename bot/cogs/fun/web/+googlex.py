from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import urllib
from discord.ext.commands import cooldown

class google(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    @cooldown(1,10,commands.BucketType.user) 
    async def googlex(self,ctx, *, query):
    
        global link, i
        searchInput = "https://google.com/search?q="+urllib.parse.quote(query)
        res = requests.get(searchInput)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        linkElements = soup.select('div#main > div > div > div > a')
        if len(linkElements) == 0:
            await ctx.send("Couldn't find any results...")
    
        else:
            link = linkElements[0].get("href")
            i = 0
    
        while link[0:4] != "/url" or link[14:20] == "google":
            i += 1
            link = linkElements[i].get("href")
    
        await ctx.send("http://google.com"+link)

def setup(bot):
    bot.add_cog(google(bot))
