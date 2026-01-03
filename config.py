import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "23903140"))
API_HASH = environ.get("API_HASH", "579f1bcf3eac1660d81ef34b09906012")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003166629808"))
ADMINS = int(environ.get("ADMINS", "1416433622"))
DB_URI = environ.get("DB_URI", "mongodb+srv://Ovesh:ovesh.boss@ovesh.95jpp8g.mongodb.net/?retryWrites=true&w=majority&appName=Ovesh")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
