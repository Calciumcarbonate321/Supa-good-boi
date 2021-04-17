import discord
from discord.ext import commands
import contextlib
import io
import textwrap
import traceback
from discord.ext.commands.help import Paginator
from traceback import format_exception
from discord.ext.buttons import Paginator

def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content

class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass

class evale(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(name='eval')
    @commands.is_owner()
    async def eval(self,ctx,*,code):
        code = clean_code(code)

        local_variables = {
        "discord": discord,
        "commands": commands,
        "client": self.client,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message
        }

        stdout = io.StringIO()

        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"""async def func():\n{textwrap.indent(code, '    ')}""", local_variables
                )

                obj = await local_variables["func"]()
                result = f"{stdout.getvalue()}\n-- {obj}\n"
        except Exception as e:
            result = "".join(format_exception(e, e, e.__traceback__))

        pager = Pag(
        timeout=100,
        entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
        length=1,
        prefix="```py\n",
        suffix="```"
        )

        await pager.start(ctx)

def setup(client):
    client.add_cog(evale(client))
