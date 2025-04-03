from utils_v2 import *

def test_create_status_code_v2():
    """Тестовая функция, которая показывает какой Status code имеет POST запрос после обработки и какой json-ответ приходит"""

    one = 4  # (200, 200, {'id': 4, 'category': {'id': 0, 'name': 'Antagonist'}, 'name': 'Madara', 'photoUrls': ['None'], 'tags': [{'id': 0, 'name': 'Have Susanoo'}], 'status': 'available'})
    two = "4"  # (200, 200, {'id': 4, 'category': {'id': 0, 'name': 'Antagonist'}, 'name': 'Madara', 'photoUrls': ['None'], 'tags': [{'id': 0, 'name': 'Have Susanoo'}], 'status': 'available'})
    tree = "***"  # (500, None, {'code': 500, 'type': 'unknown', 'message': 'something bad happened'})
    four = {}  # (500, None, {'code': 500, 'type': 'unknown', 'message': 'something bad happened'})
    five = None  # (200, 404, {'id': 9223372036854775807, 'category': {'id': 0, 'name': 'Antagonist'}, 'name': 'Madara', 'photoUrls': ['None'], 'tags': [{'id': 0, 'name': 'Have Susanoo'}], 'status': 'available'})
    six = "null"  # (200, 404, {'id': 9223372036854775807, 'category': {'id': 0, 'name': 'Antagonist'}, 'name': 'Madara', 'photoUrls': ['None'], 'tags': [{'id': 0, 'name': 'Have Susanoo'}], 'status': 'available'})

    One = test_create_new_pet_by_id_with_read_info(one, time_sleep=0)
    Two = test_create_new_pet_by_id_with_read_info(two, time_sleep=0)
    Tree = test_create_new_pet_by_id_with_read_info(tree, time_sleep=0)
    Four = test_create_new_pet_by_id_with_read_info(four, time_sleep=0)
    Five = test_create_new_pet_by_id_with_read_info(five, time_sleep=0)
    Six = test_create_new_pet_by_id_with_read_info(six, time_sleep=0)

    print(f'\n{one} = {One}\n{two} = {Two}\n{tree} = {Tree}\n{four} = {Four}\n{five} = {Five}\n{six} = {Six}')


def test_update_status_code_v2():
    """Тестовая функция, которая показывает какой Status code имеет UPDATE запрос после обработки и какой json-ответ приходит"""

    one = 4  # (200, 200, {'id': 4, 'category': {'id': 1, 'name': 'Protagonist'}, 'name': 'Naruto', 'photoUrls': ['None'], 'tags': [{'id': 0, 'name': 'Have Bijou'}], 'status': 'available'})
    two = "4"  # (200, 200, {'id': 4, 'category': {'id': 1, 'name': 'Protagonist'}, 'name': 'Naruto', 'photoUrls': ['None'], 'tags': [{'id': 0, 'name': 'Have Bijou'}], 'status': 'available'})
    tree = "***"  # (500, None, {'code': 500, 'type': 'unknown', 'message': 'something bad happened'})
    four = {}  # (500, None, {'code': 500, 'type': 'unknown', 'message': 'something bad happened'})
    five = None  # (200, 404, {'id': 9223372036854775807, 'category': {'id': 1, 'name': 'Protagonist'}, 'name': 'Naruto', 'photoUrls': ['None'], 'tags': [{'id': 0, 'name': 'Have Bijou'}], 'status': 'available'})
    six = "null"  # (200, 404, {'id': 9223372036854775807, 'category': {'id': 1, 'name': 'Protagonist'}, 'name': 'Naruto', 'photoUrls': ['None'], 'tags': [{'id': 0, 'name': 'Have Bijou'}], 'status': 'available'})

    One = test_update_data_pet_by_id_with_read_info(one, time_sleep=0)
    Two = test_update_data_pet_by_id_with_read_info(two, time_sleep=0)
    Tree = test_update_data_pet_by_id_with_read_info(tree, time_sleep=0)
    Four = test_update_data_pet_by_id_with_read_info(four, time_sleep=0)
    Five = test_update_data_pet_by_id_with_read_info(five, time_sleep=0)
    Six = test_update_data_pet_by_id_with_read_info(six, time_sleep=0)

    print(f'\n{one} = {One}\n{two} = {Two}\n{tree} = {Tree}\n{four} = {Four}\n{five} = {Five}\n{six} = {Six}')


def test_delete_status_code_v2():
    """Тестовая функция, которая показывает:
     Если запрос обработан успешно: какой Status code имеет DELETE запрос удаления после обработки и какой Status code имеет GET запрос проверки после обработки
     Если запрос оне удалось обработать: какой Status code имеет DELETE запрос после обработки и какой text-ответ приходит
    """

    one = 4  # (200, 404, '{"code":200,"type":"unknown","message":"4"}')
    two = "4"  # (200, 404, '{"code":200,"type":"unknown","message":"4"}')
    tree = "***"  # (404, None, {'code': 404, 'type': 'unknown', 'message': 'java.lang.NumberFormatException: For input string: "***"'})
    four = {}  # (404, None, {'code': 404, 'type': 'unknown', 'message': 'java.lang.NumberFormatException: For input string: "{}"'})
    five = None  # (404, None, {'code': 404, 'type': 'unknown', 'message': 'java.lang.NumberFormatException: For input string: "None"'})
    six = "null"  # (404, None, {'code': 404, 'type': 'unknown', 'message': 'java.lang.NumberFormatException: For input string: "null"'})

    One = test_delete_pet_by_id_with_read_info(one, time_sleep=0)
    Two = test_delete_pet_by_id_with_read_info(two, time_sleep=0)
    Tree = test_delete_pet_by_id_with_read_info(tree, time_sleep=0)
    Four = test_delete_pet_by_id_with_read_info(four, time_sleep=0)
    Five = test_delete_pet_by_id_with_read_info(five, time_sleep=0)
    Six = test_delete_pet_by_id_with_read_info(six, time_sleep=0)

    print(f'\n{one} = {One}\n{two} = {Two}\n{tree} = {Tree}\n{four} = {Four}\n{five} = {Five}\n{six} = {Six}')