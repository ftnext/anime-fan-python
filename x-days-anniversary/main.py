from datetime import date

from sparkling_counter import XthDayCount

AINOUTA_DAY = date(2021, 10, 29)


if __name__ == "__main__":
    count = XthDayCount(AINOUTA_DAY)
    print(f"『アイの歌声を聴かせて』公開から{count(date.today())}日目です")
