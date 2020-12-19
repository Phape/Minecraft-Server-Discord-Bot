import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg_content = message.content.lower()

    if msg_content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))