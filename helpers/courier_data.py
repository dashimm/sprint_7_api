import requests
from faker import Faker
from test_data import ScooterApi


def generate_random_courier_data():
    fake = Faker()
    login = fake.user_name()
    password = fake.password()
    first_name = fake.first_name()
    data = {
        "login": login,
        "firstname": first_name,
        "password": password
    }

    return data


def generate_courier_without_login():
    fake = Faker()
    password = fake.password()
    first_name = fake.first_name()
    data = {
        "login": "",
        "firstname": first_name,
        "password": password
    }

    return data


def generate_courier_without_password():
    fake = Faker()
    login = fake.user_name()
    first_name = fake.first_name()
    data = {
        "login": login,
        "firstname": first_name,
        "password": ""
    }

    return data


def register_new_courier_and_return_login_password():
    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    data = generate_random_courier_data()

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(ScooterApi.create_courier, data=data)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(data.get("login"))
        login_pass.append(data.get("password"))
        login_pass.append(data.get("first_name"))

    # возвращаем список
    return login_pass
