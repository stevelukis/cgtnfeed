from bs4 import BeautifulSoup
import requests


def get_top_news():
    url = "https://www.cgtn.com/"

    response = requests.get(url)
    response_text = response.text

    soup = BeautifulSoup(response_text, 'html.parser')

    top_news_parents = soup.find_all(attrs={'class': 'top-news-item-content'})

    news_list = []
    for parent in top_news_parents:
        news_anchor = parent.find('a')
        news_title = news_anchor.text.strip()

        news_time_span = parent.find('span', attrs={'class': 'publishTime'})
        news_time = news_time_span.text.strip()

        category_span = parent.find('span', attrs={'class': 'property'})
        category = category_span.text.strip()

        news = {
            'title': news_title,
            'time': news_time,
            'category': category,
        }

        news_list.append(news)

    return news_list
