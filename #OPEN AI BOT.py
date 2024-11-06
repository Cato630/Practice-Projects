#OPEN AI BOT
import discord
from discord.ext import commands
import openai
import yaml


discord_bot_token: "YOUR_DISCORD_BOT_TOKEN"
openai_api_key: "YOUR_OPENAI_API_KEY"


import discord
from discord.ext import commands
import openai
import yaml

# Load configuration
with open("config.yaml", "r") as file:
    config_data = yaml.safe_load(file)

# Set OpenAI API key
openai.api_key = config_data.get("openai_api_key")
bot_token = config_data.get("discord_bot_token")

# Create bot instance
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online.")

@bot.command(name="ask")
async def ask(ctx, *, question: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150
    )
    await ctx.send(response.choices[0].text.strip())

bot.run(bot_token)
python bot.py