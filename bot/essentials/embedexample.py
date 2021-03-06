from discord.ext import commands
import discord
import datetime

class embedexample(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command()
    async def embedexample(self,ctx):
        embed = discord.Embed(
            title="this *supports* a **subset** of ~~R Markdown~~",
            colour=discord.Colour(0x3b12ef),
            url="https://discord.com/",
            description="this supports [named links](https://discord.com/) on top of the subset of markdown.\nYou can use newlines too!",
            timestamp=datetime.datetime.utcfromtimestamp(1580842764) # or any other datetime type format.
        )
        embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/1.png")
        embed.set_author(
            name="author name",
            url="https://discord.com/", 
            icon_url="https://cdn.discordapp.com/embed/avatars/2.png"
        )
        embed.set_footer(
            text="footer text",
            icon_url="https://cdn.discordapp.com/embed/avatars/3.png"
        )

        embed.add_field(
            name="field title",
            value="some of these properties have different limits."
        )
        embed.add_field(
            name="another field title",
            value="try exceeding some of them! (coz idk them)"
        )
        embed.add_field(
            name=":thinking: this supports emotes! (and custom ones too)",
            value="if you exceed them, the error will tell you which value exceeds it."
        )
        embed.add_field(
            name="Inline",
            value="these last two fields",
            inline=True
        )
        embed.add_field(
            name="Fields",
            value="are inline fields",
            inline=True
        )


        await ctx.send(
            content="This is a normal message to be sent alongside the embed",
            embed=embed
        )

def setup(bot):
    bot.add_cog(embedexample(bot))