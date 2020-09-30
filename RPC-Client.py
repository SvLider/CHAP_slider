import xmlrpc.client
import getpass

s = xmlrpc.client.ServerProxy('http://localhost:8000')


# Iniiate connection
str_random_num = str(s.sign_in())
print(str_random_num)

# Get user inputm (username, password)
username = getpass.getuser(prompt="Bitte username angeben: " ) 
password = getpass.getpass(prompt="Bitte Passwort angeben: ")
if username != "" and password != ""
    login = s.check_login(username, password)
        if login == True:
            
            import hashlib
            string = password + str_random_num
            hash_num = hashlib.md5(string.encode('utf-8')).hexdigest()
            print(hash_num)
            
            print(s.hash_function(hash_num))
        else:
            print("Daten nicht korrekt")
            break                
else:
    print("Logindaten dürfen nicht leer sein.")
    break

#pw = "abc12345"



print(s.add(2,3))  # Returns 5
print(s.div(5,2))  # Returns 5//2 = 2
print(s.pow(2,3))  # Returns 2**3 = 8

# Print list of available methods
print(s.system.listMethods())