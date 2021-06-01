from datetime import datetime
from typing import Optional

from discord import Embed, Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from typing import Union
import discord

class Info(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="userinfo", aliases=["memberinfo", "ui", "mi"])
    async def user_info(self, ctx,user: Union[discord.Member, discord.User] = None):
        if user == None:
            user = ctx.author 

        embed = Embed(title="User information",
					  colour=user.colour,
					  timestamp=datetime.utcnow())

        embed.set_thumbnail(url=user.avatar_url)
            
        fields = [("Name", str(user), True),
				  ("ID", user.id, True),
				  ("Bot?", user.bot, True),
				  ("Top role", user.top_role.mention, True),
				  ("Status", str(user.status).title(), True),
				  ("Activity", f"{str(user.activity.type).split('.')[-1].title() if user.activity else 'N/A'} {user.activity.name if user.activity else ''}", True),
				  ("Created at", user.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
				  ("Joined at", user.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
				  ("Boosted", bool(user.premium_since), True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

    @command(name="serverinfo", aliases=["guildinfo", "si", "gi"])
    async def server_info(self, ctx):
        embed = Embed(title="Server information",
	                colour=ctx.guild.owner.colour,
					timestamp=datetime.utcnow())

        embed.set_thumbnail(url=ctx.guild.icon_url)

        memberinfo     = [
                    len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members))),
                    len(list(filter(lambda m: not m.bot, ctx.guild.members))),
                    len(list(filter(lambda m: m.bot, ctx.guild.members))),
                    len(ctx.guild.members),
                    len(await ctx.guild.bans())
                    ]
        channelsinfo =  [
                    len(ctx.guild.text_channels),
					len(ctx.guild.voice_channels),
					len(ctx.guild.categories),
					len(ctx.guild.roles),
                    len(await ctx.guild.invites()),
                    ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"),
                    ctx.guild.region,
                    ctx.guild.owner
                        ]

        fields = [("ID", ctx.guild.id, False),

				  ("Members Info"       , f"👥`  total:` {memberinfo[6]}\n\n🟢` online:` {memberinfo[0]}\n🟠`   idle:` {memberinfo[1]}\n🔴`    dnd:` {memberinfo[2]}\n⚪`offline:` {memberinfo[3]}\n\n👨‍🦰` humans:` {memberinfo[4]}\n🤖`   bots:` {memberinfo[5]}\n\n🔨` banned:` {memberinfo[7]}", True),

				  ("Server Info"       , f"   ⚜`  categories:` {channelsinfo[2]}\n\n#️⃣`       text:` {channelsinfo[0]}\n🔊`      voice:` {channelsinfo[1]}\n🟣`      roles:` {channelsinfo[3]}\n👋`    invites:` {channelsinfo[4]}\n\n⏰` created at:` {channelsinfo[5]}\n🌏`     region:` {channelsinfo[6]}\n\n👑`      owner:` {channelsinfo[7]}", True)]

        for name, value, inline in fields:
	        embed.add_field(name=name, value=value, inline=inline)
        embed.set_footer(text=f'requested by {ctx.author}',icon_url = ctx.author.avatar_url)

        await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Info(bot))