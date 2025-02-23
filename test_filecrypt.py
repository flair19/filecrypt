import unittest
import os
import tempfile
from src.decripritor.decryptor import Decrypter


class TestDecrypter(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.decrypter = Decrypter()
        self.test_text = "Hello, World!"

        # Create temporary directory for test files
        self.temp_dir = tempfile.mkdtemp()

        # Create test files
        self.test_file_path = os.path.join(self.temp_dir, "test.txt")
        self.test_audio_path = os.path.join(self.temp_dir, "test.mp3")

        # Write test content to files
        with open(self.test_file_path, 'w') as f:
            f.write("Test file content")
        with open(self.test_audio_path, 'wb') as f:
            f.write(b"Fake audio content")

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        # Remove test files and directory
        for file_path in [self.test_file_path, self.test_audio_path]:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.rmdir(self.temp_dir)

    def test_init(self):
        """Test that initialization creates valid key and Fernet instance."""
        self.assertIsNotNone(self.decrypter.key)
        self.assertIsInstance(self.decrypter.key, bytes)
        self.assertIsNotNone(self.decrypter.fernet)

    def test_text_encryption_decryption(self):
        """Test text encryption and decryption."""
        # Test encryption
        encrypted_text = self.decrypter.encrypt_text(self.test_text)
        self.assertIsInstance(encrypted_text, bytes)
        self.assertNotEqual(encrypted_text, self.test_text.encode())

        # Test decryption
        decrypted_text = self.decrypter.decrypt_text(encrypted_text)
        self.assertEqual(decrypted_text, self.test_text)

    def test_text_encryption_with_empty_string(self):
        """Test text encryption with empty string."""
        empty_text = ""
        encrypted_text = self.decrypter.encrypt_text(empty_text)
        decrypted_text = self.decrypter.decrypt_text(encrypted_text)
        self.assertEqual(decrypted_text, empty_text)

    def test_text_encryption_with_special_characters(self):
        """Test text encryption with special characters."""
        special_text = "Hello! @#$%^&*()_+ 世界"
        encrypted_text = self.decrypter.encrypt_text(special_text)
        decrypted_text = self.decrypter.decrypt_text(encrypted_text)
        self.assertEqual(decrypted_text, special_text)

    def test_file_encryption_decryption(self):
        """Test file encryption and decryption."""
        original_content = "Test file content"

        # Test encryption
        self.decrypter.encrypt_file(self.test_file_path)
        with open(self.test_file_path, 'rb') as f:
            encrypted_content = f.read()
        self.assertNotEqual(encrypted_content, original_content.encode())

        # Test decryption
        self.decrypter.decrypt_file(self.test_file_path)
        with open(self.test_file_path, 'r') as f:
            decrypted_content = f.read()
        self.assertEqual(decrypted_content, original_content)

    def test_file_encryption_with_empty_file(self):
        """Test file encryption with empty file."""
        # Create empty file
        empty_file_path = os.path.join(self.temp_dir, "empty.txt")
        open(empty_file_path, 'w').close()

        # Test encryption and decryption
        self.decrypter.encrypt_file(empty_file_path)
        self.decrypter.decrypt_file(empty_file_path)

        # Verify file is still empty
        self.assertEqual(os.path.getsize(empty_file_path), 0)

        # Cleanup
        os.remove(empty_file_path)

    def test_audio_encryption_decryption(self):
        """Test audio file encryption and decryption."""
        original_content = b"Fake audio content"

        # Test encryption
        self.decrypter.encrypt_audio(self.test_audio_path)
        with open(self.test_audio_path, 'rb') as f:
            encrypted_content = f.read()
        self.assertNotEqual(encrypted_content, original_content)

        # Test decryption
        self.decrypter.decrypt_audio(self.test_audio_path)
        with open(self.test_audio_path, 'rb') as f:
            decrypted_content = f.read()
        self.assertEqual(decrypted_content, original_content)

    def test_file_not_found(self):
        """Test handling of non-existent files."""
        non_existent_file = os.path.join(self.temp_dir, "non_existent.txt")
        with self.assertRaises(FileNotFoundError):
            self.decrypter.encrypt_file(non_existent_file)

    def test_invalid_encrypted_data(self):
        """Test handling of invalid encrypted data."""
        invalid_encrypted_data = b"Invalid encrypted data"
        with self.assertRaises(Exception):
            self.decrypter.decrypt_text(invalid_encrypted_data)


if __name__ == '__main__':
    unittest.main()