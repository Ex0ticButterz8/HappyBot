import discord
from discord.ext import commands

class External_Links(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands
    @commands.Cog.listener()
    async def on_ready(self):
        print('External Link Commands Loaded')

    @commands.command(aliases=['trello'])
    async def Trello(self, ctx):
        await ctx.send(f'Link to Ex0tic Boi Trello Page: https://trello.com/b/41uzKpmi/ex0tic-boi')

def setup(client):
    client.add_cog(External_Links(client))
