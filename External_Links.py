import discord
from discord.ext import commands

class External_Links(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands
    @commands.Cog.listener()
    async def on_ready(self):
        print('External Link Beta Commands Loaded')

    @commands.command(aliases=['trello'])
    async def Trello(self, ctx):
        await ctx.send(f'Link to Ex0tic Boi Trello Page: https://trello.com/b/41uzKpmi/ex0tic-boi')
    
    @commands.command(aliases=['github', 'GitHub'])
    async def Github(self, ctx):
        await ctx.send(f'Link to the Ex0tic Boi Github Page: https://github.com/Ex0ticButterz8/Ex0tic-Boi')

def setup(client):
    client.add_cog(External_Links(client))
