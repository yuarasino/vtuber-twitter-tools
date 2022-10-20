import requests

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
