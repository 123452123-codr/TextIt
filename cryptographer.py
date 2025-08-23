import random as r

l = list("abcdefghijklmnopqrstuvwxyz")
l1 = l.copy()
key = []
cipher = {}

n = 25
for i in range(25):
    rint = r.randint(0,n)
    key.append(l[rint])
    l.pop(rint)
    n -= 1
del l

for i in range(25):
    k = l1[i]
    v = key[i]
    cipher[k] = v

'''with open("cipher.txt","w+") as f:
    contents = f.read()
    if len(contents) == 0:
        pass'''
        

def encrypter(s):
    s_iter = str(s)
    encrypted_message = ""
    for i in s_iter:
        if i.isalpha():
            if i.isupper():
                for k,v in cipher.items():
                    if i.lower() == k:
                        encrypted_message += str(v).upper()
            else:
                for k,v in cipher.items():
                    if i == k:
                        encrypted_message += v
        else:
            encrypted_message += i
    print("Encrypted:",encrypted_message)

def decrypter(s):
    s_iter = str(s)
    decrypted_message = ""
    for i in s_iter:
        if i.isalpha():
            if i.isupper():
                for k,v in cipher.items():
                    if i.lower() == v:
                        decrypted_message += str(k).upper()
            else:
                for k,v in cipher.items():
                    if i == v:
                        decrypted_message += k
        else:
            decrypted_message += i
    print("Decrypted:",decrypted_message)

#main
while True:
    print("1. Encrypt message\n2. Decrypt message\n3.Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        s = input("Enter sentence:")
        print("Encrypted:",encrypter(s))
    elif ch == 2:
        s = input("Enter sentence:")
        print("Decrypted:",decrypter(s))
    elif ch == 3:
        break
    else:
        print("Invalid input")
