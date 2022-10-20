import os

from dotenv import load_dotenv

load_dotenv()

YOUTUBE_DATA_API_URL = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_DATA_API_KEY = os.getenv("YOUTUBE_DATA_API_KEY")
YOUTUBE_CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")
