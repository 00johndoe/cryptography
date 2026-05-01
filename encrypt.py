from cryptography.fernet import Fernet

# Load key
with open("filekey.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Open file to encrypt
with open("myfile.txt", "rb") as file:
    original = file.read()

# Encrypt data
encrypted = fernet.encrypt(original)

# Write encrypted data to a separate file
with open("encrypted.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted)

print("Original:", original)
print("Encrypted:", encrypted)
print("Encrypted output saved to encrypted.txt")
from cryptography.fernet import Fernet
import os
from crypto_utils import generate_key

password = input("Enter password: ")

salt = os.urandom(16)
key = generate_key(password, salt)

fernet = Fernet(key)

with open("myfile.txt", "rb") as f:
    data = f.read()

encrypted = fernet.encrypt(data)

with open("myfile.txt", "wb") as f:
    f.write(salt + encrypted)  # store salt in file