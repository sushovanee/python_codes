import requests
import bs4

url = "https://timesofindia.indiatimes.com/gadgets-news/apple-iphone-users-theres-a-new-scam-you-need-to-be-careful-about/articleshow/79589422.cms"
result = requests.get(url)

# print(result.text)
soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup)

# print(soup.select('title')[0].getText())

# site_paragraphs = soup.select("p")
# for paras in site_paragraphs:
    # print(paras.getText())
print('---------------------------------------------------------------------')
header = soup.select("h1")
for heads in header:
    print(heads.getText())
print('---------------------------------------------------------------------')
l = soup.select('.ga-headlines') 
for i in l:
    print(i.getText())
