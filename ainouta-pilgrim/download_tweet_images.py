import argparse
import logging
import time
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

import jsonlines

logging.basicConfig(level=logging.INFO)


def tweet_iterator(tweets_jsonl_path):
    with jsonlines.open(tweets_jsonl_path) as reader:
        for tweet in reader:
            yield tweet


def build_image_path(url):
    """
    >>> build_image_path("https://example.com/images/egg.jpg")
    'egg.jpg'
    """
    parsed = urlparse(url)
    _, image_path = parsed.path.rsplit("/", 1)
    return image_path


def download_image(src_url, dest_path):
    with urlopen(src_url) as res, open(dest_path, "wb") as fb:
        fb.write(res.read())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tweets_jsonl")
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args()

    args.output_root.mkdir(exist_ok=True, parents=True)

    for tweet in tweet_iterator(args.tweets_jsonl):
        if "attachments" not in tweet:
            continue
        for attachment in tweet["attachments"]:
            src_url = attachment["url"]
            dest_path = args.output_root / build_image_path(src_url)
            download_image(src_url, dest_path)
            logging.info("Downloaded %s", src_url)
            time.sleep(1)  # randomにして負荷をより減らせる
