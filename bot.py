import asyncio
import tgcrypto
from pyrogram import Client, filters

# Define your API ID, API Hash, and Bot Token
API_ID = "18979569"
API_HASH = "45db354387b8122bdf6c1b0beef93743"
BOT_TOKEN = "7195222206:AAGsp4RstBtnChHAx_aQNNV-PJ6_cQEE54w"

# Create a new Client instance
bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


async def main():
    await bot.start()
    print("Bot is running...")


@bot.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_chat_action("Typing...")
    await message.reply_text(
        f"Hello {message.from_user.first_name}, I am your bot!")

@bot.on_message(filters.command("help"))
async def start_command(client, message):
    await message.reply_chat_action("Typing...")
    await message.reply_text(
        f"Hello {message.from_user.first_name}, I am your bot!")
