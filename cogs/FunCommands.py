import discord
from discord.ext import commands
import random
import asyncio

from config import *

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command(aliases = ["noobrate", "noob", "noobiebooby"], help = "noob rating")
    async def noobRate(self, ctx, noobiee = None):

        if not noobiee:
            author = f"<@{ctx.author.id}>"
        else:
            author = noobiee
        
        noobPercentage = random.randint(0, 100)
        if noobPercentage == 0:
            noobEmoji = "👽"
        elif noobPercentage > 0 and noobPercentage < 31:
            noobEmoji = "😳"
        elif noobPercentage > 30 and noobPercentage < 51:
            noobEmoji = "😄"
        elif noobPercentage > 50 and noobPercentage < 71:
            noobEmoji = "😊"
        elif noobPercentage > 70 and noobPercentage < 91:
            noobEmoji = "🤖"
        elif noobPercentage > 90 and noobPercentage < 101:
            noobEmoji = "🤡"
        elif noobPercentage == 100:
            noobEmoji = "💩"

        desc = f"{author} is {noobPercentage}% {noobEmoji} boob"
        
        embed = discord.Embed(title = "Noobie rating", description = desc, colour = color)

        await ctx.send(embed=embed)

    @commands.command(help = "Rolls a dice")
    async def roll(self, ctx):
        embed = discord.Embed(title = "Rolling Dice", description = "...", colour = color)
        msg = await ctx.send(embed = embed)
        embed2 = discord.Embed(title = "Rolled!", description = f"{random.randint(1, 6)}", colour = color)
        await asyncio.sleep(0.5)
        await msg.edit(embed = embed2)


def setup(bot):
    bot.add_cog(FunCommands(bot))