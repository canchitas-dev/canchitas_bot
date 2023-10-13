import os

TOKEN = os.environ.get("DISCORD_TOKEN", None)
BOT_ID = os.environ.get("DISCORD_BOT_ID", None)

if BOT_ID:
    BOT_ID = int(BOT_ID)
