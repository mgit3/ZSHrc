## In this project, 

1. I used __speedtest-CLI__ (Linux software) to collect data about the internet velocity of my residence and used a scheduler with the Cron(Linux Software) to repeat the task periodically. 

2. Then I organized the output data to be ingested into  Redis.

3. From the dataset on Redis, I produce an interactive graph about my upload and download rate using the __Plotly__ (Python module). 
 
### To use the code for the first time:

1. First install the requirements, with "pip install -r install/pip_requirements.sh; sudo bash install/system_requirements.sh" using __pip__ and __bash__.

2. Secondoly, create the dataset with "create_db.py" using python.


### Use the "main.py" to run:

To collect data about your internet speed and to populate the database with the new data.

` os.system("python3 pop.py") `

To vizualize the models in the dashboard.

` os.system("python3 dash_plotly.py") `

To see the dashboard access this address __"http://127.0.0.1:8050/"__ in your web-browser.

Preview:

![screenshot](https://raw.githubusercontent.com/s33ding/speedtest-CLI_dataEngineering/main/screenshot1.png)

![screenshot2](https://raw.githubusercontent.com/s33ding/speedtest-CLI_dataEngineering/main/screenshot2.png)

