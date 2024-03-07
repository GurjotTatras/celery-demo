import requests
import random

def bulk_api(url_api_link):
    for _ in range(100):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        url_api = url_api_link + f"{number1}/{number2}"
        response = requests.get(url_api)
        assert response.status_code == 200


if __name__ == "__main__":
    url_api="http://localhost:5010/add/"
    bulk_api(url_api)