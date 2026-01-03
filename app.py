from flask import Flask
from pyrogram import Client
import os
import asyncio
from config import API_ID, API_HASH, BOT_TOKEN

# 1. Flask Setup (Render ke liye)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TechVJ ChatGPT Bot is Live!'

# 2. Pyrogram Client Setup
# Saari details config.py se automatically fetch ho rahi hain
bot = Client(
    "techvj_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins") # Aapke saare bot commands 'plugins' folder mein hone chahiye
)

if __name__ == "__main__":
    # Bot ko start karna
    print("Starting Bot...")
    bot.start()
    
    # Flask Server ko start karna (Render ke Port 10000 ke liye)
    print("Starting Flask Server...")
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
