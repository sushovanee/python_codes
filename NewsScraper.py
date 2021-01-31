# Imports
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

# Retrieve page text
# url = 'https://www.npr.org/2019/07/10/740387601/university-of-texas-austin-promises-free-tuition-for-low-income-students-in-2020'
# url = 'https://timesofindia.indiatimes.com/india/coronavirus-onus-put-on-dms-sps-to-check-influx/articleshow/74880278.cms'
url = 'https://jira2.cerner.com/activity?maxResults=10&streams=key+IS+SUPPLYCHN&providers=thirdparty+dvcs-streams-provider+issues&os_authType=basic&title=undefined'
page = requests.get(url).text

# Turn page into BeautifulSoup object to access HTML tags
soup = BeautifulSoup(page)

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
