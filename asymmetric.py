from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


def generate_asymm_private_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key
def generate_asymm_public_key(private_key):
    public_key = private_key.public_key()
    return public_key
def encrypt_asymm_message(message, public_key):
    encrypted_message = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message
def decrypt_asymm_message(message, private_key):
    decrypted_message = private_key.decrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message

def check_public_key(message, encrypted_message, public_key):
    new_encrypted_message = encrypt_asymm_message(message, public_key)
    if new_encrypted_message == encrypted_message:
        return 'Message was encrypted with public key.'
    else:
        return 'Message was not encrypted with public key.'
