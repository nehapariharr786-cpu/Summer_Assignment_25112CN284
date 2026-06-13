# Find sum and average of array

n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

sum = 0

for i in range(n):
    sum = sum + arr[i]

average = sum / n

print("Sum of array =", sum)
print("Average of array =", average)