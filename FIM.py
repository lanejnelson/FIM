import sys
import hashlib
import time
import os

if os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]) and len(sys.argv) == 3:
    hash_list = sys.argv[1]
    file_list = sys.argv[2]       
else:
    print(f"Syntax is python3 {sys.argv[0]} hash_list file_list")
    quit()



def load_hashes(hash_list): #Load contents of file
    with open(hash_list, 'r') as h:
        while True:
            hashes = h.read().splitlines()
            if not hashes:
                break
            return(hashes)

for line in load_hashes(hash_list): # Check if lines exceed lines in file
        with open(hash_list, 'r') as fp:
            lines = len(fp.readlines())
            if not lines:
                break
            original_hash = line


def load_filenames(file_list):
    with open(file_list, 'r') as f:
        while True:
            file_names = f.read().splitlines()
            if not file_names:
                break
            return file_names

def hash_file(file):
    with open(file, 'rb') as f:
        while True:
            data = f.read()
            if not data:
                break
            #sha256 = hashlib.sha256()
            result = hashlib.sha256(data).hexdigest()
            #sha256.update(data)
            #result = sha256.hexdigest()
            #sha256.update(data)
            return result


files = load_filenames(file_list)
hashes = load_hashes(hash_list)
file_dict = dict(zip(files, hashes))
#print(files)
#print(hashes)
#print(file_dict)
#print(hash_file("test1.txt"))

#for x in file_dict:
    #print(x)


while True:
    for key in file_dict:
        first_hash = file_dict[key]
        #print(first_hash)
        print(str(first_hash) + f' - Original hash for {key}')
        time.sleep(1)
        new_hash = hash_file(key)
        time.sleep(1)
        print(new_hash)
        if new_hash == file_dict[key]:
            print("Fine")
        else:
            print(f"{key} has been modified!")
            quit()