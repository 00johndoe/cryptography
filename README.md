# Professional Encryption Tool

A command-line tool for encrypting and decrypting files and folders using Fernet symmetric encryption with password-based key derivation.

## Features

- Encrypt/decrypt individual files
- Encrypt/decrypt entire folders recursively
- Password-based encryption using PBKDF2
- Robust error handling and validation
- Cross-platform compatibility

## Installation

1. Ensure Python 3.6+ is installed
2. Install dependencies:
   ```bash
   pip install cryptography
   ```

## Usage

### Encrypt a file
```bash
python app.py encrypt path/to/file.txt --password yourpassword
```

### Decrypt a file
```bash
python app.py decrypt path/to/file.txt --password yourpassword
```

### Encrypt a folder
```bash
python app.py encrypt path/to/folder --password yourpassword
```

### Decrypt a folder
```bash
python app.py decrypt path/to/folder --password yourpassword
```

### Get help
```bash
python app.py --help
```

## Security Notes

- Uses Fernet (AES 128) for encryption
- PBKDF2 with 100,000 iterations for key derivation
- Random salt per encryption operation
- Files are overwritten in-place (backup important files first)

## Examples

```bash
# Encrypt a sensitive document
python app.py encrypt secret.docx --password mysecretpass

# Encrypt an entire directory
python app.py encrypt private_folder --password mysecretpass

# Decrypt back
python app.py decrypt secret.docx --password mysecretpass
python app.py decrypt private_folder --password mysecretpass
```