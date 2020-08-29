import random,time

fruits = ['apple', 'orange', 'banana', 'grape', 'peach']
count = 1
while True:
    print(f"Count# {count} ===>{random.choice(fruits)}")
    count += 1
    time.sleep(1)
