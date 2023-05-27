from pymongo import MongoClient


client = MongoClient()
db = client.news_db
news_collection = db.news_collection


def get_new_news():
    return news_collection.find({"published": None})


def set_published(news):
    for news_item in news:
        news_collection.update_one({"title": news_item["title"]}, {"$set": {"published": True}})

