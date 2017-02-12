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

def cls():
    os.system('cls')

class User():
    user_info = ["Name", "Surname", "Address", "Phone"]

    def __init__(self):
        self.name = ''
        self.surname = ''
        self.address = ''
        self.phone = ''
        self.user_data = []
        self.phonebook = {}

    def ask_user(self):
        cls()
        self.name = raw_input("Name: ")
        cls()
        self.surname = raw_input("Surname: ")
        cls()
        self.address = raw_input("Address: ")
        cls()
        self.phone = raw_input("Phone number: ")
        cls()

        self.user_data = [self.name, self.surname, self.address, self.phone]
        return self.user_data

    def write_to_phonebook(self):
        phonebook = {}
        for i in range(0,len(User.user_info)):
            phonebook[User.user_info[i]] = self.user_data[i]
        return phonebook

class Wizard(User):
    def __init__(self):
        User.__init__(self)
        # self.phonebook = {}

    def print_phonebook(self, book):
        for i in User.user_info:
            print i + ': ' + book[i]

    def edit_data(self, s):
        the_key = s.capitalize()
        new_value = raw_input(str(the_key).capitalize() + ": ")
        self.phonebook[the_key] = new_value
        cls()
        return self.phonebook

user = User()
dane = user.ask_user()
full_phonebook = user.write_to_phonebook()
wizard = Wizard()

def gra():

    while True:
        ans = raw_input("Do you want to change anything? [name/surname/address/phone/no]")


        if ans == 'no':
            cls()
            return full_phonebook
            break
        else:
            for key in full_phonebook:
                if ans.lower() == key.lower():
                    full_phonebook_edit = wizard.edit_data(ans)
                    return full_phonebook_edit
                    cls()
                else:
                    cls()
                    continue

result = gra()

wizard.print_phonebook(result)