import discord
from discord.ext import commands
import asyncio

import chess
from typing import Union


class Chess:

    def __init__(self, *, white: discord.Member, black: discord.Member):
        self._base = "http://www.fen-to-image.com/image/128/single/coords/"
        self.white = white
        self.black = black
        self.turn = self.white
        self.winner = None
        self.board = chess.Board()
        self.message = None

    async def BuildEmbed(self) -> discord.Embed:
        color = "white" if self.turn == self.white else "black"
        embed = discord.Embed()
        embed.title = "Chess Game"
        embed.description = f"**Turn:** `{self.turn.name}`\n**Color:** `{color}`\n**Check:** `{self.board.is_check()}`"
        embed.set_image(url=f"{self._base}{self.board.board_fen()}")
        return embed

    async def PlaceMove(self, uci: str) -> chess.Board:
        self.board.push_uci(uci)
        self.turn = self.white if self.turn == self.black else self.black
        return self.board

    async def end(self):
        return

    async def fetch_results(self):
        results = self.board.result()
        embed = discord.Embed()
        embed.title = "Chess Game"

        if self.board.is_checkmate():
            embed.description = f"Game over\nCheckmate | Score: `{results}`"
        elif self.board.is_stalemate():
            embed.description = f"Game over\nStalemate | Score: `{results}`"
        elif self.board.is_insufficient_material():
            embed.description = f"Game over\nInsufficient material left to continue the game | Score: `{results}`"
        elif self.board.is_seventyfive_moves():
            embed.description = f"Game over\n75-moves rule | Score: `{results}`"
        elif self.board.is_fivefold_repetition():
            embed.description = f"Game over\nFive-fold repitition. | Score: `{results}`"
        else:
            embed.description = f"Game over\nVariant end condition. | Score: `{results}`"

        embed.set_image(url=f"{self._base}{self.board.board_fen()}")
        return embed

    async def start(self, ctx: commands.Context, *, timeout: int = None, color: Union[int, discord.Color] = 0x2F3136,
                    add_reaction_after_move: bool = True, **kwargs):

        embed = await self.BuildEmbed()
        self.message = await ctx.send(embed=embed, content=f"{self.turn.mention}", **kwargs)

        while True:

            def check(m):
                try:
                    if self.board.parse_uci(m.content.lower()):
                        return m.author == self.turn and m.channel == ctx.channel
                    else:
                        print("else trigger" + m.content.lower())
                        return False
                except ValueError:
                    print("valueerror" + m.content.lower())
                    if m.content.lower is "end":
                        print("this chess game is ended")
                    return False

            try:
                message = await ctx.bot.wait_for("message", timeout=timeout, check=check)
                print(message)
                print(message.content)
            except asyncio.TimeoutError:
                return

            await self.PlaceMove(message.content.lower())
            embed = await self.BuildEmbed()

            if add_reaction_after_move:
                await message.add_reaction("✅")

            if self.board.is_game_over():
                break

            if message.content.lower() is "end":
                await ctx.reply("this chess game is ended")
                break
            await self.message.edit(embed=embed, content=f"{self.turn.mention}")
            await asyncio.sleep(10)
            await message.delete()

        embed = await self.fetch_results()
        await self.message.edit(embed=embed)
        return await ctx.send("~ Game Over ~")
