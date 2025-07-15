import os
print("🔍 DEBUG: Available ENV keys →", list(os.environ.keys()))

import os
import random
import json
import tweepy
from datetime import datetime

# Load config
with open("config.json") as f:
    config = json.load(f)

keywords = config["keywords"]
language_mix = config["language_mix"]
tone = config.get("tone", "motivational")

# Authenticate Twitter API
client = tweepy.Client(
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_SECRET"]
)

def generate_motivational_tweet():
    topic = random.choice(keywords)
    lang = random.choices(["english", "pidgin"], weights=[
        language_mix.get("english", 0.8),
        language_mix.get("pidgin", 0.2)
    ])[0]

    emojis = ["💪", "🔥", "💯", "🚀", "🎯", "😤", "😎", "🌟", "📈", "🙏", "🧠", "💼"]

    if lang == "english":
        templates = [
            f"Stay focused on {topic}. Discipline creates freedom {random.choice(emojis)}",
            f"Your hustle around {topic} will pay off soon {random.choice(emojis)} Keep grinding!",
            f"Don't sleep on {topic}. Be consistent and patient {random.choice(emojis)}",
            f"{topic.capitalize()} is a journey. Stay on it {random.choice(emojis)}",
            f"Every day is a step toward {topic}. Let’s go! {random.choice(emojis)}"
        ]
    else:
        templates = [
            f"No dull yourself boss, {topic} na serious matter {random.choice(emojis)}",
            f"Guy, make you no give up on {topic}, your time dey come {random.choice(emojis)}",
            f"{topic.capitalize()} no easy, but we go dey push! {random.choice(emojis)}",
            f"Las las, na {topic} go make us shine. Focus! {random.choice(emojis)}",
            f"{topic}? Na steady hustle. God dey 🙏 {random.choice(emojis)}"
        ]

    return random.choice(templates)

def run_bot():
    tweet_text = generate_motivational_tweet()
    try:
        response = client.create_tweet(text=tweet_text)
        tweet_id = response.data.get("id")
        print(f"✅ Tweet posted: https://twitter.com/user/status/{tweet_id}")
    except Exception as e:
        print(f"❌ Failed to post tweet: {e}")

if __name__ == "__main__":
    now = datetime.utcnow()
    print(f"🕒 Posting tweet at: {now.isoformat()} UTC")
    run_bot()
