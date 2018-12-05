import random
import time
from datetime import datetime

import schedule
from flask import Flask

import bot

app = Flask(__name__)


@app.route("/")
def index():
    schedule.every().day.at("7:00").do(exe())
    while True:
        schedule.run_pending()
        time.sleep(86400)

    return "OK"


@app.route("/search")
def search_exe():
    bot.search(f"python until:{datetime.today().year-1}-{datetime.today().month}-{datetime.today().day} lang:ja")

    return "OK"


def exe():
    bot.tweet_select()
    tweet_time = 57600 / len(bot.day_tweets)
    index = 0

    while True:
        now = datetime.now()
        if 7 <= now.hour <= 23:
            shift_time = random.randint(1, 300)
            print(f"次のツイートまで {tweet_time - shift_time}秒")
            time.sleep(tweet_time - shift_time)
            bot.tweet(index)
            time.sleep(7)
            index += 1


        else:
            bot.day_tweets.clear()
            bot.search(
                f"python until:{datetime.today().year-1}-{datetime.today().month}-{datetime.today().day} lang:ja")
            break


if __name__ == "__main__":
    app.run(debug=True)
