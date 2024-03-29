import argparse
import asyncio
import logging
import random
import time
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

import aiofiles
import httpx
import jsonlines
from more_itertools import chunked

logging.basicConfig(level=logging.INFO)


def tweet_iterator(tweets_jsonl_path):
    with jsonlines.open(tweets_jsonl_path) as reader:
        yield from reader


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


async def download_async(client, src_url, dest_path):
    await asyncio.sleep(random.random())
    response = await client.get(src_url)
    logging.info("Downloaded %s", src_url)
    await save_image_async(dest_path, response.content)


async def save_image_async(dest_path, content):
    async with aiofiles.open(dest_path, "wb") as fb:
        await fb.write(content)


async def download_images_async(tweets, output_root):
    chunk_size = 10
    async with httpx.AsyncClient() as client:
        for tweet_chunk in chunked(tweets, chunk_size):
            download_coroutines = []
            for tweet in tweet_chunk:
                if "attachments" not in tweet:
                    continue
                for attachment in tweet["attachments"]:
                    src_url = attachment["url"]
                    dest_path = output_root / build_image_path(src_url)
                    download_coroutines.append(
                        download_async(client, src_url, dest_path)
                    )
            _ = await asyncio.gather(
                *download_coroutines, return_exceptions=True
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tweets_jsonl")
    parser.add_argument("output_root", type=Path)
    parser.add_argument("--async_mode", action="store_true")
    args = parser.parse_args()

    args.output_root.mkdir(exist_ok=True, parents=True)

    if args.async_mode:
        asyncio.run(
            download_images_async(
                tweet_iterator(args.tweets_jsonl), args.output_root
            )
        )
    else:
        for tweet in tweet_iterator(args.tweets_jsonl):
            if "attachments" not in tweet:
                continue
            for attachment in tweet["attachments"]:
                src_url = attachment["url"]
                dest_path = args.output_root / build_image_path(src_url)
                download_image(src_url, dest_path)
                logging.info("Downloaded %s", src_url)
                time.sleep(random.random())
