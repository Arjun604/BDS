#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27962072"))
API_HASH = environ.get("API_HASH", "a37e33a05ec3b9321751dec49fdb9829")
BOT_TOKEN = environ.get("BOT_TOKEN", "8330680357:AAEzrxSqqfBDkp3A9Uew-kmA-BIkmX-VdPc")

OWNER = int(environ.get("OWNER", "787410221"))
CREDIT = environ.get("CREDIT", "MEDIC 𝘽𝙊𝙏𝙎")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5680454765').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

