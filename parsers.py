# import requests
# from bs4 import BeautifulSoup
#
#
# class Parser:
#     html = ''
#     res = []
#
#     def __init__(self, url, path):
#         self.url = url
#         self.path = path
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def parsing(self):
#         news = self.html.find_all('div', class_='adaptive-card-grid__container-2l '
#                                                 'grid__adaptiveContainer-3M '
#                                                 'adaptive-card-grid__isNewGridFloorsDesktop-2R')
#         for item in news:
#             title = item.find('div', id='container').find('div',
#                                                           class_='card-video-punch__title-25 '
#             'card-video-punch__overflowLink-w9').text
#             time = item.find('h3').find('a').get('href')
#             author = item.find('a', class_='topic-info-author-link').text.strip()
#             self.res.append({
#                 'title': title,
#                 'time': time,
#                 'author': author
#             })
#             print(title)
#
#     # def save(self):
#     #     with open(self.path, 'w') as f:
#     #         i = 1
#     #         for item in self.res:
#     #             f.write(f'Новость № {i}\n\nНазвание новости: {item['title']}\nСсылка: '
#     #                     f'{item['href']}\nИмя автора: {item['author']}\n\n{'*' * 30}\n\n')
#     #             i += 1
#     #
#     def run(self):
#         self.get_html()
#         self.parsing()
#     #     self.save()
#

import requests
from bs4 import BeautifulSoup


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        # game = self.html.find_all("div", id="content")
        houses = self.html.find_all('div', class_='project_item')

        # print(game)
        for item in houses:
            name = item.find('div', class_='project_head').find('div',
                                                                class_='project_title').find(
                'h3').text
            tp = item.find('div', class_='project_head').find('div', class_='project_type').text
            # price = item.find('a', class_='topic-info-author-link').text.strip()
            self.res.append({
                'name': name,
                'type': tp,
                # 'price': price
            })
            print(name)


    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            i = 1
            for item in self.res:
                f.write(f"Игра № {i}\n\nНазвание: {self.res}\n")
                i += 1

    def run(self):
        for i in range(1, 4):
            self.url = self.url.format(i)
            self.get_html()
            self.parsing()
            self.save()


