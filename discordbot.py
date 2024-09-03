import discord 
from discord.ext import commands
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="@",intents=intents)
@bot.event
async def on_ready():
    print("El bot se ha iniciado")
@bot.command()
async def reciclar(ctx):
    respuesta = """
    🌍 ¡Hola! Aquí te explico cómo reciclar correctamente:
    - ♻️ **Plástico**: botellas, tapas, envoltorios (limpios y secos).
    - 🗞️ **Papel y Cartón**: revistas, cajas, cuadernos (sin restos de comida).
    - 🍎 **Orgánicos**: cáscaras de frutas, restos de comida (usa compostaje).
    - 🚮 **No reciclables**: toallas higiénicas, pañales, chicles.
    
    ¡Reciclar es fácil y ayuda al planeta! 🌱
    """
    await ctx.send(respuesta)

@bot.command()
async def consejos_reciclaje(ctx):
    consejos = """
    💡 **Consejos para Mejorar tu Reciclaje:**
    - **Limpia los Recipientes**: Asegúrate de que los envases estén limpios antes de reciclarlos.
    - **Clasifica Correctamente**: Separa los materiales reciclables (plástico, papel, vidrio, metal) en contenedores distintos.
    - **Reduce y Reutiliza**: Antes de reciclar, piensa si puedes reducir o reutilizar el material.

    
    ¡Ayuda al planeta =) 
    """
    await ctx.send(consejos)    

bot.run() 
