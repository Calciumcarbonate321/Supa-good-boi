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

def setup(client):
    client.add_cog(special_ones(client))
