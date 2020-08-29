import random,time
import datetime


fruits = ['apple', 'orange', 'banana', 'grape', 'peach']
count = 1
while True:
    e = datetime.datetime.now()
    print(f"{e.hour}:{e.minute}:{e.second} count# {count} ===>{random.choice(fruits)}")
    count += 1
    time.sleep(1)
