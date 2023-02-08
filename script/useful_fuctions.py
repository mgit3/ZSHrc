import pandas as pd
import os
import json
import datetime
import redis

def clear_redis_database():
    # Connect to the Redis database
    redis_client = redis.Redis(host='localhost', port=6379)

    # Delete all keys in the database
    redis_client.flushall()

    # Confirm that the database is now empty
    print("Redis database cleared successfully.")


def run_speedtest():
    # Run the speedtest and get the results
    speedtest_result = os.popen("speedtest-cli --json").read()

    # Load the result into a Python dictionary
    speedtest_data = json.loads(speedtest_result)
    speedtest_data = process_speedtest_data(speedtest_data)
    return speedtest_data

def process_speedtest_data(speedtest_data):
    # Add a timestamp to the data
    datetime_key = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    speedtest_data["datetime"] = datetime_key

    # Convert download and upload speeds from bits per second to megabits per second
    speedtest_data["download"] = round(speedtest_data["download"]/1000000, 2)
    speedtest_data["upload"] = round(speedtest_data["upload"]/1000000, 2)

    # Remove all keys except "download", "upload", and "datetime"
    keys_to_keep = ["download", "upload", "datetime"]
    for key in list(speedtest_data.keys()):
        if key not in keys_to_keep:
            del speedtest_data[key]

    return speedtest_data

def store_speedtest_data_in_redis(speedtest_data):
    # Connect to Redis
    redis_host = "localhost"
    redis_port = 6379
    r = redis.Redis(host=redis_host, port=redis_port)
    # Store the data in Redis using the datetime as the key
    r.set("speedtest_data", json.dumps(speedtest_data))

def print_speedtest_data(speedtest_data):
    # Print some useful information
    print("Speedtest data stored in Redis:")
    print("- Timestamp:", speedtest_data["datetime"])
    print("- Download Speed:", speedtest_data["download"], "Mb/s")
    print("- Upload Speed:", speedtest_data["upload"], "Mb/s")

def get_speedtest_data_from_redis():
    # Connect to Redis
    redis_host = "localhost"
    redis_port = 6379
    r = redis.Redis(host=redis_host, port=redis_port)

    # Retrieve the data from Redis
    speedtest_data = r.get("speedtest_data").decode()

    return json.loads(speedtest_data)



def json_to_dataframe(json_string, key):
    data_dict = json.loads(json_string)
    data = data_dict[key]
    df = pd.DataFrame.from_dict(data, orient='index')
    return df


