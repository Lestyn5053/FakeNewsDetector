import csv
from newspaper import Article


def scrapeArticleInfo(url):
    article = Article(url)

    article.download()
    article.parse()

    with open('articles.csv', mode='w') as article_set:
        fieldnames = ['title', 'content']
        article_writer = csv.DictWriter(article_set, fieldnames=fieldnames)
        article_writer.writeheader()
        article_writer.writerow({'title': article.title, 'content': article.text})


def getArticleTitle(url):
    article = Article(url)

    article.download()
    article.parse()

    return article.title


def getArticleText(url):
    article = Article(url)

    article.download()
    article.parse()

    return article.text
