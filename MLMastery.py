# import requests
# import bs4

# url = "https://machinelearningmastery.com/feed/"
# result = requests.get(url)

# # print(result.text)
# soup = bs4.BeautifulSoup(result.text,"lxml")
# # print(soup)
# print('ok')
# # print(soup.select('title')[0].getText())
# print(soup.select('title'))

# # site_paragraphs = soup.select("p")
# # for paras in site_paragraphs:
# #     print(paras.getText())




import feedparser

url = 'https://www.nature.com/subjects/computational-neuroscience.rss'

NewsFeed = feedparser.parse(url)
# print(NewsFeed.entries[0])

for entry in NewsFeed.entries:
    print('Post Title: ',entry.title)
    print('Post Summary: ',entry.summary)
    print('Post Time: ', entry.published)
    print('Post Link: ', entry.link)
    # print('Post Image: ', entry.storyimage)
    print('---------------------------------------------------------------')
