import disnake
from disnake.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name='help',description=('Displays every-single cog for commands, etc!'))
    async def help(ctx):
        await ctx.send('Working!')
