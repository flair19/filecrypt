from src.decripritor.decryptor import Decrypter

dc  = Decrypter()

message = "this is a b test"

encrypted_msg = dc.encrypt_text(text=message)
print(encrypted_msg)

decrypted_msg = dc.decrypt_text(encrypted_text=encrypted_msg)
print(decrypted_msg)



