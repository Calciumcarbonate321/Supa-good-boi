import discord
from discord.ext import commands, tasks
import random
import time
from itertools import  cycle

client= commands.Bot(command_prefix='*')
stat= cycle(['Studying muhavre','Studying shubdh aur padh','Contemplating my 60-40 level',])
member=discord.Member
welcome= f'Welcome to our humble server {member}'

@client.event
async def on_ready():
    print("I am born ready")
    await client.change_presence(status=discord.Status.dnd,activity=discord.Game('Use * as prefix'))

@client.remove_command('help')

@client.command()
async def creeper(ctx):
    await ctx.send('Aw Man!')

@client.command(aliases=['ouija','ouija board','Ouija'])
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

@client.command(aliases=['60-40'])
async def _6040status(ctx):
    x=random.randint(0,100)
    if x<50:
        await ctx.send('Your 60-40 is not good. \n Tell some muhavre to improve your 60-40 ')
    else:
        await ctx.send('Your 60-40 is good.')

@client.command()
async def help(ctx):
    await ctx.send("""```List of commands:
    (1)*ouija [your question]
         This will tell an answer to your yes or no question
    (2)*60-40                                               
        This will check your 60-40.
    (3)*study_tips                                                              
        This will tell you about your exam. It can be a tip or a prediction.```""")

@client.command(aliases=['Namaste','Namaste Ji'])
async def namaste(ctx):
    await ctx.send('Namaste beta')

@client.command(aliases=['study tips'])
async def study_tips(ctx):
    res=['Gol kar pi lo','If you don\'t study properly then exam la kozhi mutta',
              'Improve your 60-40 to study well.','Govindaaa govinda']
    await ctx.send(f'{random.choice(res)}')
    

client.run('NzU3NTE3MzI5NTU4MTQzMDI4.X2hi_Q.oXnEon2lk2hQvRMAAe_5VFYn-9g')

