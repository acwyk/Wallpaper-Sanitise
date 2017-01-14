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
        print("Image not found")


def keep_or_delete(min_file_size, file_size, path):
	#Extracts the resolution value of the tuple. 1920, 1080 (FHD resolution) turns to 19201080
	non_tuple_min_file_size = int(''.join(map(str,min_file_size))) #non tuple of the MINIMUM file size
	non_tuple_file_size = int(''.join(map(str,file_size))) # non tuple of the file size
	
	#Deletes the file if it is below the minimum specified resolution.
	if non_tuple_file_size < non_tuple_min_file_size:
		print(path, " - DELETED")
		os.remove(path)


if __name__ == "__main__":
	try:
		pathname = ''
		mypath=sys.argv[1]
		min_size = (int(sys.argv[2]), int(sys.argv[3]))
		onlyfiles = listdir(mypath)
		
		#If run on a Mac/POSIX system, removes teh DS_Store file.
		# Causes issues if DS_Store file is present.
		# Working on a workaround
		if ".DS_Store" in onlyfiles:
			onlyfiles.remove(".DS_Store")
		
		
		for name in onlyfiles:
			filename = str(name)
			if os.path.isdir(mypath):
				pathname = os.path.join(mypath, filename)
			img_file_size = img_size(pathname)
			keep_or_delete(min_size, img_file_size, pathname)
	except:
		print('Please pass directory_name, and minimun resolution')
		print('Example: wallpaper.py <directory to wallpapers> <width> <height>')
