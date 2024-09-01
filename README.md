# Password Manager
 
A simple and secure password manager using Python, leveraging cryptography for encryption and hashing for secure password storage.

## Features

1. Encryption: Uses cryptography.fernet for encrypting and decrypting passwords.
2. Hashing: Implements SHA-256 hashing for secure master password storage.
3. File Handling: Stores encrypted passwords and hashed master password in files.
4. User Interaction: Command-line interface for adding and viewing passwords.

## Usage
1. Run the script:
   . python password_manager.py

2. Follow the prompts:
   Enter your master password.
   Choose to add a new password or view existing ones.

## Code Overview
**add_password_to_hash_file(master_password)**
   - Hashes the master password and writes it to password.hash.

**write_key(master_password)**
   - Generates an encryption key, hashes the master password, and writes both to files.

**load_key()**
   - Reads the encryption key from key.key.

**derive_key(master_password)**
- Hashes the master password and encodes it in base64.

**get_fernet(master_password)**
- Creates a Fernet object using the derived key.

**verify_password(master_password)**
- Verifies the entered master password by comparing it with the stored hash.

**view(fer)**
- Reads and decrypts passwords from passwords.txt and prints them.

**add(fer)**
- Prompts the user for an account name and password, encrypts the password, and writes it to passwords.txt.
