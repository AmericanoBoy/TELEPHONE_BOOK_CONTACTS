import os
os.system('')

def create_file():
    contact_file = 'contact.txt'
    new_file = open(contact_file, "w")
    new_file.write('ИМЯ,ФАМИЛИЯ,НОМЕР_ТЕЛЕФОНА\n')
    new_file.flush()
    new_file.close()
contact_file = None

def count_str_file():
    check_file = open('contact.txt','r')
    count_str = len(check_file.readlines())
    check_file.close()
    return count_str

def add_contact(new_contact):
    file = open('contact.txt', "a")
    new_contact_str = ','.join(new_contact)
    file.write(new_contact_str+'\n')
    file.close()

def search_contact(type_search, contact):
    file = open('contact.txt', "r")
    content_file = file.readlines()
    file.close()
    lst_temporary = []
    result_search = 'НЕ НАЙДЕН'
    for i in content_file:
        c = i.strip().split(',')
        lst_temporary.append(c)
    for i in lst_temporary[1:]:
        if i[int(type_search)-1].lower() == contact.lower():
            result_search = f': ИМЯ {i[0]}, ФАМИЛИЯ {i[1]}, ТЕЛЕФОН {i[2]}.'
    return result_search

def search_for_delete_contact(type_search, contact):
    file = open('contact.txt', "r")
    content_file = file.readlines()
    file.close()
    lst_temporary = []
    result_search = 'НЕ НАЙДЕН'
    for i in content_file:
        c = i.strip().split(',')
        lst_temporary.append(c)
    count = 0
    for i in lst_temporary:
        if i[int(type_search)-1].lower() == contact.lower():
            result_search = f': ИМЯ {i[0]}, ФАМИЛИЯ {i[1]}, ТЕЛЕФОН {i[2]}.'
            break
        count += 1
    result = [result_search, count]
    return result

def search_for_correct_contact(type_search, contact):
    file = open('contact.txt', "r")
    content_file = file.readlines()
    file.close()
    lst_temporary = []
    result_search = 'НЕ НАЙДЕН'
    lst_found_contact = None
    for i in content_file:
        c = i.strip().split(',')
        lst_temporary.append(c)
    count = 0
    for i in lst_temporary:
        if i[int(type_search)-1].lower() == contact.lower():
            lst_found_contact = i
            result_search = f': ИМЯ {i[0]}, ФАМИЛИЯ {i[1]}, ТЕЛЕФОН {i[2]}'
            break
        count += 1
    result = [result_search, count, lst_found_contact]
    return result


def delete_contact(number_string):
    file = open('contact.txt', "r")
    content_file = file.readlines()
    file.close()
    lst_temporary = [content_file[i] for i in range(len(content_file)) if i != number_string]
    file = open('contact.txt', "w")
    file.writelines(lst_temporary)
    file.close()

def correct_contact(new_contact,number_string):
    t = f'{new_contact[0]},{new_contact[1]},{new_contact[2]}'+'\n'
    file = open('contact.txt', "r")
    content_file = file.readlines()
    file.close()
    lst_temporary = [t if i == number_string else content_file[i] for i in range(len(content_file))]
    file = open('contact.txt', "w")
    file.writelines(item for item in lst_temporary )
    file.close()

def search_contact_some_part(type_search, contact):
    file = open('contact.txt', "r")
    content_file = file.readlines()
    file.close()
    z = []
    for i in content_file:
        c = i.strip().split(',')
        z.append(c)
    lst_result_not_search, lst_result_search = ['НЕ НАЙДЕНЫ.'], ['НАЙДЕНЫ :']
    for i in z[1:]:
        if contact.lower() in i[int(type_search)-1].lower():
            lst_result_search.append(f' ИМЯ {i[0]}, ФАМИЛИЯ {i[1]}, ТЕЛЕФОН {i[2]}.')
    return ["\n".join(lst_result_not_search),"\n".join(lst_result_search)][len(lst_result_search) != 1]

def show_all_contact():
    file = open('contact.txt', "r")
    content_file = file.readlines()
    file.close()
    lst_temporary = []
    for i in content_file:
        c = i.strip().split(',')
        lst_temporary.append(c)
    lst_saved_contacts = ["СПИСОК СОХРАНЕННЫХ КОНТАКТОВ В ВАШЕМ ПРИЛОЖЕНИИ:"  ]
    for i in lst_temporary:
        lst_saved_contacts.append(f' {i[0]}, {i[1]}, {i[2]}.')
    return "\n".join(lst_saved_contacts)

def show_all_contact_and_sort_name(type_sort):
    file = open('contact.txt', "r")
    content_file = file.readlines()
    file.close()
    lst_temporary = []
    lst_saved_contacts =[]
    temp_lst = []
    for i in content_file:
        c = i.strip().split(',')
        lst_saved_contacts.append(c)
    for i in lst_saved_contacts:
        temp_lst.append(i)
    lst_sort = sorted(temp_lst, key=lambda x: x[int(type_sort)])
    finish_sort_lst = []
    for i in lst_sort:
        finish_sort_lst.append(f' {i[0]}, {i[1]}, {i[2]}.')
    return "\n".join(finish_sort_lst)

def clearing_telephone_book():
    file = open('contact.txt', "w")
    file.write('ИМЯ,ФАМИЛИЯ,НОМЕР_ТЕЛЕФОНА\n')
    file.flush()
    file.close()
