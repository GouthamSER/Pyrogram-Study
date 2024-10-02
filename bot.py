import asyncio
from os import environ
import tgcrypto
from pyrogram import Client, filters

# Define your API ID, API Hash, and Bot Token
API_ID = "18979569"
API_HASH = "45db354387b8122bdf6c1b0beef93743"
BOT_TOKEN = "6228122908:AAEKGwokHIjvYsH6qgthcz5G-sOdL3Aq45o"


# Create a new Client instance
bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )
    async def start(self):
        await super().start()
        print("BotStarted...")
        



@bot.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        f"Hello {message.from_user.first_name}, I am your bot!")

@bot.on_message(filters.command("help"))
async def start_command(client, message):
    await message.reply_text(
        f"Hello {message.from_user.first_name}, I am your bot!")
