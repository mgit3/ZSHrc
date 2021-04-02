import subprocess
import os
import time

def delete_zsh_history():
    subprocess.call("rm -r ~/.zsh_history",  shell=True )

print("Congratulation, your zsh history was deleted!")

delete_zsh_history()
