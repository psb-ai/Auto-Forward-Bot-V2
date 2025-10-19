from os import environ 

class Config:
    API_ID = environ.get("API_ID", "577678")
    API_HASH = environ.get("API_HASH", "d2c6e01uuiuiouioiuiou0fc6d7a1be")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8432860625:AAFncKCECyJ-zv4_tQcWuc5c-aUgUXQ2TQU") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://philostwo02_db_user:4aQt6W8dSW6ZSgd0@cluster0.noaxhdm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1003017522').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
