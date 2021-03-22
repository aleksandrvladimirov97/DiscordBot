import discord
from discord.ext import commands
from config import settings
from config import key
import json
import requests
from aio_yandex_translate.translator import Translator

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    a = ctx.message.content
    b = ctx.guild
    await ctx.send(f'{author.mention}!')
    print(a)
    print(b)

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def t(ctx, i, arg):
    trans = Translator(key)
    author = ctx.message.author
    text = await trans.translate(arg, to_language=i)
    await ctx.send(f'{author.mention} сказал - '  + text)

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена
