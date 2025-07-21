import discord # type: ignore
from discord.ext import commands # type: ignore
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix ="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def meme(ctx):
    imagenes = os.listdir("images")
    imagen_aleatoria = random.choice(imagenes)    
    with open(f"images/{imagen_aleatoria}", "rb") as f:
        imagen = discord.File(f)
    await ctx.send(file = imagen)

def obtener_perro():
    url = "https://dog.ceo/api/breeds/image/random"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos["message"]

@bot.command()
async def perro(ctx):
    url_image = obtener_perro()
    await ctx.send(url_image)

bot.run("TU_TOKEN_AQUI")

