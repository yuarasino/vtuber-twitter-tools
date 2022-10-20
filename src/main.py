import api
import icon


def main():
    icon.make_twitter_clock_icons()
    is_livenow = api.get_is_youtube_livenow()
    clock_icon_path_now = icon.get_twitter_clock_icon_path_now(is_livenow)
    print(clock_icon_path_now)


if __name__ == "__main__":
    main()
