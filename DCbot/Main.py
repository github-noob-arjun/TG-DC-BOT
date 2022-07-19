import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

 
DCBot = Client(
      "DC_ID_Bot",
      bot_token="5589185991:AAGDjCCcp7IG1u_YQErui5yLwyfXizptXYI",
      api_id="4738674",
      api_hash="f2be74eaa9b1cb32498f45d04e4dbb54",
)

@DCBot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    reply_markup = START_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

START_TEXT = """**🆔 Your Telegram DC Is :** `{}`"""
START_BUTTON = InlineKeyboardMarkup(
             [[
             InlineKeyboardButton('♻️ Updates Channel ♻️', url=f"https://telegram.me/PYRO_BOTZ")
             ]]
        )
