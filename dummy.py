import os
import random
import math

min_file_size = 1024
max_file_size = 100000000

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

for i in range(100):
    fileSizeInBytes = random.randint(min_file_size, max_file_size)
    with open(f'test{i}.txt', 'wb') as fout:
        print(f"Creating file 'test{i}' with size of {convert_size(fileSizeInBytes)}...")
        fout.write(os.urandom(fileSizeInBytes))
        print(f"File test{i} was created.")
