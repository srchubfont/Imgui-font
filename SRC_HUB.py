from cryptography.fernet import Fernet
from telegram.ext import ApplicationBuilder  # Ensure this import is correct for your setup

def load_user_data():
    print("User data loaded.")

def decrypt_and_run():
    # Key ko read karna
    with open('secret.key', 'rb') as key_file:
        key = key_file.read()

    cipher = Fernet(key)

    # Encrypted file ko read karna
    with open('SRC_HUB.enc', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    # Decrypt karna
    decrypted = cipher.decrypt(encrypted)

    # Execute the decrypted code directly in the current namespace
    try:
        exec(decrypted.decode(), globals())
    except Exception as e:
        print(f"Error executing the code: {e}")

if __name__ == "__main__":
    decrypt_and_run()
