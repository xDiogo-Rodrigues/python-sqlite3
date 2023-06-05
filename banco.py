import sqlite3

class Banco:
    def __init__(self):
        self.bank_name = sqlite3.connect('banco_dados.db')
        self.cursor = self.bank_name.cursor()

    def create_table_people(self):
        table_pessoas = ("CREATE TABLE IF NOT EXISTS pessoas(First Name text, Last_Name text, RG text, CPF text, Address text, Email text)")
        self.cursor.execute(table_pessoas)
    
    def entering_personal_data(self, first_name, last_name, rg_person, cpf_person, address_person, email_person):
        email_exists = self.there_is_person(email_person)
        if not email_exists:
            insert_values = ("INSERT INTO pessoas VALUES('"+first_name+"', '"+last_name+"', '"+rg_person+"', '"+cpf_person+"', '"+address_person+"', '"+email_person+"')")
            self.cursor.execute(insert_values)
            self.bank_name.commit()
            return f'Email successfully registered!'
        elif email_exists:
            return f'Email already registered'

    
    def there_is_person(self, email):
         person_search = ("SELECT *FROM pessoas WHERE Email = '"+email+"'")
         exist_person = self.cursor.execute(person_search)
         exists_in_the_list = list(exist_person)
         if not exists_in_the_list:
            return False
         else:
            return True

    def update_email(self, current_email, new_email):
        email_exists = self.there_is_person(current_email)
        if email_exists:
             update_email_person = ("UPDATE pessoas SET Email = '"+new_email+"' WHERE Email = '"+current_email+"'")
             self.cursor.execute(update_email_person)
             self.bank_name.commit()
             return f'Email modified!'
        else:
            return f'There is no record with this email!'
        
    def update_address(self,email, new_address):
        email_exists = self.there_is_person(email)
        if email_exists:
            update_address_person = ("UPDATE pessoas SET Address = '"+new_address+"' WHERE Email = '"+email+"'")
            self.cursor.execute(update_address_person)
            self.bank_name.commit()
            return f'Address modified!'
        else:
            return f'There is no record with this email!'
    
    def update_surname(self,email, new_surname):
        email_exists = self.there_is_person(email)
        if email_exists:
            update_surname_person = ("UPDATE pessoas SET Last_Name = '"+new_surname+"' WHERE Email = '"+email+"'")
            self.cursor.execute(update_surname_person)
            self.bank_name.commit()
            return f'Surname modified!'
        else:
            return f'There is no record with this email!'
    
    def delete_person(self,email):
        email_exists = self.there_is_person(email)
        if email_exists:
            delete_person = ("DELETE FROM pessoas WHERE Email = '"+email+"'")
            self.cursor.execute(delete_person)
            self.bank_name.commit()
            return f'Deleted person record!'
        else:
            return f'There is no record with this email!'
        
    def list_person_data(self, email):
        email_exists = self.there_is_person(email)
        if email_exists:
            data_person = ("SELECT *FROM pessoas WHERE Email = '"+email+"'")
            data = self.cursor.execute(data_person)
            lista_data = list(data)
            return lista_data
        
        return 0
        





       
        
        
        

