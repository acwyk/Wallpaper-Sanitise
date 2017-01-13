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


def keep_or_delete(min_file_size, file_size, path):
    
    non_tuple_min_file_size = int(''.join(map(str,min_file_size))) #non tuple of the MINIMUM file size
    non_tuple_file_size = int(''.join(map(str,file_size))) # non tuple of the file size
    if non_tuple_file_size < non_tuple_min_file_size:
        print (path, " - DELETED")
        os.remove(path)
    else:
        print(path, " - RETAINED")


if __name__ == "__main__":
    try:
        mypath=sys.argv[1]
        min_size = (int(sys.argv[2]), int(sys.argv[3]))
        onlyfiles = listdir(mypath)
        onlyfiles.remove(".DS_Store")
        for name in onlyfiles:
            filename = str(name)
            pathname = ""
            pathname += mypath
            pathname += "/"
            pathname += filename
            img_file_size = img_size(pathname)
            keep_or_delete(min_size, img_file_size, pathname)

    
    except:
        print('Please pass directory_name, and minimun resolution')
        print('Example: wallpaper.py <directory to wallpapers> <width> <height>')



