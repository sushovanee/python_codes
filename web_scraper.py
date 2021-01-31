# Imports
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

# Retrieve page text
url = 'https://towardsdatascience.com/why-everyone-uses-transfer-learning-700cd788f2b7'
url_2 = 'https://towardsdatascience.com/back-to-the-future-of-data-analysis-a-tidy-implementation-of-tukeys-vacuum-87c561cdee18'
url_3 = 'https://www.magicbricks.com/'

page = requests.get(url_3).text

# Turn page into BeautifulSoup object to access HTML tags
soup = BeautifulSoup(page, features="lxml")

# Get headline
headline = soup.find('h1').get_text()

# Get text from all <p> tags.
p_tags = soup.find_all('p')
# Get the text from each of the “p” tags and strip surrounding whitespace.
p_tags_text = [tag.get_text().strip() for tag in p_tags]

# Filter out sentences that contain newline characters '\n' or don't contain periods.
sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
# Combine list items into string.
article = ' '.join(sentence_list)

summary = summarize(article, ratio=0.3)

print(f'Length of original article: {len(article)}')
print(f'Length of summary: {len(summary)} \n')
print(f'Headline: {headline} \n')
print(f'Article Summary: \n{summary}')

for i in soup.select('div._3WlLe clearfix'):
    print(i.string)
