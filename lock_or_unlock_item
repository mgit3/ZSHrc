import subprocess

print("")
def options():

    print("0 = unlock item; You will need to be logged as root to use this choice.")
    print("1 = lock item!")
    print("")

options()

choice = int(input("Type the number that represents your choice and press enter: """))        

if choice == 0:
  permission = "777"
if choice == 1:
  permission = "000"

file = input("file name: ")

def key():
    if choice == 1:
        return subprocess.call('chmod '+ permission + " " + file,  shell=True )
    if choice == 0:
        return subprocess.call('chmod '+ permission + " " + file,  shell=True )

key()
print("Congratulation!")
                                    
