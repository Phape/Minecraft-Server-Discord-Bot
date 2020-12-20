import asyncio
import discord
import os
import re
from allowed_phrases import allowed_phrases_combined
from discord.ext import commands, tasks
from itertools import cycle
from pygtail import Pygtail

client = discord.Client()
# bot = commands.Bot(command_prefix='$')
status = cycle(['Made by Phape', 'use $ to get my attention'])


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    change_status.start()
    display_minecraft_logs.start()


@client.event
async def on_message(message):
    if message.author == client.user:  # alternatively: if message.author.bot:
        return

    if message.channel.id == 789963688035352585:  # mc-chat
        os.system(
            'screen -S minecraft -X stuff \'tellraw @a {"text":"<' + message.author.name + '> ' + message.content + '", "color":"dark_purple"}' + '^M\'')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# await ctx.send(f'Pong! {round (client.latency * 1000)}ms')

@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


async def msg_mc_chat_channel(message):
    channel = client.get_guild(
        789825438284382208).get_channel(789963688035352585)
    await channel.send(message)


@tasks.loop(seconds=5)
async def display_minecraft_logs():
    for line in Pygtail("/home/pi/minecraft-server/logs/latest.log", read_from_end=True):
        if re.match(allowed_phrases_combined, line):
            chat = format_log_to_chat(line)
            await msg_mc_chat_channel(chat)
        await asyncio.sleep(1)


def format_log_to_chat(log_line):
    chat = re.sub('\[\d\d:\d\d:\d*]\s\[Server\sthread/INFO\]:', '', log_line)
    return chat


client.run(os.getenv('TOKEN'))
