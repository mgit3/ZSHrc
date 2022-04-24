import os 

os.system("bash speedTest.sh")
os.system("python3 populatingSpeedtest.py")
os.system("python3 tabulateSpeedtest.py")
os.system("python3 dash_plotly.py")
