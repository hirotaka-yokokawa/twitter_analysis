import random
import threading
import time
from datetime import datetime

# from apscheduler.schedulers.blocking import BlockingScheduler
# import schedule
import bot


def main():
    """実行用関数"""
    bot.tweet_select()
    tweet_time = 57600 / len(bot.day_tweets)
    index = 0

    while True:
        now_morning = datetime.now().hour
        # try:
        if 7 <= now_morning <= 23:
            shift_time = random.randint(1, 300)
            print(f"次のツイートまで {tweet_time - shift_time}秒")
            time.sleep(tweet_time - shift_time)
            bot.tweet(index)
            index += 1

        else:
            bot.day_tweets.clear()
            print("今日も終了です")
            bot.search(
                f"python until:{datetime.today().year-1}-{datetime.today().month}-{datetime.today().day} lang:ja")
            break
    # except:
    #     bot.day_tweets.clear()
    #     bot.search(
    #         f"python until:{datetime.today().year-1}-{datetime.today().month}-{datetime.today().day} lang:ja")
    #     break


def timer():
    now = datetime.now()
    now = now.hour * 3600 + now.minute * 60 + now.second
    print(now)
    while now <= 82800:
        time.sleep(1)
        now += 1


if __name__ == "__main__":
    threading_main = threading.Thread(target=main)
    while True:
        threading_main.start()
        timer()
        threading_main.join()
        time.sleep(28800)
