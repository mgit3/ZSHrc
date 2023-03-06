from useful_fuctions import * 

clear_redis_database()
speedtest_data = run_speedtest()
key = speedtest_data["datetime"]
del speedtest_data["datetime"]
print(speedtest_data)

all_data = {"speedtest_data":
            {key:speedtest_data}
            }

store_speedtest_data_in_redis(all_data)
