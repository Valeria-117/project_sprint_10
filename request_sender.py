import configuration
import data
import requests

# Создание пользователя
def post_new_user(body):
    return requests.post(configuration.URL_MAIN + configuration.CREATE_USER_PATH, json=body, headers=data.headers)

# Получение токена
def get_new_auth_token():
    new_user = post_new_user(data.user_body)
    return new_user.json().get('authToken')

# Создание набора
def post_new_client_kit(kit_body):
    data.headers["Authorization"] += get_new_auth_token()
    return requests.post(configuration.URL_MAIN + configuration.KITS_PATH, json=kit_body, headers=data.headers)