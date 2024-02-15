# Modified by @Kirodewal | @Hx_URLuploadBot

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import math, os, time, shutil
from config import Config
from plugins.startmsg import Translation

PROGRESS = """
⏳ **Percentage:** `{0}%`
✅ **Done:** `{1}`
💠 **Total:** `{2}`
📶 **Speed:** `{3}/s`
🕰 **ETA:** `{4}`
"""

async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    filename,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "[{0}{1}] {2}%\n".format(
            ''.join(["●" for i in range(math.floor(percentage / 5))]),
            ''.join(["○" for i in range(20 - math.floor(percentage / 5))]),
            #round(percentage, 2),
            filename
        )
        tmp = progress + PROGRESS.format( #"""🔸<b>Dᴏɴᴇ</b> ✅: {0} of {1}\n🔸<b>Sᴘᴇᴇᴅ</b> 🚀: {2}/s\n🔸<b>Tɪᴍᴇ</b> 🕒: {3}""".format(
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            TimeFormatter(time_to_completion) if time_to_completion != '' else "0 s"
        )
        try:
            await message.edit(
                text="{}\n\n {}".format(
                    ud_type,
                    tmp
                )
            )
        except:
            pass

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

