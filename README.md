# Swedish news aggregator with translation to English


Hi! I live in Sweden and I don't know Swedish right now. Sweds say that dn.se is he top news resource to get news about
Sweden. Too bad that it's in Swedish only.

Fortunately, I know python! And DN has rss feed, so I don't need to parse their website. Yay!

This is a shity code, but I will try to make it better over time. We will see..

# Usage

Right now, this tool is based on cron, MongoDB and two scripts. So if you want to set this tool for yourself you need:

1. An instance of MongoDB running on a localhost;
2. cron working;
3. python 3.10.

Then:

```bash
$ git clone git@github.com:churnikov/se-news-bot.git
$ cd se-news-bot
$ vitrualenv venv
$ source venv/bin/activate
$ pip install .
```

Then create main.sh script like this:

```bash
/absolute/path/to/project/dn-telegram/venv/bin/python /absolute/path/to/project/dn-telegram/src/dnt_etl/pipeline.py && /absolute/path/to/project/dn-telegram/venv/bin/python /absolute/path/to/project/dn-telegram/src/dn_telegram/bot.py
```

Then create cron job:

```bash
$ crontab -e
```

Inside add the following. It will make you machine run scripts once per hour.

```bash
0 * * * * sh /absolute/path/to/project/dn-telegram/main.sh
```

# Ideas for the future

- [ ] Tests!
- [ ] Make code more generic and actually production ready. Localhost db is shit.
- [ ] Add web interface for collected news (need to check if it's even legal.
- [ ] Check that we do right now legal
- [ ] Make a general Telegram bot with possibility to add any RSS feed translate to any available language! Bold, I know.
- [ ] I'm too lazy to even add a code formatters. Shame on me.
