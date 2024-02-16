class Translation(object):
    START_TEXT = """Hi {} 👋

I'm Url Upload Bot 🚀

<b>Permanent Thumbnail Support💯.</b>

<i>Send me a direct link and I will upload it to telegram as a file/video.</i>

Click /help for more details...."""
    ADD_CAPTION_HELP = """Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> and the text you wrote will be attached as the caption! 🤩
    
Example: <a href='https://te.legra.ph/file/ecf5297246c5fb574d1a0.jpg'>See This!</a> 👇"""

    INCORRECT_REQUEST = """Please make sure you submit your request correctly."""
    WAIT_PROCESS_FINISH = """Please wait for your current file to finish downloading before sending more links!

Or use /cancel to terminate incomplete processes."""
    PROCESS_CANCELLED = """File upload cancelled
You can now send a new URL."""
    NO_PROCESS_FOUND = """🤷‍♂️ No pending uploads were found. You can upload files by sending a link now!"""
    FORMAT_SELECTION = "👇𝗦𝗲𝗹𝗲𝗰𝘁 𝗔𝗻𝗱 𝗖𝗵𝗼𝘀𝗲 𝗬𝗼𝘂𝗿 𝗙𝗼𝗿𝗺𝗮𝘁👇"
    SET_CUSTOM_USERNAME_PASSWORD = """\n👮‍♂ Powered By :</b> @HxBots"""
    DOWNLOAD_START = "📥 DOWNLOADING..."
    UPLOAD_START = "📤 UPLOADING..."
    RCHD_TG_API_LIMIT = "<b>Downloaded in:</b> {} seconds.\n<b>Detected file size:</b> {}.\n\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations 😕."
    #AFTER_SUCCESSFUL_UPLOAD_MSG = "𝘛𝘏𝘈𝘕𝘒𝘚 𝘍𝘖𝘙 𝘜𝘚𝘐𝘕𝘎 𝘔𝘌 🥰"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Uploaded Successfully!"
    SAVED_CUSTOM_THUMB_NAIL = "Thumbnail Saved ✅."
    DEL_ETED_CUSTOM_THUMB_NAIL = "Thumbnail Deleted ✅."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = """<b>I think you have entered an unaccessible url or a private url.</b>
<i>Go check if you can access the content in the url from your browser first!</i>

<b>YouTubeDL</b> said: {}"""
    HELP_USER = """<b>How to Use Me?</b> 🤔

1. Send your URL link

2. Send thumbnail photo to save it permanently.

3. Select the desired option

4. Send /delthumbnail To Delete Your Thumbnail.

5.  Use /caption to Set caption as Reply to Media

6. Comments /about /viewthumbnail /info
"""
    ABOUT_TEXT = """<b>🔘 My Name :</b> URL-UploadBot V3 🚀

<b>🔘 Channel :</b> <a href="https://t.me/HxBots">HxBots</a>

<b>🔘 Source :</b> <a href="https://github.com/oVo-HxBots/URL-UploadBot">Soon..</a>

<b>🔘 Language :</b> <a href="https://www.python.org/">Python 3.10.8</a>

<b>🔘 Framework :</b> <a href="https://docs.pyrogram.org/">Pyrogram 2.0.106</a>

<b>🔘 Creater :</b> @Kiridewal"""

    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Send your thumbnail pic to generate custom thumbail."
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    CANCEL_STR = "❌ Cancelled ❌"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds."
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my time, I am in no mood to download this file. Meanwhile, why don't you try transloading and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    INFO_TEXT = """
🌸 First Name : <b>{}</b>

🌸 Second Name : <b>{}</b>

🌸 Username : <b>@{}</b>

🌸 Id : <code>{}</code>

🌸 Profile : <b>{}</b>

🌸 Dc : <b>{}</b>

🌸 Language : <b>{}</b>

🌸 Status : <b>{}</b>
"""
    # Soon 💯
    #START_BUTTONS = InlineKeyboardMarkup(
       #  [[
       #  InlineKeyboardButton('HELP', callback_data='help')
       #  InlineKeyboardButton('ABOUT', callback_data='about')
       #  ],[
      #   InlineKeyboardButton('CLOSE', callback_data='close')
        # ]]
  #  )
  # BUTTONS = InlineKeyboardMarkup(

