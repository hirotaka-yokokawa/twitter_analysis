#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import threading
import time
from datetime import datetime

import bot

query = ""


def main():
    """実行用関数"""
    bot.tweet_select()
    tweet_time = 57600 / len(bot.day_tweets)
    index = 0

    while True:
        now_morning = datetime.now().hour
        print(f"{now_morning}時です")
        if 0 <= now_morning <= 15:
            shift_time = random.randint(1, 300)
            print(f"次のツイートまで {tweet_time - shift_time}秒")
            time.sleep(tweet_time - shift_time)
            bot.tweet(index)
            index += 1

        else:
            bot.day_tweets.clear()
            bot.tweet(999)
            print("今日も終了です")
            bot.search(query)
            break


def timer():
    now = datetime.now()
    now = now.hour * 3600 + now.minute * 60 + now.second
    print(now)
    while now <= 54000:
        time.sleep(1)
        now += 1


if __name__ == "__main__":
    threading_main = threading.Thread(target=main)
    while True:
        threading_main.start()
        timer()
        threading_main.join()
        print("今日は終了中です")
        time.sleep(32400)
