import asyncio
import discord
import os
import time
from pygtail import Pygtail
from discord.ext import commands

client = discord.Client()
# bot = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    client.loop.create_task(status_task())
    client.loop.create_task(display_minecraft_logs())


@client.event
async def on_message(message):
    if message.author == client.user:  # alternatively: if message.author.bot:
        return

    msg_content = message.content.lower()

    if msg_content.startswith('$hello'):
        await message.channel.send('Hello!')


# await ctx.send(f'Pong! {round (client.latency * 1000)}ms')

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Made by Phape'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game('use $ to get my attention'))
        await asyncio.sleep(60)


async def msg_mc_chat_channel(message):
    channel=client.get_guild(789825438284382208).get_channel(789963688035352585)
    await channel.send(message)


async def display_minecraft_logs():
    while True:
        for line in Pygtail("/home/pi/minecraft-server/logs/latest.log", read_from_end=True):
            # print(line)
            await msg_mc_chat_channel(line)
            await asyncio.sleep(5)


client.run(os.getenv('TOKEN'))
