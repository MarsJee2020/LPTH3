from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("I you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncatin the file. Goodbye!")
target.truncate()

prit("N")
