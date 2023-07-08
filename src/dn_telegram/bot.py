from origamibot import OrigamiBot as Bot

from src.db import get_new_news, set_published
from src.translate import translate
from src.settings import settings


if __name__ == "__main__":
    API_TOKEN = settings.API_TOKEN
    CHAT_ID = settings.CHAT_ID
    bot = Bot(API_TOKEN)
    news = get_new_news()
    for news_item in news:
        title_original = news_item["title"]
        title_en = f"*{translate(title_original)}*\n\n"
        title_original = f"*{title_original}*\n\n"
        description_original = news_item["description"] + "\n\n"
        description = f"{translate(description_original)}\n\n\n"
        link_to_translation = f"htts://translate.google.com/translate?js=n&sl=auto&tl=en&u={news_item['link']}"

        message = title_en + description + title_original + description_original + f"{news_item['publish_date']}\n" + news_item["link"]
        bot.send_message(CHAT_ID, message, parse_mode="Markdown")
        set_published([news_item])
