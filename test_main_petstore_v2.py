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

    t_create = test_create_new_pet_by_id_with_read_info(pet_id, time_sleep=10)   # Возвращаем (SCC, SCR, результат теста, SCC_response.text, SCR_response.text)
    if not t_create[2]:  # Проверяем, что возвращаемый результат теста True, если нет, то сработает исключение
        test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete)  # Автоматическое удаление питомца в случае неудачи теста
        assert False, f"❌❌❌Error: Failed to create pet with ID {pet_id}❌❌❌!"  # Исключение остановки теста

    t_update = test_update_data_pet_by_id_with_read_info(pet_id, time_sleep=10) # Возвращаем (SCU, SCR, результат теста, SCU_response.text, SCR_response.text)
    if not t_update[2]:  # Проверяем, что возвращаемый результат теста True, если нет, то сработает исключение
        test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete)  # Автоматическое удаление питомца в случае неудачи теста
        assert False, f"❌❌❌Error: Failed to update pet with ID {pet_id}❌❌❌!"  # Исключение остановки теста

    # Check if pet deletion was successful
    t_delete = test_delete_pet_by_id_with_read_info(pet_id, time_sleep=10)  # Возвращаем (SCD, SCR, результат теста, SCC_response.text, SCR_response.text)
    if not t_delete[2]:  # Проверяем, что возвращаемый результат теста True, если нет, то сработает исключение
        test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete)  # Автоматическое удаление питомца в случае неудачи теста
        assert False, f"❌❌❌Error: Failed to delete pet with ID {pet_id}❌❌❌!"  # Исключение остановки теста

    print("✔️✔️✔️ALL TESTS PASSED✔️✔️✔️")