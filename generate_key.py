from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()

# Save key to a file
with open("filekey.key", "wb") as key_file:
    key_file.write(key)