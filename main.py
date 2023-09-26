#!/usr/bin/env python

import discord
from settings import TOKEN, BOT_ID
from string import digits
from random import randint


def process_text_detectors(message):
    is_haiku(message)


class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(f"Mentions for message: {message.mentions}")

        process_text_detectors(message)

        if len(message.mentions) == 1 and message.mentions[0].id == BOT_ID:
            await message.channel.send("num 0 to 9")
            message = await client.wait_for('message', timeout=30.0)
            print("got num: ", message.content)


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)
