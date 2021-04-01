###AUTOMATICALLY COPY YOUR ZSH SOURCE CODE FROM YOUR USER TO THE ROOT USER OR TO THE ROOT USER TO YOUR DEFAULT USER.

import subprocess
import os
import time

#m3 is my hostname

print("""

0 == m3   >>> root

1 == root >>> m3

      """)  


#REPLACE the word m3 to your hostname

menu = int(input("how do you wanna overwrite the files?"))

if menu == 0:
  zsh = "cp /home/m3/.zshrc /root/.zshrc"
       
      
if menu == 1:
  zsh = "cp /root/.zshrc /home/m3/.zshrc|chmod 777 /home/m3/.zshrc"

def mv_zsh():
   subprocess.call( zsh ,  shell=True )
   print("Congratulation!")

mv_zsh
