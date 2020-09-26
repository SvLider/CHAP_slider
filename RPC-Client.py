import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')


pw = "abc12345"
str_random_num = str(s.sign_in())

import hashlib
string = pw + str_random_num
hash_num = hashlib.md5(string.encode('utf-8')).hexdigest()

print(str_random_num)
print(hash_num)

print(s.hash_function(hash_num))


print(s.add(2,3))  # Returns 5
print(s.div(5,2))  # Returns 5//2 = 2
print(s.pow(2,3))  # Returns 2**3 = 8

# Print list of available methods
print(s.system.listMethods())