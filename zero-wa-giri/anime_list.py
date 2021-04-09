import re
from datetime import date
from operator import itemgetter
from pathlib import Path
from typing import Optional
from urllib.request import urlopen

from bs4 import BeautifulSoup


def extract_latest_date(schedule: str) -> Optional[date]:
    """放送スケジュールを表す想定の文字列から、最新の日付を取り出す。

    >>> extract_latest_date("2021年4月6日（火）～テレビ東京ほか")
    datetime.date(2021, 4, 6)
    >>> extract_latest_date("2021年春～")
    >>> s = "\\n【本放送】2020年10月3日（土）～TOKYO MXほか【再放送】2021年4月11日（日）～NHK Eテレ\\n"
    >>> extract_latest_date(s)
    datetime.date(2021, 4, 11)
    """
    # TODO: dateutil を使うともっと簡単かも
    dates = []
    matches = re.finditer(r"(\d{4})年(\d{1,2})月(\d{1,2})日", schedule)
    for m in matches:
        schedule_date = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        dates.append(schedule_date)
    if not dates:
        return None
    if len(dates) == 1:
        return dates[0]
    # 複数見つかった場合は最新の日付を返す（再放送のケース）
    return sorted(dates, reverse=True)[0]


if __name__ == "__main__":
    PAGE_URL = "https://www.animatetimes.com/tag/details.php?id=5228"
    cache_dir = Path(".cache")
    if not cache_dir.exists():
        cache_dir.mkdir(exist_ok=True)

    html_cache = cache_dir / "animatetimes.html"
    if not html_cache.exists():
        with urlopen(PAGE_URL) as res:
            raw_html = res.read().decode("utf-8")
        with html_cache.open("w", encoding="utf-8") as f:
            f.write(raw_html)
    else:
        with html_cache.open(encoding="utf-8") as f:
            raw_html = f.read()

    soup = BeautifulSoup(raw_html, "html.parser")
    section = soup.section

    # 各アニメのタイトルには、目次から移動できるようにid属性が指定されている
    titles = [h2 for h2 in section.find_all("h2") if h2.has_attr("id")]
    # h2とtable（と他のタグ）の組で、1つのアニメの情報を表している
    tables = section.find_all("table")

    assert len(titles) == len(tables)

    schedules: list[str] = []
    for table in tables:
        for tr in table.find_all("tr"):
            if tr.td.get_text().endswith("スケジュール"):  # {放送,配信}スケジュール
                schedules.append(tr.th.get_text().strip())
                break

    assert len(titles) == len(schedules)

    # scheduleの降順にしたい。dateでないものもある
    known_date_schedules, unknown_date_schedules = [], []
    for i, schedule in enumerate(schedules):
        if start_date := extract_latest_date(schedule):
            known_date_schedules.append((i, start_date))
        else:
            unknown_date_schedules.append((i, schedule))

    get_date = itemgetter(1)
    whole_schedules = sorted(known_date_schedules, key=get_date)
    whole_schedules.extend(unknown_date_schedules)
    for i, start_date in whole_schedules:
        print(titles[i].get_text())
        print(f"{PAGE_URL}#{titles[i].get_attribute_list('id')[0]}")
        print(schedules[i])
        print()
