from bs4 import BeautifulSoup
import requests


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    p1 = soup.find('section', class_='section1').find('div', class_='left').find('h1').text
    p2 = soup.find('section', class_='section4').find('div', class_='center').find('div', class_='text').text
    p3 = [soup.find('section', class_='section2').find('div', class_='content').find('h2').text,
          soup.find('section', class_='section2').find('div', class_='info').text]

    return f'{p1}\n{p2}\n{p3[0]}:{p3[1]}'


def main():
    url = 'https://teremok-rm.ru/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()