from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


class Asymmetric:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_asymm_private_key(self):
        """
        Generating a special key using in asymmetric decryption.
        :return: private key
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        return private_key

    def generate_asymm_public_key(self, private_key):
        """
        Generating a special key using in asymmetric encryption.
        :param private_key: private key to make public key for encryption
        :return: public key
        """
        public_key = private_key.public_key()
        return public_key

    def encrypt_asymm_message(self, message, public_key):
        """
        Encrypting message using asymmetric method and public key generated in generate_asymm_public_key().
        :param message: message that will be encrypted
        :param public_key: public key for encryption
        :return: encrypted message
        """
        encrypted_message = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message

    def decrypt_asymm_message(self, message, private_key):
        """
        Decrypting message using asymmetric method and private key generated in generate_asymm_private_key().
        :param message: message that will be decrypted
        :param private_key: private key for decryption
        :return: decrypted message
        """
        decrypted_message = private_key.decrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_message

    def check_public_key(self, message, encrypted_message, public_key):
        """
        Checking if the message is encrypted with selected public key.
        :param message: message that we want to encrypt with selected public key
        :param encrypted_message: originally encrypted message
        :param public_key: public key that we want to check encryption
        :return: information if the messages were encrypted using the same public key
        """
        new_encrypted_message = self.encrypt_asymm_message(message, public_key)
        if new_encrypted_message == encrypted_message:
            return 'Message was encrypted with public key.'
        else:
            return 'Message was not encrypted with public key.'
