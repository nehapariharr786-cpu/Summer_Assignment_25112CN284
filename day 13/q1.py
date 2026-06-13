# Input and display array

n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

print("Array elements are:")

for i in range(n):
    print(arr[i], end=" ")