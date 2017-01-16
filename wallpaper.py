from PIL import Image
from os import listdir
from pathlib import Path
import os, sys, argparse


def img_size(file_path):
    file = Path(file_path)
    try:
    	img = Image.open(file)
    	return img.size
    except:
    	print(file_path, " - Not an image file.")
    	return 0

def keep_or_delete(min_file_size, file_size, path):
    #Extracts the resolution value of the tuple. (1920, 1080) (FHD resolution) turns to 19201080
    non_tuple_min_file_size = int(''.join(map(str,min_file_size))) #non tuple of the MINIMUM file size
    non_tuple_file_size = int(''.join(map(str,file_size))) # non tuple of the file size
    
    #Deletes the file if it is below the minimum specified resolution.
    if non_tuple_file_size < non_tuple_min_file_size:
	os.remove(path)
	print(path, " - DELETED")

def file_finder(file_tuple, file_path):
    for file_name in file_fuple:
        if os.path.isdir(file_path):
            path = os.path.join(file_path, file_tuple)
            return path


if __name__ == "__main__":
    try:
	count = 0
	pathname = ''
        mypath=sys.argv[1]
	min_size = (int(sys.argv[2]), int(sys.argv[3]))
    	only_files = listdir(mypath)
    	pathname = file_finder(only_files)
    	img_file_size=img_size(pathname)
    	if img_file_size != 0:
            keep_or_delete(min_size, img_file_size, pathname)
        

    	"""
    	for name in onlyfiles:
            count+= 1
            filename = str(name)
            if os.path.isdir(mypath):
                pathname = os.path.join(mypath, filename)
	    img_file_size = img_size(pathname)
	    if img_file_size != 0:
                keep_or_delete(min_size, img_file_size, pathname)
	    else:
		continue
	    print(count, " files scanned")
	"""
    except:
	print('Please pass directory_name, and minimun resolution')
	print('Example: wallpaper.py <directory to wallpapers> <width> <height>')
