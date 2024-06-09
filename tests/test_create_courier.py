from test_data import *
import allure
from helpers.courier_data import *


class TestCreateCourier:
    @allure.title("Создание курьера со всеми обязательными данными")
    def test_create_courier_return_ok(self):
        data = generate_random_courier_data()
        response = requests.post(ScooterApi.create_courier, json=data)
        assert response.status_code == 201
        assert ResponseData.successful_text in response.text

    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login_return_error(self):
        data = generate_courier_without_login()
        response = requests.post(ScooterApi.create_courier, json=data)
        assert response.status_code == 400
        assert ResponseData.bad_request_created_text in response.text

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password_return_error(self):
        data = generate_courier_without_password()
        response = requests.post(ScooterApi.create_courier, json=data)
        assert response.status_code == 400
        assert ResponseData.bad_request_created_text in response.text

    @allure.title("Создание курьера с уже существующим логином")
    def test_create_existent_courier_return_error(self):
        data = CourierData.existent_courier
        response = requests.post(ScooterApi.create_courier, json=data)
        assert response.status_code == 409
        assert ResponseData.conflict_text in response.text

    @allure.title("Создание курьера с пустыми данными")
    def test_create_null_courier_return_error(self):
        data = {"login": "", "firstname": "", "password": ""}
        response = requests.post(ScooterApi.create_courier, json=data)
        assert response.status_code == 400
        assert ResponseData.bad_request_created_text in response.text
