# Print out feed meta data
print(feed.language)
print(feed.version)


# Iteratively print feed items
for item in feed.feed:
    print("-----")
    print(item.title)
    print(f"pub_date: {item.publish_date} en: ", translate(item.title))
    print(item.description)
    print(item)


