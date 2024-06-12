import allure
from helpers.courier_data import *
from test_data import ResponseData


class TestLoginCourier:
    @allure.title("Авторизация курьера с валидными данными")
    def test_login_courier_return_ok(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(ScooterApi.courier_login, json={"login": data[0], "password": data[1]})
        assert response.status_code == 200
        assert ResponseData.created_id_text in response.text

    @allure.title("Авторизация курьера без логина")
    def test_login_courier_without_login_return_error(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(ScooterApi.courier_login, json={"login": "", "password": data[1]})
        assert response.status_code == 400
        assert ResponseData.bad_request_login_text in response.text

    @allure.title("Авторизация курьера без пароля")
    def test_login_courier_without_password_return_error(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(ScooterApi.courier_login, json={"login": data[0], "password": ""})
        assert response.status_code == 400
        assert ResponseData.bad_request_login_text in response.text

    @allure.title("Авторизация курьера с валидным логином и невалидным паролем")
    def test_login_courier_with_invalid_password_return_error(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(ScooterApi.courier_login, json={"login": data[0], "password": "kurwa"})
        assert response.status_code == 404
        assert ResponseData.not_found_login_text in response.text

    @allure.title("Авторизация курьера с невалидным логином и валидным паролем")
    def test_login_courier_with_invalid_login_return_error(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(ScooterApi.courier_login, json={"login": "bobr", "password": data[1]})
        assert response.status_code == 404
        assert ResponseData.not_found_login_text in response.text

    @allure.title("Авторизация курьера с несуществующими данными")
    def test_login_courier_with_non_existent_data_return_error(self):
        data = generate_random_courier_data()
        response = requests.post(ScooterApi.courier_login, json=data)
        assert response.status_code == 404
        assert ResponseData.not_found_login_text in response.text
