import os
from cryptography.fernet import Fernet
from crypto_utils import generate_key

password = input("Enter password: ")

folder = "test_folder"

for root, dirs, files in os.walk(folder):
    for file in files:
        path = os.path.join(root, file)

        with open(path, "rb") as f:
            file_data = f.read()

        try:
            # Extract salt (first 16 bytes)
            salt = file_data[:16]
            encrypted = file_data[16:]

            key = generate_key(password, salt)
            fernet = Fernet(key)

            decrypted = fernet.decrypt(encrypted)

            with open(path, "wb") as f:
                f.write(decrypted)

            print(f"✅ Decrypted: {path}")

        except Exception as e:
            print(f"⚠️ Skipped (not encrypted or wrong password): {path}")