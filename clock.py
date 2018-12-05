import time

# from apscheduler.schedulers.blocking import BlockingScheduler
import schedule

import bot


def main():
    schedule.every().day.at("7:00").do(job_func=bot.exe())
    while True:
        schedule.run_pending()
        time.sleep(86400)


if __name__ == "__main__":
    main()
