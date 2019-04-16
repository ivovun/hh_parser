import requests
from bs4 import BeautifulSoup as bs


def hh_parse(base_url, headers):

    """
        назовем функцию head hunter парс принимать она будет был и headers когда мы заходим на сайт мы же с одного
    браузера кликаем по разным вакансиям меня ими страничке заходим на различные вакансии их а катар не блокируют
     нас потому что понимает что мы зашли с одного браузера и как один пользователь делаем различные действия до
     то есть наши шаги можно отследить для того чтобы создать такую же иллюзию то есть непрерывности действия во
     времени нам необходимо создать сессию мы создадим переменную s 04:57 c сион
    """
    jobs = []

    session = requests.Session()  # благодаря вот этой строчке сайт как hunter будет думать что на него зашел
    # один пользователь и просматривать 05:09 большое количество вакансий
    request = session.get(base_url, headers=headers)  # теперь нам необходимо
    # и эмулировать открытии
    # страницы в браузере для этого мы сделаем переменную request песен . get
    # передадим юрия а в нашем
    # случае это был и передадим хедер равно хедер это чтобы проверить ч
    # то сервер 05:28 отдал нам данные
    # которые нам необходимо
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')  # request контент это по
        # сути весь ответ который нам
        # отправляет 06:33 сервер
        # 'html.parser' это встроенный парсер в python который позволяет
        # разбивать ответ сервера на
        # определенные блоки 06:42 html-страницы
        divs = soup.find_all('div', attrs={'data-qa': "vacancy-serp__vacancy"})  # список вакансий на одной странице
        for div in divs:
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            text1 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            text2 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            content = text1 + text2
            jobs.append({
                'title': title,
                'href': href,
                'company': company,
                'content': content,
            })
            print(jobs)

        print(len(divs))
    else:
        print("ERROR")


def main():
    headers = {'accept': r'*/*',
               'user-agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36'
                             '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

    base_url = 'https://hh.ru/search/vacancy?area=1&search_period=7&text=Python&page=1'
    hh_parse(base_url, headers)
    #testcomment1


main()



