import os
path = input("Enter the path: ")
filename = input("Enter the file name: ")
fullpath = os.path.join(path, filename)

if os.path.isfile(fullpath):
    print("File exists")
else:
    print("File does not exist")
