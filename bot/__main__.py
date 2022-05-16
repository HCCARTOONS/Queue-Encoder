from pyrogram import filters
from bot import app, data, sudo_users
from bot.helper.utils import add_task
import asyncio

video_mimetype = [
  "video/x-flv",
  "video/mp4",
  "application/x-mpegURL",
  "video/MP2T",
  "video/3gpp",
  "video/quicktime",
  "video/x-msvideo",
  "video/x-ms-wmv",
  "video/x-matroska",
  "video/webm",
  "video/x-m4v",
  "video/quicktime",
  "video/mpeg"
  ]

@app.on_message(filters.user(sudo_users) & filters.command(["start", "help"]))
async def help_message(app, message):
    await message.reply_text(f"Hi {message.from_user.mention()}\n**•I can encode Telegram files in x265/x264, just send me a video.**\n**•This Bot is Developed by @S136r136a1**\n**•Simple, Easy and Convenient to use**\n**Thanks**")

@app.on_message(filters.user(sudo_users) & filters.incoming & (filters.video | filters.document))
async def encode_video(app, message):
    if message.document:
      if not message.document.mime_type in video_mimetype:
        await message.reply_text("Invalid Video !\nMake Sure Its A Valid Video file.", quote=True)
        return
    await message.reply_text("Added to Queue Please Wait 🕔", quote=True)
    data.append(message)
    if len(data) == 1:
     await add_task(message)
     time.sleep(2)
app.run()
