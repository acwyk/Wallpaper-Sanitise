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
	#Deletes the file if it is below the minimum specified resolution.
	
	#minimum defined values
	min_width = min_file_size[0]
	min_height = min_file_size[1]
	
	#file values
	file_width = file_size[0]
	file_height = file_size[1]
	
	#reason codes:
	height = "HEIGHT"
	width = "WIDTH"
	
	if file_width < min_width:
		#remove file
		os.remove(path)
		delete_log(path, width, file_width)
	elif file_height < min_height:
		#remove file
		os.remove(path)
		delete_log(path, height, file_height)
	else:
		print(path, " - KEPT")

def delete_log(path, reason, value):
	log_path = "sanitize.log"
	log_file = open(log_path, 'a')
	log_file.write(path)
	log_file.write(' - Reason: ' + reason)
	log_file.write(' - Value: ' + str(value))
	log_file.write('\n')
	log_file.close()
	
if __name__ == "__main__":
	try:
		count = 0
		pathname = ''
		mypath=sys.argv[1]
		min_size = (int(sys.argv[2]), int(sys.argv[3]))
		onlyfiles = listdir(mypath)
		print("Working through the Directory...")
		for name in onlyfiles:
			count+= 1
			
			# extracts the file name from the path
			filename = str(name)
			if os.path.isdir(mypath):
				pathname = os.path.join(mypath, filename)
			img_file_size = img_size(pathname)
			
			#Determins if path is an image.
			if img_file_size != 0:
				print(pathname, " - RETURNED 1 | FILE SIZE - ", img_file_size, "\n")
				keep_or_delete(min_size, img_file_size, pathname)
			else:
				print(pathname, " - RETURNED 0")
				continue
		print(count, " files scanned")
		print("Please view sanitize.log for a list of deleted files")
	except:
		print('\nPlease pass directory_name, and minimum resolution')
		print('Example: wallpaper.py <directory to wallpapers> <width> <height>')