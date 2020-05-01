import random
import datetime 
import os
import aiohttp
import praw 
import discord
from discord.ext import commands, tasks
from itertools import cycle

class Moderation(commands.Cog):

    def  __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation Cog Has Been Loaded")

    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=["clear", "prune"])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount : int):
        ''' Purges messages ''' 
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Purged {amount} messages! :white_check_mark:", delete_after=3) 

    @commands.has_permissions(kick_members=True)
    @commands.command(aliases=["yeet"])
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        ''' Kicks a fool '''
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.name}#{member.discriminator} :white_check_mark:")

    @commands.has_permissions(ban_members=True)
    @commands.command(aliases=["remove"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        ''' Bans a fool '''
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention} :white_check_mark:")

    @commands.has_permissions(ban_members=True)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        ''' Unbans A Fool ''' 
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention} :white_check_mark:")  
    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member : discord.Member = None, *, reason="an unspecified reason"):
        if not member:
            return await ctx.send("**Inform a member!**", delete_after=3)

        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(muted_role)
        await ctx.send(f"{member.mention} got muted for {reason}")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member : discord.Member = None):
        if not member:
            return await ctx.send("**Please inform a member!", delete_after=3)

        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(muted_role)
        await ctx.send(f"{member.mention} has been unmuted")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, member : discord.Member, *, roles = None):
         role = discord.utils.get(ctx.guild.roles, name=roles)
         await member.add_roles(role)
         await ctx.send(f"Changed Roles For {member.mention} +**{roles}**")

    @commands.command()
    async def removerole(self, ctx, member : discord.Member, *, roles = None):
         role = discord.utils.get(ctx.guild.roles, name=roles)
         await member.remove_roles(role)
         await ctx.send(f"Changed Roles For {member.mention} -**{roles}**")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lockdown(self, ctx, *, channel: discord.TextChannel = None, role: discord.Role = None):
        if not role:
            role = ctx.guild.default_role
        if not channel:
             return await ctx.send("**Specify a channel!**", delete_after=3)
        try:
            await channel.set_permissions(role, send_messages=False)
        except Exception:
            return await ctx.send(f"**I couldn't lock this channel for the {role} role!**", delete_after=5)
        embed = discord.Embed(description=f':white_check_mark: Successfully locked {channel} !', colour=0x3b12ef)
        return await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx, *, channel: discord.TextChannel = None, role: discord.Role = None):
        if not role:
            role = ctx.guild.default_role
        if not channel:
            return await ctx.send("**Specify a channel!**", delete_after=3)
        try:
            await channel.set_permissions(role, send_messages=True)
        except Exception:
            return await ctx.send(f"**I couldn't lock this channel for the {role} role!**", delete_after=5)
        embed = discord.Embed(description=f':white_check_mark: Successfully unlocked {channel}!', colour=0x3b12ef)
        return await ctx.send(embed=embed)

    @commands.command()
    async def verify(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name="Unverified")
        await ctx.author.remove_roles(role)
        await ctx.send(f"You have been verified! :white_check_mark:")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Testing, Testing, 1, 2, 3.")

def setup(client):
    client.add_cog(Moderation(client))
