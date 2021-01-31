import feedparser
# from BeautifulSoup4 import BeautifulSoup as BSHTML
# import urllib2
from bs4 import BeautifulSoup as BSHTML
import urllib3

#economictimes RSS Feeds
url_home = 'https://economictimes.indiatimes.com/rssfeedsdefault.cms'
url_top = 'https://economictimes.indiatimes.com/rssfeedstopstories.cms'
url_stocks = 'https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms'
url_media = 'https://economictimes.indiatimes.com/multimedia/rssfeeds/68004546.cms'
url_TOI = 'https://timesofindia.indiatimes.com/rssfeedstopstories.cms'
url_recent = 'https://timesofindia.indiatimes.com/rssfeeds/1221656.cms'
url_india = 'http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms'
url_world = 'http://timesofindia.indiatimes.com/rssfeeds/296589292.cms'
url_tech = 'http://timesofindia.indiatimes.com/rssfeeds/66949542.cms'
url_list = [url_TOI, url_recent, url_india, url_world, url_tech]

for urls in url_list:
    NewsFeed = feedparser.parse(urls)
    for entry in NewsFeed.entries:
        print('Post Title: ',entry.title)
        print('Post Summary: ',entry.summary)
        print('Post Time: ', entry.published)
        print('Post Link: ', entry.id)
        http = urllib3.PoolManager()
        # url = entry.id

        response = http.request('GET', entry.id)
        soup = BSHTML(response.data, "html.parser")
        images = soup.findAll('img')
        print('Post Image: ', images[0]['src'])
        print('------------------------------------------------------------------------')


# NewsFeed = feedparser.parse(url_TOI)
# # print('Number of RSS posts :', len(NewsFeed.entries))
# entry = NewsFeed.entries[1]
# print(entry.id)
#
# http = urllib3.PoolManager()
# # url = entry.id
#
# response = http.request('GET', entry.id)
# soup = BSHTML(response.data, "html.parser")
# images = soup.findAll('img')
# print(images[0]['src'])

# for image in images:
#     #print image source
#     print(image['src'])
#     #print(image)
#     #print alternate text
#     #print(image['alt'])
#
# for entry in NewsFeed.entries:
#     print('Post Title :',entry.title)
#
