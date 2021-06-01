from discord.ext import commands
import base64
import discord
import asyncio
import traceback
from discord.ext.commands import cooldown

class enc(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(name='base64', aliases=["./b64","b64"])
    @cooldown(1,10,commands.BucketType.user) 
    async def base64(self, ctx,tag,*,inputb64):
        outputdec = None 
        outputenc = None
        random_sleep_time = 3
        try:
            if tag in ["-e","--encode"]:
                encoded_as_bytes = base64.b64encode(inputb64.encode())
                outputenc = str(encoded_as_bytes, "utf-8")
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
                embed=discord.Embed(title="ENCRYPT SUCCESSFUL!! ", description=f"```{outputenc}```", color=0xff0000)				
                await ctx.reply(embed=embed, mention_author=False)

            if tag in ["-d","--decode"]: 
                decoded_as_bytes = base64.b64decode(inputb64.encode()) 
                outputdec = str(decoded_as_bytes,"utf-8") 
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
                embed=discord.Embed(title="DECRYPT SUCCESSFUL!! ",description=f"```{outputdec}```", color=0x37ff00)			
                await ctx.reply(embed=embed, mention_author=False)

            if outputdec  == None and outputenc == None:
                await ctx.reply("pls check the tag and try again (-e/-d)", mention_author=False)
        
        except Exception as e:
                traceback.print_exc()
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
                await msg.edit ( content = "[100%]" + " ❌❌❌❌❌❌❌❌❌❌ 🔒 DECRYPT NOT FOUND..." )
                await ctx.reply('error! pls check the command again!')
                await ctx.author.send(e)

def setup(bot):
    bot.add_cog(enc(bot))
