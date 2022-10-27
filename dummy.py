import os

fileSizeInBytes = 1000000000
for i in range(2):
    with open(f'test{i}', 'wb') as fout:
        print(f"Creating file 'test{i}'...")
        fout.write(os.urandom(fileSizeInBytes))
        print(f"File test{i} was created.")