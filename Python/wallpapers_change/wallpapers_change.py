#wallpaper changer
import os
import time
import random
import subprocess
import argparse

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

#run programm in background
def run_detached(cmd):
    subprocess.run(
        cmd, 
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.DEVNULL, 
        stdin=subprocess.DEVNULL,
        start_new_session=True 
    )

while True:
    wallpaper = random.choice(wallpapers)
    wallpaper_path = os.path.join(path, wallpaper)
    
    run_detached(["swww", "img", wallpaper_path])
    run_detached(["wal", "-n", "-q", "-i", wallpaper_path])
    run_detached(["matugen", "image", wallpaper_path])
    
    time.sleep(args.change_duration)
