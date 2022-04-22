IN PROGRESS, I'AM CHANGING A LOT OF THINGS TO START USE A DB!


In this project, 

-I used speedtest-CLI(Linux software)  to collect data about the internet velocity of my residence and used a scheduler with the Cron(Linux Software) to repeat the task periodically. 

-Then I organized the output data to be ingested into a dataset in a CSV format using the Pandas(Python module).

-From the dataset, I produce an interactive graph about my upload and download rate using the Plotly(Python module). 

-And finally, I share the graph on the internet through the S3(AWS Simple Cloud Storage ) using the boto3(Python module). 

output >>> http://roberto-server.s3.amazonaws.com/graph.html
