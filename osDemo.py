import os

for path, directories, files in os.walk('./'):
    print(path)
    print(directories)
    print(files)
    print('-' * 50)

import sys

print("Параметри на програмата:")
print(sys.argv)
for idx, a in enumerate(sys.argv):
    print("Argument #{} - '{}'".format(idx, a))
