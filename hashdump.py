import sys
import pathlib
import os
import hashlib



if len(sys.argv[1]) > 1:
    file_list = sys.argv[1]
elif len(sys.argv[2]) > 1:
    output_list = sys.argv[2]
else:
    print("Syntax is python3 hashdump.py file_list output_file")
    quit()
list = []

if os.path.isfile(file_list):
    file_list = sys.argv[1]
    #print(file_list)
else:
    print("File doesn't exist")

def hash_files(file_list):
    with open(file_list, 'r') as f:
        files = f.read()
        file_array = (files.splitlines())
        sha256 = hashlib.sha256()
        for x in file_array:
            with open(x, 'rb') as f:
                data = f.read()
                if not data:
                    break
                sha256.update(data)
                list.append(sha256.hexdigest())
                

hash_files(file_list)
print(list)

def write_files(list):
    with open(output_file, 'w') as o:
