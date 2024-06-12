import allure
import pytest
import requests
from test_data import *


class TestCreateOrders:
    @allure.title("Создание заказа с разными цветами самоката")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["GREY", "BLACK"], []])
    def test_create_orders_with_color(self, color):
        data = UserData.test_user
        data["color"] = color
        response = requests.post(ScooterApi.create_orders, json=data)
        assert response.status_code == 201
        assert ResponseData.created_track_text in response.text
