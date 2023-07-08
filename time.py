import time

import datetime

tim1 = time.strftime("%H:%M:%S")
print("Current time is : ")
print(tim1)

# time setting
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = (time.strftime('%M'))
print(timestamp)
timestamp = (time.strftime('%S'))
print(timestamp)
if (timestamp <= 12):
    print("Good morning ")
else:
    print("Good afternoon")
