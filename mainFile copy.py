# !rm -r dataset_speedtest/main.db
import os 
os.system("bash speedTest.sh")
os.system("python3 creatingDataset.py")
os.system("python3 populatingSpeedtest.py")
os.system("python3 tabulateSpeedtest.py")
