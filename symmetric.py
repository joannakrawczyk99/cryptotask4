from cryptography.fernet import Fernet


def generate_fernet_key():
    """
    Generating a special key using in symmetric encryption and decryption.
    :return: key
    """
    key = Fernet.generate_key()
    fernet_key = Fernet(key)
    return fernet_key


def encrypt_symm_message(fernet_key, message):
    """
    Encrypting message using symmetric method and key generated in generate_fernet_key().
    :param fernet_key: generated key in generate_fernet_key()
    :param message: message that will be encrypted
    :return: encrypted message
    """
    return fernet_key.encrypt(message)


def decrypt_symm_message(fernet_key, message):
    """
    Decryptinh message using symmetric method and key generated in generate_fernet_key().
    :param fernet_key: key that is necessary for decrypting message
    :param message: encrypted message that will be decrypted
    :return: decrypted message
    """
    return fernet_key.decrypt(message)
