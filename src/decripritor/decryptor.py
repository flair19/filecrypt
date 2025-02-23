from tokenize import String
from cryptography.fernet import Fernet
import os


class Decrypter:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt_text(self, text: String) -> bytes:
        """
        Encrypts text using Fernet symmetric encryption
        Args:
            text (String): Text to encrypt
        Returns:
            bytes: Encrypted text
        """
        encoded_text = self.fernet.encrypt(text.encode())
        return encoded_text

    def decrypt_text(self, encrypted_text: bytes) -> str:
        """
        Decrypts encrypted text
        Args:
            encrypted_text (bytes): Encrypted text to decrypt
        Returns:
            str: Decrypted text
        """
        decrypted_text = self.fernet.decrypt(encrypted_text)
        return decrypted_text.decode()

    def encrypt_file(self, file_path: str) -> None:
        """
        Encrypts a file in place
        Args:
            file_path (str): Path to the file to encrypt
        """
        # Read the file content
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Encrypt the data
        encrypted_data = self.fernet.encrypt(file_data)

        # Write the encrypted data back to the file
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_file(self, file_path: str) -> None:
        """
        Decrypts an encrypted file in place
        Args:
            file_path (str): Path to the encrypted file
        """
        # Read the encrypted file
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()

        # Decrypt the data
        decrypted_data = self.fernet.decrypt(encrypted_data)

        # Write the decrypted data back to the file
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)

    def encrypt_audio(self, audio_path: str) -> None:
        """
        Encrypts an audio file in place
        Args:
            audio_path (str): Path to the audio file to encrypt
        """
        # Audio files are treated as binary files
        self.encrypt_file(audio_path)

    def decrypt_audio(self, audio_path: str) -> None:
        """
        Decrypts an encrypted audio file in place
        Args:
            audio_path (str): Path to the encrypted audio file
        """
        # Audio files are treated as binary files
        self.decrypt_file(audio_path)