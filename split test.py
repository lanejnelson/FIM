import sys

file_list = sys.argv[1]

with open(file_list, 'r') as f:
        files = f.read()
        #file_array = (files.splitlines())
        print(files.splitlines())