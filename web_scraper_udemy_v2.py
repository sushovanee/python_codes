import requests
import bs4

# url = "https://www.ndtv.com/india-news/bharat-bandh-today-amid-farmer-protests-cops-issue-travel-advisory-10-points-2335538?pfrom=home-ndtv_topscroll"
# url = "https://sports.ndtv.com/athletics/was-successful-with-a-single-kidney-olympian-anju-bobby-george-makes-stunning-revelation-2335443"
# url = "https://www.nytimes.com/2020/12/01/business/economy/workers-jobs-training.html?utm_source=pocket-newtab-intl-en"
# url = "https://www.nytimes.com/live/2020/12/08/world/covid-19-coronavirus"
# url = "https://www.thehindu.com/news/national/govt-approves-to-set-up-public-wi-fi-networks-under-pm-wani/article33289290.ece?homepage=true"
# url = "https://towardsdatascience.com/clearly-explained-top-2-types-of-decision-trees-chaid-cart-8695e441e73e"
# url = "https://navbharattimes.indiatimes.com/state/bihar/bhagalpur/bhagalpur-ankhfodwa-scandal-after-40-years-victims-wait-rehabilitation-pension-also-stopped/articleshow/79677662.cms?story=5"
# url = "https://dev.to/ezzy1337/a-pythonic-guide-to-solid-design-principles-4c8i"
# url = "https://thesequence.substack.com/p/edge51"
# url = "https://machinelearningmastery.com/machine-learning-modeling-pipelines"
url = "https://www.educative.io/module/lesson/intro-python-data-analysis/YMKN9YDAOVM"


result = requests.get(url)

soup = bs4.BeautifulSoup(result.text,"lxml")

print('---------------------------------------------------------------------')
header = soup.select("h1")
for heads in header:
    print(heads.getText())
print('---------------------------------------------------------------------')

# l = soup.select(".sp-cn.ins_storybody")
# l = soup.select(".story__content")
# l = soup.select(".css-158dogj.evys1bk0")
# l = soup.select(".paywall")
# l = soup.select(".n.p")
# l = soup.select(".story-content")
# l = soup.select(".crayons-article__body.text-styles.spec__body")
# l = soup.select(".post")
# l = soup.select(".inner-wrapper")
l = soup.select(".ArticlePage__Container-sc-1eiji3g-1.gAZlDv")

# news_text = l[0].select("p")

# print(l)

for i in l:
    print(i.getText())
    
# print("*************************")
# for items in news_text:
    # print(items.getText())

# print('---------------------------------------------------------------------')

# 325191