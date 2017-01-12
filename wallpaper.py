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


def keep_or_delete(file_size, path, filename):
    if file_size < 19201080:
        print (path, " - DELETED")
        os.remove(path)
    else:
        print(path, " - RETAINED")


if __name__ == "__main__":
    try:
        mypath=sys.argv[1]
        onlyfiles = listdir(mypath)
        onlyfiles.remove(".DS_Store")
        for name in onlyfiles:
            filename = str(name)
            pathname = ""
            pathname += mypath
            pathname += "/"
            pathname += filename
            img_file_size = img_size(pathname)
            non_tuple_file_size = int(''.join(map(str,img_file_size)))
            keep_or_delete(non_tuple_file_size, pathname, filename)

    
    except:
        print('Please pass directory_name')
        print('Example: wallpaper.py <directory to wallpapers>')



