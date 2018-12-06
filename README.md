# twitter analysis bot
ツイッターの過去のツイートを検索・スクレイプして自動で定期的にツイートするボットです。

## はじめに
このプロダクトはselenium,twitterscraperのサードパーティを使用しています。よって、それらのライブラリの開発者に感謝いたします。<br>
9時から24時の間で20~30ツイート、ランダムで行います。

## 使いかた
 tweets.sqliteには初期設定ではデータが入っていないので、実行する際は先にbot.pyでsearch関数を実行してツイートを保存しておいてください。
 - clock.pyの10行目の検索内容を決定(一日の終りに一年前のツイートを検索して取得します)
 - bot.pyの11行目にtwitterのユーザー名、12行目にパスワードを入力
 - 実行用プログラムはclock.pyです。
 
## デプロイ方法
herokuをデプロイ先として説明します。先にheroku上にプロジェクトを作成しましょう。
```
heroku login
heroku create プロジェクト名
heroku git:remote --app プロジェクト名
```
seleniumを使用するため、環境設定をする必要があります。今回はchromeをドライバーとして使います。<br>
まず、ターミナル上でデプロイ先に移動しておく。以下のコマンドを実行。(chromeの環境を設定)
```
heroku buildpacks:set https://github.com/heroku/heroku-buildpack-chromedriver.git
heroku buildpacks:set https://github.com/heroku/heroku-buildpack-google-chrome.git
heroku config:set CHROME_DRIVER_PATH=chromedriver
heroku config:set CHROME_BINARY_LOCATION=/app/.apt/usr/bin/google-chrome
```
herokuのサイト上のセッティングでも追加することは可能です。<br>
設定してもpushしていないと使用できないので設定後にpushしましょう。

以上を設定したらデプロイしましょう。
```
git add .
git commit -m "commit message"
git push heroku master
```
これでデプロイ完了です。
