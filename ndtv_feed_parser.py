import feedparser

# top_news = 'https://feeds.feedburner.com/ndtvnews-top-stories'
# latest_news = 'https://feeds.feedburner.com/ndtvnews-latest'
# trending_news = 'https://feeds.feedburner.com/ndtvnews-trending-news'
# india_news = 'https://feeds.feedburner.com/ndtvnews-india-news'
# world_news = 'https://feeds.feedburner.com/ndtvnews-world-news'
# business_news = 'https://feeds.feedburner.com/ndtvprofit-latest'
# movie_news = 'https://feeds.feedburner.com/ndtvmovies-latest'
# sport_news = 'https://feeds.feedburner.com/ndtvsports-latest'
# tech_news = 'https://feeds.feedburner.com/gadgets360-latest'
# toi_top_news = 'https://timesofindia.indiatimes.com/rssfeeds/1221656.cms'
toi_base_url = 'https://timesofindia.indiatimes.com/rssfeeds/'
# NewsFeed = feedparser.parse(top_news)
# print(NewsFeed.entries[0])

news_section = ['1221656', '-2128936835', '296589292', '1898055', '66949542', '-2128833038']

# url_list = [toi_top_news]

for urls in news_section:
    NewsFeed = feedparser.parse(toi_base_url+str(urls)+'.cms')
    for entry in NewsFeed.entries:
        print('Post Title: ',entry.title)
        print('Post Summary: ',entry.summary)
        print('Post Time: ', entry.published)
        print('Post Link: ', entry.link)
        # print('Post Image: ', entry.storyimage)
        print('---------------------------------------------------------------')
