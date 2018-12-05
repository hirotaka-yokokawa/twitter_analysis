import random
import sqlite3
import time
from datetime import datetime

import twitterscraper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

day_tweets = []


def init_db():
    conn = sqlite3.connect("tweets.sqlite")
    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        sql = f.read()

    cursor.executescript(sql)

    conn.commit()
    conn.close()


def search(query):
    now_day = datetime.today().day
    counter = 1
    conn = sqlite3.connect("tweets.sqlite")
    cursor = conn.cursor()

    sql = "INSERT INTO tweets (user,text,likes,retweets,url) VALUES (?,?,?,?,?)"

    for result in twitterscraper.query.query_tweets_once_generator(query=query, limit=1, lang="ja"):
        if result[0].timestamp.day == now_day - 1:
            cursor.execute(sql, (result[0].user, result[0].text, int(result[0].likes), int(result[0].retweets),
                             "https://twitter.com" + str(result[0].url)))
        counter += 1

    conn.commit()
    conn.close()


def tweet_select():
    global day_tweets
    tweet_num = random.randint(20, 31)
    conn = sqlite3.connect("tweets.sqlite")
    cursor = conn.cursor()

    sql = "SELECT * FROM tweets"

    result = cursor.execute(sql).fetchall()

    conn.commit()
    conn.close()
    results = []

    for a in result:
        results.append(a[2])

    print(len(results))
    print(tweet_num)
    day_tweets = random.sample(results, tweet_num)

    # for num in range(tweet_num):


def tweet(index):
    driver = webdriver.Firefox(executable_path="/Users/kudouhibiki/PycharmProjectst/twitter_analysis/geckodriver")
    driver.get("https://twitter.com/")
    driver.find_element_by_name("session[username_or_email]").send_keys("hibikikkk_9712")
    time.sleep(2)
    driver.find_element_by_name("session[password]").send_keys("Kudo9712")
    driver.find_element_by_name("session[password]").send_keys(Keys.ENTER)

    time.sleep(3)
    driver.find_element_by_name("tweet").send_keys(day_tweets[index])
    time.sleep(10)
    driver.find_element_by_xpath('//span[@class="button-text tweeting-text"]').click()
    time.sleep(1)

    driver.close()


def exe():
    tweet_select()
    tweet_time = 57600 / len(day_tweets)
    index = 0

    while True:
        now = datetime.now()
        if 7 <= now.hour <= 23:
            shift_time = random.randint(1, 300)
            print(f"次のツイートまで {tweet_time - shift_time}秒")
            time.sleep(tweet_time - shift_time)
            tweet(index)
            time.sleep(7)
            index += 1


        else:
            day_tweets.clear()
            search(
                f"python until:{datetime.today().year-1}-{datetime.today().month}-{datetime.today().day} lang:ja")
            break



if __name__ == "__main__":
    # init_db()
    print(
        f"python min_retweets:50 until:{datetime.today().year-1}-{datetime.today().month}-{datetime.today().day} lang:ja")
    search(f"python lang:ja")
    # tweet_select()
    # tweet()

    #
    # while  :
    #     datetime.datetime.now()
    #     if now.strftime("%H:%M:%S") == "08:00:00":
    #         driver.find_element_by_name("tweet").send_keys("おはよう")
    #         driver.find_element_by_xpath('//span[@class="button-text tweeting-text"]').click()
    #     if now.strftime("%H:%M:%S") == "12:00:00":
    #         driver.find_element_by_name("tweet").send_keys("こんにちは")
    #         driver.find_element_by_xpath('//span[@class="button-text tweeting-text"]').click()
    #     if now.strftime("%H:%M:%S") == "20:00:00":
    #         driver.find_element_by_name("tweet").send_keys("こんばんは")
    #         driver.find_element_by_xpath('//span[@class="button-text tweeting-text"]').click()
    #     if now.strftime("%H:%M:%S") == "22:00:00":
    #         driver.find_element_by_name("tweet").send_keys("おやすみ")
    #         driver.find_element_by_xpath('//span[@class="button-text tweeting-text"]').click()
