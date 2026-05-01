#!/usr/bin/env python3
"""
Professional Encryption Tool
Encrypt and decrypt files and folders using Fernet symmetric encryption.
"""

import argparse
import os
import sys
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken
from crypto_utils import generate_key


def encrypt_file(file_path: Path, password: str):
    """Encrypt a single file."""
    salt = os.urandom(16)
    key = generate_key(password, salt)
    fernet = Fernet(key)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(file_path, "wb") as f:
        f.write(salt + encrypted)

    print(f"✅ Encrypted: {file_path}")


def decrypt_file(file_path: Path, password: str):
    """Decrypt a single file."""
    with open(file_path, "rb") as f:
        data = f.read()

    if len(data) < 16:
        raise ValueError("File too small to be encrypted")

    salt = data[:16]
    encrypted = data[16:]

    key = generate_key(password, salt)
    fernet = Fernet(key)

    try:
        decrypted = fernet.decrypt(encrypted)
    except InvalidToken:
        raise ValueError("Invalid password or corrupted file")

    with open(file_path, "wb") as f:
        f.write(decrypted)

    print(f"✅ Decrypted: {file_path}")


def encrypt_folder(folder_path: Path, password: str):
    """Encrypt all files in a folder recursively."""
    salt = os.urandom(16)
    key = generate_key(password, salt)
    fernet = Fernet(key)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = Path(root) / file
            try:
                with open(file_path, "rb") as f:
                    data = f.read()

                encrypted = fernet.encrypt(data)

                with open(file_path, "wb") as f:
                    f.write(salt + encrypted)

                print(f"✅ Encrypted: {file_path}")
            except Exception as e:
                print(f"⚠️ Skipped {file_path}: {e}")


def decrypt_folder(folder_path: Path, password: str):
    """Decrypt all files in a folder recursively."""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = Path(root) / file
            try:
                with open(file_path, "rb") as f:
                    data = f.read()

                if len(data) < 16:
                    print(f"⚠️ Skipped (too small): {file_path}")
                    continue

                salt = data[:16]
                encrypted = data[16:]

                key = generate_key(password, salt)
                fernet = Fernet(key)

                decrypted = fernet.decrypt(encrypted)

                with open(file_path, "wb") as f:
                    f.write(decrypted)

                print(f"✅ Decrypted: {file_path}")
            except InvalidToken:
                print(f"⚠️ Skipped (invalid password or not encrypted): {file_path}")
            except Exception as e:
                print(f"⚠️ Skipped {file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Professional Encryption Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Encrypt command
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt files or folders")
    encrypt_parser.add_argument("path", type=Path, help="Path to file or folder")
    encrypt_parser.add_argument("--password", required=True, help="Encryption password")

    # Decrypt command
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt files or folders")
    decrypt_parser.add_argument("path", type=Path, help="Path to file or folder")
    decrypt_parser.add_argument("--password", required=True, help="Decryption password")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    path = args.path
    password = args.password

    if not path.exists():
        print(f"❌ Path does not exist: {path}")
        sys.exit(1)

    try:
        if args.command == "encrypt":
            if path.is_file():
                encrypt_file(path, password)
            elif path.is_dir():
                encrypt_folder(path, password)
            else:
                print("❌ Invalid path type")
                sys.exit(1)
        elif args.command == "decrypt":
            if path.is_file():
                decrypt_file(path, password)
            elif path.is_dir():
                decrypt_folder(path, password)
            else:
                print("❌ Invalid path type")
                sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()