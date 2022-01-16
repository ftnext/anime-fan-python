import os

from helium import (
    S,
    Text,
    click,
    go_to,
    kill_browser,
    start_firefox,
    wait_until,
    write,
)


def login():
    go_to("https://www.dreampass.jp/users/sign_in")
    write(os.getenv("DREAMPASS_EMAIL"), into=S("#user_email"))
    write(os.getenv("DREAMPASS_PASSWORD"), into=S("#user_password"))
    click("ログイン")
    wait_until(Text("ようこそ").exists)


if __name__ == "__main__":
    start_firefox()

    login()

    kill_browser()
