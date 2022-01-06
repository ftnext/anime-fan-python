collect:
	# TODO: source .env for ${ainouta_movie_id}
	# Collect tweets by official account
	python collect_tweets.py ${ainouta_movie_id} outputs/tweets.jsonl

download:
	python download_tweet_images.py outputs/tweets.jsonl outputs/images

pilgrimage:
	python open_images.py outputs/images/
