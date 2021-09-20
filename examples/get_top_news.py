import cgtnfeed

top_news = cgtnfeed.get_top_news()

for news in top_news:
    print(news['title'])
