import discord
from discord.ext import commands

from config import *

bot = commands.Bot(command_prefix = prefix, help_command = None)

global recentMsg

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="quack help"))
    print(f'{bot.user.name} has connected to Discord!')
    print("Discord.py API version:", discord.__version__)
    print(f"Name : {bot.user.name}")
    print(f"Client ID : {bot.user.id}")
    print("Currently active on " + str(len(bot.guilds)) + " server(s).\n")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error

@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
        return
    recentMsg[before.guild.name] = f"{before.content} \n-> \n{after.content}"

for extension in extensions:
    bot.load_extension(f"cogs.{extension}")

bot.run(TOKEN)