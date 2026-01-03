from flask import Flask
from pyrogram import Client
import os
from config import API_ID, API_HASH, BOT_TOKEN

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TechVJ ChatGPT Bot is Live!'

bot = Client(
    "techvj_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    # Bot start karein
    bot.start()
    print("Bot Started!")

    # Render ke liye port aur host set karna zaruri hai
    # Port Render automatically provide karta hai environment variable mein
    port = int(os.environ.get("PORT", 10000))
    
    # host="0.0.0.0" hona bahut zaruri hai Render ke liye
    app.run(host="0.0.0.0", port=port)
