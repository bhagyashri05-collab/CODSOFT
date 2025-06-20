import random
import string

print("Welcome to the Password Generator")

# Ask the user for password length
length = input("How long should the password be? ")

# Convert input to integer
length = int(length)

# Characters to use in the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_chars = letters + digits + symbols

# Create the password
password = ""

for i in range(length):
    password += random.choice(all_chars)

# Show the password
print("\nYour generated password is:")
print(password)
print("-----------------------------")
