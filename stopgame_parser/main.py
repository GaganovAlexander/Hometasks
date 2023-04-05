import requests
from bs4 import BeautifulSoup as bs


def main():
    # Это парсер сайта stopgame.ru
    # Я спарсил все игры со вкладки обзоры, категории "изумительно"
    r = requests.get(
        f"https://stopgame.ru/review/p1?subsection=izumitelno")
    soup = bs(r.content, "html.parser")
    # Так как количество страниц категории может изменяться, для начала
    # я нахожу номер последней страницы по списку с их переключением снизу
    last_page = max([int(i.text) for i in soup.find(
        "div", class_="_container_1mcqg_1").find_all("a", class_='item')])
    page = 1
    all_ = []
    for page in range(1, last_page + 1):
        r = requests.get(
            f"https://stopgame.ru/review/p{page}?subsection=izumitelno")
        soup = bs(r.content, "html.parser")
        items = soup.find_all(
            "article", class_="_card_8sstg_1 _card--autoheight-mobile_8sstg_388")

        for item in items:
            # Из всей информации об играх я беру только название и количество коментариев
            title = item.find("a", class_=[
                              "_card__title_8sstg_1 _card__title--has-subtitle_8sstg_1", "_card__title_8sstg_1"])
            title = title.text.replace(": Обзор", "")[1:]
            num_of_comments = int(item.find(
                "a", class_="_card__info__attribute_8sstg_1").text)
            all_.append((title, num_of_comments))

    # На stopgame.ru не реализована сортировка категории по количеству комментариев, поэтому
    # я решил сделать такую
    all_ = sorted(all_, key=lambda x: x[1], reverse=True)
    # В качестве вывода - у нас топ 10 игр из категории "изумительно" по количеству комментариев
    for i, j in enumerate(all_[:10]):
        print(f"#{i + 1}\n{j[0]}\nNumber of comments: {j[1]}\n")


if __name__ == '__main__':
    main()
