from cryptography.fernet import Fernet

def encrypt_file(path):
    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(path, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(data)
    encrypted_path = path + ".encrypted"

    with open(encrypted_path, "wb") as f:
        f.write(encrypted)

    with open(path, "wb") as f:
        f.write(encrypted)

    return encrypted_path
