import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("Bot token not found. Put it inside .env file.")

# Secure intents (only what we need)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Bot is ready!")

@bot.command(name="sumbarine")
async def sumbarine(ctx: commands.Context):
    message = (
        "💀THE GOAT OF SERVER 💀\n"
        "😈ULTRA SIGMA OG😈\n"
        "EXCELLENT EXTREMELY HIGHLY TRUST🤑\n"
        "LIKE OG 🤑\n"
        "❤️CO OWNER ❤️\n"
        "high respect from everyone\n"
        "Sumbarine!"
    )
    await ctx.send(message)

bot.run(TOKEN)
