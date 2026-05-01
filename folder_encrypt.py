import os
from cryptography.fernet import Fernet
from crypto_utils import generate_key

password = input("Password: ")
salt = os.urandom(16)
key = generate_key(password, salt)
fernet = Fernet(key)

folder = "test_folder"

for root, dirs, files in os.walk(folder):
    for file in files:
        path = os.path.join(root, file)

        with open(path, "rb") as f:
            data = f.read()

        encrypted = fernet.encrypt(data)

        with open(path, "wb") as f:
            f.write(salt + encrypted)

print("✅ Folder encrypted")