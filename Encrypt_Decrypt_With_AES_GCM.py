from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate a random 256-bit key (32 bytes)
key = os.urandom(32)

# Generate a random 12-byte IV
iv = os.urandom(12)

# Create a new AES-GCM cipher
cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
encryptor = cipher.encryptor()

# Encrypt the message
actual_message = "This is a secret message."
message = bytes(actual_message, 'utf-8')

ciphertext = encryptor.update(message) + encryptor.finalize()
tag = encryptor.tag


print (ciphertext)


decryptor = cipher.decryptor()

# Verify the integrity of the ciphertext and the authenticity of the sender
try:
    decryptor.authenticate_additional_data(tag)
    print("Looks good")
except Exception as e:
    print("The ciphertext has been tampered with or the sender is not authentic.")

# Decrypt the message    
plaintext = decryptor.update(ciphertext) + decryptor.finalize(tag)
print(plaintext) # b"This is a secret message."
