import discord
from discord.ext import commands
import random

class ouija(commands.Cog):

    def __init__(self,client):
        self.client=client

    @commands.command(aliases=["ouija","Ouija"])
    async def ouija_board(self,ctx, *, question):
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

def setup(client):
    client.add_cog(ouija(client))
