import os


class Config:
    def __init__(self):
        self.tg_token = os.getenv("TELEGRAM_TOKEN")
        self.nasa_key = os.getenv("NASA_KEY")
