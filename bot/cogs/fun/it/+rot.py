from discord.ext import commands
import discord
import asyncio
import traceback
from discord.ext.commands import cooldown
random_sleep_time = 3
class rot(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(aliases=["./r"]) 
    @cooldown(1,10,commands.BucketType.user) 
    async def rot(self,ctx,tag:str,num:int,*,inputstr:str):
        try:
            outputstr = None
            inputstr = inputstr
            tag = tag
            d = {}
            if tag in ["-e","--encode"]:
                d = {}
                for c in (65, 97):
                    for i in range(26):
                        d[chr(i+c)] = chr((i-num) % 26 + c)
                outputstr = ("".join([d.get(c, c) for c in inputstr]))
                msg = await ctx.reply("[0%] " + " 🔑⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 🔓 encrypting...", mention_author=False)
                await asyncio.sleep(random_sleep_time)
                await msg.edit ( content = "[20%] " + " 🟩🟩🔑⬜⬜⬜⬜⬜⬜⬜ 🔓 encrypting..." )
                await asyncio.sleep(random_sleep_time)
                await msg.edit ( content = "[40%] " + " 🟩🟩🟩🟩🔑⬜⬜⬜⬜⬜ 🔓 encrypting..." )
                await asyncio.sleep(random_sleep_time)
                await msg.edit ( content = "[60%] " + " 🟩🟩🟩🟩🟩🟩🔑⬜⬜⬜ 🔓 encrypting..." )
                await asyncio.sleep(random_sleep_time)
                await msg.edit ( content = "[80%] " + " 🟩🟩🟩🟩🟩🟩🟩🟩🔑⬜ 🔓 encrypting..." )
                await asyncio.sleep(random_sleep_time)
                await msg.edit ( content = "[100%]" + " ✅✅✅✅✅✅✅✅✅✅ 🔒 ENCRYPTED!..." )
                embed=discord.Embed(title="ENCRYPT SUCCESSFUL!! ", description=f"```{outputstr}```", color=0xff0000)				
                await ctx.reply(embed=embed, mention_author=False)
    
            if tag in ["-d","--decode"]: 
                d = {}
                for c in (65, 97):
                    for i in range(26):
                        d[chr(i+c)] = chr((i+num) % 26 + c)
                outputstr = ("".join([d.get(c, c) for c in inputstr])) 
                msg = await ctx.reply("[0%] " + " 🔑⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 🔒 Derypting...", mention_author=False)
                await asyncio.sleep(random_sleep_time)
                await msg.edit ( content = "[20%] " + " 🟩🟩🔑⬜⬜⬜⬜⬜⬜⬜ 🔒 Derypting..." )
                await asyncio.sleep(random_sleep_time)
                await msg.edit ( content = "[40%] " + " 🟩🟩🟩🟩🔑⬜⬜⬜⬜⬜ 🔒 Derypting..." )
                await asyncio.sleep(random_sleep_time)
                await msg.edit ( content = "[60%] " + " 🟩🟩🟩🟩🟩🟩🔑⬜⬜⬜ 🔒 Derypting..." )
                await asyncio.sleep(random_sleep_time)
                await msg.edit ( content = "[80%] " + " 🟩🟩🟩🟩🟩🟩🟩🟩🔑⬜ 🔒 Derypting..." )
                await asyncio.sleep(random_sleep_time)
                await msg.edit ( content = "[100%]" + " ✅✅✅✅✅✅✅✅✅✅ 🔓 DECRYPT FOUND..." )
                embed=discord.Embed(title="DECRYPT SUCCESSFUL!! ",description=f"```{outputstr}```", color=0x37ff00)			
                await ctx.reply(embed=embed, mention_author=False)   
            if outputstr == None and inputstr == None:
                await ctx.reply("pls check the tag and try again (-e/-d)", mention_author=False)
    
            else:
                print('')
    
        except Exception:
            traceback.print_exc()
            

def setup(bot):
    bot.add_cog(rot(bot))