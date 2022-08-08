#pip3 install pandas
#importação das dependencias

import re
import pandas as pd
import os  
import sys 
import getpass 
import string
import re
import pwd 
string.ascii_lowercase 
string.ascii_uppercase 
string.ascii_letters 
string.digits 
string.punctuation 
from random import choice
import string
import subprocess
import pwd

#definindo função de criação de usuario!
def add_user(name, password, email):    
    os.system('net', name, password, '/add')  
    print("User: "), print(name)
    print("Password: "), print(password)
    print("USUARIO CRIADO COM SUCESSO!!! ")  
        


#definindo strings para gerar o password.

width = 10
width2 = 4
value = string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters + string.digits
value2 = string.digits

#definindo strings para a leitura e manipulação do CSV.
 
table = pd.read_csv("UsersGoogleWorkSpace.csv")
tabble_df = pd.DataFrame(table)

#Aqui eu puxo as informalçoes do CSV para usar
# na criação de Usuarios, que já está declarado no meu def.

for index, row in tabble_df.iterrows():
    name = row['First Name [Required]']
    email = row['Email Address [Required]']
    password = ''
    uiid = ''
    for i in range(width):
        password += choice(value)
    for i in range(width2):
        uiid  += choice(value2)
        
        # Acrescentei posteriormente uma função
        # para realizar a checagem de Users duplicados
        # por tanto mesmo a tabela sendo atualizada o scrpit
        # continua funcional
        
    username = name
    usernames = [x[0] for x in pwd.getpwall()]
    if username in usernames:
        print("Usuario "), print(name), print("Já Existe!!!")
    else:
        add_user(name, password, email,)


    