
from cryptography.fernet import Fernet
import hashlib
import base64
def add_password_to_hash_file(master_password):
    hashed_password = hashlib.sha256(master_password.encode()).hexdigest()
    with open("password.hash", "w") as hash_file:
        hash_file.write(hashed_password)
    print("Password has been added to password.hash")
def write_key(master_password):
    key = Fernet.generate_key()
    hashed_password = hashlib.sha256(master_password.encode()).hexdigest()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    with open("password.hash", "w") as hash_file:
        hash_file.write(hashed_password)

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

def derive_key(master_password):
    digest = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def get_fernet(master_password):
    key = derive_key(master_password)
    return Fernet(key)

def verify_password(master_password):
    with open("password.hash", "r") as hash_file:
        stored_hash = hash_file.read()
    entered_hash = hashlib.sha256(master_password.encode()).hexdigest()
    return entered_hash == stored_hash

def view(fer):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            username, password = data.split("|")
            print("Username: " + username + " Password: " + str(fer.decrypt(password.encode()).decode()))

def add(fer):
    name = input("Account Name: ")
    passwo = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(passwo.encode()).decode() + "\n")

def main():
    master_password = input("What is your master password: ")
    add_password_to_hash_file(master_password)

    
    if not verify_password(master_password):
        print("Incorrect master password.")
        return
    
    fer = get_fernet(master_password)

    while True:
        mode = input("Would you like to add a new password or view existing ones (Enter either 'view' or 'add' or 'q' to quit): ")
        if mode == "q":
            break
        elif mode == "view":
            view(fer)
        elif mode == "add":
            add(fer)
        else:
            print("Invalid mode")

if __name__ == "__main__":
    main()
