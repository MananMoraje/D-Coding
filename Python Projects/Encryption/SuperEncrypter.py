import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = input('Enter password   ')
password = password_provided.encode()

salt = b'8uKx3TDpOTvVx7-JUTEE9HCAnV2w1ciPyA14L5FZPec='
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64decode(kdf.derive(password))
print(key)
