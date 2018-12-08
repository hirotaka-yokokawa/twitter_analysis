import random
import sqlite3
import time
from datetime import datetime

import twitterscraper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

user_name = ""
passward = ""
pass_email = ""

day_tweets = []

options = Options()
options.binary_location = '/app/.apt/usr/bin/google-chrome'
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=options, executable_path="chromedriver")


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


def tweet(index):
    global driver

    if index == 0:
        driver.get("https://twitter.com/")
        driver.set_window_size(1124, 1124)
        driver.execute_script("window.scrollTo(0, document.head.scrollHeight);")
        time.sleep(5)
        driver.save_screenshot("screenshot_login.png")
        driver.find_element_by_name("session[username_or_email]").send_keys(user_name)
        time.sleep(2)
        driver.find_element_by_name("session[password]").send_keys(passward)
        driver.find_element_by_name("session[password]").send_keys(Keys.ENTER)
        time.sleep(2)
        if driver.current_url != "https://twitter.com/":
            driver.find_element_by_id("challenge_response").send_keys(pass_email)
            driver.find_element_by_id("challenge_response").send_keys(Keys.ENTER)
            time.sleep(3)

        print(driver.current_url)
        driver.save_screenshot("screenshot_tweet.png")

    if index != 999:
        time.sleep(5)
        driver.find_element_by_name("tweet").send_keys(day_tweets[index])
        time.sleep(10)
        driver.find_element_by_xpath('//span[@class="button-text tweeting-text"]').click()
        time.sleep(3)

    if index == 999:
        driver.close()


if __name__ == "__main__":
    init_db()
    # tweet_select()
    # search(f"")  #例:f"python until:{datetime.today().year-2}-{datetime.today().month}-{datetime.today().day-1} lang:ja"
    # tweet_select()
    # tweet(0)

#