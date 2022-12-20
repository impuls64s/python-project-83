import requests
from bs4 import BeautifulSoup


# Функция принимает url адресс вида str --> "https://google.com" и возвращает
# словарь с ключами h1, tittle, description
# если теги были обнаружены на странице

def data_from_html(url):
    data_html_dict = {}
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    if soup.h1:
        data_html_dict["h1"] = soup.h1.string

    if soup.title:
        data_html_dict["title"] = soup.title.string.strip()

    if soup.find(attrs={"name": "description"}):
        data_html_dict["description"] = (
            soup.find(attrs={"name": "description"})['content'].strip()
            )

    return data_html_dict
