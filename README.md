# twitter analysis bot
ツイッターの過去のツイートを検索・スクレイプして自動で定期的にツイートするボットです。

## はじめに
このプロダクトはselenium,twitterscraperのサードパーティを使用しています。よって、それらのライブラリの開発者に感謝いたします。<br>
このボットでは7時から22時の間で20~30ツイート、ランダムで行います。起動時間街になったら自動的に一年前の同日のツイートを検索してスクレイプしてくれます。

## 使いかた
 tweets.sqliteには初期設定ではデータが入っていないので、実行する際は先にbot.pyでsearch関数を実行してツイートを保存しておいてください。
 - clock.pyの10行目の検索内容を決定(一日の終りに一年前のツイートを検索して取得します)
 - bot.pyの11行目にtwitterのユーザー名、12行目にパスワードを入力
 - bot.pyの13行目のpass_emailでは乗っ取り対策として、登録していたメールアドレスか電話番号を入力してください
 - 実行用プログラムはclock.pyです。
 
## デプロイ方法
herokuをデプロイ先として説明します。まず先に、heroku上にプロジェクトを作成しましょう。
```
heroku login
heroku create プロジェクト名
heroku git:remote --app プロジェクト名
```
seleniumを使用するので、環境設定をする必要があります。今回はchromeをウェブドライバーとして使います。<br>
ターミナル上でherokuのプロジェクトがある階層に移動しておきましょう。以下のコマンドを実行して、chromeの環境を設定します。
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
