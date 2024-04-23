class Article:
    def __init__(self, title, author, pages, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.description = description

    def __str__(self):
        return f'{self.title} ({self.author})'


class ArticleModel:
    def __init__(self):
        self.articles = {}  # {'qqq': {'title': qqq, 'author': www}}

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            'название': article.title,
            'author': article.author,
            'количество страниц': article.pages,
            'описание': article.description
        }
        return dict_article
