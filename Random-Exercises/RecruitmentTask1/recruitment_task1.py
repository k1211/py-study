# Simple window/ console application like Windows Wizard
#
# INPUT:
# One element at a time:
# Name [string]
# Surname [string]
# Address [string]
# Phone number [string]
#
# OUTPUT:
# After filling all the data application should print it all out, every element in a new line
# Before the printing, user can go back to any step to change the given values.
import os

def ask_user():
    name = raw_input("Name: ")
    os.system('cls')
    surname = raw_input("Surname: ")
    os.system('cls')
    address = raw_input("Address: ")
    os.system('cls')
    phone = raw_input("Phone number: ")
    os.system('cls')

    return name, surname, address, phone

user_info = ["Name", "Surname", "Address", "Phone"]
user_data = list(ask_user())

phonebook = {}

def write_to_phonebook(db):
    for i in range(0,len(user_info)):
        phonebook[user_info[i]] = user_data[i]
    return phonebook

full_phonebook = write_to_phonebook(phonebook)

def print_phonebook(diki):
    for i in user_info:
        print i + ': ' + diki[i]

def edit_data(s):
    new_value = raw_input(str(s).capitalize() + ": ")
    full_phonebook[s] = new_value
    os.system('cls')
    return full_phonebook[s]

while True:
    ans = raw_input("Do you want to change anything? [name/surname/address/phone/no]")

    if ans == 'no':
        break
    else:
        for element in user_info:
            if ans.lower() in element.lower():
                edit_data(ans)
            else:
                continue

print_phonebook(full_phonebook)

