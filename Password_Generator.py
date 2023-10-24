import string
import random

characters= list(string.ascii_letters + string.digits + "!@#$%&*/")

def generate_password():
    password_length=int(input("How long would you like your password to be? "))
    print("-"*50)
    random.shuffle(characters)
    password=[]

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password ="".join(password)
    print(password)
    print("-"*50)


option=input("Do you want to generate a new password? (Yes or no): ")
print("-"*50)

if option=="Yes" or option=="yes":
    generate_password()
    
elif option=="No" or option=="no":
    print("Program Ended")
else:
    print("Invalid input\nPlease enter either 'yes' or 'no")
    


