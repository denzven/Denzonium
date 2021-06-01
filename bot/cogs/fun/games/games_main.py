import discord
import random
import asyncio
from discord.ext import commands
from bot.cogs.fun.games.games import tictactoe, wumpus, minesweeper, twenty, connect_four, tictactoe3, hangman, twenty_48, aki, \
    ChessGame, typeracer


class games(commands.Cog,
            description="test descrption",
            name="Discord Games"
            ):
    def __init__(self, bot):
        self.bot = bot

    ################################################################
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(
        name="2048",
        help="play 2048 in a codebloack form! might not be suitable for mobiles",
        brief="2048 game in discord!",
        usage="+2048",
        aliases=["two zero four eight"]
    )
    async def twenty(self, ctx):
        await twenty.play(ctx, self.bot)

    ################################################################

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(
        name="minesweeper",
        help="play minesweeper using spoilers",
        brief="minesweeper game in discord!",
        usage="+minesweeper",
        aliases=["ms"]
    )
    async def minesweeper(self, ctx, columns=None, rows=None, bombs=None):
        await minesweeper.play(ctx, columns, rows, bombs)

    ################################################################

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(
        name="wumpus",
        help="play the wumpus game",
        brief="play the wumpus hunting game",
        usage="+wumpus",
        aliases=["wumpusgame"]
    )
    async def _wumpus(self, ctx):
        await wumpus.play(self.bot, ctx)

    ################################################################

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(
        name="random_number",
        help="random number generator",
        brief="get a random number",
        usage="+randomnumber",
        aliases=["randint", "randomnum"]
    )
    async def randomnumber(self, ctx, num1: int, num2: int):
        embed = discord.Embed(title="Random Number Generator", description=(random.randint(num1 + 1, num2 - 1)))
        await ctx.send(embed=embed)

    ################################################################

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Roll a dice!")
    async def dice(self, ctx):
        embed = discord.Embed(
            title="Rolling Dice...",
        )
        msg = await ctx.message.reply(embed=embed)

        embed = discord.Embed(
            title="Dice!",
            description=f"You rolled a **{random.randint(1, 6)}**"
        )
        await msg.edit(embed=embed)

    ################################################################

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(
        name="8ball",
        help="ask the mystic 8ball and it will answer",
        brief="ask the mystic 8ball and it will answer",
        usage="+8ball",
        aliases=["8b"]
    )
    async def _8ball(self, ctx, *, question):

        responses = ['Yes.',
                     'No.', 'Probably. ', 'Maybe.',
                     'IDK bro ', 'Seems like it.',
                     'Nahh.', 'Oh hell yeah.',
                     'Yes Definitely.', 'I Think not',
                     'lol no bro', 'Concentrate and ask again',
                     'Ask a better question lol', 'Umm Yes', 'Umm No',
                     'Yes lmao', 'No, but imagine if it was yes lol',
                     'Yes, but imagine if it was no lol', 'hmm, good question',
                     'Yes, obviously', 'Definitely not']

        embed = discord.Embed(title=f"**:man_detective:  Prediction**", color=0x696969)
        embed.add_field(name=f"Question Asked:", value=f"{question}", inline=False)
        embed.add_field(name=f"Predicted Answer:", value=f"{random.choice(responses)}", inline=False)
        await ctx.send(embed=embed)

    ################################################################

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(
        name="flip",
        help="flip a coin",
        brief="flip a coin",
        usage="+flip",
        aliases=["coinflip"]
    )
    async def coinflip(self, ctx):
        outcomes = ['Heads', 'Tails']

        embed = discord.Embed(
            title="Flipping the Coin...",
            # color = MAIN_COLOR
        )
        msg = await ctx.message.reply(embed=embed)

        embed = discord.Embed(
            title=f"Coin!",
            description=f"Result: **{random.choice(outcomes)}**",
            # color=MAIN_COLOR
        )
        await msg.edit(embed=embed)

    ################################################################

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(
        name="rockpaperscissors",
        help="play rock paper scissors with the bot!",
        brief="play rock paper scissors with the bot! using reactions",
        usage="+rps",
        aliases=["rps", "rockpaper"]
    )
    async def rps(self, ctx):
        def check_win(p, b):
            if p == '🌑':
                return False if b == '📄' else True
            if p == '📄':
                return False if b == '✂' else True
            # p=='✂'
            return False if b == '🌑' else True

        async with ctx.typing():
            reactions = ['🌑', '📄', '✂']
            game_message = await ctx.send("**Rock Paper Scissors**\nChoose your shape:", delete_after=15.0)
            for reaction in reactions:
                await game_message.add_reaction(reaction)
            bot_emoji = random.choice(reactions)

        def check(reaction, user):
            return user != self.bot.user and user == ctx.author and (str(reaction.emoji) == '🌑' or '📄' or '✂')

        try:
            reaction, _ = await self.bot.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Time's Up! :stopwatch:")
        else:
            await ctx.send(f"**Your Choice:\t{reaction.emoji}\nMy Choice:\t{bot_emoji}**")
            # if conds
            if str(reaction.emoji) == bot_emoji:
                await ctx.send("**It's a Tie :ribbon:**")
            elif check_win(str(reaction.emoji), bot_emoji):
                await ctx.send("**You win :sparkles:**")
            else:
                await ctx.send("**I win :robot:**")

    ################################################################

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(aliases=['ttt', 'tic-tac-toe'])
    async def tictactoe(self, ctx):
        await tictactoe.play_game(self.bot, ctx, chance_for_error=0.2)  # Win Plausible

    @commands.command(
        name="tictactoe2",
        help="play tictactae with a user!",
        brief="mention a person to play tictactoe with them using reactions",
        usage="+tictactoe2",
        aliases=["ttt2"]
    )
    @commands.guild_only()
    async def tictactoe2(self, ctx, member: discord.Member, usage='<other player.mention>'):
        '''Play Amazing Tictactoe Game'''
        if member == ctx.author or member.bot:
            await ctx.send('*You cannot play this game yourself or with a bot*')
            return
        await ctx.send('*Positions are marked with 1,2,3.. just like 3x3 cube*')
        await ctx.send(f'{ctx.author.mention} you are taking *cross*')
        await ctx.send(f'{member.mention} you are taking *circle*')
        game = tictactoe3.Tictactoe(
            cross=ctx.author,
            circle=member,
        )
        await game.start(ctx, remove_reaction_after=True)

    ################################################################

    @commands.command(aliases=['connect_four', 'c4', 'cf'], usage='<other player.mention>')
    @commands.guild_only()
    async def connectfour(self, ctx, member: discord.Member):
        '''Play Amazing Connect Four Game'''
        if member == ctx.author or member.bot:
            await ctx.send('*You cannot play this game yourself or with a bot*')
            return
        await ctx.send('**Here is the link to know about** *Connect Four*:')
        await ctx.send('<https://en.wikipedia.org/wiki/Connect_Four#firstHeading>')
        await ctx.send(f'{ctx.author.mention} you are taking *red*')
        await ctx.send(f'{member.mention} you are taking *blue*')
        game = connect_four.ConnectFour(
            red=ctx.author,
            blue=member,
        )
        await game.start(ctx, remove_reaction_after=True)

    ################################################################

    @commands.command(aliases=['hg'])
    async def hangman(self, ctx):

        await ctx.send('**Here is the link to know about** *Hangman*:')
        await ctx.send('<https://en.wikipedia.org/wiki/Hangman_(game)#Example_game>')

        await ctx.send('__After execution__ of **hangman** command *reply* to the embed *to guess the word/movie.*')
        game = hangman.Hangman()
        await game.start(ctx)

    ################################################################

    @commands.command(aliases=['aki'])
    async def akinator(self, ctx):
        '''Play Akinator'''
        import time
        await ctx.send('**Here is the link to know about** *Akinator*:')
        await ctx.send('<https://en.wikipedia.org/wiki/Akinator#Gameplay>')
        a = await ctx.send('**Now get ready for the game**')
        time.sleep(1)
        await a.edit(content='Starting in 5 seconds')
        for i in range(4):
            await a.edit(content=4 - i)
            time.sleep(1)
        await a.delete()
        game = aki.Akinator()
        await game.start(ctx)

    ################################################################

    @commands.command(aliases=['20482', 't48'])
    async def twenty_48(self, ctx):
        '''Play 20487 Game'''
        await ctx.send('**Here is the link to know about** *2048*:')
        await ctx.send('<https://en.wikipedia.org/wiki/2048_(video_game)#Gameplay>')
        game = twenty_48.Twenty48()
        game.update_emojis(
            # a dictionary with number as a key and display value as value
            # ex: {"2": "<:two:123238299123342>"...}
            {
                "0": "⬛",
                "2": "<:two:844095350250799124>",
                "4": "<:four:844095371394547763>",
                "8": "<:eight:844095400561606676>",
                "16": "<:sixteen:844095172023418890>",
                "32": "<:thirty_two:844095226121682984>",
                "64": "<:sixty_four:844095267204628520>",
                "128": "128",
                "256": "256",
                "512": "512",
                "1024": "1024",
            }
        )
        await game.start(ctx, remove_reaction_after=True, delete_button=True)

    ################################################################

    @commands.command(usage='<other player.mention>')
    @commands.guild_only()
    async def chess(self, ctx, member: discord.Member):
        # Play Chess with your partner
        if member == ctx.author or member.bot:
            await ctx.send('*You cannot play this game yourself or with a bot*')
            return
        await ctx.send('**Here is the rules of the** *Chess*:')
        await ctx.send('<https://en.wikipedia.org/wiki/Rules_of_chess#Gameplay>')
        await ctx.send('use uci moves (example: e2e4),valid moves get a ✅ and are deleted after 10s')
        await ctx.send('**the ChessBoard take a while to load and render.**')
        await ctx.send(f'{ctx.author.mention} you are taking the *White Pieces*')
        await ctx.send(f'{member.mention} you are taking the *Black Pieces*')
        game = ChessGame.Chess(
            white=ctx.author,
            black=member
        )
        # await game.start(ctx)
        # async def start(self, ctx: commands.Context, *, timeout: int = None, color: Union[int, discord.Color] = 0x2F3136, add_reaction_after_move: bool = False, **kwargs):
        await game.start(ctx)

    ################################################################

    @commands.command(aliases=['typerace'])
    async def typeracer(self, ctx):
        '''Play typereacer Game'''
        game = typeracer.TypeRacer()
        await game.start(
            ctx,
            embed_color=0x2F3136,  # embed color
            path_to_text_font='bot/games/games/Arial.ttf',  # or use arial.ttf if you dont have one
            timeout=100,
            mode="sentence"
        )


################################################################

def setup(bot):
    bot.add_cog(games(bot))
