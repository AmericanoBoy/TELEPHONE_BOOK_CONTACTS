
def valid_input_number(string):
    valid = string
    valid = [None, valid][len(valid) == 11 and valid[:2] == '89' and sum(i.isdigit() for i in valid) == 11]
    return valid

def valid_search_number(contact):
    control_mistake= [sum(i.isalpha() for i in contact) != 0, len(contact) != 11, len(contact) == 11 and contact[:2] != '89' ]
    lst_mistake=[ 'ПРИСУТСТВУЮТ НЕДОПУСТИМЫЕ СИМВОЛЫ', 'КОЛ-ВО ЭЛЕМЕНТОВ НЕ РАВНО 11', 'ПРИ 11 ЦИФРАХ НОМЕРА ОН ДОЛЖЕН НАЧИНАТЬСЯ С: "89"']
    mistake_input = ''
    for i in range(len(control_mistake)):
        if control_mistake[i] == True:
            mistake_input += ' И '+lst_mistake[i]
    return [contact, f'В ВВЕДЕННОМ НОМЕРЕ {mistake_input[3:]}'][len(mistake_input) != 0]

def valid_search_number_part(contact):
    control_mistake = [sum(i.isalpha() for i in contact) != 0, len(contact) > 11, len(contact) == 11 and contact[:2] != '89']
    lst_mistake = ['ПРИСУТСТВУЮТ НЕДОПУСТИМЫЕ СИМВОЛЫ', 'КОЛ-ВО ЭЛЕМЕНТОВ   БОЛЬШЕ 11', 'ПРИ 11 ЦИФРАХ НОМЕРА ОН ДОЛЖЕН НАЧИНАТЬСЯ С: "89"']
    mistake_input = ''
    for i in range(len(control_mistake)):
        if control_mistake[i] == True:
            mistake_input += ' И ' + lst_mistake[i]
    return [contact, f'В ВВЕДЕННОМ НОМЕРЕ {mistake_input[3:]}'][len(mistake_input) != 0]



