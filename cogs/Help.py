import discord
from discord.ext import commands
from config import *

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command(help = "Shows This message")
    async def help(self, ctx):
        embed = discord.Embed(title = f"HELP", description = f"Hey {ctx.author.mention}, here are my commands\nYou can also find them [here]({botSiteHelpLink})", color = color)
        embed.set_thumbnail(url = ctx.author.avatar_url)

        embed.add_field(name = f"**Prefix**", value = prefix, inline = False)

        for cog in self.bot.cogs:
            commands = self.bot.get_cog(cog).get_commands()
            desc = ""
            for command in commands:
                desc += f"`{command.name}` -- {command.help}\n"
            embed.add_field(name = f"⚙️**{cog}**", value = desc + "\n", inline = False)

        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Help(bot))