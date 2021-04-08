from fastapi import FastAPI

from asymmetric import generate_asymm_private_key, generate_asymm_public_key, encrypt_asymm_message, \
    decrypt_asymm_message, check_public_key
from symmetric import generate_fernet_key, encrypt_symm_message, decrypt_symm_message

mess = b'encrypt me'
symmetric_key = generate_fernet_key()
symmetric_encrypted_message = encrypt_symm_message(symmetric_key, mess)
symmetric_decrypted_message = decrypt_symm_message(symmetric_key, symmetric_encrypted_message)
print(symmetric_key)
print(symmetric_encrypted_message)
print(symmetric_decrypted_message)
print()
asymmetric_private_key = generate_asymm_private_key()
asymmetric_public_key = generate_asymm_public_key(asymmetric_private_key)
asymm_encrypted_message = encrypt_asymm_message(mess, asymmetric_public_key)
asymm_decrypted_message = decrypt_asymm_message(asymm_encrypted_message, asymmetric_private_key)
sign_public_key = check_public_key(mess, asymm_encrypted_message, asymmetric_public_key)
print(asymmetric_private_key)
print(asymmetric_public_key)
print(asymm_encrypted_message)
print(asymm_decrypted_message)



app = FastAPI()


@app.get("/")
def say_hello():
    return {"Hello everyone!"}


@app.get("/symetric/key")
def get_symmetric_key():
    return symmetric_key

@app.post("/symetric/encode")
def post_symmetric_encode():
    return symmetric_encrypted_message

@app.post("/symetric/decode")
def post_symmetric_encode():
    return symmetric_decrypted_message


@app.get("/asymetric/key")
def get_asymmetric_key():
    return {"Klucz publiczny": asymmetric_public_key,
            "Klucz prywatny": asymmetric_private_key}


@app.post("/asymetric/sign")
def post_asymmetric_sign():
    return sign_public_key

@app.post("/asymetric/encode")
def post_asymmetric_encode():
    return asymm_encrypted_message


@app.post("/asymetric/decode")
def post_asymmetric_decode():
    return asymm_decrypted_message

