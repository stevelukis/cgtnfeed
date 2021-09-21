# cgtnfeed

A python package which collects information from CGTN (China Global TV Network)

## Background

CGTN is a international media from China. Their website is very slow. It is probably because the servers are in China,
there are a lot of animations on their website, and the size of the image is very large.

This project is a web scrapper that will collect important information from the website so we won't need to open the
website to get informations.

Currently this project collects the titles of the top news from CGTN. In the long run, I will add more data to collect
and then make the API.

## How to use

### Top News

The function `get_top_news()` returns a list of dictionary. The dictionary currently has 
three key-value pairs.
```
Key
----
title
time
category
```
Example code:
```
import cgtnfeed

top_news = cgtnfeed.get_top_news()

for news in top_news:
    print(news['title'])
```
This will print something like this:
```
Xi Jinping to attend UNGA General Debate via video link
Beijing hails 'advancement in quality of democracy' in Hong Kong
China launches Tianzhou-3 cargo spacecraft for space station mission
Chinese ambassador: U.S.-UK-Australia pact 'extremely irresponsible'
U.S. launches mass expulsion of Haitian migrants from Texas
```