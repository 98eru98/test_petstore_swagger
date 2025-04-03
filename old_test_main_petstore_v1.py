from utils_v2 import *


# [4, "74568", (-1), 0, "***", None, "null", {}] Список проверок

@pytest.mark.parametrize("pet_id", [4])
def test_CRUD(pet_id):
    """
    Функция тестирования полного цикла создания, изменения, удаления питомца (https://petstore.swagger.io/#/)
    При возникновении ошибок во время теста, тест прекращается с результатом "FAILED" и созданный питомец автоматически удаляется
    Status code create == SCC
    Status code read == SCR
    Status code update == SCU
    Status code delete == SCD
    Результат теста может быть True или False
    """
    # Устанавливаем время задержки между циклами авто удаления питомца, при возникновении ошибки
    time_sleep_manual_delete = 2

    t_create = test_create_new_pet_by_id_with_read_info(pet_id, time_sleep=10)   # Возвращаем (SCC, SCR, SCC_response.text, результат теста)
    if t_create[3]:  # Проверяем, что возвращаемый результат теста True

        t_update = test_update_data_pet_by_id_with_read_info(pet_id, time_sleep=10)  # Возвращаем (SCU, SCR, SCU_response.text, результат теста)
        if t_update[3]:  # Проверяем, что возвращаемый результат теста True

            t_delete = test_delete_pet_by_id_with_read_info(pet_id, time_sleep=10)  # Возвращаем (SCD, SCR, SCC_response.text, результат теста)
            if t_delete[3]:  # Проверяем, что возвращаемый результат теста True

                print("✔️✔️✔️ALL TESTS PASSED✔️✔️✔️")

            else:
                test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete)  # Автоматическое удаление питомца в случае неудачи теста
                pytest.fail(f"Test failed at {test_delete_pet_by_id_with_read_info.__name__}")  # Сообщение о том, в каком тесте произошла ошибка

        else:
            # Автоматическое удаление питомца в случае неудачи теста
            test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete)  # Автоматическое удаление питомца в случае неудачи теста
            pytest.fail(f"Test failed at {test_update_data_pet_by_id_with_read_info.__name__}")  # Сообщение о том, в каком тесте произошла ошибка

    else:
        # Автоматическое удаление питомца в случае неудачи теста
        test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete)  # Автоматическое удаление питомца в случае неудачи теста
        pytest.fail(f"Test failed at {test_create_new_pet_by_id_with_read_info.__name__}")  # Сообщение о том, в каком тесте произошла ошибка
