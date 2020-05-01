import random
import datetime 
import os
import aiohttp
import praw 
import discord
from discord.ext import commands, tasks
from itertools import cycle

creatortag = "MantisFan#0001"

class Support(commands.Cog):

    def  __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Support Cog Has Been Loaded")
        
    @commands.command()
    async def support(self, ctx):
        ''' Shows all the contact info '''
        embed = discord.Embed(title="Support", description="Here are my contacts", color= discord.Colour(0x3b12ef))

        embed.add_field(name="Support Server: ", value="https://discord.gg/KjCme2S")
        embed.add_field(name="Contact the Owner: ", value=f"{creatortag}")

        embed.set_footer(text="Made by MantisFan", icon_url="https://cdn.discordapp.com/avatars/691966118713098311/0add59b3327d3f6eebca983bdd137000.png?size=256")
    
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Support(client))
