import re
import tweepy

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAAT%2FyAEAAAAAHq%2B4KlyYQ6HnZy2fjk%2FQltT9hyg%3D495TgPFoRCTawnjwrp9ZMNXX5TFJ1eogkdXx4c6rIUGgTI01KD"
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def extract_tweet_id(url):
    match = re.search(r"status/(\d+)", url)
    return match.group(1) if match else None

def get_tweet_comments(tweet_id, max_results=100):
    try:
        query = f"conversation_id:{tweet_id}"
        all_comments = []
        next_token = None

        while True:
            response = client.search_recent_tweets(
                query=query,
                tweet_fields=['author_id', 'conversation_id', 'text'],
                max_results=max_results,
                next_token=next_token
            )
            if response.data:
                all_comments.extend([{'username': tweet.author_id, 'text': tweet.text} for tweet in response.data])

            next_token = response.meta.get('next_token') if 'meta' in response else None
            if not next_token:
                break

        return all_comments
    except Exception as e:
        print(f"Error: {e}")
        return []
