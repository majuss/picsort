import os
#from fnmatch import fnmatch
from PIL import Image

root = '/Users/majuss/Desktop'
suffixes = '.jpg', '.jpeg', '.gif', '.png', '.PNG', '.JPG', '.GIF', '.raw', '.RAW', '.JPEG'

for path, subdirs, files in os.walk(root):
    for name in files:
        #if fnmatch(name, pattern):
        if name.endswith(suffixes):
            raw_path = path + '/' + name
            path_img = r'{}'.format(raw_path)
            print(path)
            img = Image.open(path_img)
            exif_data = img._getexif()
            #print (os.path.join(path, name))
            print(exif_data)