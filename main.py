import os
from pyrogram import Client

bot_token = os.environ["6686437724:AAEd2HCxSC5otL5-XS3NuRtQ2nhVG63V5vE"]
api_id = int(os.environ["23762978"])
api_hash = os.environ["eff30dac5504a8660e69bfe19f668571"]
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
