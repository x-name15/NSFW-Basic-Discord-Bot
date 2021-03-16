import os
import requests
import random
import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import Game

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
Game = [
    "Status1",
    "Status2",
    "Status3",
    "Status4"
]
gamePlaying = random.choice(Game)

@bot.event
async def on_ready():
    print("Im ready!")
    print("----------")
    print('Logued in:')
    print(bot.user.name)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(gamePlaying))

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='All Commands', description=None)
    embed.set_thumbnail(url="https://i.imgur.com/pEePm5E.gif")
    embed.add_field(name="!help", value="Displays all available commands", inline=False)
    embed.add_field(name="!anal", value="Gets a anal GIF or Image", inline=False)
    embed.add_field(name="!erofeet", value="Gets a erofeet GIF or Image",inline=False)
    embed.add_field(name="!femdom", value="This shit is really good", inline=False)
    embed.add_field(name="!pussy", value="Gets a PUSSY GIF or Image",inline=False)
    embed.add_field(name="!feet", value="Gets a feet GIF or Image", inline=False)
    embed.add_field(name="!hentai", value="Gets a hentai GIF or Image", inline=False)
    embed.add_field(name="!boobs", value="Gets some boobs GIF or Image", inline=False)
    embed.add_field(name="!tits", value="Gets some tits GIF or Image", inline=False)
    embed.add_field(name="!blowjob", value="Gets a blowjob GIF or Image", inline=False)
    embed.add_field(name="!lewdneko", value="Gets a lewd neko .-.", inline=False)
    embed.add_field(name="!lesbian", value="Uhmmm nice, lesbian porn", inline=False)
    embed.add_field(name="!traps", value="Someone like this?", inline=False)
    embed.add_field(name="!futanari", value="I think some people would like this . . .", inline=False)
    embed.set_footer(text="This bot is open source: https://github.com/x-name15/NSFW-Basic-Discord-Bot")
    await ctx.send(embed=embed)

@bot.command()
async def anal(ctx):
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await ctx.send(embed=em) 

@bot.command()
async def erofeet(ctx): 
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def feet(ctx): 
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def hentai(ctx):
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em) 

@bot.command()
async def boobs(ctx): 
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def tits(ctx): 
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()    
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def blowjob(ctx): 
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def lewdneko(ctx):
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@bot.command()
async def lesbian(ctx): 
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def traps(ctx):
  r = requests.get("https://nekos.life/api/v2/img/trap")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@bot.command()
async def futanari(ctx):
  r = requests.get("https://nekos.life/api/v2/img/futanari")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@bot.command()
async def femdom(ctx):
  r = requests.get("https://nekos.life/api/v2/img/femdom")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@bot.command()
async def pussy(ctx):
  r = requests.get("https://nekos.life/api/v2/img/pussy")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
