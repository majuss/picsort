import os

root = '/Users/majuss/Desktop/'
existant_suffixes = []

for path, subdirs, files in os.walk(root):
    for name in files:
        filename, file_extension = os.path.splitext(path + '/' + name)
        existant_suffixes.append(file_extension)

suffixes = list(set(existant_suffixes))

print(suffixes)