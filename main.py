
import discord # type: ignore
from discord.ext import commands # type: ignore

bot = commands.Bot(command_prefix="$", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def say(ctx, *, mensaje):
    await ctx.send(f"{mensaje}")

bot.run("TU TOKEM AQUI")
