from __future__ import print_function
import discord
import random
import os
import mechanicalsoup
import getpass
import argparse

from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('and making your quarantine happier!'))
    print('Activity & Game Displayed')

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
@commands.has_permissions(manage_messages=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

#custom check
def is_it_me(ctx):
    return ctx.author.id == 300246955681120256

@client.command()
async def Hello(ctx):
    await ctx.send(f'Hello, {ctx.author}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('B:\PythonAMD64\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('discord_bot_code')
