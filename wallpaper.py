from PIL import Image
from os import listdir
from pathlib import Path
import os, sys, argparse

# Extracts the file size of image in tuple.
# eg. (1920, 1080) for a full HD image.
def img_size(file_path):
    file = Path(file_path)
    if file.is_file():
        img = Image.open(file)
        return img.size


def keep_or_delete(file_size, path):
    if file_size < 19201080:
        print (path, " - DELETED")
        os.remove(path)
    else:
        print(path, " - RETAINED")

#scans through the wallpaper folder
mypath="wallpapers"

if __name__ == "__main__":
    try:
        directory_name=sys.argv[1]
        print(directory_name)
        onlyfiles = listdir(mypath)
        onlyfiles.remove(".DS_Store")
        for name in onlyfiles:
            file_name = str(name)
            path_name = ""
            path_name += mypath
            path_name += "/"
            path_name += file_name
            img_file_size = img_size(path_name)
            non_tuple_file_size = int(''.join(map(str,img_file_size)))
            keep_or_delete(non_tuple_file_size, path_name, file_name)#

    
    except:
        print('Please pass directory_name')



