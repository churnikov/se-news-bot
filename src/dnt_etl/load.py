from typing import List

from loguru import logger

from ..db import news_collection


def insert_new_news(news: List[dict]) -> None:
    new_titles = [news_item["title"] for news_item in news]
    inserted = 0
    for title, news_item in zip(new_titles, news):
        logger.trace(news_item)
        up_result = news_collection.update_one({"title": title}, {"$setOnInsert": news_item}, upsert=True)
        inserted += up_result.modified_count
        if up_result.modified_count:
            logger.debug(f"added to the database {title}")
    logger.debug(f"Added {inserted} news to the database")
    return inserted

