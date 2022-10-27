import discord
from discord.ext import commands
from config import *

class YoutubeCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command(help = "Not ready yet...")
    async def channelInfo(self, ctx, channelLink):
        embed = discord.Embed(title = f"Youtube channel", description = f"[{channelLink}]", color = color)
        embed.set_thumbnail(url = ctx.author.avatar_url)


        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(YoutubeCommands(bot))