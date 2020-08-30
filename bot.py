# bot.py
import os
import random
import user
import fetch
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
    u = user.loadusers()
    ru = user.registeruser(u,ctx.message.author.id,battlenetid)
    if ru == 1:
        response = 'You have been added.'
    elif ru == 2:
        response = 'I would have overwritten your data, but not sure how..'
    await ctx.send(response)

@bot.command('embed')
async def embed(ctx,reqtype):
    if reqtype == 'l5':
        reqtype = 'Last 5 Games'
    #description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```"
    embed = discord.Embed(title=f"Call of Duty - {reqtype} Summary", colour=discord.Colour(0x200893), description="**Game Mode:** Kingslayer Trios")
    embed.add_field(name="Kills", value="9", inline=True)
    embed.add_field(name="Deaths", value="15", inline=True)
    embed.add_field(name="Kill/Death Ratio", value="0.60 (-.03)", inline=True)
    embed.add_field(name="Damage Dealt", value="1490", inline=True)
    embed.add_field(name="Damage Taken", value="1490", inline=True)
    embed.add_field(name="Gulag Score", value="0-0", inline=False)
    embed.add_field(name="Loadout", value="Yes", inline=True)
    embed.add_field(name="Primary Weapon", value="Grau 5.56", inline=True)
    embed.add_field(name="Secondary Weapon", value="HDR", inline=True)
    embed.set_thumbnail(url="https://imag.malavida.com/mvimgbig/download-fs/call-of-duty-warzone-26418-0.jpg")
    embed.set_author(name=f"{ctx.message.author.name}", icon_url=f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/{ctx.message.author.avatar}.png")
    embed.set_footer(text="Project source code available @ https://github.com/Amschon90", icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
    await ctx.send(embed=embed)

@bot.command('summary')
async def summary(ctx,num):
    u = user.loadusers()
    if int(num) > 20:
        await ctx.send('I can only show your last 20 games.')
        num = 20
    if user.isregistered(u, ctx.message.author.id):
        s = fetch.summaryStats(int(num), u[str(ctx.message.author.id)])
        embed = discord.Embed(title=f"Call of Duty - Last {num} Games Summary", colour=discord.Colour(0x200893))
        embed.add_field(name="Kills", value=f"{int(s.k)}", inline=True)
        embed.add_field(name="Deaths", value=f"{int(s.d)}", inline=True)
        embed.add_field(name="Kill/Death Ratio", value=f"{round(s.k/s.d,2)} ({round(s.k/s.d-s.akd,2)})", inline=True)
        embed.add_field(name="Gulag Score", value=f"W: {int(s.gk)} - L: {int(s.gd)}", inline=False)
        embed.add_field(name="Damage Dealt", value=f"{int(s.dd)}", inline=True)
        embed.add_field(name="Damage Taken", value=f"{int(s.dt)}", inline=True)
        embed.set_thumbnail(url="https://imag.malavida.com/mvimgbig/download-fs/call-of-duty-warzone-26418-0.jpg")
        embed.set_author(name=f"{ctx.message.author.name}", icon_url=f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/{ctx.message.author.avatar}.png")
        embed.set_footer(text="Project source code available @ https://github.com/Amschon90", icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
        await ctx.send(embed=embed)
    else:
        await ctx.send("You aren't registered. Please use the !register command, followed by your Battle.net ID.")

bot.run(TOKEN)