arr = list(map(int, input("Enter array elements: ").split()))

max_count = 0
element = arr[0]

for i in arr:
    count = arr.count(i)

    if count > max_count:
        max_count = count
        element = i

print("Maximum frequency element:", element)
print("Frequency:", max_count)










