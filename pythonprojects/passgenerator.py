import random

print("Welcome to password generator :D")

symb = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+=<>?/[]{},.:;"

number = int(input("Enter how many passwords you want to generate: "))

length = int(input("Enter your passwords length: "))
print("\nhere are your passwords: ")

for i in range(number):
    answer = ""
    for x in range(length):
        answer = answer + random.choice(symb)
    print(answer)
