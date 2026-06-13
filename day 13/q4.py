# Count even and odd elements

n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

even = 0
odd = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even elements =", even)
print("Odd elements =", odd)