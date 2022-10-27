import discord
from discord.ext import commands
from config import *

class ServerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command(help = "Sends the link for your server")
    async def serverLink(self, ctx):
        embed = discord.Embed(title = f"Invite link for {ctx.message.guild.name}", description = f"[here]()", color = color)
        embed.set_thumbnail(url = ctx.author.avatar_url)
        link = await ctx.channel.create_invite()
        embed.add_field(name = f"Copy link [here]({link})", value = f"{link}")

        await ctx.send(embed = embed)
    
    @commands.command(help = "Shows server info")
    async def serverInfo(self, ctx):
        embed = discord.Embed(title = f"{ctx.guild.name}", description = f"", color = color)
        embed.set_thumbnail(url = ctx.guild.icon_url)
        embed.add_field(name = f"Owner", value = f"{ctx.guild.owner}", inline = False)
        embed.add_field(name = f"Region", value = f"{ctx.guild.region}", inline = False)
        embed.add_field(name = f"Member Count", value = f"{ctx.guild.member_count}", inline = False)

        await ctx.send(embed = embed)
    
    @commands.command(help = "Shows recently deleted or edited message")
    async def recentMessage(self, ctx):
        gName = ctx.guild.name
        if not recentMsg[gName]:
            embed = discord.Embed(title = f"No recent message in {gName}", description = f"", color = color)
        else:
            embed = discord.Embed(title = f"Recent message in {gName}:", description = f"{recentMsg[gName]}", color = color)

        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(ServerCommands(bot))