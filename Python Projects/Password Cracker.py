import hashlib

flag = 0
counter = 0

pass_hash = input("Insert md5 hash: ")
wordlist = input("File name: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    print(word)
    print(digest)
    print(pass_hash)
    counter += 1

    if digest == pass_hash:
        print("Password has been found: ")
        print("Password" + word)
        flag += 1
        break

if flag == 0:
    print("Password is not in the list")