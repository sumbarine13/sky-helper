import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

# =========================
# Load token securely
# =========================
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("DISCORD_TOKEN not set")

# =========================
# Web server (keeps Render alive)
# =========================
app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

def run_web():
    app.run(host="0.0.0.0", port=8080)

Thread(target=run_web).start()

# =========================
# Discord bot setup
# =========================
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="sumbarine")
async def sumbarine(ctx):
    await ctx.send(
        "💀THE GOAT OF SERVER 💀\n"
        "😈ULTRA SIGMA OG😈\n"
        "EXCELLENT EXTREMELY HIGHLY TRUST🤑\n"
        "LIKE OG 🤑\n"
        "❤️CO OWNER ❤️\n"
        "high respect from everyone\n"
        "Sumbarine!"
    )

# =========================
# Start bot
# =========================
bot.run(TOKEN)
