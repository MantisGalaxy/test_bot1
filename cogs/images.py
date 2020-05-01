import random
import datetime 
import os
import aiohttp
import praw 
import discord
from discord.ext import commands, tasks
from itertools import cycle

class Images(commands.Cog):

    def  __init__(self, client):
        self.client = client

    @commands.command()
    async def dog(self, ctx):
        ''' Shows Dog Command '''
        HEADERS = {
            'User-Agent' : "Magic Browser"
        }
        URL = f"https://www.reddit.com/r/dogpictures/hot.json?limit=100"
    
        async with aiohttp.request("GET", URL, headers=HEADERS) as response:
            if response.status == 200:
                json_data = await response.json()
            else:
                data = {}

            var1 = random.choice(json_data["data"]["children"])
            var2 = var1["data"]["url"]
            
        embed = discord.Embed(title="Here's a cute dog!", color=0x3b12ef)

        embed.set_footer(text="Made by MantisFan", icon_url="attachment://snowflake.png")
        embed.set_image(url=var2)

        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        ''' Shows a cat '''
        HEADERS = {
            'User-Agent' : "Magic Browser"
        }
        URL = f"https://www.reddit.com/r/catpictures/hot.json?limit=100"
    
        async with aiohttp.request("GET", URL, headers=HEADERS) as response:
            if response.status == 200:
                json_data = await response.json()
            else:
                data = {}

            var1 = random.choice(json_data["data"]["children"])
            var2 = var1["data"]["url"]
            
        embed = discord.Embed(title="Here's a cat!", color=0x3b12ef)

        embed.set_footer(text="Made by MantisFan", icon_url="attachment://snowflake.png")
        embed.set_image(url=var2)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Images(client))