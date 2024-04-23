from view import UserInterface
from model import ArticleModel


class Controller:
    def __init__(self):
        self.article_model = ArticleModel()  #
        self.user_interface = UserInterface()  # view

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            article = self.user_interface.add_user_article()
            self.article_model.add_article(article)
        elif answer == '2':
            articles = self.article_model.get_all_articles()
            self.user_interface.show_all_articles(articles)
        elif answer == '3':
            article_title = self.user_interface.get_user_article()
            article = self.article_model.get_single_article(article_title)
            self.user_interface.show_single_article(article)