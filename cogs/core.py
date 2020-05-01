import random
import datetime 
import os
import aiohttp
import praw 
import discord
from discord.ext import commands, tasks
from itertools import cycle

class Core(commands.Cog):

    def  __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Core Cog Has Been Loaded")

    @commands.command()
    async def help(self, ctx):
        ''' Shows all the commands of the bot ''' 
        embed = discord.Embed(
        title="**Snowflake**",
        colour=discord.Colour(0x3b12ef),
        description="Hello! I am Snowflake, a **powerful** moderation but that sorts out all your moderation, fun, etc.\nI was created by MantisFan\nPrefix ``+``",
        timestamp=datetime.datetime.utcfromtimestamp(1580842764) # or any other datetime type format.
        )
        embed.set_image(url="attachment://snowflake.png")
        embed.set_author(
        name="Snowflake#2128",
        icon_url="https://cdn.discordapp.com/avatars/691966118713098311/355df999edf74157129b20c79062eae9.png?size=2048?size=1024"
        )
        embed.add_field(
        name="Core",
        value="ping | help | ",
        inline=False
        )
        embed.add_field(
        name="Fun",
        value="8ball | kill | joke | coinflip ",
        inline=False
        )
        embed.add_field(
        name="Economy",
        value="*Coming Soon*",
        inline=False
        )
        embed.add_field(
        name="Images",
        value="meme | cat | dog | avatar | ",
        inline=False
        )
        embed.add_field(
        name="Moderation",
        value="ban <@user> reason | kick <@user> <reason> | mute <@user> <reason> | unmute <@user> | addrole <@user> <role> | removerole <@user> <role> | lockdown #channel | unlock #channel  ",
        inline=False
        )
        embed.add_field(
        name="Info",
        value=" avatar | info | serverinfo | userinfo",
        inline=False
        )
        embed.add_field(
        name="Text",
        value="embed | say | ascii",
        inline=False
        )
        embed.add_field(
        name="Support",
        value="contact | support",
        inline=False
        )
        embed.set_footer(
            text="Made By MantisFan",
            icon_url="https://cdn.discordapp.com/avatars/691966118713098311/0add59b3327d3f6eebca983bdd137000.png?size=256"
        )
        await ctx.send(
        content="These are my commands",
        embed=embed
    )

    @commands.command()
    async def ping(self, ctx):
        ''' Sends the latency of the bot ''' 
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms.")


def setup(client):
    client.add_cog(Core(client))

    
