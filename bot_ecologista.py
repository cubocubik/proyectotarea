import discord # type: ignore
from discord.ext import commands # type: ignore

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "!", intents=intents)

degradacion_materiales = {
    "papel": "📄 El papel tarda entre 2 y 5 meses en degradarse.",
    "plastico": "🧴 El plástico puede tardar hasta 1000 años.",
    "vidrio": "🍾 El vidrio puede tardar más de 4000 años.",
    "aluminio": "🥫 El aluminio tarda unos 200 años.",
    "carton": "📦 El cartón tarda unos 2 meses.",
    "banana": "🍌 Una cáscara de banana tarda unos 2 semanas.",
    "chicle": "🍬 El chicle puede tardar 5 años.",
    "botella": "🥤 Una botella plástica puede tardar hasta 450 años.",
    "tela": "👕 Una camiseta de algodón tarda 1 año.",
    "lata": "🥫 Una lata de refresco tarda 200 años."
}

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def degradacion(ctx, *, material: str):
    material = material.lower()
    respuesta = degradacion_materiales.get(material, "❓ Lo siento, no tengo información sobre ese material. Puedes intentar con: papel, plastico, vidrio, banana, etc.")
    await ctx.send(respuesta)

bot.run("TU_TOKEM_AQUI")
