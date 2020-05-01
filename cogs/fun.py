import random
import datetime 
import os
import aiohttp
import praw 
import discord
from discord.ext import commands, tasks
from itertools import cycle

class Fun(commands.Cog):

    def  __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun Cog Has Been Loaded")

    @commands.command(aliases=["8ball", "magic"])
    async def _8ball(self, ctx, *, question):
        ''' An _8ball Command '''
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "It's best not to tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


    @commands.command()
    async def meme(self, ctx):
        ''' Sends a meme '''
        HEADERS = {
            'User-Agent' : "Magic Browser"
        }
        URL = f"https://www.reddit.com/r/memes/hot.json?limit=100"
    
        async with aiohttp.request("GET", URL, headers=HEADERS) as response:
            if response.status == 200:
                json_data = await response.json()
            else:
                data = {}

            var1 = random.choice(json_data["data"]["children"])
            var2 = var1["data"]["url"]
            
        embed = discord.Embed(title="Here's a meme!", color=0x3b12ef)

        embed.set_footer(text="Made by MantisFan", icon_url="attachment://snowflake.png")
        embed.set_image(url=var2)

        await ctx.send(embed=embed)

        
    @commands.command()
    async def joke(self, ctx):
        ''' Sends a joke '''
        jokes = ["Why did the kid throw his clock out the window? Because he wanted to see time fly!",
                      "Why are fish so smart? Because they live in schools!",
                      "Where do polar bears keep their money? In a snow bank!",
                      "Why did the pony get sent to his room? He wouldn’t stop horsing around!",
                      "What do you call a bear with no ears? A “B!",
                      "What do you call a cheese that’s not yours? Nacho Cheese!",
                      "Why wouldn’t the shrimp share his treasure? Because he was a little shellfish!",
                      "Why is Cinderella bad at soccer? Because she’s always running away from the ball!",
                      "Where do cows go on Friday nights? They go to the moo-vies!",
                      "If a seagull flies over the sea, what flies over the bay? A bagel!",
                      "Why did the cookie go to the nurse? Because he felt crummy!",
                      "What animal can you always find at a baseball game? A bat!"]
        await ctx.send(f"Here's a joke! \n{random.choice(jokes)}")


    @commands.command()
    async def kill(self, ctx, members: commands.Greedy[discord.Member], *, reason='no item'):
        ''' Kills a fool '''
        slapped = ", ".join(x.name for x in members)
        await ctx.send('{} was killed with {}'.format(slapped, reason))

    @commands.command()
    async def coinflip(self, ctx):
        sides = ["Heads", "Tails"]
        await ctx.send(f"You flipped {random.choice(sides)}!")


def setup(client):
    client.add_cog(Fun(client))