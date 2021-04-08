from asymmetric import generate_asymm_private_key, generate_asymm_public_key, encrypt_asymm_message, \
    decrypt_asymm_message
from symmetric import generate_fernet_key, encrypt_symm_message, decrypt_symm_message




if __name__ == "__main__":
    mess = b'encrypt me'
    #symmetric_key = generate_fernet_key()
    #symmetric_encrypted_message = encrypt_symm_message(symmetric_key, mess)
    #symmetric_decrypted_message = decrypt_symm_message(symmetric_key, symmetric_encrypted_message)
    #print(symmetric_encrypted_message)
    #print(symmetric_decrypted_message)

    asymmetric_private_key = generate_asymm_private_key()
    asymmetric_public_key = generate_asymm_public_key(asymmetric_private_key)

    #print(asymmetric_public_key)
    #print(asymmetric_private_key)
    asymm_encrypted_message = encrypt_asymm_message(mess, asymmetric_public_key)
    asymm_decrypted_message = decrypt_asymm_message(asymm_encrypted_message, asymmetric_private_key)
    print(asymm_encrypted_message)
    print(asymm_decrypted_message)