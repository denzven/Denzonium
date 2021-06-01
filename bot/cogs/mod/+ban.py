from discord.ext import commands
import discord

class ban(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self,ctx, member : discord.Member = None,*,reason="Reason not given"):
      if ctx.author == member:
        await ctx.send("Yea you cant ban your self nerd")
        return
      if member is None:
        return await ctx.send("Please put a member") 

      if member.top_role.position > ctx.author.top_role.position:
        return await ctx.send("You're not high enough in the role hierarchy to do that.")

      try:
        guild = ctx.guild
        await member.send(f"Your were banned from {member.guild} for {reason} by {ctx.author}")
        await ctx.send(f"**BANNED** {member}")
        await member.ban(reason=reason)
        em = discord.Embed(title="Ban", timestamp=ctx.message.created_at, description=f"**Offender**: {member.name}\n**Reason**: {reason}\n **Responsible Moderator:** {ctx.author}", color=discord.Color.red())
        em.set_footer(text=f"ID: {member.id}")
        mod_log2 = discord.utils.get(guild.channels, name="parallel-logs")
        await ctx.send(embed=em)

      except:
        guild = ctx.guild
        await ctx.send(f"**BANNED** {member}")
        await member.ban(reason=reason)
        em = discord.Embed(title="Ban", timestamp=ctx.message.created_at, description=f"**Offender**: {member.name}\n**Reason**: {reason}\n **Responsible Moderator:** {ctx.author}", color=discord.Color.red())
        em.set_footer(text=f"ID: {member.id}")
        mod_log2 = discord.utils.get(guild.channels, name="parallel-logs")
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(ban(bot))