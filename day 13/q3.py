# Find largest and smallest element

n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

largest = arr[0]
smallest = arr[0]

for i in range(n):
    if arr[i] > largest:
        largest = arr[i]

    if arr[i] < smallest:
        smallest = arr[i]

print("Largest element =", largest)
print("Smallest element =", smallest)