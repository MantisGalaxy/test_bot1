import random
import datetime 
import os
import aiohttp
import praw 
import discord
from discord.ext import commands, tasks
from itertools import cycle

class Text(commands.Cog):

    def  __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Text Cog Has Been Loaded")

    @commands.command()
    async def say(self, ctx, *, arg):
        if not ctx.message.author.id == 331451561387753472:
            return await ctx.send("You cannot do this command!", delete_after=3)
        ''' Allows you to send messages through the bot '''
        await ctx.send(arg)
        await ctx.message.delete()

    @commands.command()
    async def embed(self, ctx, *, arg):
        ''' Embed A Message '''
        embed = discord.Embed(description=arg, color=0x3b12ef)

        await ctx.send(embed=embed)
        await ctx.message.delete()



def setup(client):
    client.add_cog(Text(client))