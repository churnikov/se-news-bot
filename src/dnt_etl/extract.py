from rss_parser import Parser
from rss_parser.models import RSSFeed
from requests import get, post
from loguru import logger


def download_rss(rss_url: str) -> RSSFeed:
    logger.info(f"downloading: {rss_url}")
    xml = get(rss_url)
    xml.raise_for_status()

    # Limit feed output to 5 items
    # To disable limit simply do not provide the argument or use None
    parser = Parser(xml=xml.content, limit=10)
    feed = parser.parse()

    return feed

