from cryptography.fernet import Fernet

class Symmetric:

    def __init__(self):
        self.key = None

    def generate_fernet_key(self):
        """
        Generating a special key using in symmetric encryption and decryption.
        :return: key
        """
        key = Fernet.generate_key().hex()
        return key

    def set_key(self, key):
        return Fernet(bytearray.fromhex(key))

    def encrypt_symm_message(self, setted_key, message):
        """
        Encrypting message using symmetric method and key generated in generate_fernet_key().
        :param fernet_key: generated key in generate_fernet_key()
        :param message: message that will be encrypted
        :return: encrypted message
        """
        return setted_key.encrypt(message)

    def decrypt_symm_message(self, setted_key, message):
        """
        Decryptinh message using symmetric method and key generated in generate_fernet_key().
        :param fernet_key: key that is necessary for decrypting message
        :param message: encrypted message that will be decrypted
        :return: decrypted message
        """
        return setted_key.decrypt(message)
