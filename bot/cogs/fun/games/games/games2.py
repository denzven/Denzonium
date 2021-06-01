import discord
from discord.ext import commands
from bot.cogs.fun.games.games import connect_four, tictactoe3, hangman, twenty_48, aki, ChessGame,typeracer
from typing import Union

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Play some amazing games"
    
    @commands.command(aliases=['tc'])
    @commands.guild_only()
    async def tictactoe3(self, ctx, member: discord.Member, usage='<other player.mention>'):
        '''Play Amazing Tictactoe Game'''
        if member == ctx.author or member.bot:
            await ctx.send('*You cannot play this game yourself or with a bot*')
            return
        await ctx.send('*Positions are marked with 1,2,3.. just like 3x3 cube*')
        await ctx.send(f'{ctx.author.mention} you are taking *cross*')
        await ctx.send(f'{member.mention} you are taking *circle*')
        game = tictactoe3.Tictactoe(
            cross  = ctx.author,   
            circle = member,
        )
        await game.start(ctx, remove_reaction_after=True)
    
    @commands.command(aliases=['connect_four','c4','cf'], usage='<other player.mention>')
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
            red  = ctx.author,   
            blue = member,
        )
        await game.start(ctx, remove_reaction_after=True)

    @commands.command(aliases=['hg'])
    async def hangman(self, ctx):
        
        await ctx.send('**Here is the link to know about** *Hangman*:')
        await ctx.send('<https://en.wikipedia.org/wiki/Hangman_(game)#Example_game>')
        
        await ctx.send('__After execution__ of **hangman** command *reply* to the embed *to guess the word/movie.*')
        game = hangman.Hangman()
        await game.start(ctx)

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
            await a.edit(content=4-i)
            time.sleep(1)
        await a.delete()
        game = aki.Akinator()
        await game.start(ctx)
    
    @commands.command(aliases=['20482','t48'])
    async def twenty_48(self, ctx):
        '''Play 20487 Game'''
        await ctx.send('**Here is the link to know about** *2048*:')
        await ctx.send('<https://en.wikipedia.org/wiki/2048_(video_game)#Gameplay>')
        game = twenty_48.Twenty48()
        game.update_emojis(
    #a dictionary with number as a key and display value as value
    #ex: {"2": "<:two:123238299123342>"...}
    {
        "0":"⬛",
        "2":"<:two:844095350250799124>",
        "4":"<:four:844095371394547763>",
        "8":"<:eight:844095400561606676>",
        "16":"<:sixteen:844095172023418890>",
        "32":"<:thirty_two:844095226121682984>",
        "64":"<:sixty_four:844095267204628520>",
        "128":"128",
        "256":"256",
        "512":"512",
        "1024":"1024",
    }
)
        await game.start(ctx, remove_reaction_after = True, delete_button = True)


    @commands.command(usage='<other player.mention>')
    @commands.guild_only()
    async def chess(self, ctx, member: discord.Member):
        #Play Chess with your partner
        if member == ctx.author or member.bot:
            await ctx.send('*You cannot play this game yourself or with a bot*')
            return
        await ctx.send('**Here is the rules of the** *Chess*:')
        await ctx.send('<https://en.wikipedia.org/wiki/Rules_of_chess#Gameplay>')
        await ctx.send('use uci moves (example: e2e4),valid moves get a ✅ and are deleted after 10s')
        await ctx.send(f'{ctx.author.mention} you are taking the *White Pieces*')
        await ctx.send(f'{member.mention} you are taking the *Black Pieces*')
        await ctx.send('**the ChessBoard take a while to load and render.**')
        game = ChessGame.Chess(
            white=ctx.author,
            black=member
        )
        #await game.start(ctx)
        #async def start(self, ctx: commands.Context, *, timeout: int = None, color: Union[int, discord.Color] = 0x2F3136, add_reaction_after_move: bool = False, **kwargs):
        await game.start(ctx)

    @commands.command(aliases=['typrace'])
    async def typeracer(self, ctx):
        '''Play typereacer Game'''        
        game = typeracer.TypeRacer()
        await game.start(
            ctx, 
            embed_color=0x2F3136,                     #embed color
            path_to_text_font='Arial.ttf', #or use arial.ttf if you dont have one
            timeout=100, 
            mode="sentence"
        )

def setup(bot):
    bot.add_cog(Games(bot))
