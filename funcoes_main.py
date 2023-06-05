import os
def register_person():
     first_name = input('Enter your name:\nName: ')
     last_name = input('Enter your surname\nSurname: ')
     your_rg = input('Enter your RG:\nRG: ')
     your_cpf = input('Enter your CPF:\nCPF: ')
     your_address = input('Enter your address:\nAddress: ')
     email = input('Enter your email:\nEmail: ')
     data_person = [first_name,last_name,your_rg, your_cpf, your_address, email]
     return data_person

def edit_address():
     print('--------- Edit Address ------------')
     email_person = input('Enter with email:\nEmail: ')
     new_address = input('Enter with new address:\nNew Address: ')
     data_address = [email_person, new_address]
     return data_address

def edit_email():
     print('---------- Edit Email ------------')
     email_current = input('Enter with email current:\nEmail current: ')
     new_email = input('Enter with new email:\nNew email: ')
     data_email = [email_current, new_email]
     return data_email

def edit_surname():
     print('---------- Edit Surname ------------')
     email_person = input('Enter with email:\nEmail: ')
     new_surname = input('Enter with new surname:\nNew surname: ')
     data_surname = [email_person, new_surname]
     return data_surname

def delete_person_record():
     print('----------- Delete Person Record --------------')
     email_person = input('Enter with email:\nEmail: ')
     return email_person

def list_person_data():
     print('----------- List Personal Data -------------')
     email_person = input('Enter with email:\nEmail: ')
     return email_person

def data_person(*args):
     os.system("cls")
     for arg in args:
          print(f'Name: {arg[0][0]}')
          print(f'Surname: {arg[0][1]}')
          print(f'RG: {arg[0][2]}')
          print(f'CPF: {arg[0][3]}')
          print(f'Endereço: {arg[0][4]}')
          print(f'Email: {arg[0][5]}')
