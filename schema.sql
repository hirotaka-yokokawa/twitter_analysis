DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
  id       INTEGER PRIMARY KEY,
  USER     TEXT,
  text     TEXT,
  likes    INTEGER,
  retweets INTEGER,
  url      TEXT
);