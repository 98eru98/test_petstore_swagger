import time
import pytest
import requests

"""Информация о запросе"""
base_url = "https://petstore.swagger.io/v2"
endpoint = "/pet"
api_key = "simple_key"
headers = {"Content-Type": "application/json", "api_key": api_key}
body = "Null"

#------------------------------------------------------Basic test functions

def test_create_new_pet_by_id_with_read_info(pet_id, *, time_sleep=20):
    """Функция тестирования создания питомца по id
    После успешного ответа 200 происходит проверка методом GET, чтобы убедиться, что создание прошло успешно
    """
    print(f'\nTest: {test_create_new_pet_by_id_with_read_info.__name__}')

    """Информация о запросе"""
    url = base_url + endpoint
    print(f"Request URL: {url}")

    """Тело запроса"""
    body = {"id": pet_id,
        "category": {'id': 0, 'name': 'Antagonist'},
        "name": 'Madara',
        "photoUrls": ["None"],
        "tags": [{'id': 0, 'name': 'Have Susanoo'}],
        "status": 'available'}

    """Ответ сервера, статус код, ожидание обработки"""
    response = requests.post(url, json=body, headers=headers)
    code_create = response.status_code

    """Создание питомца"""
    if code_create == 200:
        print(f'Status creation code : {code_create}')
        print(f'Pet {pet_id} successfully created.')

        """Проверка успешности создания питомца"""
        time.sleep(time_sleep)
        url = base_url + endpoint + f'/{pet_id}'
        check_response = requests.get(url, headers=headers)
        check_code = check_response.status_code

        if check_code == 200:
            print(f'Status check code : {check_code}')
            print(f'Pet {pet_id} successfully found.')
            print('🟢 Test PASSED')
            return code_create, check_code, True, response.text, check_response.text

        else:
            print(f'Status check code: {check_code}')
            print(f'Pet {pet_id} not found.')
            print('🔴 Test NOT PASSED')
            return code_create, check_code, False, response.text, check_response.text

    else:
        print(f'Status creation code : {code_create}')
        print(f'Failed to create pet {pet_id}.')
        print('🔴 Test NOT PASSED')
        return code_create, None, False, response.text, None


def test_update_data_pet_by_id_with_read_info(pet_id, *, time_sleep=20):
    """Функция тестирования изменения питомца по id
    После успешного ответа 200 происходит проверка методом GET, чтобы убедиться, что изменение прошло успешно
    """
    print(f'\nTest: {test_update_data_pet_by_id_with_read_info.__name__}')

    """Информация о запросе"""
    url = base_url + endpoint
    print(f"Request URL: {url}")

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
    update_code = response.status_code

    """Изменение питомца"""
    if update_code == 200:
        print(f'Status update code: {update_code}')
        print(f'Pet {pet_id} successfully update.')

        """Проверка успешности изменения питомца"""
        time.sleep(time_sleep)
        url = base_url + endpoint + f'/{pet_id}'
        check_response = requests.get(url, headers=headers)
        check_code = check_response.status_code

        if check_code == 200 and response.text == check_response.text:
            print(f'Status check code : {check_code}')
            print(f'Changes for pet {pet_id} come into effect.')
            print('🟢 Test PASSED')
            return update_code, check_code, True, response.text, check_response.text

        elif check_code == 200 and response.text != check_response.text:
            print(f'Status check code : {check_code}')
            print(f'Changes for pet {pet_id} no come into effect')
            print('🔴 Test NOT PASSED')
            return update_code, check_code, False, response.text, check_response.text

        else:
            print(f'Status check code: {check_code}')
            print(f'Failed to update for pet {pet_id}.')
            print('🔴 Test NOT PASSED')
            return update_code, check_code, False, response.text, check_response.text

    else:
        print(f'Status update code : {update_code}')
        print(f'Failed to update pet {pet_id}.')
        print('🔴 Test NOT PASSED')
        return update_code, None, False, response.text, None


def test_delete_pet_by_id_with_read_info(pet_id, *, time_sleep=20):
    """Функция тестирования удаления созданного питомца по id
    После успешного ответа 200 происходит проверка методом GET, чтобы убедиться, что удаление прошло успешно
    """
    print(f'\nTest: {test_delete_pet_by_id_with_read_info.__name__}')

    """Информация о запросе"""
    url = f"{base_url}{endpoint}/{pet_id}"
    print(f"Request URL: {url}")

    """Ответ сервера, статус код, ожидание обработки"""
    response = requests.delete(url, headers=headers)
    code_delete = response.status_code

    """Удаление питомца"""
    if code_delete == 200:
        print(f'Status deletion code: {code_delete}')
        print(f'Pet {pet_id} successfully deleted.')

        """Проверка успешности удаления питомца"""
        time.sleep(time_sleep)
        check_response = requests.get(url, headers=headers)
        check_code = check_response.status_code

        if check_code == 404:
            print(f'Status check code : {check_code}')
            print(f'Pet {pet_id} successfully not found.')
            print('🟢 Test PASSED')
            return code_delete, check_code, True,  response.text, check_response.text

        else:
            print(f'Status check code: {check_code}')
            print(f'Pet {pet_id} still exist.')
            print('🔴 Test NOT PASSED')
            return code_delete, check_code, False, response.text, check_response.text

    else:
        print(f'Status deletion code: {code_delete}')
        print(f'Failed to delete pet {pet_id}.')
        print(f'Error text: {response.text}')
        print('🔴 Test NOT PASSED')
        return code_delete, None, False, response.text, None

#------------------------------------------------------Helper test functions

def test_manual_delete_pet(pet_id, *, time_sleep=20):
    """Циклическая функция, для удаления созданного питомца по id
    Используется для удаления питомца после неудачно выполненного теста
    """
    print(f'\nForced deletion is in progress...')

    """Информация о запросе"""
    url = f"{base_url}{endpoint}/{pet_id}"
    print(f"Request URL: {url}")

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