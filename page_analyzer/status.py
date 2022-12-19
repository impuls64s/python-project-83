import requests
from requests.exceptions import HTTPError

def valid_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        return 'bad_status'
    except Exception as err:
        return 'bad_status'
    else:
        return response.status_code
