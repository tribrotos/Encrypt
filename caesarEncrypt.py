#run this apps in python3

def encrypt():
    plainText = input("Plaintext : ")
    shift = int(input("Shift : "))
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift
        else:
            stayInAlphabet = ord(ch)
        if stayInAlphabet > ord('z'):
            stayInAlphabet -= 26
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter
    print("=========<Result>========")
    print ("Ciphertext : "+str(cipherText))

def decrypte():
    encryption=input("Encrypted Text : ")
    encryption_shift=int(input("Shift : "))
    cipherText1 = ""
    for c in encryption:
        if c.isalpha():
            stayInAlphabet1 = ord(c) - encryption_shift
        else:
            stayInAlphabet1 = ord(c)
        if stayInAlphabet1 > ord('z'):
            stayInAlphabet1 += 26
        finalLetter1 = chr(stayInAlphabet1)
        cipherText1 += finalLetter1
    print("=========<Result>========")
    print ("Ciphertext : "+str(cipherText1))

print("Select mode for Caesar Cipher")
print("1. Encrypt")
print("2. Decrypt")
print("Press any key to close")
select = str(input("Select : "))
print("=========================")
if ((select) == '1'):
    encrypt()
elif ((select) == '2'):
    decrypte()
else:
    print("See you !")
