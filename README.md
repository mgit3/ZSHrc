# cron_plotly_aws_speedtestCLI

In this project, I automated a process to collect data about the internet velocity of my residence with speedtest-CLI(Linux software) and the Cron(Linux Software) as a scheduler to repeat the task periodically. Then I organized the output data to be ingested into a dataset in a CSV format using the Pandas(Python module). From the dataset, I produce an interactive graph with Plotly about my upload and download rate. And finally, I use the boto3(Python module) to share the graph on the internet using S3(tool from AWS cloud). 
