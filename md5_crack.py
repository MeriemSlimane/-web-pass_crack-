# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)

import hashlib


hashes = open("admins.txt","r").read().split("\n")
wordlist = open("wordlist.txt","r").read().split("\n")



users = {} # initiate users dictionary with hashed passwords
found = {} # initiate users dictionary for cracked passwords

print("username and their passwords hashes")
for i in hashes:
	username = i.split(":")[0]
	password = i.split(":")[1]
	users[username]=password
	for clear_password in wordlist:
		encoded =  hashlib.md5(clear_password.encode()).hexdigest()
		if password == encoded:
			found[username]=clear_password


print("************** Password Founds ************** ")
for f in found:
	print("[+] Password found {} ==> {}".format(f,found[f]))

intersection = list(set(list(found.keys())).symmetric_difference(list(users.keys())))
print("************** Password Not Cracked ************** ")
for nf in intersection:
	print("[-] Password not found {} ==> {}".format(nf,users[nf]))
