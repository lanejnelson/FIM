import sys
import os
import hashlib



if len(sys.argv) == 3:
    file_list = sys.argv[1]
    output_file = sys.argv[2]
else:
    print("Syntax is python3 hashdump.py file_list output_file")
    quit()

list = []

if os.path.isfile(file_list):
    file_list = sys.argv[1]
    print(file_list)
else:
    print("File doesn't exist")

def hash_files(file_list):
    with open(file_list, 'r') as f:
        files = f.read()
        print(files)
        file_array = files.splitlines()
        for x in file_array:
            with open(x, 'rb') as f:
                data = f.read()
                if not data:
                    break
                sha256 = hashlib.sha256()
                sha256.update(data)
                list.append(sha256.hexdigest())
                

hash_files(file_list)



def write_files(list):
    with open(output_file, 'w') as o:
        for l in list:
            o.writelines(l+'\n')
        o.close()


write_files(list)
print("Hashes written to " + output_file)