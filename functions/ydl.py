import subprocess

link = input(str("Paste the Youtube link and hit enter >>> "))

def YDL(): 
   subprocess.call("youtube-dl -F "  + link ,  shell=True)

YDL()

print("___________________________________________________________")


download_type = input(str("Type the number that represents the type of download and  hit enter >>> "))


song_name = input(str("Type the name you want to give to the file (use underline instead of space) >>> "))

def ydl():
    subprocess.call("youtube-dl -f "+ download_type +" " + link +" --output " + song_name + ".webm",  shell=True)

ydl()

print("___________________________________________________________")

print("Congratulation!")
