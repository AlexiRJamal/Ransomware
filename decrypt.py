import os
from cryptography.fernet import Fernet
import time

start_time = time.time()

files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "dummy.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secret_key = key.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    print(f"Decrypting {file}...") 
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
        print(f"File {file} has been decrypted.")

print("Files have been decrypted.")
print(f"Exec time: {time.time() - start_time} seconds.")