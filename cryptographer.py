import random as r

l = list("abcdefghijklmnopqrstuvwxyz")
l1 = l.copy()
key = []

f = open("key.txt",'w+')
if not f:
    for i in range(26):
        rint = r.randint(0,25)
        key.append(l[rint])
        l.pop(rint)
    del l
        

def encrypter(s):
    encrypted_message = ""
    ls = str(s).split()
    for i in ls:
        for j in i:
            x = j
            word = ""
            for k in l1:
                if x == k:
                    x = key[l1.index(k)]
                    word += j
        encrypted_message += str(word)+" "
    return encrypted_message

def decrypter(s):
    decrypted_message = ""
    ls = str(s).split()
    for i in ls:
        for j in i:
            x = j
            word = ""
            for k in key:
                if x == k:
                    x = l1[key.index(k)]
                    word += j
        decrypted_message += str(word)+" "
    return decrypted_message

#main
while True:
    print("1. Encrypt message\n2. Decrypt message\n3.Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        s = input("Enter sentence:")
        encrypter(s)
    elif ch == 2:
        s = input("Enter sentence:")
        decrypter(s)
    elif ch == 3:
        break
    else:
        print("Invalid input")

