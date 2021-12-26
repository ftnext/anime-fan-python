import argparse
import json
import logging
import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import jsonlines

logging.basicConfig(level=logging.INFO)


def fetch_tweets(user_id, bearer_token, /, max_results=100):
    timeline_endpoint = f"https://api.twitter.com/2/users/{user_id}/tweets"

    query_parameters = {
        "tweet.fields": "created_at",
        "exclude": "retweets",
        "max_results": max_results,
        # media (photo) のURLを取得するための指定
        "expansions": "attachments.media_keys",
        "media.fields": "media_key,type,url",
    }
    url = f"{timeline_endpoint}?{urlencode(query_parameters)}"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    request = Request(url, headers=headers, method="GET")

    with urlopen(request) as raw_response:
        return json.loads(raw_response.read())


def tidy_attachments_of_tweets(response):
    media_map = {
        media["media_key"]: media["url"]
        for media in response["includes"]["media"]
        if media["type"] == "photo"
    }
    for datum in response["data"]:
        if not (attachments := datum.pop("attachments", None)):
            continue
        photos = [
            {"media_key": key, "url": media_map[key]}
            for key in attachments["media_keys"]
            if key in media_map
        ]
        datum["attachments"] = photos
    return response["data"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user_id")
    parser.add_argument("output_jsonl")
    parser.add_argument("--max_results", type=int, default=100)
    args = parser.parse_args()

    bearer_token = os.getenv("BEARER_TOKEN")
    assert bearer_token, "Set environment variable `BEARER_TOKEN`"

    response = fetch_tweets(
        args.user_id, bearer_token, max_results=args.max_results
    )
    logging.info("Fetched %d tweets", response["meta"]["result_count"])

    tweets = tidy_attachments_of_tweets(response)
    with jsonlines.open(args.output_jsonl, "w") as writer:
        writer.write_all(tweets)
