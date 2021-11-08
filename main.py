import discord
from discord import message
from discord.ext import commands, tasks
import datetime
from urllib import parse, request
import re

bot = commands.Bot(command_prefix="_", description="Este es un bot de prueba", help_command=None)

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
    embed.set_author(name="KaizoInc",icon_url="https://www.google.com/url?sa=i&url=https%3A%2F%2Ftenor.com%2Fes%2Fver%2F%25EC%25B5%259C%25EC%2598%2588%25EB%2582%2598-choi-yena-%25ED%2594%2584%25EB%25A1%259C%25EB%2593%2580%25EC%258A%25A448-produce48-%25EC%259C%2584%25EC%2597%2590%25ED%2599%2594-gif-11178998263481883010&psig=AOvVaw0D2gUJ4JzKKMRe364CHxH7&ust=1636408484845000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCMiIieaeh_QCFQAAAAAdAAAAABAJ")

    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=()', html_content.read().decode())
    print(search_results)

# `Streaming ` status
@bot.event
async def on_ready():
    print("El Bot esta conectado")
    await bot.change_presence(activity=discord.Streaming(name="Desarrollo del Bot", url="https://www.twitch.tv/kaizo_inc"))

TOKEN_DEL_BOT = "Nzk0NjI3ODI4NTA2NTU4NDY0.X-9k1Q.3x6fkUN4CETI8hcrebH8BPGPDPw"

bot.run(TOKEN_DEL_BOT)