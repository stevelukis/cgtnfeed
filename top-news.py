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

title_parents = soup.find_all(attrs={'class': 'top-news-item-content-title'})

for tp in title_parents:
    title_anchor = tp.find('a')
    print(title_anchor.text.strip())
    print('---------')
