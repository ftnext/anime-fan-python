import argparse
import time
from pathlib import Path
from webbrowser import open_new_tab

import schedule


def alarm_job_executed_once():
    open_new_tab(f"file://{Path.cwd() / 'autoplay.html'}")
    return schedule.CancelJob


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("minutes", type=int)
    args = parser.parse_args()

    schedule.every(args.minutes).minutes.do(alarm_job_executed_once)

    while True:
        schedule.run_pending()
        time.sleep(1)
