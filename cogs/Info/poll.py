import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def poll(self,ctx,question,channelid : int,option1=None,option2=None):
        channel = self.client.get_channel(int(channelid))
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
    client.add_cog(Poll(client))             