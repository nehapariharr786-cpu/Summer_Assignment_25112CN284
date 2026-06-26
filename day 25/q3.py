names = input("Enter names separated by space: ").split()

names.sort()

print("Names in alphabetical order:")

for name in names:
    print(name)