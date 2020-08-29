import requests
import csv
from bs4 import BeautifulSoup as bs


woman = [] #Словарь куда записывается информация о девушках


def files_write():
    with open("woman.csv", "w", encoding="UTF-8", newline="") as f:
        writer = csv.writer(f, delimiter="@")
        writer.writerow(("Район", "Ссылка на дувушку", "Имя", "Номер телефона", "Цена", "Возраст", "Рост", "Вес", "Размер груди"))
        for w in woman:
            writer.writerow((w["area"], w["href"], w["title"], w["number"], w["price"], w["age"], w["height"], w["weight"], w["size"]))




def parser():
    a = 1
    u = "https://prostitutkitambovacool.com/page/"
    while a <= 3:
        url = u + str(a)
        r = requests.get(url)
        if r.status_code == 200:
            soup = bs(r.content, "html.parser")
            for item in soup.find_all("div", attrs={"class": "catalog-item list"}):
                try: item_area = item.find("div", attrs={"class": "local-label"}).text #Район девушки
                except: item_area = "Не указано"
                try: item_href = item.find("a")["href"] #Ссылка на девушку
                except: item_href = "Не указано"
                try: item_title = item.find("a")["title"] #Имя девушки
                except: item_title = "Не указано"
                try: item_number = item.find("div", attrs={"class": "catalog-panel"}).find("div", attrs={"class": "btn btn-phone"}).find("a").text #Номер телефона девушки
                except: item_number = "Не указано"
                try: item_price = item.find("div", attrs={"class": "catalog-panel"}).find("div", attrs={"class": "label-price"}).find("span").text #Цена девушки
                except: item_price = "Не указано"
                item_options_all = item.find_all("div", attrs={"class": "info-options-item"}) #Находим информацию о девушки
                try: item_age = item_options_all[0].find("span").text #Находи возраст девушки
                except: item_age = "Не указано"
                try: item_height = item_options_all[1].find("span").text #Находим рост девушки
                except: item_height = "Не указано"
                try: item_weight = item_options_all[2].find("span").text #Находим вес девушки
                except: item_weight = "Не указано"
                try: item_size = item_options_all[3].find("span").text #Находим размер груди девушки
                except: item_size = "Не указано"

                woman.append({
                    "area": item_area,
                    "href": item_href,
                    "title": item_title,
                    "number": item_number,
                    "price": item_price,
                    "age": item_age,
                    "height": item_height,
                    "weight": item_weight,
                    "size": item_size
                }) #Записывае информацию о девушки в словарь
        a += 1
    files_write()


if __name__ == "__main__":
    parser()
    print("Файл с девушками создан.\nПарсинг закончен.")