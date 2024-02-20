import sys
import hashlib
import time
import pathlib
import os


try:
    if os.path.isfile(sys.argv[1]):
        hash_list = sys.argv[1]
    else:
        print("File does not exist")
except:
    print("Syntax is python3 FIM.py hash_list")
    quit()
#if len(sys.argv[1]) > 1 and os.path.isfile(sys.argv[1]):
    #file = sys.argv[1]
#else:
    #print("Please supply a file to hash")
    #quit()


def hashfile(hash_list):
    sha256 = hashlib.sha256()    
    with open(hash_list, 'rb') as f:
        while True:
            data = f.read()
            if not data:
                break
            sha256.update(data)
            return sha256.hexdigest()
        
        


original_hash = hashfile(hash_list)

while True:
    print(original_hash + ' - Original hash')
    time.sleep(2)
    next_hash = hashfile(hash_list)
    if original_hash == next_hash:
        print("Hashes are correct")
    else:
        print("File has been modified!")
        break