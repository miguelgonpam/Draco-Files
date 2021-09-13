from pyfiglet import Figlet
import os
import os.path
from cryptography.fernet import Fernet
from PyPDF2 import PdfFileWriter, PdfFileReader
import time

class Menu():
    
    def Encrypt():
        key = Fernet.generate_key()
        pathFile = input('\n Input file and path, example /root/tools/main.py >> ')
        path = os.path.dirname(pathFile)
        with open(f'{path}/file_key.key', 'wb') as filekey:
            filekey.write(key)
        fernet = Fernet(key)
        with open(pathFile, 'rb') as f:
            file = f.read()
        encrypt_file = fernet.encrypt(file)
        with open(pathFile, 'wb') as encrypted_file:
            encrypted_file.write(encrypt_file)

        print('\n File encrypted ')

    def Decrypt():
        pathFile = input('\n Input file and path, example /root/tools/main.py >> ')
        path = os.path.dirname(pathFile)
        with open(f'{path}/file_key.key', 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        with open(pathFile, 'rb') as f:
            file = f.read()
        decrypt_file = fernet.decrypt(file)
        with open(pathFile, 'wb') as decrypted_file:
            decrypted_file.write(decrypt_file)

        print('\n File decrypted')
    def Exit():
        exit()

def pFiglet(text):
    printFiglet= Figlet(font='starwars')
    return str(printFiglet.renderText(text))
print(pFiglet("Draco-Files"))
print('\n version 0.1')
print('\n [01] Encrypt file')
print('\n [02] Decrypt file')
print('\n')
print('\n [99] Exit')
print('\n')
option= input('\n Select option >> ')
menu = Menu()

if (option == '01'):
    print('\n')
    Menu.Encrypt()
elif (option == '02'):
    print('\n')
    Menu.Decrypt()
elif (option == '99'):
    exit
else:
    print('\n Syntax error, try again')
    time.sleep(1.5)
    exit
    
    


