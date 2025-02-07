from cryptography.fernet import Fernet

# decryptions key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message(message: str) -> str:
    """encryption"""
    return cipher_suite.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message: str) -> str:
    """decryption"""
    return cipher_suite.decrypt(encrypted_message.encode()).decode()
