
def CreateList(num,gap):
    i = 0
    numbers = []
    while( i < num):
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + gap
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for i in numbers:
        print(i)


CreateList(10,4)
