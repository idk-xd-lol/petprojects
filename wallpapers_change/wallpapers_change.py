import os
import time
import random
import subprocess
import argparse

#install swww for it to work
#work only on linux, maybe

#geting arguments
parser = argparse.ArgumentParser()

#set path to your wallpaper folder
parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="Set path to wallpaper"
)

#set change duration time
parser.add_argument( 
    "--change_duration",
    type=int,
    default=60,
    help="Set changing duration time in seconds(default=60)"
)

args = parser.parse_args()

path = args.path
path = os.path.expanduser(path) #make full path (from ~ to /home/username...)

wallpapers = os.listdir(path) #gets wallpapers to list
 
while True:
    wallpaper = random.choice(wallpapers) #gets random wallpaper
    wallpaper_path = os.path.join(path, wallpaper) #making full path to random wallpaper
    subprocess.run(["swww", "img", wallpaper_path]) #execute program
    time.sleep(args.change_duration)

