In this project, 

-I used speedtest-CLI(Linux software)  to collect data about the internet velocity of my residence and used a scheduler with the Cron(Linux Software) to repeat the task periodically. 

-Then I organized the output data to be ingested into a dataset in a CSV format using the Pandas(Python module).

-From the dataset, I produce an interactive graph about my upload and download rate using the Plotly(Python module). 

-And finally, I share the graph on the internet through the S3(AWS Simple Cloud Storage ) using the boto3(Python module). 

output >>> http://roberto-server.s3.amazonaws.com/graph.html

To use 4 the 1st time:

-First install the requirements, with "install_requirements.sh" using bash.

-Secondoly, create the dataset with "creatingDataset.py" using python.


Use the "mainFile.py" to run:

-os.system("bash speedTest.sh") --> to collect data about your internet speed.

-os.system("python3 populatingSpeedtest.py") --> populate the database with the new data

-os.system("python3 dash_plotly.py") --> vizualize the models in the dashboard
  
To see the dashboard access this address "http://127.0.0.1:8050/" in your web-browser.

You also can vizualize the database in terminal with the "tabulateSpeedtest.py".
