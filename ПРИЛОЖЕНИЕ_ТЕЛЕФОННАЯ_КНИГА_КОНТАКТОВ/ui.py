
def print_info(message):
    print("\033[34minfo:\033[0m " + message)

def print_result(message):
    print(message)

def print_error(message):
    print("\033[91merror:\033[0m " + message)

def print_3_mistake_command():
    print("ВЫ ТРИЖДЫ ВВЕЛИ НЕДОПУСТИМУЮ КОМАНДУ! ВОЗВРАТ В ОСНОВНОЕ МЕНЮ.")

def print_3_mistake_in_start_work():
    print("ТРИЖДЫ ВВЕДЕНА НЕВЕРНАЯ КОМАНДА. ПРИЛОЖЕНИЕ ЗАКРЫТО.")

def input_user(message):
    print_info(message)
    return input(">>  ")

def print_matrix(matrix):
    for i in matrix:
        print(*i)

def print_menu(possible_command):
    available_comand = ["Доступные команды:",
                        "меню - Вывод меню",
                        "чао - Завершение работы",
                        "1 - Создать и сохранить новый контакт",
                        "2 - Редактирование сохраненного контакта",
                        "3 - Удаление сохраненного ранее контакта",
                        "4 - Поиск необходимого конакта по имени, фамилии  или номеру телефона",
                        "5 - Поиск необходимого контакта по части имени, фамилии или номера телефона",
                        "6 - Чтение и вывод на дисплей всех сохраненных контактов ",
                        "7 - Полная очистка телефонной книги и удаление всех сохраненных контактов ",
                        "8 - Сортровка телефонной книги по именам или фамилиям"]
    for i in available_comand[:possible_command]:
        print(i)
