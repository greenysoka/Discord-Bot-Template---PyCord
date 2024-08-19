import discord                                          #pip install py-cord
from discord.ext import commands
from discord import Option
from discord.ext import tasks, commands
import dotenv                                           #pip install python-dotenv
dotenv.load_dotenv()
import os
import yaml                                             # pip install pyyaml
from datetime import datetime
import pytz                                             #pip install pytz
import random

from commands.cogcmd import COG                         #import the cog command

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True
intents.presences = True 


# configure your bot. You'll need it for all commands and ui components
# If you only use slash commands, you don't need a command_prefix
bot = commands.Bot(command_prefix='!bot', intents=intents)

# Loop to show the time and day every hour in the console 
@tasks.loop(minutes=60)
async def logtime():
    current_time = datetime.now(pytz.timezone('Europe/Berlin'))
    formatted_time = current_time.strftime("%d.%m.%y == %H:%M:%S")
    print(f"=============== {formatted_time} ===============")



# Send a message in your console when the bot is ready.
@bot.event
async def on_ready():
    logtime.start()
    with open('config/bot.yaml', encoding='utf-8') as config_file:
        botinfo = yaml.safe_load(config_file)
        version = botinfo['version']
        ticketsystemv = botinfo['ticketsystem']
    latency_rounded = round(bot.latency, 2)
    print("")
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print("")
    print("   ______   ____  __   ____                _   _           ")
    print("  / ___\ \ / /\ \/ /  / ___|_ __ ___  __ _| |_(_)_   _____ ")
    print(" | |  _ \ V /  \  /  | |   | '__/ _ \/ _` | __| \ \ / / _ \\")
    print(" | |_| | | |   /  \  | |___| | |  __/ (_| | |_| |\ V /  __/")
    print("  \____| |_|  /_/\_\  \____|_|  \___|\__,_|\__|_| \_/ \___|")
    print("")
    print(f"❱ BOT STARTED AS:")
    print(f"『 {bot.user.name} 』")
    print("")
    print("❱ Ping:")
    print(f"『 {latency_rounded}ms 』")
    print("")
    print("❱ Bot-Version:")
    print(f"『 {version} 』")
    print("")
    print("❱ Ticketsystem:")
    print(f"『 {ticketsystemv} 』")
    print("")
    print("")
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    change_status.start()



# Auto-changing status for your bot
@tasks.loop(seconds=50) 
async def change_status():
    serverid = int(1242551094492532876) # put in correct server id!
    guild = bot.get_guild(serverid)
    member_count = guild.member_count
    latency_rounded = round(bot.latency, 2)
    with open('config/bot.yaml', encoding='utf-8') as config_file:
        botinfo = yaml.safe_load(config_file)
        version = botinfo['version']
        
    # Here you can put in your custom message that should be displayed
    status_messages = [
    "Playing with admin commands", "Made with 🤍 by @greenysoka", f"Ping: {latency_rounded}s", "eating pizza",
    f"chatting with {member_count} users", version
]
    new_status = random.choice(status_messages)
    await bot.change_presence(activity=discord.CustomActivity(new_status), status=discord.Status.Online)




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

# TEMPLATE BY GREENY > (Discord: @greenysoka)
# Contact me for questions or suggestions
# Made by me as template for my own bots