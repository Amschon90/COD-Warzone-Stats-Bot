# bot.py
import os
import random
import users
import main
from dotenv import load_dotenv

# 1
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='opinion', help='Tells you what it thinks of someone.')
async def opinion(ctx, name):
    if name.upper() == 'KITH':
        response = 'Fuck Kith!'
    else:
        response = f'{name}? Oh yeah, he\'s cool.'
    await ctx.send(response)

@bot.command('whoami')
async def who(ctx):
    response = ctx.message.author.name
    await ctx.send(response)

@bot.command('register')
async def reg(ctx, battlenetid):
    u = users.loadusers()
    ru = users.registeruser(u,ctx.message.author.name,battlenetid)
    if ru == 1:
        response = 'You have been added.'
    elif ru == 2:
        response = 'I would have overwritten your data, but not sure how..'
    await ctx.send(response)

@bot.command('stats')
async def getstats(ctx):
    response = main.statsprintout
    await ctx.send(response)

@bot.command('embed')
async def embed(ctx,reqtype):
    if reqtype == 'l5':
        reqtype = 'Last 5 Games'
    #description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```"
    embed = discord.Embed(title=f"Call of Duty - {reqtype} Summary", colour=discord.Colour(0x200893), description=f"{main.statsprintout}")
    embed.set_thumbnail(url="https://imag.malavida.com/mvimgbig/download-fs/call-of-duty-warzone-26418-0.jpg")
    embed.set_author(name=f"{ctx.message.author.name}", icon_url=f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/{ctx.message.author.avatar}.png")
    embed.set_footer(text="Project source code available @ https://github.com/Amschon90", icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
    await ctx.send(embed=embed)
bot.run(TOKEN)
