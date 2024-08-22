import random
import string

def generate_password(length):
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


try:
    length = int(input("Enter the password length: "))
    password = generate_password(length)
    if password:
        print("Generated password:", password)
except ValueError:
    print("Please enter a valid number.")