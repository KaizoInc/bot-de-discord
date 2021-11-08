import discord
from discord import message
from discord.channel import VoiceChannel
from discord.ext import commands, tasks
import datetime
from urllib import parse, request
import re

from musica import music_cog

bot = commands.Bot(command_prefix="_", description="Este es un bot de prueba", help_command=None)

bot.add_cog(music_cog(bot))

#Ping-Pong
@bot.command()
async def ping(ctx):
    await ctx.send("Ten por seguro que suspenderas y dejaras la carrera zorra puta")

@bot.command()
async def help(ctx):
    des= """
    Comandos de Botprac1

    > ping: El bot te responde pong

    > Prefix: El prefijo del bot es "_"

    Hecho con amor por Kaizo <3"""
    embed = discord.Embed(title="recuperacion FOPR",url="https://cdn.discordapp.com/avatars/809827305295314967/babea11271bbf5a89d5bf15220e7c278.webp?size=1024",description= des,timestamp=datetime.datetime.utcnow(),color=discord.Color.dark_blue())
    embed.set_footer(text="solicitado por: {}".format(ctx.author.name))
    embed.set_author(name="KaizoInc",icon_url= "https://cdn.discordapp.com/icons/902907870222364733/f7fce497ffdede6f6624fa0859a78aa7.png?size=128")

    await ctx.send(embed=embed)

# `Streaming ` status
@bot.event
async def on_ready():
    print("El Bot esta conectado")
    await bot.change_presence(activity=discord.Streaming(name="Desarrollo del Bot", url="https://www.twitch.tv/kaizo_inc"))

TOKEN_DEL_BOT = "Nzk0NjI3ODI4NTA2NTU4NDY0.X-9k1Q.fNfA8ELc0CUSqtUfTxtxTHmYePw"

bot.run(TOKEN_DEL_BOT)