# Wallpaper-Sanitiser
Sanitise your wallpaper folders to keep resolutions above the specified resolution.

Usage:
  <p>wallpaper.py < wallpaper directory > < minimum width > < minimum height></p>
  <p>wallpaper.py ~/Pictures/Wallpapers 1920 1080</p>
  
  Required tehse Python Libraries to run:
  <ul>
  <li>PIL (Pillow)</li>
  <li>pathlib</li>
  </ul>
  
The script scans through that directory and removes any image files that are under the minimum specified resolution.
The script outputs what files are removed.
  Removed files bear the " - REMOVED" tag on output.
