import os
from pyrogram import Client

bot_token = os.environ["6372645892:AAGCSvh6mDAQuzu01OW4S-k9G9mAJgJYH4w"]
api_id = int(os.environ["28280795"])
api_hash = os.environ["3f02c2df6069de8c1a2abf623da0a4b8"]
plugins = dict(
    root="plugins"
)

Bot = Client(
    "URL-Shortner-Bot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins,
    workers=50,
    sleep_threshold=10
)

Bot.run()
