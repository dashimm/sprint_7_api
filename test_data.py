class Urls:
    main_url = 'https://qa-scooter.praktikum-services.ru'


class ScooterApi:
    create_courier = f'{Urls.main_url}/api/v1/courier'
    courier_login = f'{Urls.main_url}/api/v1/courier/login'
    create_orders = f'{Urls.main_url}/api/v1/orders'
    get_orders_list = f'{Urls.main_url}/api/v1/orders'


class UserData:
    test_user = {
        'firstname': 'Скотт',
        'lastname': 'Пилигрим',
        'address': 'Торонто, Канада',
        'metroStation': 19,
        'phone': '+79999999999',
        'rentTime': 5,
        'deliveryDate': '2024-07-26',
        'comment': 'Для Рамоны',
        'color': []

    }


class CourierData:
    existent_courier = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }


class ResponseData:
    successful_text = '{"ok":true}'
    bad_request_created_text = "Недостаточно данных для создания учетной записи"
    conflict_text = "Этот логин уже используется"
    created_track_text = "track"
    get_orders_list_text = "orders"
    created_id_text = "id"
    bad_request_login_text = "Недостаточно данных для входа"
    not_found_login_text = "Учетная запись не найдена"

