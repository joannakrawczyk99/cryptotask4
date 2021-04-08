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


# GET symetric/key -> zwraca losowo wygenerowany klucz symetryczny w postaci HEXów (może być JSON)
@app.get("/symetric/key")
def get_symmetric_key():
    return symmetric_key


# POST symetric/key -> ustawia na serwerze klucz symetryczny podany w postaci HEX w request

# POST symetric/encode -> wysyłamy wiadomość, w wyniku dostajemy ją zaszyfrowaną
@app.post("/symetric/encode")
def post_symmetric_encode():
    return symmetric_encrypted_message


# POST symetric/decode -> wysyłamy wiadomość, w wyniku dostajemy ją odszyfrowaną
@app.post("/symetric/decode")
def post_symmetric_encode():
    return symmetric_decrypted_message


# GET asymetric/key -> zwraca nowy klucz publiczny i prywatny w postaci HEX (w JSON jako dict) i ustawia go na serwerze
@app.get("/asymetric/key")
def get_asymmetric_key():
    return {"Klucz publiczny": asymmetric_public_key,
            "Klucz prywatny": asymmetric_private_key}

# GET asymetric/key/ssh -> zwraca klucz publiczny i prywatny w postaci HEX zapisany w formacie OpenSSH
# POST asymetric/key -> ustawia na serwerze klucz publiczny i prywatny w postaci HEX (w JSON jako dict)
# POST asymetric/verify -> korzystając z aktualnie ustawionego klucza prywatnego, podpisuje wiadomość i zwracaą ją podpisaną


# POST asymetric/sign -> korzystając z aktualnie ustawionego klucza publicznego, weryfikuję czy wiadomość była zaszyfrowana przy jego użyciu
@app.post("/asymetric/sign")
def post_asymmetric_sign():
    return sign_public_key

# POST asymetric/encode -> wysyłamy wiadomość, w wyniku dostajemy ją zaszyfrowaną
@app.post("/asymetric/encode")
def post_asymmetric_encode():
    return asymm_encrypted_message


# POST asymetric/decode -> wysyłamy wiadomość, w wyniku dostajemy ją odszyfrowaną
@app.post("/asymetric/decode")
def post_asymmetric_decode():
    return asymm_decrypted_message

