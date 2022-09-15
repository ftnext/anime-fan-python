import json
import os
from urllib.request import urljoin, urlopen

from getgauge.python import step

BASE_URL = os.getenv("API_ENDPOINT")


@step("さかなー すると ちんあなごー を返す")
def assert_chisato():
    with urlopen(urljoin(BASE_URL, "sakana")) as res:
        response = json.load(res)

    assert response == "ちんあなごー🙌"


@step("ちんあなごー すると さかなー を返す")
def assert_takina():
    with urlopen(urljoin(BASE_URL, "chinanago")) as res:
        response = json.load(res)

    assert response == "さかなー🐟"
