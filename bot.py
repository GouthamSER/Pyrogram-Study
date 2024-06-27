import asyncio
from os import environ
import tgcrypto
from aiohttp import web as webserver
from pyrogram import Client, filters

# Define your API ID, API Hash, and Bot Token
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
PORT_CODE = environ.get("PORT", "8080")

# Create a new Client instance
bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


async def main():
    await bot.start()
        client = webserver.AppRunner(await bot_run())
        await client.setup()
        bind_address = "0.0.0.0"
        await webserver.TCPSite(client, bind_address,
        PORT_CODE).start()
        
    print("Bot is running...")


@bot.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        f"Hello {message.from_user.first_name}, I am your bot!")

@bot.on_message(filters.command("help"))
async def start_command(client, message):
    await message.reply_text(
        f"Hello {message.from_user.first_name}, I am your bot!")
