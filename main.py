import discord
from discord.ext import commands
import random
client= commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("I am born ready")

@client.command()
async def creeper(ctx):
    await ctx.send('Aw Man!')

@client.command(aliases=['ouija','ouija board'])
async def ouija_board(ctx, *,question):
    responses=["It is certain.",
               "It is decidedly so.",
               "Without a doubt.",
               "Yes - definitely.",
               "You may rely on it.",
               "As I see it, yes.",
               "Most likely.",
               "Outlook good.",
               "Yes.",
               "Signs point to yes.",
               "Reply hazy, try again.",
               "Ask again later.",
               "Better not tell you now.",
               "Cannot predict now.",
               "Concentrate and ask again.",
               "Don't count on it.",
               "My reply is no.",
               "My sources say no.",
               "Outlook not so good.",
               "Very doubtful."]
    await ctx.send('This must be a yes or no question or else do not ask me about the answer.')
    await ctx.send(f'Question you asked:{question} \n My Answer:{random.choice(responses)}')
    await ctx.send('You can believe it if you want.')

@client.event()
asyn def on_member_join(member):
    await.ctx.send(f'Welcome to our humble server {member}')

@client.event()
async def on_member_remove(member):
    await.ctx.send(f'So long {member}')

client.run('NzU3NTE3MzI5NTU4MTQzMDI4.X2hi_Q.RI17Ys2Bgcz-qUn-BCIZNSQyoH8')

