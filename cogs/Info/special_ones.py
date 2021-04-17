import discord
from discord.ext import commands
import asyncio

class special_ones(commands.Cog):

    def __init__(self,client):
        self.client=client


    @commands.Cog.listener()
    async def on_message_delete(self,message):

        global snipe_message_content
        global snipe_message_author

        snipe_message_content = message.content
        snipe_message_author = message.author.name
        await asyncio.sleep(60)
        snipe_message_author = None
        snipe_message_content = None

    @commands.command()
    async def snipe(self,message):
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
    @commands.command()
    async def prenk(self,ctx,user : discord.Member):
        await ctx.send(user.mention)
        await ctx.channel.purge(limit=2)

    @commands.command()
    async def invite(self,ctx):
        embed=discord.Embed(title="My invite link")
        embed.add_field(name="Invite link",value="https://discord.com/api/oauth2/authorize?client_id=757517329558143028&permissions=0&scope=bot%20applications.commands")
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(special_ones(client))
