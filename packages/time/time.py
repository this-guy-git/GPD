import time
import datetime

def current_time():
    return time.time()

def formatted_time():
    return time.strftime("%H:%M:%S")

def future_date(days):
    return (datetime.datetime.now() + datetime.timedelta(days=days)).strftime("%Y-%m-%d")
