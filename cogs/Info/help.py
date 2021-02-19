import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self,client):
        self.client=client

    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        em=discord.Embed(title="`HELP`",url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",description="`Use *help <command> to get more information on a commamd.`")

        em.add_field(name="`Fun`",value="ouija,meme",inline=True)
        em.add_field(name="`Moderation`",value="clear,ar",inline=True)
        em.add_field(name="`TO PISS OF PEOPLE`",value="snipe",inline=True)

        await ctx.send(embed=em)

    @help.command()
    async def ouija(self,ctx):
        em=discord.Embed(title="`OUIJA`",url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",description="`This one takes in a question from the user and gives an answer.`")
        em.add_field(name="`Syntax`",value="*ouija <question>")
        em.add_field(name="`Aliases`",value="Ouija,ouija")
        await ctx.send(embed=em)





def setup(client):
    client.remove_command("help")
    client.add_cog(Help(client))
