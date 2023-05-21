import re, os
from time import time

id_pattern = re.compile(r'^.\d+$') 

BOT_START_TIME = time()

API_ID = os.environ.get("API_ID", "28643132")

API_HASH = os.environ.get("API_HASH", "510c3009ea589830a89e045bf8aae656")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5925633630:AAHePK4xeagl_XauSU0tTAgJmVwjxdPxeq4") 

FORCE_SUB = os.environ.get("FORCE_SUB", "MLZ_BOTZ") 

DB_NAME = os.environ.get("DB_NAME","MONGOO:MONGOO")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://MONGOO:MONGOO@cluster0.rh6p7y3.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/62472f793d410e849b40b.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1833209093 5845960615 5596825598 6172502825 1957296068').split()]

PORT = os.environ.get('PORT', '8080')

LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001898159090'))

