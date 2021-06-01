import discord, asyncio, os, platform, sys, random
from discord.ext.commands import Bot
from discord.ext import commands
import json
from keep_alive import run
from flask import Flask
from flask import render_template
from datetime import time
import time
import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord import User, errors


class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setprofile(self, ctx):
        embed = discord.Embed(title="Profil", description="Czas ustawić twój profil! Odpowiedz na poniższe pytania w ciągu 30 sekund!", color=discord.Color.green())
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

        questions = ["What is your Name?",
                    "How old are you?",
                    "W jakim województwie mieszkasz?",
					"Co lubisz robić?",
					"Czego nie lubisz robić",
					"Podaj link do zdjęcia profilowego jakie chcesz mieć"]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
		
        def profile_data(users, user):
            if not str(user.id) in users:
                users[str(user.id)] = {}
                users[str(user.id)]['Name'] = answers[0]
                users[str(user.id)]['Age'] = answers[1]
                users[str(user.id)]['Województwo'] = answers[2]
                users[str(user.id)]['Lubie'] = answers[3]
                users[str(user.id)]['Nie_lubie'] = answers[4]
                users[str(user.id)]['Profilowe'] = answers[5]

        for i in questions:
            embed = discord.Embed(title="Profil", description=i, color=discord.Color.green())
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)          
            await ctx.send(embed=embed)

            try:
                msg = await self.bot.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                embed = discord.Embed(title="Profil", description="Nie odpowiedziałeś na czas, proszę bądź szybszy następnym razem!!", color=discord.Color.red())
                embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                return
            else:
                answers.append(msg.content)
                with open('bot/json/warn.json', 'r') as f:
                   users = json.load(f)
                   user = ctx.author.id
                await profile_data(users, user)
                embed = discord.Embed(title=f"Profil", color=discord.Color.purple(), description="Udało ci się ustawić wszystkie informacje wpisz komende `profil` aby sprawdzić swój lub kogoś profil")
                embed.set_footer(text=f"{ctx.author}")
                embed.set_author(name="PrzegrywBOT", icon_url=f"{ctx.author.avatar_url}")
                await ctx.send(embed=embed)
                with open('bot/json/warn.json', 'w') as f:
                    json.dump(users, f, sort_keys=True, ensure_ascii=False, indent=4, default=str)

def setup(bot):
    bot.add_cog(profile(bot))