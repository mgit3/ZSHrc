In this project, 

-I used speedtest-CLI(Linux software)  to collect data about the internet velocity of my residence and used a scheduler with the Cron(Linux Software) to repeat the task periodically. 

-Then I organized the output data to be ingested into a database in SQLite format using the SQLAlchemy and Pandas(Python module).

-From the dataset, I produce an interactive graph about my upload and download rate using the Plotly(Python module). 

-Then, I share the graph on the internet through the S3(AWS Simple Cloud Storage) using the boto3(Python module). output >>> http://roberto-server.s3.amazonaws.com/graph.html

-Finally, I made a dashboard('dash_plotly.py') using Dash and Plotly(Python modules). In this dashboard, I presented statistical information about the Download and Upload internet speed such as the maximum, minimum, median, and standard deviation rate. 
