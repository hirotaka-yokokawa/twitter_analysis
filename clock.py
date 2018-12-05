import time

# from apscheduler.schedulers.blocking import BlockingScheduler
import schedule

# from datetime import datetime
import bot


def main():
    schedule.every().day.at("7:00").do(bot.exe())
    while True:
        schedule.run_pending()
        time.sleep(86400)


if __name__ == "__main__":
    main()
