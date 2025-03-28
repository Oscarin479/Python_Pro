from bot_logic import gen_pass
import discord
from discord.ext import commands
#esto le da permisos al bot
print(gen_pass(10))
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def activo():
    print(f'Hemos iniciado sesion con el {bot.user}')
    
@bot.command
async def repetir(ctx, *, message:str):
    
    await ctx.send(message)
    
@bot.command()
async def saludo(ctx, *, mensaje: str):
    mensaje = mensaje.lower().strip()  # Convierte el mensaje a minúsculas y elimina espacios extra
    # Comprobamos si el mensaje contiene ciertas palabras clave
    if "hola" in mensaje:
        await ctx.send("¡Hola! ¿Cómo estás? 😊")
    elif "adiós" in mensaje:
        await ctx.send("¡Hasta luego! 👋")
    elif "gracias" in mensaje:
        await ctx.send("¡De nada! 😃")
    else:
        await ctx.send("No entendí tu saludo. 😕")  # Si no reconoce la palabra, responde con un mensaje neutral
    
token = 'MTM1Mjc1ODMzNDM4MTQ5NDM3Nw.GsqtPN.ZDAGP6EodMw_YTqJwP4byklm-wOdvDy73Kf9uY'
bot.run(token)