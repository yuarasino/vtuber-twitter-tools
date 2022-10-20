import api
import icon


def main():
    icon.make_twitter_clock_icons()
    is_livenow = api.get_is_youtube_livenow()
    clock_icon_path = icon.get_twitter_clock_icon_path(is_livenow)
    api.change_twitter_clock_icon(clock_icon_path)


if __name__ == "__main__":
    main()
