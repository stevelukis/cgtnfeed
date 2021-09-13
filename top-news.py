from bs4 import BeautifulSoup
import requests

url = "https://www.cgtn.com/"

# response = requests.get(url)
# response_text = response.text
# #
# with open('cgtn_home.html', 'w', encoding='utf8') as f:
#     f.write(response_text)

f = open('cgtn_home.html', 'r', encoding='utf8')
response_text = f.read()

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

    print(news_title)
    print(news_time)
    print(category)
    print('---------')
