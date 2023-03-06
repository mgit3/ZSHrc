from useful_fuctions import * 

all_data = get_speedtest_data_from_redis()
speedtest_data = run_speedtest()
key = speedtest_data["datetime"]
del speedtest_data["datetime"]
all_data["speedtest_data"][key]=speedtest_data
store_speedtest_data_in_redis(all_data)
