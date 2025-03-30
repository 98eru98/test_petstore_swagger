from utils import *

@pytest.fixture
def pet_id():
    ids = [4, "74568", (-1), 0, "***", None, "null", {}]
    return ids[0]


def test_CRUD(pet_id):
    """
    Функция тестирования полного цикла создания, изменения, удаления питомца (https://petstore.swagger.io/#/)
    При возникновении ошибок во время теста, тест прекращается с результатом "FAILED" и созданный питомец автоматически удаляется
    Используемые функции возвращают:


    """
    # Устанавливаем время задержки между циклами авто удаления питомца, при возникновении ошибки
    time_sleep_manual_delete = 0

    t_create = test_create_new_pet_by_id(pet_id, time_sleep=10)   # Возвращаем Status code

    if t_create[0] == 200:  # Проверяем Status code
        t_read_1 = test_read_info_pet_by_id(pet_id, response_json=t_create[1]) # Возвращаем Status code

        # Проверяем чтобы созданный питомец совпадал с ответом, что вернулся после проверки
        if t_read_1 == t_create:  # Проверяем Status code
            t_update = test_update_data_pet_by_id(pet_id, time_sleep=10)  # Возвращаем Status code

            if t_update[0] == 200:  # Проверяем Status code
                t_read_2 = test_read_info_pet_by_id(pet_id, response_json=t_update[1])

                # Проверяем чтобы измененный питомец совпадал с ответом, что вернулся после проверки и не совпадал с изначально созданным
                if t_read_2 == t_update != t_create[1]:  # Проверяем Status code
                    t_delete = test_delete_pet_by_id_with_read_info(pet_id, time_sleep=10)  # Возвращаем Status code

                    # Проверяем что Status code удаления 200 и Status code запроса на существование питомца не 200
                    if t_delete[0] == 200 and t_delete[1] != 200:  # Проверяем Status code

                        print("✔️✔️✔️ALL TESTS PASSED✔️✔️✔️")

                    else:
                        # Автоматическое удаление питомца в случае неудачи теста
                        test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete)
                        pytest.fail(f"Test failed at {test_delete_pet_by_id_with_read_info.__name__}")

                else:
                    # Автоматическое удаление питомца в случае неудачи теста
                    test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete)
                    pytest.fail(f"Test failed at {test_read_info_pet_by_id.__name__}")

            else:
                # Автоматическое удаление питомца в случае неудачи теста
                test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete)
                pytest.fail(f"Test failed at {test_update_data_pet_by_id.__name__}")

        else:
            # Автоматическое удаление питомца в случае неудачи теста
            test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete)
            pytest.fail(f"Test failed at {test_read_info_pet_by_id.__name__}")

    else:
        # Автоматическое удаление питомца в случае неудачи теста
        test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete)
        pytest.fail(f"Test failed at {test_create_new_pet_by_id.__name__}")
