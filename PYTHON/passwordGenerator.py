import string
import random

print("Welcome to the our random password generator")

# characters to generate password from
characters = list(string.ascii_letters + string.digits + string.punctuation)


def generate_random_password():
    # length of password from the user
    length = int(input("How many characters do you want in your password : "))

    # shuffling the characters
    random.shuffle(characters)

    # creating a password list to pick random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))
        print(password)

    # shuffling the resultant password
    random.shuffle(password)

    # converting the list to string
    password = "".join(password)
    # printing the list
    print("Your strong password is :", password)
    print("WOW!")#updation
    


# invoking the function
generate_random_password()
