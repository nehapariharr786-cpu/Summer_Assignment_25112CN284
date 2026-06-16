arr = list(map(int, input("Enter array elements: ").split()))

new_arr = []

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print("Array after removing duplicates:", new_arr)