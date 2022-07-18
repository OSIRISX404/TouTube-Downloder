from pytube import YouTube
import os
from time import sleep

#show
os.system('cls')

print("Created By: Adithyan.A.J")
print("Please Wait: 1")
print("Loding...")

sleep(1)

os.system('cls')

print("Created By: Adithyan.A.J")
print("Please Wait: 2")
print("Loding...")

sleep(1)

os.system('cls')

print("Created By: Adithyan.A.J")
print("Please Wait: 3")
print("Loding...")

sleep(1)

os.system('cls')

print("Created By: Adithyan.A.J")
print("Please Wait: 4")
print("Loding...")

sleep(1)

os.system('cls')

print("Created By: Adithyan.A.J")
print("Please Wait: 5")
print("Loding...")

sleep(1)

os.system('cls')

print("Created By: Adithyan.A.J")
print("Please Wait: 6")
print("Loding...")

sleep(1)
os.system('cls')

print('')
print("[#] Checking the Installation of Packages.")
print("------------------------------------------")
os.system('pip install pytube')
sleep(4)
os.system('cls')
sleep(1)
print('')
print("[*] The packages are Installed.")
sleep(5)
os.system('cls')
print('')
print("[*] Copy pase your link here.")
print('----------------------------')
ul_Source = input("Ender your url: ")
yt = YouTube(ul_Source)
print('')

os.system('cls')
sleep(1)
#
# Song
#
#
def Song(ul_Source):
    title = yt.title
    auther = yt.author
    views = yt.views
    print("")
    print("Your select the Song Downloder.")
    print("--------------------------------")
    print(f"The title  : {title}")
    print(f"The author : {auther}")
    print(f"The views  : {views}")
    print("")
    print("Select the Song Qulity.")
    song_resulation = yt.streams.filter(only_audio=True)
    song_resulations = list(enumerate(song_resulation))
    while True:
        i = 0 
        for resulation in song_resulations:
            print(f"[{i}]. {resulation}")
            i += 1
        s = i - 1
        choice = int(input(f"\nChoose the Song (0 to {s}): "))
        if 0 <= choice < i:
            song_resulation[choice].download()
            # command for downloading the video

            print("\nSong was successfully downloaded!")
            sleep(5)
            os.system('cls')
            print('')
            print("[*] Thankes for using this Tool, Hop you are enjoy it.")
            sleep(6)
            os.system('cls')
            break
        else:
            print("[!] Invalid choice.\n")
#    
#
# Video   
#
#
def Video(ul_Source):
    title = yt.title
    auther = yt.author
    views = yt.views
    print("")
    print("Your select the video Downloder.")
    print("--------------------------------")
    print(f"The title  : {title}")
    print(f"The author : {auther}")
    print(f"The views  : {views}")
    print("")
    print("Select the video Qulity.")
    video_resulation = yt.streams.filter(file_extension='mp4')
    video_resulations = list(enumerate(video_resulation))
    while True:
        i = 0 
        for resulation in video_resulations:
            print(f"[{i}]. {resulation}")
            i += 1
        s = i - 1
        choice = int(input(f"\nChoose the video (0 to {s}): "))
        if 0 <= choice < i:
            video_resulation[choice].download()
            # command for downloading the video

            print("\nVideo was successfully downloaded!")
            sleep(5)
            os.system('cls')
            print("[*] Thankes for using this Tool, Hop you are enjoy it.")
            sleep(6)
            os.system('cls')
            break
        else:
            print("[!] Invalid choice.\n")
    

#
#
print("")
print("")
print("""
          ______   _______ 
|\     /|(  ___  )(  ____ \ YouTube
| )   ( || (   ) || (    \/
| |   | || (___) || (_____ 
( (   ) )|  ___  |(_____  )
 \ \_/ / | (   ) |      ) |
  \   /  | )   ( |/\____) |
   \_/   |/     \|\_______) Version: 1.0.2v
   
               +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+
 Created By:   |A| |d| |i| |t| |h| |y| |a| |n|
               +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ 
            
    Plese select the option
    
    [1] Song 
    [2] Video
    
   """)
print("") 
opt = int(input("Please select your option (1 OR 2): "))

if (opt == 1): 
    Song(ul_Source)
        
elif (opt == 2):
    Video(ul_Source)
    
        
else:
    sleep(1)
    print("")
    print("Invalid input please try again...")
    sleep(3)
    os.system('python VaS.py')