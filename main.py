import discord
from discord.ext import commands, tasks
import random
import time
import asyncio
import os
from dotenv import load_dotenv

client = commands.Bot(command_prefix='*')
ar=True
@client.event
async def on_ready():
    print("I am born ready")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="you"))


@client.remove_command('help')
@client.event  #on_member_join
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(
                f"""Welcome to the server {member.mention}""")


@client.command()  #creeper
async def creeper(ctx):
    await ctx.send('Aw Man!')


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
    await ctx.send("""```List of commands:
    (1)*ouija [your question]
         This will tell an answer to your yes or no question```""")


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
async def ar_toggle(ctx,* ,toggle,):
    turn_on=['on','On','True','true','T','t']
    turn_off=['off','Off','false','False','F','f']
    if toggle in turn_on:
        ar=True
        await ctx.send("Auto-response successfully turned on.")
    if toggle in turn_off:
        ar=False
        await ctx.send("Auto-response successfully turned off.")
    else:
        await ctx.send("Next time please send a valid option dumbass.")
'''
@client.event
async def on_message(message):
    if message.author == client.user:
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
    await message.channel.send(response)
    await client.process_commands(message)'''

class auto_response(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_message(self,message):
        try:
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
        except:
            return
        await message.channel.send(response)
def setup(client):
    client.add_cog(auto_response(client))
setup(client)
load_dotenv('.env')
client.run(os.getenv('DISCORD_TOKEN'))
