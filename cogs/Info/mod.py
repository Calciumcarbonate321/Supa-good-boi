import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def clear(self,ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)

def setup(client):
    client.add_cog(mod(client))        
