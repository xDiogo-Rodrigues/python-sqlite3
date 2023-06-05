import os
from banco import Banco
from funcoes_main import register_person, edit_email, edit_address, edit_surname,delete_person_record, list_person_data, data_person
banco = Banco()
banco.create_table_people()

choice = '1'
    
while choice == '1':
    choice = input('What would you like to do?\n1: Register\n2: Edit address\n3: Edit email\n4: Edit surname\n5: Delete person record\n6: List perosnal data\n0: Exit\nChoice: ')
    if choice == '1':
        data_new_person = register_person()
        print(banco.entering_personal_data(*data_new_person))
    elif choice == '2':
        repeat_edit_address = '1'
        while repeat_edit_address == '1':
            data_new_address = edit_address()
            print(banco.update_address(*data_new_address))
            print('-------------------------------------')
            repeat_edit_address = input('Would you like to edit address again? 1 = Yes | 2 = No\nChoice: ')
            choice = '1'
    elif choice == '3':
        repeat_edit_email = '1'
        while repeat_edit_email == '1':
            data_new_email = edit_email()
            print(banco.update_email(*data_new_email))
            print('-------------------------------------')
            repeat_edit_email = input('Would you like to edit email again? 1 = Yes | 0 = No\nChoice: ')
            choice = '1'
    elif choice == '4':
        repeat_edit_surname = '1'
        while repeat_edit_surname == '1':
            data_new_surname = edit_surname()
            print(banco.update_surname(*data_new_surname))
            print('-------------------------------------')
            repeat_edit_surname = input('Would you like to edit surname again? 1 = Yes | 0 = No\nChoice: ')
            choice = '1'
    elif choice == '5':
        repeat_delete = '1'
        while repeat_delete == '1':
            print(banco.delete_person(delete_person_record()))
            repeat_delete = input('Would you like to delete record person again? 1 = Yes | 0 = No\nChoice: ')
            choice = '1'
    elif choice == '6':
        repeat_list_data = '1'
        while repeat_list_data == '1':
            email_person = list_person_data()
            list_data_person = banco.list_person_data(email_person)
            if list_data_person == 0:
                print('There is no record with this email!')
            else:
                data_person(list_data_person)
            repeat_list_data = input('Do you want to delete any more person records? 1 = Yes | 0 = No\nChoice: ')
            choice = '1'
    elif choice == '0':
        print('Saindo do programa!!')
        





































