import aiohttp
import disnake
import json

from disnake import Embed
from disnake.ext import commands

class MiscCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command(name='quote', description='A quote to boost your confidence')
    async def quote(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en') as response:
                data = await response.json()
                quote = data['quoteText']

        embed = Embed(
            title='Generated Quote!',
            description=quote,
            colour=disnake.Color.green()
        )

        embed.set_footer(text="{}#{}".format(ctx.author.name,ctx.author.discriminator),icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)

