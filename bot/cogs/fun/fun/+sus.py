import discord
from discord.ext import commands
import random
from discord.ext.commands import cooldown

def get_embed(_title, _description, _color):
    return discord.Embed(title=_title, description=_description, color=_color)

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ["sus"])
    @cooldown(1,10,commands.BucketType.user) 
    async def findimposter(self, ctx):
        """Impostors can sabotage the reactor, 
        which gives Crewmates 30–45 seconds to resolve the sabotage. 
        If it is not resolved in the allotted time, The Impostor(s) will win."""


        # determining
        embed1 = discord.Embed(title = "Who's the imposter?" , description = "Find out who the imposter is, before the reactor breaks down!" , color=0xff0000)
        
        # fields
        embed1.add_field(name = 'Red'   , value= '🟥' , inline= True)
        embed1.add_field(name = 'Blue'  , value= '🟦' , inline= True)
        embed1.add_field(name = 'Lime'  , value= '🟩' , inline= True)
        embed1.add_field(name = 'White' , value= '⬜' , inline= True)
        embed1.add_field(name = 'Yellow' , value= '🟨' , inline= True)
        embed1.add_field(name = 'Orange' , value= '🟧' , inline= True)
        
        # sending the message
        msg = await ctx.send(embed=embed1)
        
        # emojis
        emojis = {
            'red':   '🟥',
            'blue':  '🟦',
            'lime':  '🟩',
            'white': '⬜',
            'yellow': '🟨',
            'orange':   '🟧'
        }
        
        # who is the imposter?
        imposter = random.choice(list(emojis.items()))
        imposter = imposter[0]
        counter = 1

        while True:
            # for testing...
            print(emojis[imposter])

            # adding choices
            for emoji in emojis.values():
                await msg.add_reaction(emoji)

            # a simple check, whether reacted emoji is in given choises.
            def check(reaction, user):
                self.reacted = reaction.emoji
                return user == ctx.author and str(reaction.emoji) in emojis.values()

            # waiting for the reaction to proceed
            try: 
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)

            except TimeoutError:
                # reactor meltdown - defeat
                description = "Reactor Meltdown.{0} was the imposter...".format(imposter)
                embed = get_embed("Defeat", description, discord.Color.red())
                await ctx.send(embed=embed)

            else:
                # victory
                if str(self.reacted) == emojis[imposter]:
                    description = "**{0}** was the imposter...".format(imposter)
                    embed = get_embed("Victory", description, discord.Color.blue())
                    await ctx.send(embed=embed)
                    return

                # defeat
                else:
                    for key, value in emojis.items(): 
                        if value == str(self.reacted):
                            
                            if counter == 3:
                                description = "**{0}** was not the imposter...".format(key)
                                embed = get_embed("Defeat", description, discord.Color.red())
                                await ctx.send(embed=embed)
                                return
                            if counter <= 3:
                                counter += 1
                                description = "**{0}** was not the imposter...".format(key)
                                embed = get_embed("", description, discord.Color.red())
                                await ctx.send(embed=embed)
                                continue
                            




def setup(bot):
    bot.add_cog(games(bot))