import os
from bot import data, download_dir
import asyncio
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified
from .ffmpeg_utils import encode, get_thumbnail

async def on_task_complete():
    del data[0]
    if len(data) > 0:
      await add_task(data[0])

async def add_task(message: Message):
    try:
      msg = await message.reply_text("⬇️ **Downloading Video** ⬇️", quote=True)
      filepath = await message.download(file_name=download_dir)
      await msg.edit(f"**Encoding The Given File\n-->** ```{filepath}```")
      new_file, og = await encode(filepath)
      if new_file:
        await msg.edit("**⬆️ Video Encoded Starting To Upload ⬆️**")
        await msg.edit("**⬆️ Uploading Video ⬆️**")
        await message.reply_document(new_file, file_name=og, quote=True, force_document=True, caption=og)
        os.remove(new_file)
        await msg.edit("**File Encoded**")
      else:
        await msg.edit("**Error Contact @NIRUSAKIMARVALE**")
        os.remove(filepath)
    except MessageNotModified:
      pass
    except Exception as e:
      await msg.edit(f"```{e}```")
    await on_task_complete()
