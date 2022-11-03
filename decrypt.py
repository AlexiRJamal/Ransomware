import os
from cryptography.fernet import Fernet
import time
import math

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

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        print(f"Encrypting {file} with size of {convert_size(os.stat(file).st_size)}...") 
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
        print(f"File {file} has been decrypted.")

print("Files have been decrypted.")
print(f"Exec time: {round((time.time() - start_time)/60)} minutes.")