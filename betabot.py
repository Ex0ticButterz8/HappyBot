from __future__ import print_function
import discord
import random
import os
import mechanicalsoup
import getpass
import argparse
import time
from discord import FFmpegPCMAudio
from discord.utils import get

from discord.ext import commands

client = commands.Bot(command_prefix = '!')

#custom check
def is_it_me(ctx):
    return ctx.author.id == 300246955681120256

@client.event
async def on_ready():
    print('Bot is ready.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('and making your quarantine happier!'))
    time.sleep(5)
    print('Activity & Game Displayed')
    time.sleep(5)
    print("--------------------------------------------\n           Ex0tic Boi Discord Bot\n            v. 0.1.1 Beta\n--------------------------------------------")

@client.command()
async def sadness(ctx):
    await ctx.send(f'Sorry to hear that you are sad, be happy, because this server loves you')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
	responses = ['It is yes','No','Maybe','If Kenneth likes fortnite','Why you have to ask me?','If Minecraft has circles','If you are sad',
                     'I will decide later',
                     'Try Again Later',
                     'It will happen']
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def Hello(ctx):
    await ctx.send(f'Hello, {ctx.author}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir(r'B:\PythonAMD64\BetaCogs'):
    if filename.endswith('.py'):
        client.load_extension(f'BetaCogs.{filename[:-3]}')


client.run('Discord Bot Code')
