from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from PIL import Image

images_dir = Path(__file__).parent / "images"
icon_name_default = "icon_default"
icon_name_livenow = "icon_livenow"


def make_twitter_clock_icons():
    clock_icon_dir_default = images_dir / icon_name_default
    clock_icon_dir_livenow = images_dir / icon_name_livenow

    if not clock_icon_dir_default.exists():
        clock_icon_dir_default.mkdir()
        icon_path = images_dir / f"{icon_name_default}.png"
        with Image.open(icon_path) as icon:
            for i in range(12):
                clock_icon_path = (
                    clock_icon_dir_default / f"{icon_name_default}_{i:02}.png"
                )
                clock_icon = icon.rotate(-30 * i)
                clock_icon.save(clock_icon_path)

    if not clock_icon_dir_livenow.exists():
        clock_icon_dir_livenow.mkdir()
        icon_path = images_dir / f"{icon_name_livenow}.png"
        with Image.open(icon_path) as icon:
            for hour in range(12):
                clock_icon_path = (
                    clock_icon_dir_livenow / f"{icon_name_livenow}_{hour:02}.png"
                )
                clock_icon = icon.rotate(-30 * i)
                clock_icon.save(clock_icon_path)


def get_twitter_clock_icon_path_now(is_livenow: bool) -> Path:
    now = datetime.now(ZoneInfo("Asia/Tokyo"))
    hour = now.hour % 12
    icon_name_now = icon_name_livenow if is_livenow else icon_name_default
    clock_icon_dir_now = images_dir / icon_name_now
    clock_icon_path_now = clock_icon_dir_now / f"{icon_name_now}_{hour:02}.png"
    return clock_icon_path_now
