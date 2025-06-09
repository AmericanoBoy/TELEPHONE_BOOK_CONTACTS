import ui
import modul
import control
import contr
def run():
    ui.print_info("ДОБРО ПОЖАЛОВАТЬ В ПРИЛОЖЕНИЕ КОНСОЛИ 'КНИГА КОНТАКТОВ'")
    CORRECT_INPUT = 'UNCORRECT'
    count_mistake = 0
    while CORRECT_INPUT == 'UNCORRECT':
        command = ui.input_user("Создать приложение 'КНИГА КОНТАКТОВ'? (да/нет):")
        if command == "нет" or count_mistake == 3:
            ui.print_info('ДО СВИДАНИЯ. БУДЕМ ЖДАТЬ ВАС СНОВА')
            return None
        elif command == "да":
            m = modul.create_file()
            ui.print_info("ПРИЛОЖЕНИЕ 'КОНТАКТНАЯ КНИГА' ЗАПУЩЕНО И ГОТОВО К ДАЛЬНЕЙШЕЙ РАБОТЕ")
            core_run(m)
            CORRECT_INPUT = 'CORRECT'
        else:
            count_mistake += 1
            ui.print_info("ВВЕДЕНА НЕВЕРНАЯ КОМАНДА (ВЫБИРТЕ: да/нет): ")
            if count_mistake == 3:
                ui.print_3_mistake_in_start_work()
                CORRECT_INPUT = 'CORRECT'

    return  CORRECT_INPUT
def core_run(m):
    TOTAL_COUNT_MISTAKE = 0
    while True:
        exist_file = control.check_existence_file()
        count_str = 0
        if exist_file == True:
            count_str = [4,11][modul.count_str_file() > 1]
            ui.print_menu(count_str)
        command = ui.input_user("Выберите действие:")
        if command == "1":
            ui.print_info('СОЗДАЕМ НОВЫЙ КОНТАКТ')
            lst_contact = ['имя', 'фамилию', 'номер телефона']
            count = 0
            count_mistake = 0
            new_contact = []
            temp_lst=[]
            count_control_names_valid = 0
            count_exist_telephone_number = 0
            count_correct_telephone = 0
            all_dates_valid = False
            while count != 3 and count_control_names_valid != True:
                name = ui.input_user(f'Введитите {lst_contact[count]} контакта: ')
                temp_lst.append(name.lower())
                count += 1
                if len(temp_lst) == 2:
                    valid_input = control.valid_input_1(temp_lst, count)
                    if valid_input != None:
                        new_contact = temp_lst
                    else:
                        ui.print_info(f'{" ".join(temp_lst)} УЖЕ СУЩЕСТВУЕТ В ТЕЛЕФОННОЙ КНИГЕ!')
                        ui.print_info(f'ВВЕДИТЕ {" и ".join(lst_contact[:2])}  КОРРЕКТНО!')
                        count = 0
                        temp_lst = []
                        count_mistake += 1
                        if count_mistake == 3:
                            count_control_names_valid = True
                            ui.print_3_mistake_command()
                if len(temp_lst) == 3:
                    correct_telephone = contr.valid_search_number(temp_lst[-1])  #v
                    if correct_telephone == temp_lst[2]:
                        exist_telephone_in_book = control.valid_tel(correct_telephone) #r
                        if exist_telephone_in_book == correct_telephone:
                            count_control_names_valid = True
                            new_contact = temp_lst
                            all_dates_valid = True
                        else:
                            ui.print_info("УКАЗАННЫЙ НОМЕР УЖЕ СУЩЕСТВУЕТ В СПИСКЕ КОНТАКТОВ!")
                            count = 2
                            temp_lst = temp_lst[:2]
                            count_exist_telephone_number += 1
                            if count_exist_telephone_number == 3:
                                count_control_names_valid = True
                    else:
                        ui.print_info(correct_telephone)
                        count_correct_telephone += 1
                        count = 2
                        temp_lst = temp_lst[:2]
                        if count_correct_telephone == 3:
                            ui.print_3_mistake_command()
                            count_control_names_valid = True
            if len(new_contact) == 3 and count_control_names_valid == 1 and all_dates_valid == True:
                modul.add_contact(new_contact)
                ui.print_info("НОВЫЙ КОНТАКТ УСПЕШНО ДОБАВЛЕН")

        elif command == "2" and count_str > 4:
            ui.print_info("ДЛЯ РЕДАКТИРОВАНИЯ СОХРАННОГО РАНЕЕ КОНТАТКА НЕОБХОДИМО ЕГО НАЙТИ.")
            CORRECT_INPUT = 'ВВЕДЕНА НЕВЕРНАЯ КОМАНДА'
            count_mistake = 0
            search_contact = None
            while CORRECT_INPUT == 'ВВЕДЕНА НЕВЕРНАЯ КОМАНДА':
                type_search = ui.input_user("Выберите принцип поиска {1:по имени,2:по фамилии,3:по номеру телефона.}:  ")
                if type_search in ['1', '2', '3']:
                    CORRECT_INPUT = 'ВВЕДЕНА ВЕРНАЯ КОМАНДА'
                    if type_search in ['1', '2']:
                        contact = ui.input_user(f"Введите {['имя', 'фамилию'][int(type_search) - 1]} искомого контакта: ")
                        search_contact = modul.search_for_correct_contact(type_search, contact)
                        ui.print_result(f"ИСКОМЫЙ КОНТАКТ {search_contact[0]}")
                    if type_search == '3':
                        valid = 0
                        count_uncorrect_input_telephone = 0
                        while valid == 0:
                            contact = ui.input_user(f"Введите телефон искомого контакта: ")
                            result_correct = contr.valid_search_number(contact)
                            if result_correct == contact:
                                search_contact = modul.search_for_correct_contact(type_search, contact)
                                ui.print_result(f"ИСКОМЫЙ КОНТАКТ {search_contact[0]}")
                                valid = 1
                            if result_correct != contact:
                                ui.print_info(result_correct)
                                count_uncorrect_input_telephone += 1
                                if count_uncorrect_input_telephone == 3:
                                    ui.print_3_mistake_command()
                                    valid = 1
                else:
                    ui.print_info(CORRECT_INPUT)
                    if count_mistake == 2:
                        CORRECT_INPUT = 'ВВЕДЕНА ВЕРНАЯ КОМАНДА'
                        ui.print_3_mistake_command()
                    count_mistake += 1
            if search_contact != None and search_contact[0] != 'НЕ НАЙДЕН':
                result_correct = 0
                finish_correct = False
                finish_correct_2 = 0
                while result_correct == 0 :
                    correct = ui.input_user("РЕДАКТИРОВАТЬ НАЙДЕННЫЙ КОНТАКТ? (1-да/2-нет):  ")
                    if correct == "1":
                        ui.print_info('РЕДАКТИРУЕМ СУЩЕСТВУЮЩИЙ КОНТАКТ')
                        lst_contact = [['новое имя', 'прежнее'],['новую фамилию', 'прежнюю'], ['новый номер телефона','прежний']]
                        lst_contact_for_correct = ['имя', 'фамилия', 'номер телефона']
                        count = 0
                        count_mistake = 0
                        new_contact = []
                        temp_lst = []
                        count_control_names_valid = 0  # y
                        count_exist_telephone_number = 0  # s
                        count_correct_telephone = 0  # x
                        while count != 3 and count_control_names_valid != True:
                            ui.print_info(f'{lst_contact_for_correct[count]} контакта: {search_contact[-1][count]} ')
                            name = ui.input_user(f'Введите {lst_contact[count][0]} контакта или сохраните {lst_contact[count][-1]}: ')
                            temp_lst.append(name.lower())
                            count += 1
                            if len(temp_lst) == 2:
                                valid_input = control.valid_input_for_correct(temp_lst, count,search_contact[1])
                                if valid_input != None:
                                    new_contact = temp_lst
                                else:
                                    ui.print_info(f'{" ".join(temp_lst)} УЖЕ СУЩЕСТВУЕТ В ТЕЛЕФОННОЙ КНИГЕ!')
                                    ui.print_info(f'ВВЕДИТЕ {" и ".join(lst_contact_for_correct[:2])}  КОРРЕКТНО!')
                                    count = 0
                                    temp_lst = []
                                    count_mistake += 1
                                    if count_mistake == 3:
                                        count_control_names_valid = True
                                        ui.print_3_mistake_command()
                            if len(temp_lst) == 3:
                                correct_telephone = contr.valid_search_number(temp_lst[-1])  # v
                                if correct_telephone == temp_lst[2]:
                                    exist_telephone_in_book = control.valid_tel_for_correct(correct_telephone, search_contact[1])  # r
                                    if exist_telephone_in_book == correct_telephone:
                                        new_contact = temp_lst
                                        modul.correct_contact(new_contact, search_contact[1])
                                        count_control_names_valid = True
                                        finish_correct = True
                                    else:
                                        ui.print_info("УКАЗАННЫЙ НОМЕР УЖЕ СУЩЕСТВУЕТ В СПИСКЕ КОНТАКТОВ!")
                                        count = 2
                                        temp_lst = temp_lst[:2]
                                        count_exist_telephone_number += 1
                                        if count_exist_telephone_number == 3:
                                            count_control_names_valid = True
                                else:
                                    ui.print_info(correct_telephone)
                                    count_correct_telephone += 1
                                    count = 2
                                    temp_lst = temp_lst[:2]
                                    if count_correct_telephone == 3:
                                        ui.print_3_mistake_command()
                                        count_control_names_valid = True
                    if finish_correct == True:
                        result_correct = 1
                    if correct == "2":
                        ui.print_info('КОНТАКТ ОСТАВЛЕН В ТЕЛЕФОННОЙ КНИГЕ БЕЗ ИЗМЕНЕНИЙ.')
                        result_correct = 1
                    else:
                        finish_correct_2 += 1
                        if finish_correct == 3:
                            ui.print_3_mistake_command()
                            result_correct = 1

        elif command == "3" and count_str > 4:
            ui.print_info("ДЛЯ УДАЛЕНИЯ СОХРАННОГО РАНЕЕ КОНТАТКА НЕОБХОДИМО ЕГО НАЙТИ.")
            CORRECT_INPUT = 'ВВЕДЕНА НЕВЕРНАЯ КОМАНДА'
            count_mistake = 0
            while CORRECT_INPUT == 'ВВЕДЕНА НЕВЕРНАЯ КОМАНДА':
                type_search = ui.input_user("Выберите принцип поиска {1:по имени,2:по фамилии,3:по номеру телефона.}:  ")
                if type_search in ['1', '2', '3']:
                    CORRECT_INPUT = 'ВВЕДЕНА ВЕРНАЯ КОМАНДА'
                    if type_search in ['1', '2']:
                        contact = ui.input_user(f"Введите {['имя', 'фамилию'][int(type_search) - 1]} искомого контакта: ")
                        search_contact = modul.search_for_delete_contact(type_search, contact)
                        ui.print_info(f'ИСКОМЫЙ КОНТАКТ {search_contact[0]}')
                        real_delete_contact = ui.input_user("ВЫ ПОДТВЕРЖДАЕТЕ УДАЛЕНИЕ КОНТАКТА (1- да/2-нет)?  ")
                        if real_delete_contact == "1":
                            modul.delete_contact(search_contact[-1])
                            ui.print_info("КОНТАКТ УДАЛЕН ИЗ ТЕЛЕФОНННОЙ КНИГИ.")
                        if real_delete_contact == "2":
                            ui.print_info("КОНТАКТ ОСТАВЛЕН В ТЕЛЕФОНННОЙ КНИГЕ")
                    if type_search == '3':
                        valid = 0
                        count_uncorrect_input_telephone = 0
                        while valid == 0:
                            contact = ui.input_user(f"Введите телефон искомого контакта: ")
                            result_correct = contr.valid_search_number(contact)
                            if result_correct == contact:
                                search_contact = modul.search_for_delete_contact(type_search, contact)
                                ui.print_result(f'ИСКОМЫЙ КОНТАКТ {search_contact[0]}')
                                real_delete_contact = ui.input_user("ВЫ ПОДТВЕРЖДАЕТЕ УДАЛЕНИЕ КОНТАКТА (1- да/2-нет)?  ")
                                if real_delete_contact == "1":
                                    modul.delete_contact(search_contact[-1])
                                    ui.print_info("КОНТАКТ УДАЛЕН ИЗ ТЕЛЕФОНННОЙ КНИГИ.")
                                    valid = 1
                                if real_delete_contact == "2":
                                    ui.print_info("КОНТАКТ ОСТАВЛЕН В ТЕЛЕФОНННОЙ КНИГЕ")
                                    valid = 1
                            if result_correct != contact:
                                ui.print_info(result_correct)
                                count_uncorrect_input_telephone += 1
                                if count_uncorrect_input_telephone == 3:
                                    ui.print_3_mistake_command()
                                    valid = 1
                else:
                    ui.print_info(CORRECT_INPUT)
                    if count_mistake == 2:
                        CORRECT_INPUT = 'ВВЕДЕНА ВЕРНАЯ КОМАНДА'
                        ui.print_3_mistake_command()
                    count_mistake += 1

        elif command == "4" and count_str > 4:
            ui.print_info("ВКЛЮЧЕНА ФУНКЦИЯ 'ПОИСК КОНТАКТА ПО ИМЕНИ, ФАМИЛИИ ИЛИ НОМЕРУ ТЕЛЕФОНА'")
            CORRECT_INPUT = 'ВВЕДЕНА НЕВЕРНАЯ КОМАНДА'
            count_mistake = 0
            while CORRECT_INPUT == 'ВВЕДЕНА НЕВЕРНАЯ КОМАНДА':
                type_search = ui.input_user("Выберите принцип поиска {1:по имени,2:по фамилии,3:по номеру телефона.}:  ")
                if type_search in ['1', '2', '3']:
                    CORRECT_INPUT = 'ВВЕДЕНА ВЕРНАЯ КОМАНДА'
                    if type_search in ['1', '2']:
                        contact = ui.input_user(f"Введите {['имя', 'фамилию'][int(type_search)-1]} искомого контакта: ")
                        search_contact = modul.search_contact(type_search, contact)
                        ui.print_info(f'ИСКОМЫЙ КОНТАКТ {search_contact}')
                    if type_search == '3':
                        valid = False
                        count_valid = 0
                        while valid == False:
                            contact = ui.input_user(f"Введите телефон искомого контакта: ")
                            result_correct = contr.valid_search_number(contact)
                            if result_correct == contact:
                                search_contact = modul.search_contact(type_search, contact)
                                ui.print_result(f'ИСКОМЫЙ КОНТАКТ {search_contact}')
                                valid = True
                            else:
                                ui.print_info(result_correct)
                                count_valid += 1
                                if count_valid == 3:
                                    valid = True
                                    ui.print_3_mistake_command()
                else:
                    count_mistake += 1
                    ui.print_info(CORRECT_INPUT)
                    if count_mistake == 3:
                        CORRECT_INPUT = 'ВВЕДЕНА ВЕРНАЯ КОМАНДА'
                        ui.print_3_mistake_command()

        elif command == "5" and count_str > 4:
            ui.print_info("ВКЛЮЧЕНА ФУНКЦИЯ 'ПОИСК КОНТАКТА ПО ЧАСТИ: ИМЕНИ, ФАМИЛИИ ИЛИ НОМЕРА ТЕЛЕФОНА'")
            CORRECT_INPUT = 'ВВЕДЕНА НЕВЕРНАЯ КОМАНДА'
            count_mistake = 0
            while CORRECT_INPUT == 'ВВЕДЕНА НЕВЕРНАЯ КОМАНДА':
                type_search = ui.input_user("Выберите принцип поиска {1:по  части имени,2:по части фамилии,3:по части номера телефона.}:  ")
                if type_search in ['1', '2', '3']:
                    CORRECT_INPUT = 'ВВЕДЕНА ВЕРНАЯ КОМАНДА'
                    if type_search in ['1', '2']:
                        contact = ui.input_user(f"Введите часть{[' имени', ' фамилии'][int(type_search)-1]} искомого контакта: ")
                        search_contact = modul.search_contact_some_part(type_search, contact)
                        ui.print_result(f'ИСКОМЫЕ КОНТАКТЫ {search_contact}')
                    if type_search == '3':
                        valid = False
                        count_valid = 0
                        while valid == False:
                            contact = ui.input_user(f"Введите телефон искомого контакта: ")
                            result_correct = contr.valid_search_number_part(contact)
                            if result_correct == contact:
                                search_contact = modul.search_contact_some_part(type_search, contact)
                                ui.print_result(f'ИСКОМЫЙ КОНТАКТ {search_contact}')
                                valid = True
                            else:
                                ui.print_info(result_correct)
                                count_valid += 1
                                if count_valid == 3:
                                    valid = True
                                    ui.print_3_mistake_command()

                else:
                    count_mistake += 1
                    ui.print_info(CORRECT_INPUT)
                    if count_mistake == 3:
                        CORRECT_INPUT = 'ВВЕДЕНА ВЕРНАЯ КОМАНДА'
                        ui.print_3_mistake_command()

        elif command == "6" and count_str > 4:
            contacts_telephone_book = modul.show_all_contact()
            ui.print_result(contacts_telephone_book)

        elif command == "7":
            count_mistake = 0
            CORRECT_INPUT = "НЕВЕРНАЯ КОМАНДА"
            while CORRECT_INPUT == "НЕВЕРНАЯ КОМАНДА":
                confirmation_command = ui.input_user("ВЫ УВЕРЕНЫ, ЧТО ХОТИТЕ ОЧИСТИТЬ КНИГУ КОНТАКТОВ: (да/нет):  ")
                if confirmation_command == "да":
                    modul.clearing_telephone_book()
                    CORRECT_INPUT = "ВЕРНАЯ КОМАНДА"
                elif confirmation_command == "нет":
                    ui.print_info("КНИГА КОНТАКТОВ СОХРАНЕНА")
                    CORRECT_INPUT = "ВЕРНАЯ КОМАНДА"
                else:
                    count_mistake += 1
                    ui.print_info("ДОПУСТИМЫЕ КОМАНДЫ: (да/нет)")
                    if count_mistake == 3:
                        CORRECT_INPUT = "ВЕРНАЯ КОМАНДА"
                        ui.print_3_mistake_command()
        elif command == "8" and count_str > 4:
            count_mistake = 0
            command_sort = 'ВВЕДЕНА НЕВЕРНАЯ КОМАНДА'
            while count_mistake <= 2 and command_sort == 'ВВЕДЕНА НЕВЕРНАЯ КОМАНДА' :
                type_sort = ui.input_user("КАК ПРОИЗВОДИТЬ СОРТИРОВКУ КОНТАКТОВ (1-по имени/2-по фамилии):  ")
                if type_sort in ['1','2']:
                    result_sort = modul.show_all_contact_and_sort_name(type_sort)
                    command_sort = 'ВВЕДЕНА ВЕРНАЯ КОМАНДА'
                    count_mistake = 3
                    ui.print_info(f"OТСОРТИРОВАННАЯ  ПО {['ИМЕНАМ','ФАМИЛИЯМ'][int(type_sort)]} КНИГА КОНТАКТОВ:")
                    ui.print_result(result_sort)
                else:
                    ui.print_info(command_sort)
                    if count_mistake == 2:
                        ui.print_3_mistake_command()
                    count_mistake += 1
        elif command == "чао":
            return None
        else:
            TOTAL_COUNT_MISTAKE += 1
            ui.print_info("ВАШЕЙ КОМАНДЫ НЕТ В СПИСКЕ ДОСТУПНЫХ!!!")
            if TOTAL_COUNT_MISTAKE == 3:
                ui.print_3_mistake_in_start_work()
                return None


