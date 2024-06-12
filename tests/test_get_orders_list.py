import allure
import requests
from test_data import ScooterApi, ResponseData


class TestGetOrdersList:
    @allure.title("Получение списка заказов курьера")
    def test_get_order_list(self):
        response = requests.get(ScooterApi.get_orders_list)
        assert response.status_code == 200
        assert ResponseData.get_orders_list_text in response.text
