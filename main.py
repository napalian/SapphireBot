import disnake
import aiohttp

from disnake.ext import commands
from Cogs.HelpCog import HelpCog
from Cogs.MiscCog import MiscCog

client = commands.Bot(command_prefix="!",case_insensitive=True,intents=disnake.Intents.all())


with open ('bot_token.txt','r') as token:
    token = token.read()
    client.add_cog(HelpCog(client))
    client.add_cog(MiscCog(client))
    client.run(token)