import discord
from discord.ext import commands
from config import *

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command(help = "test")
    async def test(self, ctx):
        embed = discord.Embed(title = f"test", description = f"test", color = color)
        embed.set_thumbnail(url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(TestCog(bot))