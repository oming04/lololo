#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Owner : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ PAID PROMOTE : <a href='https://t.me/tontonvid'>PP MURAH</a>\n○ Channel : @wicwicviral\n○ Source Code : <a href='https://t.me/belominsyaf'>Tanya Creator</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Tutup Jangan Kepo", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass