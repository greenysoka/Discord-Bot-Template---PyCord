import discord                                          #pip install py-cord
from discord.ext import commands
from discord import Option
from discord.ext import tasks, commands
import dotenv                                           #pip install python-dotenv
dotenv.load_dotenv()
import os


intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True
intents.presences = True 


# configure your bot. You'll need it for all commands and ui components
# If you only use slash commands, you don't need a command_prefix
bot = commands.Bot(command_prefix='!bot', intents=intents)

# Send a message in your console when the bot is ready.
@bot.event
async def on_ready():
    print(f">> Started as {bot.user.name} | Ping: {bot.latency}")
    # Change the bot's status
    await bot.change_presence(activity=discord.CustomActivity("Template is online. Congrats!"), status=discord.Status.online)


# This is an example for a slash command. You have to give permission for slash commands.
@bot.slash_command(
        name="ping",
        description="Check the ping for the template bot!")
async def pingcmd(ctx):
    # Define what should happen on /ping command
    await ctx.respond(f"Bot is online! > Ping: {bot.latency}s")

# Get your TOken from the .env File and start bot. Don't change these lines
token = str(os.getenv("TOKEN"))
bot.run(token)

# TEMPLATE BY GREENY > (Discord: @greenydev)
# Contact me for questions or suggestions
# Made by me as template for my own bots