import os
from PIL import Image

root = '/Users/majuss/Desktop/testing'
suffixes = '.jpg', '.jpeg', '.gif', '.png', '.PNG', '.JPG', '.GIF', '.raw', '.RAW', '.JPEG', '.mov', '.MOV' #implement case insensitive approach

#understand gps tag: https://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/GPS.html
#understand exif tag: https://sno.phy.queensu.ca/~phil/exiftool/TagNames/EXIF.html


for path, subdirs, files in os.walk(root):
    for name in files:        
        if name.endswith(suffixes):
            raw_path = path + '/' + name
            path_img = r'{}'.format(raw_path)

            try:
                img = Image.open(path_img)
            except:
                print("cant open image")
                #copy image to special folder
            try:
                exif_data = img._getexif()
                print(exif_data[36867]) #creation date
                print(exif_data[34853]) #gps ifd tag
                print(path+name)
                #check if picture has EXIF creation date, if not take creation date from OS-metadata
                #check if picture has EXIF GPS, if not put unknown
                #put image path into dict, with its creationDate and GPS
            except:
                pass
                #copy picture to special folder
                #print("Error raised")
