def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f' {title} '.center(50, '='))
            output = func(*args, **kwargs)
            print('=' * 50)
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_title('Ввод пользовательских данных')
    def wait_user_answer(self):
        # print(' Ввод пользовательских данных '.center(50, '='))
        print('Действия со статьями:')
        print('\n1 - создание статьи'
              '\n2 - просмотр статей'
              '\n3 - просмотр определенной статьи'
              '\nq - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        # print('=' * 50)
        return user_answer

    @add_title('Создание статьи')
    def add_user_article(self):
        dict_article = {
            'название': None,
            'author': None,
            'количество страниц': None,
            'описание': None
        }
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} статьи: ')
        return dict_article

    @add_title('Список статей')
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, start=1):
            print(f'{ind}. {article}')

    @add_title('Ввод названия статьи')
    def get_user_article(self):
        user_article = input('Введите название статьи: ')
        return user_article

    @add_title('Просмотр статьи')
    def show_single_article(self, article):
        for key in article:
            print(f'{key} статьи - {article[key]}')