import discord  # type: ignore
from discord.ext import commands # type: ignore
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Necesario para detectar nuevos miembros

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

# 1. Responder a saludos
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() in ["hola", "holi", "buenas"]:
        await message.channel.send(f"¡Hola {message.author.name}! 👋")
    
    await bot.process_commands(message)  # Importante para que los comandos sigan funcionando

# 2. Comando ping
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Latencia en ms
    await ctx.send(f"Pong! 🏓 {latency}ms")

# 3. Comando dado
@bot.command()
async def dado(ctx):
    resultado = random.randint(1, 6)
    await ctx.send(f"🎲 Has sacado un **{resultado}**")

# 4. Mensaje de bienvenida
@bot.event
async def on_member_join(member):
    canal = discord.utils.get(member.guild.text_channels, name="general")  # Cambia si el canal tiene otro nombre
    if canal:
        await canal.send(f"👋 ¡Bienvenido/a {member.mention} al servidor!")

bot.run("MTM4OTc2OTgzMTQ0MzU5OTQ5MQ.GkNe7A.E828FLc8U64UTdFeOitw3qtpo9b3Jb6hDbs6H0")

