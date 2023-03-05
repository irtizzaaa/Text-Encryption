from cryptography.fernet import Fernet

# generate a new encryption key
key = Fernet.generate_key()

# create a new Fernet cipher object using the encryption key
cipher = Fernet(key)

# define the plaintext message to be encrypted
plaintext = "Hello, world!"

# encrypt the plaintext message using the Fernet cipher
ciphertext = cipher.encrypt(plaintext.encode())

# print the encrypted ciphertext
print("Encrypted message:", ciphertext)

# decrypt the ciphertext using the Fernet cipher
decrypted_plaintext = cipher.decrypt(ciphertext)

# print the decrypted plaintext message
print("Decrypted message:", decrypted_plaintext.decode())
