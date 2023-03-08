import os
import redis
import json
from datetime import datetime
import redis
import pandas as pd
from jinja2 import Template
from useful_fuctions import  *

def create_html_table():
    # Get data from Redis
    data = get_speedtest_data_from_redis()
    print(data)
    # Create a Pandas dataframe from the data
    df = pd.DataFrame.from_dict(data['speedtest_data'], orient='index', columns=['download', 'upload'])
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'date'}, inplace=True)
    # Use the to_html method to create a HTML table
    table = df.to_html()

    # Use Jinja to create a template for the HTML page
    template = Template("""
        <html>
            <head>
                <title>Speedtest Data</title>
                <link rel="stylesheet" type="text/css" href="style.css">

            </head>
            <body>
                {{ table }}
            </body>
        </html>
    """)

    # Render the template with the table variable
    rendered_template = template.render(table=table)

    # Write the rendered template to a file
    with open("home.html", "w") as f:
        f.write(rendered_template)

create_html_table()
