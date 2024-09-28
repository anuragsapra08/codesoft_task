import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# password generator function
def password_generator(size):
    chars = upper + lower + digits + symbols
    password = ''
    for i in range(size):
        password += random.choice(chars)
    return password

print(password_generator(8))
print(password_generator(12))