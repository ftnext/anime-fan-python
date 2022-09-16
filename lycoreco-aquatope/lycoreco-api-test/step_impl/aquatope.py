import json
import os
from urllib.request import urljoin, urlopen

from getgauge.python import data_store, step

BASE_URL = os.getenv("API_ENDPOINT")


def call_api(path):
    with urlopen(urljoin(BASE_URL, path)) as res:
        return json.load(res)


@step("さかなー🐟")
def do_fish():
    response = call_api("sakana")
    data_store.suite["sakana"] = response


@step("ちんあなごー🙌 が返ること")
def assert_chisato():
    assert data_store.suite.sakana == "ちんあなごー🙌"


@step("ちんあなごー🙌")
def do_chinanago():
    response = call_api("chinanago")
    data_store.suite.chinanago = response


@step("さかなー🐟 が返ること")
def assert_takina():
    assert data_store.suite["chinanago"] == "さかなー🐟"
