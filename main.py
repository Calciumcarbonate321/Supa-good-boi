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


@client.remove_command('help')
@client.event  #on_member_join
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(
                f"""Welcome to the server {member.mention}""")

@client.command(aliases=['ouija','Ouija'])  #ouija_board
async def ouija_board(ctx, *, question):
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Outlook not so good.", "Very doubtful."
    ]
    await ctx.send(
        'This must be a yes or no question or else do not ask me about the answer.'
    )
    await ctx.send(
        f'Question you asked:{question} \n My Answer:{random.choice(responses)}'
    )


@client.command()  #help command
async def help(ctx):
    embed=discord.Embed(title="HELP", description="CATEGORIES", color=0x16c038)
    embed.add_field(name="FUN", value="ouija,ghostping,snipe", inline=True)
    embed.add_field(name="ADMIN", value="clear,auto-response", inline=True)
    embed.add_field(name="CURRENCY", value="coming soon", inline=True)
    embed.set_footer(text="Type *help (command name for more information on it)")


@client.command(name='say')  #say command
async def say(ctx, thing: str, channel_id: int):
    if ctx.author.id == 437163344525393920:
        channel = client.get_channel(int(channel_id))
        await channel.send(thing)

snipe_message_content = None
snipe_message_author = None
@client.event  #snipe_command_pre-requisite
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author

    snipe_message_content = message.content
    snipe_message_author = message.author.name
    await asyncio.sleep(60)
    snipe_message_author = None
    snipe_message_content = None

@client.command()  #snipe_command
async def snipe(message):
    if snipe_message_content == None:
        await message.channel.send("Theres nothing to snipe.")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(
            text=
            f"Asked by {message.author.name}#{message.author.discriminator}",
            icon_url=message.author.avatar_url)
        embed.set_author(name=f"{snipe_message_author}")
        await message.channel.send(embed=embed)
        return


@client.command(name="clear")
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
async def test(ctx):
    await ctx.send("Yes I am online.")

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

@client.command(aliases=['gp','ghostping'])
async def ur_mom(ctx,user : discord.Member):
    await ctx.send(user.mention)
    await ctx.channel.purge(limit=2)



class auto_response(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_message(self,message):
        try:
            if client.ar is True:
                if message.author==client.user:
                    return
                if message.author.bot:
                    return
                ar_ = ['f','oof','pog','poggers']
                responses=['f','F','https://tenor.com/bkY4z.gif']
                if message.content == 'f' or message.content=='F':
                    response = ar_[0]
                if message.content=='oof':
                    response=responses[2]
                if message.content in ['pog','poggers','Pog','Poggers']:
                    pog_gifs=['https://tenor.com/8kQd.gif',
                                        'https://tenor.com/NqQh.gif',
                                        'https://tenor.com/ZiI7.gif',
                                        'https://tenor.com/blxuC.gif']
                    response=random.choice(pog_gifs)
                if message.content=='creeper':
                    response='Aw man!'
                await message.channel.send(response)
            else:
                return
        except:
            pass


'''
class memer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if clientid and clientsec:
            self.reddit=praw.Reddit(client_id = os.getenv('clientid'),
            client_secret = os.getenv('clientsec'),
            username = os.getenv('reduser'),
            password = os.getenv('redpas'),
            user_agent = "pogman")
        @commands.Cog.command()
        async def meme(ctx,subreddit = "memes"):
            subreddit = reddit.subreddit("memes")
            all_subs = []
            top = subreddit.hot(limit = 100)
            for submission in top:
                all_subs.append(submission)
                random_sub = random.choice(all_subs)
                name = random_sub.title
                url = random_sub.url
                likes = random_sub.score
                em = discord.Embed(title = name,url=f"{url}")
                em.set_image(url = url)
                em.set_footer(text= "This post has 🔺" + str(likes) + " Upvotes" )
            await ctx.send(embed = em)'''



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
    elif option2!=None:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title=f"{question}", url="https://youtu.be/dQw4w9WgXcQ")
        embed.add_field(name="Yes",value="✅",inline=True)
        embed.add_field(name=f"{option2}",value="❎",inline=True)
        sent= await channel.send(embed=embed)
        await sent.add_reaction('✅')
        await sent.add_reaction('❎')
    elif option1!=None:
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

client.run(os.getenv('DISCORD_TOKEN'))
