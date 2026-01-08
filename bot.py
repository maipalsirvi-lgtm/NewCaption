from pyrogram import Client, filters

API_ID = int("30239641")
API_HASH = "f81acbe7ba69b9d04bbec9b4a07811aa"
BOT_TOKEN = "8370986939:AAGnYrl_4U7SFIJ1PjgKK-T0KbH4zBrh4MM"

FIXED_TEXT = "\n\n**Share Our Channel : https://t.me/tmkocdirect**\n\n**Do Like Now 👍🏻 And Subscribe 😎**"

app = Client(
    "auto_caption_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.channel & (filters.video | filters.photo | filters.document))
async def auto_caption(client, message):
    caption = message.caption or ""
    if FIXED_TEXT in caption:
        return
    await message.edit_caption(caption + FIXED_TEXT)

app.run()