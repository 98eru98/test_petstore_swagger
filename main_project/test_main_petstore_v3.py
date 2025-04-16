from main_project.utils_v2 import *

@pytest.fixture
def created_and_cleaned_pet():
    """ Фикстура, которая подготавливает окружение. Предварительно создаёт питомца и удаляет его после теста
    Status code create == SCC, Status code read == SCR """

    # Список проверок
    pet_id = [4, "74568", (-1), 0, "***", None, "null", {}][0]
    # Устанавливаем время задержки между циклами авто удаления питомца, при возникновении ошибки
    time_sleep_manual_delete = 2

    try:
        # Возвращаем (SCC, SCR, результат теста (True или False), SCC_response.text, SCR_response.text)
        t_create = test_create_new_pet_by_id_with_read_info(pet_id, time_sleep=10)
        # Проверяем успешность создания питомца
        if not t_create[2]:
            # Вызывает исключение остановки теста, если питомец не был создан
            raise Exception(f"❌❌❌Error: Failed to create pet with ID {pet_id}❌❌❌!")
        # Передаём pet_id в тест
        yield pet_id

    finally:
        # Автоматическое удаление питомца по итогам теста или если питомец не был создан
        test_manual_delete_pet(pet_id, time_sleep=time_sleep_manual_delete, fixture=True)


def test_update(created_and_cleaned_pet):
    # Передаём pet_id из подготовленного окружения
    pet_id = created_and_cleaned_pet
    # Возвращаем (SCU, SCR, результат теста, SCU_response.text, SCR_response.text)
    t_update = test_update_data_pet_by_id_with_read_info(pet_id, time_sleep=10)
    # Проверяем, что возвращаемый результат теста True, если нет, то сработает исключение
    if not t_update[2]:
        # Вызывает исключение остановки теста, если питомец не был создан
        raise Exception(f"❌❌❌Error: Failed to update pet with ID {pet_id}❌❌❌!")


