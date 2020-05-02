import random
import datetime 
import os
import aiohttp
import asyncpg
import discord
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = "+")
creator = "MantisFan"
creatortag = "MantisFan#0001"
client.remove_command("help")

# Handles the errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have enough permissions to do that!")

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please, inform all the parameters!')

    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have enough perms to do that!")

    else:
        raise(error)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Snowflakes Fall...| +help"))
    print(f"{client.user} is ready!")


@commands.has_permissions(administrator=True)
@client.command()
async def load(ctx, extension):
    if not ctx.message.author.id == 331451561387753472:
        return await ctx.send("You cannot do this command!", delete_after=3)
    ''' Loads a Cog '''
    client.load_extension(f"cogs.{extension}")

@commands.has_permissions(administrator=True)
@client.command()
async def unload(ctx, extension):
    if not ctx.message.author.id == 331451561387753472:
        return await ctx.send("You cannot do this command!", delete_after=3)
    ''' Unloads A Cog '''
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run()
        



