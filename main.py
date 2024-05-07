import discord                                          #pip install py-cord
from discord.ext import commands
from discord import Option
from discord.ext import tasks, commands
import dotenv                                           #pip install python-dotenv
dotenv.load_dotenv()
import os


intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
intents.guilds = True
intents.members = True
intents.messages = True
intents.presences = True 



bot = commands.Bot(command_prefix='!bot', intents=intents)


@bot.event
async def on_ready():
    print(f">> Started as {bot.user.name} | Ping: {bot.latency}")
    await bot.change_presence(activity=discord.CustomActivity("Template is online. Congrats!"), status=discord.Status.online)






@bot.slash_command(
        name="ping",
        description="Check the ping for the template bot!")
async def record(ctx):
    await ctx.respond(f"Bot is online! > Ping: {bot.latency}s")
    
token = str(os.getenv("TOKEN"))
bot.run(token)

# TEMPLATE BY GREENY > (Discord: @greenydev)
# Contact me for questions or suggestions