import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get

class Voice(commands.Cog):

    def __init__(self, client):
        self.client = client
    #Commands:
    @commands.Cog.listener()
    async def on_ready(self):
        print('Voice Commands Beta Commands Loaded')

    @commands.command(pass_content = True)
    async def join(ctx, self):
        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("Voice Channel Not Detected")
            return
        voice = get(commands.voice_client, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel_connect()
        source = FFmpegPCMAudio('1.m4a')
        player = voice.play(source)

def setup(client):
    client.add_cog(Voice(client))