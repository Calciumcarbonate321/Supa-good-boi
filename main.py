from logging import exception
from aiohttp.helpers import TOKEN
import discord
from discord.ext import commands, tasks
import random
import time
import asyncio
import os
from discord.ext.commands.core import is_owner
from discord.ext.commands.errors import NotOwner
from dotenv import load_dotenv
import praw
import itertools
import aiohttp
import json
import time

load_dotenv('.env')

client = commands.Bot(command_prefix='*')


@client.event
async def on_ready():
    print("I am born ready")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="you",url=""))

@client.command()
@is_owner()
async def load(ctx,ext):
    try:
        client.load_extension(f"cogs.{ext}")
        await ctx.send(f"{ext} cog successfully loaded.")
    except:
        await ctx.send(f"{ext} is not a valid cog name.")

@client.command()
@is_owner()
async def unload(ctx,ext):
    try:
        client.unload_extension(f"cogs.{ext}")
        await ctx.send(f"{ext} cog successfully unloaded.")
    except:
        await ctx.send(f"{ext} is not a valid cog name.")


def load_cogs():
    cogs=[
        "cogs.Info.help",
        "cogs.fun.ouija",
        "cogs.Info.special_ones",
        "cogs.Info.mod",
        "cogs.Info.ar",
        "cogs.Info.poll"
    ]
    for i in cogs:
        client.load_extension(i)
client.load_extension('jishaku')     


@commands.command()
async def say(ctx, thing: str, channel_id: int):
    if ctx.author.id == 437163344525393920:
        channel = client.get_channel(int(channel_id))
        await channel.send(thing)


@client.command()
async def ping(ctx):
    await ctx.send("Pong")

@client.command()
@is_owner()
async def shutdown(ctx):
    await ctx.send("Shutting down...")
    try:
        await client.close()  
    except RuntimeError:
        print("Bot successfully turned off")    



@client.command(name='meme')
async def meme(ctx):
    embed = discord.Embed(title="Meme", description=None)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0,1)]['data']['url'])
            embed.set_footer(text="r/memes")
            await ctx.send(embed=embed, content=None)


load_cogs()
client.run(os.getenv('DISCORD_TOKEN'))

