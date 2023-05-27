from rss_parser import Parser
from requests import get, post

from src.dnt_etl.extract import download_rss
from src.dnt_etl.transform import feed_to_dict
from src.dnt_etl.load import insert_new_news

if __name__ == "__main__":
    sthlm_url = "https://www.dn.se/sthlm/m/rss/"
    feed = download_rss(sthlm_url)
    news = feed_to_dict(feed)
    insert_new_news(news)

