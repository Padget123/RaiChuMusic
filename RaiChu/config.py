## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Alisha Music")
API_ID = int(getenv("API_ID", "7479775"))
API_HASH = getenv("API_HASH", "02a267a070d8540844a2680fda3bcc38")
OWNER_NAME = getenv("OWNER_NAME", "Abhimanyu Singh Ranawat")
ALIVE_NAME = getenv("ALIVE_NAME", "Alisha")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Queen_Alisha")
BOT_USERNAME = getenv("BOT_USERNAME", "QueenAlisha_Robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Queen Alisha")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FriendshipWorldGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Sad_shayari_lovers")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5745099463").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
