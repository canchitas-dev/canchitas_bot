#!/usr/bin/env python

import discord
from settings import TOKEN, BOT_ID
from text_utils import is_haiku, contains_trigger_word


async def detect_patterns(message):
    detectors = {
        is_haiku: "Woaaa, tu mensaje es un haiku!",
        contains_trigger_word: 'Puto tú'
    }

    if message.author.id == BOT_ID:
        # dont reply to ourselves
        return

    for detector, response in detectors.items():
        if detector(message.content):
            await message.channel.send(response)


class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        print("Ready to accept DS gateway events")

    async def on_message(self, message):
        # process command logic here

        # if this is not a command, evaluate fun bot dections (or conversation input)
        await detect_patterns(message)


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)
