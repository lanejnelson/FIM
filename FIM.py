import sys
import hashlib
import time
import pathlib
import os


try:
    if os.path.isfile(sys.argv[1]):
        file = sys.argv[1]
    else:
        print("File does not exist")
except:
    print("You did something wrong idk what")
    quit()
#if len(sys.argv[1]) > 1 and os.path.isfile(sys.argv[1]):
    #file = sys.argv[1]
#else:
    #print("Please supply a file to hash")
    #quit()


def hashfile(file):
    sha256 = hashlib.sha256()    
    with open(file, 'rb') as f:
        while True:
            data = f.read()
            if not data:
                break
            sha256.update(data)
            return sha256.hexdigest()
        
        


original_hash = hashfile(file)

while True:
    print(original_hash + ' - Original hash')
    time.sleep(2)
    next_hash = hashfile(file)
    if original_hash == next_hash:
        print("Hashes are correct")
    else:
        print("File has been modified!")
        break