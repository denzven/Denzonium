
#welcome fellow botdev/coder, hope you are fine and find my python module helpfull
#this is a part of my denzonium bot if you want to invite it to your server 
# https://dsc.gg/denzonium_bot
# goto to this link and invite :)

import discord
import os
import alexflipnote
from discord.ext import commands
from bot.essentials.keep_alive import keep_alive
from pretty_help import PrettyHelp
from bot.essentials.statuslist import inputstatus
from bot.coglist import cogs
import json
import asyncio
import datetime
from datetime import datetime
import random

defaults = os.listdir()
description = 'description'
#intents.members = True,
#intents.presences = True,
#bot = commands.Bot(command_prefix=commands.when_mentioned_or("+"), intents = intents,help_command=PrettyHelp())
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("+"), 
    intents = discord.Intents.all(),
    case_insensitive = True,
    allowed_mentions = discord.AllowedMentions(
        users = True,
        replied_user = False,
        roles = False,
        everyone = False
    )
)
alex_api = alexflipnote.Client(os.environ['apitoken'])


@bot.event
async def on_connect():
    print("The bot connected!")

@bot.event
async def on_command(ctx):
    server = ctx.guild.name
    channel = ctx.channel
    user = ctx.author
    command = ctx.command
    print(f'{server} > {channel} > {user} > {command}')

@bot.event
async def on_command_error(ctx, error):
    raise error

async def status_task():
    while True:
        random_status = random.choice(inputstatus)
        await bot.change_presence(activity=discord.Game(name=f"+help | Guilds: {len(bot.guilds)} | Members: {len(bot.users)}"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"{random_status}"))
        await asyncio.sleep(10)

from discord import User
from discord.ext.commands import Bot, guild_only

@bot.command(name='unban')
@guild_only()  # Might not need ()
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    
    print('We have logged in as {0.user}\n'.format(bot))
    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"{cog}")
        except Exception as e:
            print(e)
    for guild in bot.guilds:
        print(f'name:{guild.name}\nguild id:{guild.id}') 
    print('\n#######################')
    print('ready to rock and roll!')
    print('#######################')

@bot.command()
@commands.is_owner()
async def say(ctx, *,text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

@bot.command(pass_context=True, aliases=["pls change my nickname"])
@commands.is_owner()
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')


@bot.command(aliases=["r"])
async def reload(ctx, cog):
    if not cog:
        await ctx.reply('Specify the cog to reload!')
        return
    try:
        bot.unload_extension(f'{cog}')
        bot.load_extension(f'{cog}')
        await ctx.reply(f"{cog} reloaded")
    except Exception as e:
        print(f'{cog} could not be loaded!')
        await ctx.reply(e)

@bot.command()
@commands.is_owner()
async def nuke(ctx):
    embed = discord.Embed(
        title=f":boom: Channel ({ctx.channel.name}) has been nuked :boom:",
        description=f"Nuked by: {ctx.author.name}#{ctx.author.discriminator}"
    )
    embed.set_footer(text=f"{ctx.guild.name}  •  {datetime.strftime(datetime.now(), '%d.%m.%Y at %I:%M %p')}")
    await ctx.channel.delete(reason="nuke")
    channel = await ctx.channel.clone(reason="nuke")
    await channel.send(embed=embed)
    
keep_alive()
bot.run(os.environ['BOTTOKEN'])