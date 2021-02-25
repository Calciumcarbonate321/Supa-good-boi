import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions


class Mod(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def clear(self,ctx, amount: int):
        try:
            await ctx.channel.purge(limit=amount + 1)
        except:
            await ctx.send("LMFAO you don't have the perms for that!")

def setup(client):
    client.add_cog(Mod(client))
