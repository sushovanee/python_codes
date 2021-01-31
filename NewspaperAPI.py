import newspaper
from newspaper import Article
from newspaper import news_pool

# url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
#
# article = Article(url)
# article.download()
#
# article.parse()
#
# print(article.authors)
#
# print(article.publish_date)
#
# print(article.text)

toi_paper = newspaper.build('https://timesofindia.indiatimes.com/')
ndtv_paper = newspaper.build('https://www.ndtv.com/')
hindu_paper = newspaper.build('https://www.thehindu.com/')

papers = [toi_paper, hindu_paper]

news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
news_pool.join()

print(slate_paper.articles[10])
