import json
from urllib.request import urlopen

from getgauge.python import step


@step("さかなー すると ちんあなごー を返す")
def assert_chisato():
    with urlopen("http://127.0.0.1:8000/sakana") as res:
        response = json.load(res)

    assert response == "ちんあなごー🙌"
