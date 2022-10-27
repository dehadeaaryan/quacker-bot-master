"""
VARIABLES
"""
import discord
import os

prefix = ("quack ", "Quack ")

botName = "quacker"

color = discord.Color.dark_orange()

devServerLink = "https://discord.gg/E5wXQGjxsd"
botInviteLink = "https://discord.com/api/oauth2/authorize?client_id=843026451531956225&permissions=8&scope=bot"
botSiteLink = "https://gfrkad21.github.io/quacker-bot/index.html"
botSiteHelpLink = "https://gfrkad21.github.io/quacker-bot/help.html"

extensions = ["Help", 
"SimpleInteractions", 
"FunCommands", 
# "ImageCommands", 
"YoutubeCommands", 
"ServerCommands", 
"DevServerCommands", 
"TestCog", 
]

global recentMsg
recentMsg = {}


TOKEN = os.environ['TOKEN']