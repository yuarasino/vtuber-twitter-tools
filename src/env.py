import os

from dotenv import load_dotenv

load_dotenv()

YOUTUBE_DATA_API_URL = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_DATA_API_KEY = os.getenv("YOUTUBE_DATA_API_KEY")
YOUTUBE_CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")

TWITTER_ICON_API_URL = "https://api.twitter.com/1.1/account/update_profile_image.json"
TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECLET = os.getenv("TWITTER_CONSUMER_SECLET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECLET = os.getenv("TWITTER_ACCESS_TOKEN_SECLET")
