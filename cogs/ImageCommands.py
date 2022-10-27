import discord
from discord.ext import commands
from config import *

from io import BytesIO
import os
from PIL import Image, ImageEnhance

cwd = f"{os.getcwd()}\\"
name = f"{cwd}output.png"

class ImageCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command(help = "You, but wide")
    async def wide(self, ctx, user: discord.Member = None):
        if not user:
            av = ctx.author.avatar_url_as(format = "png")
        else:
            av = user.avatar_url_as(format = "png")
        ab = await av.read()

        img = Image.open(BytesIO(ab))
        imgn = img.resize((img.size[0] * 2, img.size[1]))
        imgn.save(name)

        file = discord.File(name)
        await ctx.send(file = file)
        os.remove(name)

def setup(bot):
    bot.add_cog(ImageCommands(bot))