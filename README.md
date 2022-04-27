### In this project, 

1. I used speedtest-CLI(Linux software)  to collect data about the internet velocity of my residence and used a scheduler with the Cron(Linux Software) to repeat the task periodically. 

2. Then I organized the output data to be ingested into a dataset in a CSV format using the Pandas(Python module).

3. From the dataset, I produce an interactive graph about my upload and download rate using the Plotly(Python module). 
 
4. And finally, I share the graph on the internet through the S3(AWS Simple Cloud Storage ) using the boto3(Python module). 

link to see the output on AWS SERVER: [GRAPH](http://roberto-server.s3.amazonaws.com/graph.html)

### To use 4 the 1st time:

1. First install the requirements, with "install_requirements.sh" using bash.

2. Secondoly, create the dataset with "creatingDataset.py" using python.


### Use the "mainFile.py" to run:

` os.system("bash speedTest.sh")`

To collect data about your internet speed. 

` os.system("python3 populatingSpeedtest.py") `

To populate the database with the new data.

` os.system("python3 dash_plotly.py") `

To vizualize the models in the dashboard.
  
To see the dashboard access this address __"http://127.0.0.1:8050/"__ in your web-browser.

You also can vizualize the database in terminal with the __"tabulateSpeedtest.py"__.
