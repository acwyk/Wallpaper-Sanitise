# Wallpaper-Sanitiser-
Sanitise your wallpaper folders to keep resolutions above the specified resolution.

Usage:
  <p>wallpaper.py < wallpaper directory > < minimum width > < minimum height></p>
  <p>wallpaper.py ~/Pictures/Wallpapers 1920 1080</p>
  
The script scans through that directory and removes any image files that are under 1920x1080 in resolution.
The script outputs what files are removed, and what files are kept. 
  Removed files bear the " - REMOVED" tag on output.
  Kept files bear the " - RETAINED" tag on output.
