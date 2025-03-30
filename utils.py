import time
import pytest
import requests

#------------------------------------------------------Basic test functions


def test_create_new_pet_by_id(pet_id, *, time_sleep=20):
    """Функция тестирования создания питомца"""
    print(f'\nTest: {test_create_new_pet_by_id.__name__}')


    """Информация о запросе"""
    base_url = "https://petstore.swagger.io/v2"
    endpoint = "/pet"
    url = base_url + endpoint
    api_key = "simple_key"
    headers = {"Content-Type": "application/json", "api_key": api_key}


    """Тело запроса"""
    body = {"id": pet_id,
        "category": {'id': 0, 'name': 'Antagonist'},
        "name": 'Madara',
        "photoUrls": ["None"],
        "tags": [{'id': 0, 'name': 'Have Susanoo'}],
        "status": 'available'}


    """Ответ сервера, статус код, ожидание обработки"""
    response = requests.post(url, json=body, headers=headers)
    code = response.status_code
    time.sleep(time_sleep)


    """Проверка теста"""
    if code == 200:
        print(f'{"Request:".ljust(10)}{body}\n{"Response:".ljust(10)}{response.json()}\nStatus code: {code}\n🟢 Test PASSED')
        return code, response.json()

    else:
        print(f'{"Request:".ljust(10)}{body}\n{"Response:".ljust(10)}{response.json()}\nStatus code: {code}\n🔴 Test NOT PASSED')
        return code, response.json()


def test_read_info_pet_by_id(pet_id, *, response_json=None):
    """Функция тестирования чтения информации о созданном питомце по id"""
    print(f'\nTest: {test_read_info_pet_by_id.__name__}')

    """Информация о запросе"""
    base_url = "https://petstore.swagger.io/v2"
    endpoint = "/pet"
    url = base_url + endpoint + f'/{pet_id}'
    api_key = "simple_key"
    headers = {"Content-Type": "application/json", "api_key": api_key}
    print(url)

    """Ответ сервера, статус код запроса"""
    response = requests.get(url, headers=headers)
    code = response.status_code


    """Проверка теста"""
    if code == 200 and response_json == response.json():
        print(f'{"Response:".ljust(10)}{response.json()}\nStatus code: {code}\n🟢 Test PASSED')
        return code, response.json()

    elif code != 200 or response_json != response.json():
        print(f'{"Response:".ljust(10)}{response.json()}\nStatus code: {code}\n🔴 Test NOT PASSED')
        return code, response.json()


def test_update_data_pet_by_id(pet_id, *, time_sleep=20):
    """Функция тестирования обновления информации о созданном питомце по id"""
    print(f'\nTest: {test_update_data_pet_by_id.__name__}')


    """Информация о запросе"""
    base_url = "https://petstore.swagger.io/v2"
    endpoint = "/pet"
    url = base_url + endpoint
    api_key = "simple_key"
    headers = {"Content-Type": "application/json", "api_key": api_key}


    """Тело запроса"""
    body = {
    "id": pet_id,
    "category": {"id": 1,"name": "Protagonist"},
    "name": 'Naruto',
    "photoUrls": ["None"],
    "tags": [{'id': 0, 'name': 'Have Bijou'}],
    "status": "available"}


    """Ответ сервера, статус код запроса, ожидание обработки"""
    response = requests.put(url, json=body, headers=headers)
    code = response.status_code
    time.sleep(time_sleep)


    """Проверка теста"""
    if code == 200:
        print(f'{"Request:".ljust(10)}{body}\n{"Response:".ljust(10)}{response.json()}\nStatus code: {code}\n🟢 Test PASSED')
        return code, response.json()

    else:
        print(f'{"Request:".ljust(10)}{body}\n{"Response:".ljust(10)}{response.json()}\nStatus code: {code}\n🔴 Test NOT PASSED')
        return code, response.json()


def test_delete_pet_by_id_with_read_info(pet_id, *, time_sleep=20):
    """Функция тестирования удаления созданного питомца по id
    После успешного ответа 200 происходит проверка методом GET, чтобы убедиться, что удаление прошло успешно
    """
    print(f'\nTest: {test_delete_pet_by_id_with_read_info.__name__}')

    """Информация о запросе"""
    base_url = "https://petstore.swagger.io/v2"
    endpoint = "/pet"
    url = f"{base_url}{endpoint}/{pet_id}"
    api_key = "simple_key"
    headers = {"Content-Type": "application/json", "api_key": api_key}
    print(f"Request URL: {url}")

    """Удаляем питомца"""
    response = requests.delete(url, headers=headers)
    code_delete = response.status_code

    """Проверка теста"""
    if code_delete == 200:
        print(f'Status code: {code_delete}\nPet {pet_id} successfully deleted.')
        time.sleep(time_sleep)
        check_response = requests.get(url, headers=headers)
        check_code = check_response.status_code

        if check_code == 404:
            print(f'🟢 Test PASSED: Pet {pet_id} was successfully deleted and no longer exists.')
            return code_delete, check_code

        else:
            print(f'🔴 Test NOT PASSED: Pet {pet_id} still exists after deletion!')

            try:
                print(f'Response: {check_response.json()}')

            except ValueError:
                print(f'Invalid JSON Response: {check_response.text}')

            return code_delete, check_code,

    elif code_delete == 404:
        print(f'Status code: {code_delete}\n🔴 Test NOT PASSED: Pet {pet_id} was not found, nothing to delete.')

        return code_delete, response.text

    else:
        print(f'Status code: {code_delete}\n🔴 Unexpected error! Status code: {code_delete}')
        try:
            error_response = response.json()
            print(f'Response JSON: {error_response}')
        except ValueError:
            print(f'Invalid JSON Response: {response.text}')
        return code_delete, response.text


#------------------------------------------------------Helper test functions


def test_manual_delete_pet(pet_id, *, time_sleep=20):
    """Циклическая функция, для удаления созданного питомца по id
    Используется для удаления питомца после неудачно выполненного теста
    """

    print(f'\nForced deletion is in progress...')


    """Информация о запросе"""
    base_url = "https://petstore.swagger.io/v2"
    endpoint = "/pet"
    url = f"{base_url}{endpoint}/{pet_id}"
    api_key = "simple_key"
    headers = {"Content-Type": "application/json", "api_key": api_key}
    print(url)


    """Удаляем питомца"""
    code = None
    count = 0
    while code != 404 and count < 5:
        count += 1
        response = requests.delete(url, headers=headers)
        code = response.status_code  # Возвращаем Status code
        time.sleep(time_sleep)
    print(f'Removal attempts have been made: {count}')


    """Проверка теста"""
    if code == 404:
        print(f"🟠 Pet with ID {pet_id} successfully deleted.")

    else:
        print(f"🔴 Failed to delete pet with ID {pet_id}.")