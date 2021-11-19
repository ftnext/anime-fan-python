from datetime import date, timedelta

AINOUTA_DAY = date(2021, 10, 29)


def calculate_passed_timedelta(the_day: date) -> timedelta:
    return date.today() - the_day


def passed_days(td: timedelta) -> int:
    return td.days + 1


if __name__ == "__main__":
    passed_td = calculate_passed_timedelta(AINOUTA_DAY)
    print(f"『アイの歌声を聴かせて』公開から{passed_days(passed_td)}日目です")
