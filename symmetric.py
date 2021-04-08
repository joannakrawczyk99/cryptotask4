from cryptography.fernet import Fernet

def generate_fernet_key():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return fernet

def encrypt_symm_message(f, message):
    return f.encrypt(message)

def decrypt_symm_message(f, message):
    return f.decrypt(message)