from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from PIL import Image

images_dir = Path(__file__).parent / "images"
icon_path = images_dir / "icon.png"
frame_path = images_dir / "frame.png"
clock_dir_default = images_dir / "default"
clock_dir_livenow = images_dir / "livenow"


def make_twitter_clock_icons():
    if not clock_dir_default.exists():
        clock_dir_default.mkdir()
        with Image.open(icon_path) as icon:
            for i in range(12):
                clock_icon_path = clock_dir_default / f"icon_{i:02}.png"
                clock_icon = icon.rotate(-30 * i)
                clock_icon.save(clock_icon_path)

    if not clock_dir_livenow.exists():
        clock_dir_livenow.mkdir()
        with Image.open(icon_path) as icon, Image.open(frame_path) as frame:
            for hour in range(12):
                clock_icon_path = clock_dir_livenow / f"icon_{hour:02}.png"
                clock_icon = icon.rotate(-30 * hour)
                clock_icon.paste(frame, mask=frame)
                clock_icon.save(clock_icon_path)


def get_twitter_clock_icon_path(is_livenow: bool) -> Path:
    now = datetime.now(ZoneInfo("Asia/Tokyo"))
    hour = now.hour % 12
    clock_dir = clock_dir_livenow if is_livenow else clock_dir_default
    clock_icon_path = clock_dir / f"icon_{hour:02}.png"
    return clock_icon_path
