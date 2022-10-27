import discord
from discord.ext import commands
from config import *

class SimpleInteractions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command(help = "says hi back")
    async def hi(self, ctx):
        embed = discord.Embed(title = f"Hey", description = f"{ctx.author.mention} how you doin'?😏", color = color)
        embed.set_thumbnail(url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(SimpleInteractions(bot))