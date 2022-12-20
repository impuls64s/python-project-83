import requests
from requests.exceptions import HTTPError


# Функция принимает url адресс вида str --> "https://yotube.com" и возвращает
# status_code чисто int--> 200, если статус код положительный или
# строку 'bad_status' если адрес открывается с ошибками

def valid_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError:
        return 'bad_status'
    except Exception:
        return 'bad_status'
    else:
        return response.status_code
