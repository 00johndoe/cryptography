from cryptography.fernet import Fernet

# Load key
with open("filekey.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Read encrypted file
with open("encrypted.txt", "rb") as enc_file:
    encrypted = enc_file.read()

try:
    # Decrypt
    decrypted = fernet.decrypt(encrypted)
except Exception as exc:
    print("❌ Decryption failed:", exc)
    raise

# Write original data back
with open("myfile.txt", "wb") as dec_file:
    dec_file.write(decrypted)

print("Decryption successful. Plaintext restored to myfile.txt")
from cryptography.fernet import Fernet
from crypto_utils import generate_key

password = input("Enter password: ")

with open("myfile.txt", "rb") as f:
    file_data = f.read()

salt = file_data[:16]
encrypted = file_data[16:]

key = generate_key(password, salt)
fernet = Fernet(key)

decrypted = fernet.decrypt(encrypted)

with open("myfile.txt", "wb") as f:
    f.write(decrypted)