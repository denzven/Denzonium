from akinator.async_aki import Akinator
import akinator as ak
from discord.ext import commands
from discord.ext.commands import cooldown

class akinator(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(aliases=["aki"])
    @cooldown(1,10,commands.BucketType.user) 
    async def akinator(self,ctx):
        await ctx.reply("Akinator is here to guess!")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n","p","b","c"]
        try:
            aki = ak.Akinator()
            q = aki.start_game()
            while aki.progression <= 80:
                await ctx.reply(q, mention_author=False)
                await ctx.send("Your answer:(y/n/p/b/c)")
                msg = await  self.bot.wait_for("message", check=check)
                if msg.content.lower() == "b":
                    try:
                        q=aki.back()
                    except ak.CantGoBackAnyFurther as e:
                        await ctx.reply(e, mention_author=False)
                        continue
                elif msg.content.lower() == "c":
                    await ctx.reply("Game cancelled!", mention_author=False)
                    return
                else:
                    try:
                        q = aki.answer(msg.content.lower())
                    except ak.InvalidAnswerError as e:
                        await ctx.reply(e, mention_author=False)
                        continue
            aki.win()
            await ctx.reply(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?(y/n)\n{aki.first_guess['absolute_picture_path']}\n\t", mention_author=False)
            correct = await self.bot.wait_for("message", check=check)
            if correct.content.lower() == "y":
                await ctx.reply("Yay\n", mention_author=False)
            else:
                await ctx.reply("Oof\n", mention_author=False)
        except Exception as e:
            await ctx.reply(e, mention_author=False)
def setup(bot):
    bot.add_cog(akinator(bot))