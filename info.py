# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6139759254"))
API_ID = int(getenv("API_ID", "23631217"))
API_HASH = str(getenv("API_HASH", "567c6df308dc6901790309499f729d12"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://mrnoffice692:PsO4VGHI9heKd7WA@cluster0.e7vboom.mongodb.net/?appName=Cluster0",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='telegram.me/Mrn_Officialx'>{file_name} Telegram : @Mrn_Officialx\n\nForward the file before Downloading.</a></b>",
    )
)

