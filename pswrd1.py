import random

print("This is a password generator")
print("============================")

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?0123456789"


question=input("Would you like a password?")

number=input("Enter number of passwords: ")
number=int(number)

length=input("Enter length of password: ")
length=int(length)

print("\nHere is your password")

for psd in range(number):
    Passwords=" "
    for pwd in range(length):
        Passwords += random.choice(chars)
    print(Passwords)
