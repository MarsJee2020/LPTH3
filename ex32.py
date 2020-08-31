the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']  # apricot 杏桃
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go throuth mixed list too
#notice
for i in change:
    print(f"I got {i}")

    #we can also build lists.
    elements = []
    elements2 = []
    elements2 = list(range(0,6))

    # use range function
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # append function
    elements.append(i)

#no , print the lists
for i in elements:
    print(f"Element was: {i}")

for i in elements2:
    print(f"Element2 was: {i}")
