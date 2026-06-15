arr = list(map(int, input("Enter array elements: ").split()))

result = []

zero_count = 0

for i in arr:
    if i != 0:
        result.append(i)
    else:
        zero_count += 1

result.extend([0] * zero_count)

print("Array after moving zeroes:", result)