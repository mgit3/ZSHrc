import subprocess
import time

interface="wlp2s0"
print("__________________________________________________________________________")

subprocess.call('nmcli dev wifi', shell=True)

time.sleep(2)

print("__________________________________________________________________________")

def wf(bssid = input("bssid: "), password = input("password: ")):

    return subprocess.call('nmcli d wifi connect "' + bssid + '" password ' + password + ' ifname '+ interface,  shell=True)

wf()
time.sleep(6)

print("")
print("Congratulation!")
print("")

print("__________________________________________________________________________")
