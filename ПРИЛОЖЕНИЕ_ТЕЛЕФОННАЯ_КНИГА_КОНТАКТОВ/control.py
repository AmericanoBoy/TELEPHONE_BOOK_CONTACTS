import core
import modul
import contr

import os.path

def valid_input_1(new_contact,count):
    file = open('contact.txt', "r")
    content_file = file.readlines()
    valid = new_contact
    file.close()
    z = []
    for i in content_file:
        c = i.strip().split(',')
        z.append(c)
    for i in z:
        if i[:count] == new_contact and count<3:
            valid = None
        if i[count-1] == new_contact[-1] and count==3:
            valid = None
    return valid

def valid_input_for_correct(new_contact,count,exeption):
    file = open('contact.txt', "r")
    content_file = file.readlines()
    valid = new_contact
    file.close()
    z = []
    for i in content_file:
        c = i.strip().split(',')
        z.append(c)
    count_exception = 0
    for i in z:
        if count_exception != exeption:
            if i[:count] == new_contact and count<3:
                valid = None
            if i[count-1] == new_contact[-1] and count==3:
                valid = None
        count_exception += 1
    return valid


def valid_tel(number):
    file = open('contact.txt', "r")
    content_file = file.readlines()
    valid = number
    file.close()
    z = []
    for i in content_file:
        c = i.strip().split(',')
        z.append(c)
    for i in z:
        if i[-1] == number:
            valid = None
    return valid

def valid_tel_for_correct(number,exception):
    file = open('contact.txt', "r")
    content_file = file.readlines()
    valid = number
    file.close()
    z = []
    count = 0
    for i in content_file:
        c = i.strip().split(',')
        z.append(c)
    for i in z:
        if i[-1] == number and count != exception:
            valid = None
        count += 1
    return valid

def valid_input(name,count):
    file = open('contact.txt', "r")
    content_file = file.readlines()
    valid = name
    file.close()
    z = []
    for i in content_file:
        c = i.strip().split(',')
        z.append(c)
    for i in z:
        if i[count].lower() == name.lower() and count <2:
            valid = None
        if count == 2:
            valid_number = contr.valid_input_number(name)
            if valid_number == None:
               valid = None
    return valid

def check_existence_file():
    name_file = 'contact.txt'
    return os.path.exists(name_file)
