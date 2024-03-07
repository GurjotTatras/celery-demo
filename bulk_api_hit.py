import requests
import random

def bulk_addition(url_api_link):
    for _ in range(200):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        url_api = url_api_link + f"{number1}/{number2}"
        response = requests.get(url_api)
        assert response.status_code == 200


def bulk_multiplication(url_api_link):
    for _ in range(200):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        url_api = url_api_link + f"{number1}/{number2}"
        response = requests.get(url_api)
        assert response.status_code == 200

def bulk_prime_number(url_api_link):
    
    for _ in range(200):
        number1 = random.randint(1, 1000)
        json_data = {}
        json_data['number'] = number1
        response = requests.post(url_api_link, json=json_data)
        assert response.status_code == 200

if __name__ == "__main__":
    addition_api="http://localhost:5010/add/"
    multiplication_api = "http://localhost:5010/multiply/"
    prime_number_api = "http://localhost:5010/check_prime_number/"

    bulk_addition(addition_api)
    bulk_multiplication(multiplication_api)
    bulk_prime_number(prime_number_api)
