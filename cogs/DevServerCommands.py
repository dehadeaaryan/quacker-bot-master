import discord
from discord.ext import commands
from config import *

class DevServerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command(help = "sends the Developer's server link")
    async def devServerLink(self, ctx):
        embed = discord.Embed(title = f"Dev Server link", description = f"[here]({devServerLink})", color = color)
        embed.set_thumbnail(url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
    
    @commands.command(help = "Sends this bot's invite link")
    async def botInviteLink(self, ctx):
        embed = discord.Embed(title = f"Bot Invite link", description = f"[here]({botInviteLink})", color = color)
        embed.set_thumbnail(url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
    
    @commands.command(help = f"Sends the link to the official site for {botName}")
    async def botSiteLink(self, ctx):
        embed = discord.Embed(title = f"Bot Site link", description = f"[here]({botSiteLink})", color = color)
        embed.set_thumbnail(url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(DevServerCommands(bot))