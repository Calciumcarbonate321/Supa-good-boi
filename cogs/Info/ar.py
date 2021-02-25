import discord
from discord.ext import commands
import random
import asyncio

class auto_response(commands.Cog):
    def __init__(self, client):
        self.client = client
        global ar
        ar = True
    @commands.command(aliases=['ar','auto-response','autoresponse'])
    async def ar_toggle(self,ctx,* ,toggle : bool):
        if toggle is True:
            ar=True
            await ctx.send("Auto-response set to True.")
        elif toggle is False:
            ar=False
            await ctx.send("Auto-response set to False.")
        else:
            await ctx.send("Please enter a valid option.")

    @commands.Cog.listener()
    async def on_message(self,message):
        sad_words=["sad", "depressed", "unhappy", "miserable"]
        starter_encouragements = [
                                  "Cheer up!",
                                  "Hang in there.",
                                  "You are a great person !",
                                  "Everything will be fine soon, don't worry",
                                  ]
        try:
            if ar:
                if message.author==self:
                    return
                if message.author.bot:
                    return
                ar_ = ['f','oof','pog','poggers']
                responses=['f','F','https://tenor.com/bkY4z.gif']
                if message.content == 'f' or message.content=='F':
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
                if message.content=='creeper':
                    response='Aw man!'
                if message.content in ['no u','No u','NO U']:
                    response='no u'
                if message.content in ['1 sec','one second','One second','1 second']:
                    response='One second got over.'
                await message.channel.send(response)
            else:
                return
        except:
            pass

def setup(client):
    client.add_cog(auto_response(client))