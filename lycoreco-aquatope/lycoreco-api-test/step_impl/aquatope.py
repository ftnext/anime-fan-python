import json
import os
from urllib.request import urljoin, urlopen

from getgauge.python import data_store, step

BASE_URL = os.getenv("API_ENDPOINT")


@step("さかなー🐟")
def do_fish():
    with urlopen(urljoin(BASE_URL, "sakana")) as res:
        response = json.load(res)
    data_store.suite["sakana"] = response


@step("ちんあなごー🙌 が返ること")
def assert_chisato():
    assert data_store.suite.sakana == "ちんあなごー🙌"


@step("ちんあなごー すると さかなー を返す")
def assert_takina():
    with urlopen(urljoin(BASE_URL, "chinanago")) as res:
        response = json.load(res)

    assert response == "さかなー🐟"
