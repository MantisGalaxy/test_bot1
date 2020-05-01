import random
import datetime 
import os
import aiohttp
import praw 
import discord
from discord.ext import commands, tasks
from itertools import cycle

creator = "MantisFan"

class Info(commands.Cog):

    def  __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Info Cog Has Been Loaded")
    
    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        ''' Shows info of a user '''
        member = ctx.author if not member else member
        roles = [role for role in member.roles]
        
        embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {member}")
    
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}. Made by {creator}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Guild Name:", value=member.display_name)

        embed.add_field(name="Created At:", value=member.created_at)
        embed.add_field(name="Joined:", value=member.joined_at)

        embed.add_field(name=f"Roles [{len(roles)}]", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Highest Role:", value=member.top_role.mention)

        embed.add_field(name="Bot?", value=member.bot)

        await ctx.send(embed=embed)

        
    @commands.command()
    async def info(self, ctx):
        ''' I didn't know what to add here '''
        embed = discord.Embed(title="Snowflake", description="A powerful moderation bot made with Discord.py", color=0x3b12ef)

        embed.set_footer(text="Made By MantisFan", icon_url="attachment://snowflake.png")

        embed.add_field(name="Creator: ", value="MantisFan#0001")
        embed.add_field(name="Server count", value=f"{len(self.client.guilds)}")

        embed.add_field(name="Invite", value="[Invite Me To Your Server!](https://discordapp.com/api/oauth2/authorize?client_id=691966118713098311&permissions=8&scope=bot)")

        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(title= f"{member.display_name}'s Avatar'")
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"Requested By {ctx.author.display_name}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Info(client))

