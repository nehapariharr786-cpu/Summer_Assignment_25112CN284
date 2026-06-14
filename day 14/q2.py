arr = list(map(int, input("Enter array elements: ").split()))

element = int(input("Enter element: "))

count = 0

for i in arr:
    if i == element:
        count += 1

print("Frequency of", element, "is", count)