from base64 import b64encode
from pathlib import Path

import requests
from requests_oauthlib import OAuth1Session

import env


def get_is_youtube_livenow() -> bool:
    res = requests.get(
        env.YOUTUBE_DATA_API_URL,
        params={
            "key": env.YOUTUBE_DATA_API_KEY,
            "channelId": env.YOUTUBE_CHANNEL_ID,
            "part": "snippet",
            "type": "video",
            "eventType": "live",
        },
    )
    data = res.json()
    is_youtube_livenow = data["pageInfo"]["totalResults"] > 0
    return is_youtube_livenow


def change_twitter_clock_icon(clock_icon_path: Path):
    twitter = OAuth1Session(
        env.TWITTER_CONSUMER_KEY,
        env.TWITTER_CONSUMER_SECLET,
        env.TWITTER_ACCESS_TOKEN,
        env.TWITTER_ACCESS_TOKEN_SECLET,
    )

    with open(clock_icon_path, "rb") as icon_bytes:
        icon_data = b64encode(icon_bytes.read())

    res = twitter.post(
        env.TWITTER_ICON_API_URL,
        data={
            "image": icon_data,
        },
    )
    print(res.text)
