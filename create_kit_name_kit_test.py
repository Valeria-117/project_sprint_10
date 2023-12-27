import data
import request_sender

# Позитивная проверка
def positive_assert(test_name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = test_name
    new_kit = request_sender.post_new_client_kit(kit_body)
    assert new_kit.status_code == 201
    assert new_kit.json()["name"] == test_name

# Негативная проверка
def negative_assert(test_name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = test_name
    new_kit = request_sender.post_new_client_kit(kit_body)
    assert new_kit.status_code == 400

# Негативная проверка на 10 тест
def negative_assert_clear_kit_body():
    kit_body = data.kit_body.copy().clear()
    new_kit = request_sender.post_new_client_kit(kit_body)
    assert new_kit.status_code == 400

# Тест 1. Допустимое количество символов (1)
def test_1():
    positive_assert("a")

# Тест 2. Допустимое количество символов (511)
def test_2():
    positive_assert(data.name511)

# Тест 3. Количество символов меньше допустимого (0)
def test_3():
    negative_assert("")

# Тест 4. Количество символов больше допустимого (512)
def test_4():
    negative_assert(data.name512)

# Тест 5. Разрешены английские буквы
def test_5():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы
def test_6():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы
def test_7():
    positive_assert("№%@,")

# Тест 8. Разрешены пробелы
def test_8():
    positive_assert(" Человек и КО ")

# Тест 9. Разрешены цифры
def test_9():
    positive_assert("123")

# Тест 10. Параметр не передан в запросе
def test_10():
    negative_assert_clear_kit_body()

# Тест 11. Передан дргой тип параметра
def test_11():
    negative_assert(123)