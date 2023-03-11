import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5938646919:AAFzCjHEpm9DTXUJ9KNvNME1LPCxGw7xQtQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzgBuzinVLBeejAMbsYeeB2qux9CMuerrMCKi3JlFjqphOTDVVnmHa2UHTO17272MYAW7tb5js1jAu1Imaj_cjGvt499KE8zgmK1oS8VD_SRxNuqmMW6MgrZmu0ZzBT9EVzoScy-JiGTNNgDkAJ1nB-CvGaDf1NYg12-VnMOlhHSO7-s1NwGQn_vVpdLUdTANukBkuSNiYt-i2yC-Vb3Xe3l9Ogo6gwsH5J_ME0rDvNCHA4dKiLHyRUnb_gaPeRmLH9y-8oMe8hWD9TxnXNCCHjK6Ye3dUlJVI-XCj_ccSGNxrrdMbfMoSxf9GXqZR9B2UtBlukUNJuFNk3GcX0Sj1AdfrE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "DarlzzzMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "darlzzzbots") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Darlzzzbots") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/33596565517cf29b8e079.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5909442665")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
