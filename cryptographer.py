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
print("Cipher:",cipher)
        

def encrypter():
    s = input("Enter sentence:")
    encrypted_message = ""
    ls = s.split()
    for i in ls:
        for j in i:
            word = ""
            for k,v in cipher.values():
                if k == j:
                    word += v
            encrypted_message += str(word)+" "
    print("Encrypted:",encrypted_message)

def decrypter():
    s = input("Enter sentence:")
    decrypted_message = ""
    ls = str(s).split()
    for i in ls:
        for j in i:
            word = ""
            for k,v in cipher:
                if j == k:
                    word += v
        decrypted_message += str(word)+" "
    print("Decrypted:",decrypted_message)

#main
while True:
    print("1. Encrypt message\n2. Decrypt message\n3.Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        s = input("Enter sentence:")
        encrypter()
    elif ch == 2:
        s = input("Enter sentence:")
        decrypter()
    elif ch == 3:
        break
    else:
        print("Invalid input")

