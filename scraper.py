import csv
import requests
from bs4 import BeautifulSoup

page = requests.get('https://abcnews.go.com/Health/wireStory/volunteers-needed-test-variety-covid-19-vaccines-74254323')
soup = BeautifulSoup(page.content, 'html.parser')

page_title = soup.title.text
page_body = soup.body

print(page_title)
print(page_body)

with open('articles.csv', mode='w') as article_set:
    fieldnames = ['title', 'content']
    article_writer = csv.DictWriter(article_set, fieldnames=fieldnames)
    article_writer.writeheader()
    # article_writer = csv.writer(article_set, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    article_writer.writerow({'title': page_title, 'content': 'The economy'})
