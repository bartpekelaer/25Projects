import random

print("Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()?[]_`~;@#$%^&*+="

pwds = input("How many Passwords would like: ")
pwds = int(pwds)

length = input("How long do you want the passwords to be: ")
length = int(length)

print("Here are your passwords: ")

for pwd in range(pwds):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
