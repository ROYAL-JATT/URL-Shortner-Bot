import os
from pyrogram import Client

bot_token = os.environ.get("6372645892:AAGCSvh6mDAQuzu01OW4S-k9G9mAJgJYH4w")
api_id_str = os.environ.get("28280795")  # Retrieve the environment variable
if api_id_str is not None and api_id_str.isdigit():
    api_id = int(api_id_str)
api_hash = os.environ.get("3f02c2df6069de8c1a2abf623da0a4b8")
plugins = dict(
    root="plugins"
)

Bot = Client(
    "URL-Shortner-Bot",
    bot_token=bot_token,
    # Obtain the API ID from environment variables
    api_id=api_id_str,
    api_hash=api_hash,
    plugins=plugins,
    workers=50,
    sleep_threshold=10
)

Bot.run()
