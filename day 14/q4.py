arr = list(map(int, input("Enter array elements: ").split()))

duplicates = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

if len(duplicates) > 0:
    print("Duplicate elements are:", duplicates)
else:
    print("No duplicates found")
    