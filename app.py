from flask import Flask
from pyrogram import Client
import os
from config import API_ID, API_HASH, BOT_TOKEN

# 1. Flask Setup
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TechVJ ChatGPT Bot is Live!'

# 2. Pyrogram Setup
bot = Client(
    "techvj_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    # Bot ko start karein
    bot.start()
    print("Bot Started!")

    # RENDER FIX: Host '0.0.0.0' aur Port '10000' hona zaruri hai
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
