import discord
from discord.ext import commands, tasks
import random
import time
import asyncio
import os
from dotenv import load_dotenv
import praw
import itertools
import aiohttp
import json

load_dotenv('.env')

client = commands.Bot(command_prefix='*')
client.ar=True

@client.event
async def on_ready():
    print("I am born ready")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="you",url=""))

@client.command()
async def load(ctx,ext):
    try:
        client.load_extension(f"cogs.{ext}")
        await ctx.send(f"{ext} cog successfully loaded.")
    except:
        await ctx.send(f"{ext} is not a valid cog name.")



@client.command()
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
        "cogs.Info.mod"
    ]
    for i in cogs:
        client.load_extension(i)


@commands.command()
async def say(ctx, thing: str, channel_id: int):
    if ctx.author.id == 437163344525393920:
        channel = client.get_channel(int(channel_id))
        await channel.send(thing)


@client.command(name="clear")
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
async def ping(ctx):
    await ctx.send("Pong")

@client.command(aliases=['ar','auto-response','autoresponse'])
async def ar_toggle(ctx,* ,toggle : bool):
    if toggle is True:
        client.ar=True
        await ctx.send("Auto-response set to True.")
    elif toggle is False:
        client.ar=False
        await ctx.send("Auto-response set to False.")
    else:
        await ctx.send("Please enter a valid option.")

'''
@client.command(aliases=['gp','ghostping'])
async def ur_mom(ctx,user : discord.Member):
    await ctx.send(user.mention)
    await ctx.channel.purge(limit=2)'''



class auto_response(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_message(self,message):
        sad_words=["sad", "depressed", "unhappy", "miserable"]
        starter_encouragements = [
                                  "Cheer up!",
                                  "Hang in there.",
                                  "You are a great person !",
                                  "Everything will be fine soon, don't worry",

                                  ]
        dead=['died','rip']
        try:
            if client.ar is True:
                if message.author==client.user:
                    return
                if message.author.bot:
                    return
                ar_ = ['f','oof','pog','poggers']
                responses=['f','F','https://tenor.com/bkY4z.gif']
                if message.content == 'f' or message.content=='F'or any(w in message.content for w in dead):
                    response = ar_[0]
                if message.content in ['oof','Oof','I died']:
                    response=responses[2]
                if message.content in ['bruh','Bruh','BRUH']:
                    response='Bruh'
                if message.content in ['pog','poggers','Pog','Poggers']:
                    pog_gifs=['https://tenor.com/8kQd.gif',
                                        'https://tenor.com/NqQh.gif',
                                        'https://tenor.com/ZiI7.gif',
                                        'https://tenor.com/blxuC.gif']
                    response=random.choice(pog_gifs)
                if any(word in message.content for word in sad_words):
                    response=random.choice(starter_encouragements)

                if message.content=='creeper':
                    response='Aw man!'
                await message.channel.send(response)
            else:
                return
        except:
            pass


@client.command(name='meme')
async def meme(ctx):
    embed = discord.Embed(title="Meme", description=None)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0,1)]['data']['url'])
            embed.set_footer(text="r/memes")
            await ctx.send(embed=embed, content=None)

@client.command(name='poll')
async def poll(ctx, question,channelid : int, option1=None, option2=None):
    channel = client.get_channel(int(channelid))
    if option1==None and option2==None:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title=f"{question}", url="https://youtu.be/dQw4w9WgXcQ")
        embed.add_field(name="Yes",value="✅",inline=True)
        embed.add_field(name="No",value="❎",inline=True)
        sent= await channel.send(embed=embed)
        await sent.add_reaction('✅')
        await sent.add_reaction('❎')
    elif option2!=None and option1== None :
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title=f"{question}", url="https://youtu.be/dQw4w9WgXcQ")
        embed.add_field(name="Yes",value="✅",inline=True)
        embed.add_field(name=f"{option2}",value="❎",inline=True)
        sent= await channel.send(embed=embed)
        await sent.add_reaction('✅')
        await sent.add_reaction('❎')
    elif option1!=None and option2==None:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title=f"{question}", url="https://youtu.be/dQw4w9WgXcQ")
        embed.add_field(name=f"{option1}",value="✅",inline=True)
        embed.add_field(name="No",value="❎",inline=True)
        sent= await channel.send(embed=embed)
        await sent.add_reaction('✅')
        await sent.add_reaction('❎')
    else:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title=f"{question}", url="https://youtu.be/dQw4w9WgXcQ")
        embed.add_field(name=f"{option1}",value="✅",inline=True)
        embed.add_field(name=f"{option2}",value="❎",inline=True)
        sent= await channel.send(embed=embed)
        await sent.add_reaction('✅')
        await sent.add_reaction('❎')

def setup(client):
    client.add_cog(auto_response(client))

setup(client)
load_cogs()
client.run(os.getenv('DISCORD_TOKEN'))
