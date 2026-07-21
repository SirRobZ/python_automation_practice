"""
import time


print(time.time())
time.sleep(5)



from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))




import threading
import time

def print_number():
    for i in range(5):
        print(i)
        #time.sleep(1)


thread = threading.Thread(target=print_number)
thread.start()
thread.join()

"""

import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


