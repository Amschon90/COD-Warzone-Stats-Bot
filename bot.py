# bot.py
import os
import random
import users
from dotenv import load_dotenv

# 1
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

bot.run(TOKEN)
