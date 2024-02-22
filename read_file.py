import sys
import hashlib
import time
import os
try:

    if os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]):
        hash_list = sys.argv[1]
        file_list = sys.argv[2]
    elif len(sys.argv[1]) < 1:
        print("Syntax is python3 read_file.py hash_list")
    else:
        print("The file does not exist or your syntax is improper. Syntax: python3 read_file.py hash_list")
except:
    print("Syntax is python3 read_file.py hash_list")

def load_hashes(hash_list): #Load contents of file
    with open(hash_list, 'r') as h:
        while True:
            hashes = h.read().splitlines()
            if not hashes:
                break
            yield(hashes)

for line in load_hashes(hash_list): # Check if lines exceed lines in file
        with open(hash_list, 'r') as fp:
            lines = len(fp.readlines())
            if not lines:
                break
            original_hash = line
            print(line)


while True:
    for x in line:
        original_hash = x
        print(original_hash + ' - Original hash')
        time.sleep(2)
        next_hash = load_hashes(hash_list)
        print(original_hash)
        print(next_hash)
        if original_hash == next_hash:
            print("Hashes are correct")
        else:
            print("File has been modified!")
            break
