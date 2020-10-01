import xmlrpc.client
import getpass
import time
import hashlib

s = xmlrpc.client.ServerProxy('http://localhost:8000')

while True:

    # Get user input (username, password)
    username = input("Bitte username angeben: ") 
    password = getpass.getpass(prompt="Bitte Passwort angeben: ")


    # Iniiate connection
    str_random_num = str(s.sign_in(username))

    if str_random_num != "0":
        string = password + str_random_num
        hash_value = hashlib.md5(string.encode('utf-8')).hexdigest()
    else:
        pass


    if username != "" and password != "":
        login = bool(s.check_login(username, hash_value))
        if login:
                
            print("Add: 2 + 3 = " + str(s.add(2,3)))  # Returns 5
            print("Div: 5/2 = " + str(s.div(5,2)))  # Returns 5//2 = 2
            print("Pow: 2³ = " + str(s.pow(2,3)))  # Returns 2**3 = 8

            # Print list of available methods
            print(s.system.listMethods())
            break
        else:
            print("Daten nicht korrekt")                
    else:
        print("Logindaten dürfen nicht leer sein.")
        time.sleep(1)
    



