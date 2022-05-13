# main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time
import asyncio

load_dotenv()
TOKEN = os.getenv('CPL_OFFICIAL_TOKEN')

client = discord.Client()

# Welcome message
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

# Event where a message is sent on discord
@client.event
async def on_message(msg):

    # Parse username and channel name
    username = str(msg.author).split('#')[0]
    channel = str(msg.channel.name)

    # Don't react to itself
    if msg.author == client.user:
        return

    # Give Korbine an L
    if "korbine" in username.lower():
        await msg.add_reaction('\U0001F1F1')

    # Continue the chain gif train
    if ".gif" in msg.content:
        await msg.channel.send(msg.content)
        await asyncio.sleep(5)

client.run(TOKEN)