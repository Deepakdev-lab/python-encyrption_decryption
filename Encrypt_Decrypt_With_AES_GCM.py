from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate a random 128-bit key for AES-GCM
key = os.urandom(16)

# Data to be encrypted
plaintext = b"hello world"

# Initialize AES-GCM cipher
cipher = Cipher(algorithms.AES(key), modes.GCM(b'\x00' * 12), backend=openssl.backend)
encryptor = cipher.encryptor()

# Encrypt the data
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Get the authentication tag
tag = encryptor.tag

# Initialize AES-GCM cipher
decryptor = cipher.decryptor()

# Decrypt the data
decrypted_plaintext = decryptor.update(ciphertext)

# Verify the integrity of the ciphertext and the authenticity of the sender
try:
    decrypted_plaintext += decryptor.finalize_with_tag(tag)
except Exception as e:
    print("The ciphertext has been tampered with or the sender is not authentic.")


print (decrypted_plaintext.decode())

