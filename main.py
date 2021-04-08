from fastapi import FastAPI

from asymmetric import Asymmetric
from keyModel import Key
from messageModel import Message
from symmetric import Symmetric

asymemtric = Asymmetric()
symmetric = Symmetric()



app = FastAPI()


@app.get("/")
def root():
    """
    :return: message with JSON
    """
    return {"message": "Hello everyone!"}


@app.get("/symetric/key")
def get_symmetric_key():
    """
    Generating key
    :return: symmetric key in hex
    """
    symmetric_key = symmetric.generate_fernet_key()
    return symmetric_key


@app.post("/symetric/key")
def post_symetric_key(key):
    """
    :param key: symmetric key in hex
    :return: Message that key has been set in JSON.
    """
    symmetric.set_key(key)
    return {"message": "Setted key."}


@app.post("/symetric/encode")
def post_symmetric_encode(message: Message, key: Key):
    """
    Posting message to symmetric encode.
    :param message: message object
    :param key: key object
    :return: encoded message
    """
    symmetric_encrypted_message = symmetric.encrypt_symm_message(key.value, message.value)
    return {"Encoded message": f"{symmetric_encrypted_message}"}


@app.post("/symetric/decode")
def post_symmetric_encode(message: Message, key: Key):
    """
    Posting message to symmetric decode.
    :param message: message object
    :param key: key object
    :return: decoded message
    """
    symmetric_decrypted_message = symmetric.decrypt_symm_message(key.value, message.value)
    return {"Decoded Message": f"{symmetric_decrypted_message}"}


@app.get("/asymetric/key")
def get_asymmetric_key():
    """
    :return: generated public and private asymmetric keys
    """
    asymmetric_private_key = asymemtric.generate_asymm_private_key()
    asymmetric_public_key = asymemtric.generate_asymm_public_key(asymmetric_private_key)
    return {"Public key": asymmetric_public_key,
            "Private key": asymmetric_private_key}


@app.post("/asymetric/sign")
def post_asymmetric_sign(message: Message, key: Key, encrypted_message):
    """
    :param message: message object
    :param key: key object
    :param encrypted_message: originally encrypted message
    :return: message about comparison
    """
    sign_public_key = asymemtric.check_public_key(message.value, encrypted_message, key.public_key)
    return sign_public_key


@app.post("/asymetric/encode")
def post_asymmetric_encode(message: Message, key: Key):
    """
    Posting message to asymmetric encode.
    :param message: message object
    :param key: key object
    :return: encoded message
    """
    asymm_encrypted_message = asymemtric.encrypt_asymm_message(message.value, key.public_key)
    return {"Encoded message": f"{asymm_encrypted_message}"}


@app.post("/asymetric/decode")
def post_asymmetric_decode(message: Message, key: Key):
    """
    Posting message to asymmetric decode.
    :param message: message object
    :param key: key object
    :return: decoded message
    """
    asymm_decrypted_message = asymemtric.decrypt_asymm_message(message.value, key.private_key)
    return {"Decoded message": f"{asymm_decrypted_message}"}
