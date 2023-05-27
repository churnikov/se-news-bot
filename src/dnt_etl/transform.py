from rss_parser.models import RSSFeed


def feed_to_dict(feed: RSSFeed) -> bool:
    news = []
    for item in feed.feed:
        news.append(item.dict(include={"title", "link", "publish_date", "description"})
                    )
    return news
